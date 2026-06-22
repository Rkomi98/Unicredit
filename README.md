# Unicredit — Showcase 23 giugno 2026

Repo ufficiale per lo showcase Datapizza × Unicredit.  
Contiene due deliverable indipendenti: il gioco d'indagine interattivo e le guide operative su Claude Code per Windows.

---

## Struttura del repo

```
Unicredit/
├── gioco/                        ← gioco d'indagine "Trattoria della Stella"
│   ├── restaurant_game.html      ← app completa (aprire nel browser)
│   ├── fase1-dati-operativi/     ← dati finanziari, menu, personale, fornitori
│   ├── fase2-contesto-mercato/   ← recensioni, feedback, trend di settore
│   └── fase3-indagine/           ← chat, foto, vocali e prove investigative
│
├── guide-windows/                ← guide operative Claude Code su Windows
│   ├── build.py                  ← script che genera i file .docx
│   ├── Guida_installazione_Claude_Code_su_Windows.docx
│   ├── Guida_Claude_Code_su_Windows_con_API_key.docx
│   ├── render-standard/          ← render PNG della guida standard
│   └── render-api/               ← render PNG della guida con API key
│
└── README.md                     ← questo file
```

---

## gioco/

Gioco di ruolo interattivo in tre fasi su un ristorante in difficoltà.  
I partecipanti analizzano dati reali, propongono un piano di rilancio e nella fase finale scoprono chi sta sabotando il locale dall'interno.

→ Vedi [`gioco/README.md`](gioco/README.md) per la descrizione completa delle fasi, dei file e dei personaggi.

**Avvio rapido:** aprire `gioco/restaurant_game.html` nel browser. Nessun server richiesto.

---

## guide-windows/

Due guide operative in italiano per installare e configurare Claude Code su PC Windows:

- **Guida standard** — installazione con PowerShell e login browser
- **Guida con API key** — configurazione tramite `ANTHROPIC_API_KEY`

Le guide sono generate programmaticamente da `build.py` (richiede `python-docx`):

```bash
cd guide-windows
pip install python-docx
python build.py
```

I file `.docx` vengono salvati direttamente nella cartella `guide-windows/`.

---

*Datapizza — giugno 2026*
