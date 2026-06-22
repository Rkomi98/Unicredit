# 🍝 Assistente Dati del Ristorante — istruzioni

Questa è una piccola applicazione che gira **sul tuo computer**. Apre una pagina
web con una chat: scrivi una domanda sui dati del ristorante e l'assistente ti
risponde, leggendo i file, facendo conti e grafici, e cercando online se serve.

---

## ▶️ Come accenderla (il modo veloce — Mac)

1. Apri la cartella **`chatbot`**.
2. Fai **doppio click** sul file **`avvia.command`**.
3. Si apre una finestra nera (è normale, lasciala aperta). La **prima volta**
   prepara l'ambiente da sola: ci mette un minuto. Poi si apre da solo il
   browser con la chat. **Pronto: scrivi e premi Invio.**

Per **spegnere** l'assistente: chiudi la finestra nera.

> La prima volta che fai doppio click, il Mac potrebbe chiedere conferma perché
> il file arriva da fuori. In quel caso: tasto destro sul file → **Apri** →
> **Apri**. Lo devi fare solo la prima volta.

### Avvio manuale (se il doppio click non parte)

Apri l'app **Terminale**, incolla queste righe una alla volta (la prima volta) e
premi Invio dopo ciascuna:

```bash
cd "percorso/della/cartella/chatbot"   # trascina qui la cartella per avere il percorso
python3.13 -m venv .venv                # solo la prima volta (va bene anche 3.11/3.12)
./.venv/bin/python -m pip install -r requirements.txt   # solo la prima volta
./.venv/bin/python server.py
```

Le volte successive basta l'ultima riga (`./.venv/bin/python server.py`).
Poi apri il browser su `http://localhost:8000`.

> Serve **Python 3.10 o più recente**. Il `python3` di sistema su alcuni Mac è
> il 3.9 (troppo vecchio): in quel caso usa `python3.11`/`python3.12`/`python3.13`.

---

## 🔑 La chiave API: dove si mette

La "chiave API" è una specie di password che dà all'app il permesso di usare
l'intelligenza artificiale di Anthropic (quella dietro Claude).

L'app la legge **automaticamente dal file `.env` della cartella `gioco`**
(quella accanto a `chatbot`). È lo **stesso file** usato dal gioco, quindi la
chiave la scrivi una volta sola lì e vale per entrambi.

- **Se quel file ha già la riga** `ANTHROPIC_API_KEY=sk-ant-...`, sei a posto:
  non devi fare niente.
- **Se serve impostarla** (o vuoi dare l'app a un collega su un altro computer):
  1. Vai su **console.anthropic.com**, accedi (o registrati).
  2. Cerca **API Keys** → **Create Key** e copia la chiave (inizia con `sk-ant-...`).
  3. Apri il file **`gioco/.env`** e metti (o sostituisci) la riga:
     `ANTHROPIC_API_KEY=sk-ant-...incolla-qui...`
  4. Salva e fai di nuovo doppio click su `avvia.command`.

> L'app cerca la chiave in quest'ordine: variabile d'ambiente del sistema →
> `gioco/.env` → vecchio `CHIAVE_API.txt`. Il primo che la trova vince.

> ⚠️ La chiave è personale e ad ogni utilizzo ha un piccolo costo a consumo.
> Non condividerla pubblicamente e non metterla online (il file `.env` è già
> escluso da Git).

---

## 💬 Cosa puoi chiedere

L'assistente conosce i materiali nelle cartelle **Fase 1**, **Fase 2** e
**Fase 3**. Qualche esempio:

- "Quali sono i piatti che ci fanno guadagnare di più?"
- "Quanto spendiamo ogni mese di costi fissi?"
- "Fammi un grafico degli incassi per giorno della settimana."
- "Cosa lamentano di più i clienti nelle recensioni?"
- "Quanti dipendenti abbiamo e quanto ci costano in totale?"

Puoi anche fare domande di seguito: l'assistente **ricorda** quello di cui
state parlando ("…e di questi, quanti sono a tempo indeterminato?").

---

## 🧩 Cosa c'è dentro la cartella (per curiosità, non serve toccarlo)

- `avvia.command` — il pulsante di accensione.
- `server.py` — il programma che fa funzionare tutto.
- La chiave API vive in `gioco/.env` (non in questa cartella).
- `CHIAVE_API.txt` — vecchio file, usato solo se manca la chiave in `.env`.
- `index.html` — la pagina della chat che vedi nel browser.
- `requirements.txt` — l'elenco degli strumenti che usa.
- `.venv/` e `static/` — cartelle tecniche, create in automatico.

---

## 🆘 Se qualcosa non va

- **Non si apre il browser:** apri tu il browser e vai su `http://localhost:8000`.
- **La chat dice di inserire la chiave:** apri `gioco/.env` e controlla che ci sia
  la riga `ANTHROPIC_API_KEY=sk-ant-...` (vedi la sezione "La chiave API" sopra).
- **Errore "address already in use":** un assistente è già acceso. Chiudi la
  vecchia finestra nera e riprova.
- **Riparte tutto da zero:** se cancelli la cartella `.venv`, al prossimo doppio
  click verrà ricreata da sola (ci mette un minuto).
