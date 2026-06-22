# Trattoria della Stella — Gioco d'indagine

Materiali per il gioco di ruolo interattivo presentato allo showcase Unicredit del 23 giugno 2026.

---

## Premessa

**La Trattoria della Stella** è un ristorante romano gestito da Marco Stella. Il locale ha attraversato anni difficili: liquidità risicata, personale instabile, sala nuova mai valorizzata e una presenza online ferma al 2022. Di recente qualcosa di più grave è emerso: irregolarità in magazzino, cassa che non quadra, ordini con fornitori non riconosciuti.

I partecipanti vestono i panni di consulenti ingaggiati per analizzare la situazione, proporre un piano di rilancio e — nella fase finale — scoprire chi sta sabotando dall'interno.

---

## Come si gioca

Il file `restaurant_game.html` contiene l'intera interfaccia di gioco: basta aprirlo nel browser, non serve installare nulla né avviare un server. **Serve però la connessione a internet** per due cose: le icone (caricate da CDN) e l'assistente AI — il testimone della Fase 3 e i commenti del consulente (richiedono una chiave Claude o Gemini). I font del corpo (Poppins) sono inclusi in `fonts/`; i font brand Oddval vanno aggiunti lì (vedi `fonts/README.md`), altrimenti si usa un fallback pulito.

Le tre fasi si sbloccano progressivamente con le **password del facilitatore** (vedi sotto), che sono anche la leva per scandire i tempi della giornata.

## Password facilitatore (una per gate)

Riveli ogni password al momento giusto per controllare il ritmo:

