"""
Assistente Dati del Ristorante — server web.

Questo file avvia un piccolo server in locale sul tuo computer. Apre una pagina
web con una chat: i dipendenti scrivono una domanda in italiano e l'assistente
risponde ragionando sui file dati presenti nel progetto (CSV, Excel, PDF,
database, testi), facendo conti e grafici quando serve, e cercando online se
manca un'informazione esterna.

Sotto il cofano usa il Claude Agent SDK di Anthropic.
"""

import os
import json
import asyncio
from pathlib import Path
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AssistantMessage,
    TextBlock,
    ToolUseBlock,
    ResultMessage,
)

# --------------------------------------------------------------------------
# Cartelle del progetto
# --------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent       # .../test ristorante/chatbot
DATA_DIR = BASE_DIR.parent                        # .../test ristorante  (i dati)
STATIC_DIR = BASE_DIR / "static"
CHARTS_DIR = STATIC_DIR / "grafici"
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

# L'interprete Python "isolato" del progetto, che ha già pandas, matplotlib, ecc.
VENV_PY = BASE_DIR / ".venv" / "bin" / "python"

# --------------------------------------------------------------------------
# Chiave API: la cerchiamo in tre posti, in ordine di priorità:
#   1) la variabile d'ambiente ANTHROPIC_API_KEY (se l'hai già impostata);
#   2) il file gioco/.env (formato CHIAVE=valore) — è quello condiviso col gioco;
#   3) il vecchio file CHIAVE_API.txt in questa cartella (per compatibilità).
# --------------------------------------------------------------------------
# Il file .env del progetto "gioco", che sta accanto alla cartella chatbot.
ENV_GIOCO = DATA_DIR / "gioco" / ".env"


def _leggi_env(percorso: Path) -> dict[str, str]:
    """Legge un file .env (righe CHIAVE=valore) e ne ricava un dizionario.

    Ignora righe vuote e commenti (#) e toglie eventuali virgolette dai valori.
    """
    valori: dict[str, str] = {}
    if not percorso.exists():
        return valori
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        riga = riga.strip()
        if not riga or riga.startswith("#") or "=" not in riga:
            continue
        nome, _, valore = riga.partition("=")
        valori[nome.strip()] = valore.strip().strip('"').strip("'")
    return valori


def carica_chiave_api() -> str | None:
    # 1) già nell'ambiente
    chiave = os.environ.get("ANTHROPIC_API_KEY")
    if chiave:
        return chiave.strip()

    # 2) dal file gioco/.env (porta con sé anche eventuale OPENAI_API_KEY)
    env = _leggi_env(ENV_GIOCO)
    for nome, valore in env.items():
        # non sovrascriviamo variabili già presenti nell'ambiente
        os.environ.setdefault(nome, valore)
    chiave = env.get("ANTHROPIC_API_KEY")
    if chiave:
        os.environ["ANTHROPIC_API_KEY"] = chiave
        return chiave

    # 3) dal vecchio file CHIAVE_API.txt (compatibilità)
    file_chiave = BASE_DIR / "CHIAVE_API.txt"
    if file_chiave.exists():
        for riga in file_chiave.read_text(encoding="utf-8").splitlines():
            riga = riga.strip()
            if riga and not riga.startswith("#") and "INCOLLA" not in riga.upper():
                os.environ["ANTHROPIC_API_KEY"] = riga
                return riga
    return None


# Carichiamo la chiave se presente. NON è obbligatoria: se sul computer la
# Claude CLI è già collegata a un account, l'assistente funziona lo stesso.
CHIAVE = carica_chiave_api()
errore_avvio = None  # eventuale messaggio se l'assistente non riesce a partire

# Modello usato dall'assistente. Sonnet è veloce ed economico ed è perfetto per
# una demo. Per risposte ancora più "ragionate" puoi mettere "claude-opus-4-8".
MODELLO = os.environ.get("MODELLO_CLAUDE", "claude-sonnet-4-6")

