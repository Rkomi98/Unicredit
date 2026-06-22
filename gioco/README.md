# Trattoria della Stella — Gioco d'indagine

Materiali per il gioco di ruolo interattivo presentato allo showcase Unicredit del 23 giugno 2026.

---

## Premessa

**La Trattoria della Stella** è un ristorante romano gestito da Marco Stella. Il locale ha attraversato anni difficili: liquidità risicata, personale instabile, sala nuova mai valorizzata e una presenza online ferma al 2022. Di recente qualcosa di più grave è emerso: irregolarità in magazzino, cassa che non quadra, ordini con fornitori non riconosciuti.

I partecipanti vestono i panni di consulenti ingaggiati per analizzare la situazione, proporre un piano di rilancio e — nella fase finale — scoprire chi sta sabotando dall'interno.

---

## Come si gioca

Il file `restaurant_game.html` contiene l'intera interfaccia di gioco, **completamente self-contained**: basta aprirlo nel browser, non richiede server né connessione.

Le tre fasi si sbloccano progressivamente. Il facilitatore gestisce le password di avanzamento e può abilitare il **testimone AI** (richiede una chiave Claude o Gemini) per la Fase 3.

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