| Gate | Password |
|---|---|
| Sblocca **Fase 2 — Rilancio** | `Un!credit01` |
| Sblocca **Fase 3 — Il sabotatore** | `D4t4p1zz4` |
| Riepilogo finale (dopo l'accusa) | `OhNo!` |
| Reset partita (tra un gruppo e l'altro) | `ResetStella!` |

## Tempi (challenge da 1h30)

| Blocco | Durata |
|---|---|
| Apertura + scenario + setup | ~8 min |
| Tutorial (demo guidata) | ~4 min |
| **Fase 1 — Triage** | ~20 min (i primi **8 min** sono di sola analisi con Claude, poi si simula) |
| **Fase 2 — Rilancio** | ~16 min (lock di **5 min**; a ~7 min lo **chef si licenzia** a sorpresa) |
| **Fase 3 — Indagine** | ~10 min (il cronometro penalizza il tempo) |
| Speech / pitch dei migliori + giuria | ~22 min |

Dettagli operativi completi in `GUIDA_FACILITATORE.md`.

---

## Obiettivi didattici

Il filo conduttore della giornata: mostrare a un pubblico C-level come l'AI generativa diventi un **collaboratore concreto** su dati e decisioni reali — non un gadget. Ogni sezione allena una competenza diversa.

| Sezione | Obiettivo didattico |
|---|---|
| **Tutorial** | Capire il meccanismo base — input → simulazione → risultato — e prendere confidenza con l'idea di lavorare *insieme* a un assistente AI, non da soli. |
| **Fase 1 — Triage** | Usare l'AI per esplorare e dare senso a dati grezzi ed eterogenei (CSV, Excel, database) e costruire una **diagnosi economica**: dove si perdono i soldi, cosa fermare subito. → *analisi esplorativa dei dati assistita da AI*. |
| **Fase 2 — Rilancio** | Trasformare segnali qualitativi ed esterni (recensioni, report di quartiere, trend) in una **strategia**, e riadattare le decisioni a un imprevisto (lo chef si licenzia). → *decisione sotto incertezza e sintesi qualitativa con l'AI*. |
| **Fase 3 — Indagine** | Incrociare fonti **parziali e multimodali** (immagini, audio, chat, tabelle) per arrivare a una conclusione, interrogando un testimone AI e riconoscendo i depistaggi. → *ragionamento multimodale e verifica delle ipotesi*. |
| **Pitch finale** | Raccontare in modo convincente le scelte fatte e ciò che l'AI ha permesso di scoprire. → *comunicazione data-driven*. |

---

## Struttura dei materiali

```
gioco/
├── restaurant_game.html          ← app di gioco (apri nel browser)
│
├── fase1-dati-operativi/         ← Fase 1 — Triage
├── fase2-contesto-mercato/       ← Fase 2 — Rilancio
└── fase3-indagine/               ← Fase 3 — Il sabotatore
```

---

## Fase 1 — Triage

> *Quanto sta davvero male la Trattoria della Stella?*

I partecipanti ricevono i dati operativi grezzi del locale e devono costruirsi un quadro economico prima di poter proporre qualsiasi intervento.

| File | Contenuto |
|---|---|
| `cassa.md` | Situazione liquidità al 2 gennaio 2026 |
| `costi_fissi.xlsx` | Affitti, utenze, rate e costi strutturali |
| `costi_ingredienti.csv` | Prezzi di acquisto per ingrediente |
| `acquisti_magazzino.csv` | Storico ordini a fornitori |
| `menu.xlsx` | Piatti attivi, prezzi di vendita, food cost |
| `personale.csv` | Organico, ore contrattuali, costo mensile |
| `scontrini.sqlite` | Database scontrini (ultimi 12 mesi) |
| `fornitori.md` | Note qualitative su fornitori attivi e alternativi |
| `marketing.md` | Presenza online, spesa marketing 2022–2025 |

---

## Fase 2 — Rilancio

> *C'è un futuro per questo locale? Quale?*

Dati di contesto esterno: cosa dicono i clienti, cosa fa il mercato, cosa succede nel quartiere. Servono per calibrare le proposte di rilancio sulla realtà, non sulla speranza.

| File | Contenuto |
|---|---|
| `recensioni.csv` | Recensioni Google e TheFork (ultimi 18 mesi) |
| `feedback_personale.txt` | Commenti anonimi dalla scatola dei suggerimenti interni |
| `report_quartiere.pdf` | Report demografico e commerciale del quartiere |
| `trend_ristorazione.md` | Articolo di settore — cinque trend del 2026 |

---

## Fase 3 — Il sabotatore

> *Qualcuno sta sabotando il locale dall'interno. Chi?*

Prove fisiche, conversazioni private e testimonianze audio. Ogni indizio è reale ma parziale: servono più fonti incrociate per costruire un caso solido.

```
fase3-indagine/
├── dipendenti.csv              ← anagrafica e turni del personale
├── ordini_fornitori.csv        ← ordini recenti (inclusi quelli sospetti)
├── registro_cassa.csv          ← movimenti cassa giornalieri
├── biglietto_anonimo.png       ← biglietto trovato in magazzino
│
├── chat_whatsapp/              ← screenshot di conversazioni WhatsApp
│   └── descrizione_conversazioni.md   ← testi e contesto delle chat
│
├── foto_magazzino/             ← fotografie dell'area magazzino/retro
│   └── descrizione_foto.md            ← didascalie e piste investigative
│
└── vocali/                     ← messaggi vocali del personale
    └── script_vocali.md               ← trascrizioni e funzione narrativa
```

> **Nota per il facilitatore:** `descrizione_conversazioni.md` e `descrizione_foto.md` contengono le trascrizioni complete e le note di coerenza narrativa. Usarli per calibrare gli indizi da mostrare e in che ordine.

---

## Personaggi principali

| Nome | Ruolo | Note |
|---|---|---|
| **Marco Stella** | Titolare | Gestione operativa, decisioni finali |
| **Elisa Marini** | Responsabile sala | Chiude il giovedì, ha le chiavi del retro |
| **Sara Bianchi** | Cameriera | Difficoltà economiche documentate |
| **Pietro Lombardi** | Magazzino / approvvigionamenti | Gestisce gli ordini fornitori |
| **Diego** | Cucina | Ha segnalato per primo le anomalie sulle bottiglie |
| **Giulia De Santis** | Sala | Testimone involontaria dell'episodio nel vicolo |
| **Matteo** | Sala | Presenza nel gruppo staff, festeggiato nel gruppo compleanno |

---

*Showcase Unicredit — Datapizza, giugno 2026*