# --------------------------------------------------------------------------
# Istruzioni per l'assistente (in italiano, calibrate sul ristorante)
# --------------------------------------------------------------------------
SYSTEM_PROMPT = f"""Sei l'assistente dati di un ristorante. Parli con i dipendenti,
che NON sono tecnici: rispondi sempre in italiano, in modo chiaro, concreto e sintetico.

DOVE SONO I DATI
I file aziendali si trovano nella cartella di lavoro corrente, dentro le sottocartelle:
- "Fase 1/materiali": menu, costi ingredienti, costi fissi, personale, fornitori,
  scontrini (database SQLite), acquisti di magazzino, marketing, cassa.
- "Fase 2/materiali": recensioni dei clienti, trend del settore, report di quartiere, feedback del personale.
- "Fase 3/materiali": ordini fornitori, dipendenti, registro cassa (e alcune immagini/audio).
All'inizio, se non sai dove guardare, esplora le cartelle per trovare il file giusto.

COME LAVORARE SUI DATI
- Per leggere testi brevi usa pure lo strumento di lettura file.
- Per CONTI, ANALISI, somme, medie, raggruppamenti su file tabellari (CSV, Excel,
  database SQLite) scrivi ed esegui codice Python usando QUESTO interprete, che ha
  già pandas, matplotlib, openpyxl, pdfplumber installati:
      {VENV_PY}
  Esempio di esecuzione: {VENV_PY} -c "import pandas as pd; ..."
- Basa SEMPRE le risposte sui numeri reali letti dai file. Non inventare dati.
  Se un'informazione non è presente nei file, dillo con chiarezza.

GRAFICI
- Quando un grafico aiuta a capire, crealo con matplotlib (backend 'Agg') e
  SALVALO come file PNG dentro questa cartella (percorso assoluto):
      {CHARTS_DIR}
  Usa un nome di file descrittivo, ad esempio "incassi_per_mese.png".
- Poi MOSTRA il grafico nella risposta scrivendolo in markdown con questo indirizzo
  pubblico (non il percorso del disco):
      ![titolo del grafico](/static/grafici/NOME_FILE.png)

RICERCA ONLINE
- Usa la ricerca sul web SOLO se serve un'informazione esterna che non è nei file
  (es. un prezzo di mercato, una normativa, un trend generale). Per tutto ciò che
  riguarda il ristorante, usa i dati interni.

STILE DELLE RISPOSTE
- Italiano semplice, niente gergo tecnico. Usa elenchi puntati e, quando utile, tabelle.
- Vai dritto al punto: prima la risposta, poi eventuali dettagli.
"""

# --------------------------------------------------------------------------
# Configurazione dell'agente
# --------------------------------------------------------------------------
opzioni = ClaudeAgentOptions(
    cwd=str(DATA_DIR),                 # l'assistente "vede" tutta la cartella del ristorante
    system_prompt=SYSTEM_PROMPT,
    model=MODELLO,
    allowed_tools=["Read", "Glob", "Grep", "Bash", "Write", "WebSearch", "WebFetch"],
    permission_mode="bypassPermissions",  # demo locale: l'assistente lavora senza chiedere conferme
    setting_sources=[],                # ignora impostazioni globali esterne: ambiente pulito
)

client = ClaudeSDKClient(options=opzioni)
lock = asyncio.Lock()  # una domanda alla volta (demo a utente singolo)

# Messaggi "amichevoli" mostrati mentre l'assistente lavora, in base allo strumento usato
STATO_STRUMENTI = {
    "Read": "📖 Sto consultando i dati…",
    "Glob": "📂 Sto cercando i file giusti…",
    "Grep": "🔎 Sto cercando nei dati…",
    "Bash": "🧮 Sto facendo conti e analisi…",
    "Write": "✍️ Sto preparando il risultato…",
    "WebSearch": "🌐 Sto cercando online…",
    "WebFetch": "🌐 Sto leggendo una pagina web…",
}

# --------------------------------------------------------------------------
# App web
# --------------------------------------------------------------------------
@asynccontextmanager
async def ciclo_di_vita(app: FastAPI):
    # Si esegue all'accensione: prova a collegare l'assistente.
    global errore_avvio
    try:
        await client.connect()
        print("\n  Assistente pronto. Apri il browser su: http://localhost:8000\n")
    except Exception as e:
        errore_avvio = (
            "Non riesco a collegarmi al servizio di Claude. "
            "Controlla che nel file gioco/.env ci sia la riga "
            "ANTHROPIC_API_KEY=sk-ant-... e riavvia. "
            f"(dettaglio tecnico: {e})"
        )
        print("\n" + "=" * 60)
        print("  ATTENZIONE:", errore_avvio)
        print("=" * 60 + "\n")
    yield
    # Si esegue allo spegnimento.
    try:
        await client.disconnect()
    except Exception:
        pass


app = FastAPI(title="Assistente Dati del Ristorante", lifespan=ciclo_di_vita)
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/", response_class=HTMLResponse)
async def home():
    return (BASE_DIR / "index.html").read_text(encoding="utf-8")


@app.post("/chat")
async def chat(request: Request):
    dati = await request.json()
    domanda = (dati.get("messaggio") or "").strip()

    async def eventi():
        if errore_avvio:
            yield sse({"type": "error", "text": errore_avvio})
            return
        if not domanda:
            yield sse({"type": "done"})
            return

        async with lock:
            try:
                await client.query(domanda)
                risposta = ""
                async for msg in client.receive_response():
                    if isinstance(msg, AssistantMessage):
                        for blocco in msg.content:
                            if isinstance(blocco, TextBlock):
                                risposta += blocco.text
                                yield sse({"type": "answer", "text": risposta})
                            elif isinstance(blocco, ToolUseBlock):
                                stato = STATO_STRUMENTI.get(blocco.name, "⚙️ Sto lavorando…")
                                yield sse({"type": "status", "text": stato})
                    elif isinstance(msg, ResultMessage):
                        yield sse({"type": "done"})
            except Exception as e:
                yield sse({"type": "error", "text": f"Si è verificato un errore: {e}"})

    return StreamingResponse(eventi(), media_type="text/event-stream")


def sse(payload: dict) -> str:
    """Formatta un evento in stile Server-Sent Events."""
    return f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="warning")
