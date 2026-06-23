# Guida del facilitatore — Trattoria della Stella

Documento operativo per condurre la challenge dal vivo (showcase Unicredit, audience C-level).
**⚠️ Contiene spoiler e password: non distribuirlo ai partecipanti.**

---

## In breve

- I gruppi giocano **su un solo PC** ciascuno, dall'URL del gioco (`index.html` → "Avvia il gioco", oppure direttamente `restaurant_game.html`).
- Tu controlli il ritmo con le **password per gate**: le riveli una alla volta, al momento giusto.
- Durata totale: **1h30**, inclusi presentazione e speech finali.
- Serve **connessione a internet** (icone + assistente AI) e **una chiave API** (Claude o Gemini).

---

## Prima dell'evento (checklist)

1. **Deploy**: la cartella `gioco/` è pubblicata (es. GitHub Pages). Apri l'URL e verifica che il gioco parta e che le icone si vedano.
2. **Chiave AI**: procurati una chiave **Claude** (`sk-ant-…`) **oppure Gemini** (`AIza…`). Ne basta una. Si inserisce nella schermata iniziale del gioco (campo "Assistente AI") e resta **solo nel browser** del PC. Va inserita su **ogni** PC dei gruppi.
   - Senza chiave: il gioco funziona, ma **il testimone della Fase 2 non risponde** e non compaiono i commenti del consulente. Con chiave tutto attivo.
3. **Materiali**: decidi se i gruppi scaricano i file da soli dall'hub (`index.html`) o se li distribuisci tu (stampati / cartella condivisa). I file con spoiler (`descrizione_*.md`, `script_vocali.md`, questa guida) **non** sono linkati nell'hub: restano a te.
4. **Reset**: se rigiochi con più gruppi sullo stesso PC, tra un turno e l'altro fai **Reset partita** (password sotto).
5. **Prova completa**: gioca un giro intero almeno una volta per prendere confidenza con i tempi.

---

## Agenda (90 minuti)

| Blocco | Durata | Cosa fai |
|---|---|---|
| Apertura + scenario + setup | ~8 min | Presenti la trattoria in crisi, fai inserire nome locale e chiave AI |
| Tutorial (demo guidata) | ~4 min | Mostri **tu** come gli slider diventano numeri; i gruppi non devono completarlo a fondo |
| **Fase 1 — Triage** | ~28 min | Primi **8 min**: solo analisi dati **con Claude**, simulazione bloccata. Poi simulano (max 3 tentativi) |
| **Fase 2 — Indagine** | ~25 min | Parte il cronometro: ogni secondo e ogni accusa sbagliata costano. Trovano il colpevole |
| **Speech / pitch** | ~25 min | I gruppi migliori presentano; la giuria valuta (offline) |

**Dove cambiare i tempi** (nel file `restaurant_game.html`, in alto nello `<script>`):
- `COOLDOWN_MS = { 1: 8*60*1000 }` → minuti di sola analisi (simulazione bloccata) in Fase 1.

Se sei lungo: salta il tutorial per-gruppo (resta solo la tua demo) o accorcia la Fase 2.

---

## Password per gate (la tua leva sui tempi)

Rivela ogni password **solo quando vuoi che i gruppi avanzino**.

| Quando | Password |
|---|---|
| Far entrare in **Fase 2 — Il sabotatore** | `Un!credit01` |
| Andare al **riepilogo finale** (dopo l'accusa giusta) | `OhNo!` |
| **Reset partita** (footer, tra un gruppo e l'altro) | `ResetStella!` |

Le password servono sia ad **avanzare** a fine fase, sia a **sbloccare in anticipo** una fase (pulsante "Sblocca" nella schermata bloccata).

---

## Come funziona l'assistente AI

Due usi distinti, entrambi con chiave attiva (modello: Claude `sonnet-4-6` — consigliato — o in alternativa Gemini `2.5-flash`):

1. **Commento del consulente** (Fase 1): dopo ogni simulazione, l'AI commenta le scelte in modo qualitativo e suggerisce come avvicinarsi all'assetto giusto, **senza svelare la soluzione**.
2. **Testimone "Romano"** (Fase 2): un cliente abituale che ha visto qualcosa la sera del furto. **Risponde solo a domande specifiche** e fa un po' di resistenza (vorrebbe una cena in cambio). Domande utili da suggerire ai gruppi se si bloccano:
   - "Chi hai visto? Com'era?" → donna di sala, capelli scuri raccolti, 35-40 anni.
   - "Cosa portava?" → una borsa/sacco pesante che **tintinnava** (metallo: bottiglie/posate).
   - "È uscita a piedi o in auto?" → in **auto**, parcheggiata nel **vicolo sul retro**.
   - "Quando?" → **giovedì sera tardi**, verso le **23:15**, all'orario di chiusura.

---

## Soluzione dell'indagine (riservata)

**Colpevole: Elisa Marini, responsabile di sala.**

Gli indizi sono parziali: nessuno da solo basta, vanno **incrociati**. Mappa indizio → fonte:

| Indizio | Dove si trova |
|---|---|
| Donna di sala, capelli scuri, auto nel vicolo, giovedì ~23:15 | Testimone "Romano" (chat AI) |
| Elisa chiude **il giovedì**, ha le **chiavi del retro**, ha l'**auto dietro** | `chat_whatsapp` → Silvia/Elisa |
| Tono evasivo, "giovedì porto il resto", "meglio non parlarne sul gruppo" | `vocali/vocale_elisa.mp3` |
| Auto nel vicolo + rumore di tintinnio (bottiglie/posate) | `vocali/vocale_giulia.mp3` |
| Retro di notte, auto scura, **EXIF giovedì 11/12 ore 23:18** | `foto_magazzino/retro_notte_auto_giovedi.jpg` |
| Cassa **"Cantina Velia"** senza bolla, fornitore **assente** dagli ordini | `foto` + incrocio con `ordini_fornitori.csv` |
| Bottiglie e posate mancanti | `foto` (scaffale vini, cassetto posate) + chat gruppo cucina/sala |
| **Ammanchi sistematici di cassa nei turni di Elisa** | `registro_cassa.csv` |
| "Controllate chi chiude la cassa il giovedì… sparisce la merce" | `biglietto_anonimo.png` |

**Depistaggio (red herring): Sara Bianchi.** Ha un forte movente economico (chat e vocale sui debiti), ma **prende la metro, non ha l'auto e non chiude il giovedì**: l'occasione non regge. Serve a premiare chi verifica e non si ferma al movente.

---

## Pitch finale e giuria (offline)

Dopo il riepilogo, ogni gruppo può **esportare la scheda partita** (pulsante nel riepilogo) come base per il pitch.
- Fai presentare i **gruppi migliori** (es. i 3 con saldo finale più alto).
- Criteri di giudizio suggeriti: **qualità delle decisioni** (non solo il punteggio), **uso dell'AI** (come hanno interrogato i dati e il testimone), **chiarezza del racconto** e **tre cose inattese** scoperte o fatte con Claude durante la partita.

---

## Note utili

- **Punteggio**: è un saldo cumulato. Il risultato della Fase 1 è il saldo con cui si entra nell'indagine; nella Fase 2 il tempo e le accuse sbagliate **sottraggono** da quel saldo.
- **3 tentativi per fase**: dopo il terzo le decisioni si bloccano. C'è un pulsante "Dai la soluzione" se un gruppo resta incastrato.
- **Toggle "Atmosfera che si scalda"** (footer): solo estetico, cambia leggermente il colore di sfondo per fase. Lascialo pure attivo.
- **Cambiare il nome del locale**: solo nella schermata iniziale, prima di entrare.
