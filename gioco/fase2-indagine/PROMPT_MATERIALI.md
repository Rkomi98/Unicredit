# Prompt per (ri)generare i materiali multimodali — Fase 2 (indagine)

Prompt pronti all'uso per produrre gli asset dell'indagine in modo **coerente** e di buona qualità.
Le trascrizioni in `chat_whatsapp/descrizione_conversazioni.md`, `foto_magazzino/descrizione_foto.md` e `vocali/script_vocali.md` restano la **ground truth dei contenuti**: i prompt qui sotto li rendono in immagine/audio, non li reinventano.

## Regole di coerenza (valide per ogni asset)

- **Colpevole = Elisa Marini** (responsabile di sala). Ogni indizio è **parziale**: nessun asset deve "risolvere il caso" da solo o fare il nome del colpevole.
- **Sara Bianchi è un depistaggio**: movente economico sì, ma niente auto e non chiude il giovedì.
- Lingua **italiana**, ambientazione: trattoria romana a Testaccio, inverno 2025.
- Nei nomi usa il roster aggiornato: lo **chef è Lorenzo Pace** (non più "Bruno").
- Niente watermark, niente loghi di brand reali, niente testo storto/illeggibile.

---

## 1. Screenshot WhatsApp

**Strumento consigliato:** image-gen che renda testo nitido (es. Gemini "Nano Banana" / GPT-image / Ideogram). Formato verticale **1080×2160** (mockup schermo telefono), UI WhatsApp realistica in **italiano**: barra in alto con nome contatto/gruppo e foto profilo generica, bolle verdi a destra (mittente) e bianche/grigie a sinistra, orari accanto ai messaggi, doppia spunta blu, sfondo classico WhatsApp. **Nessun numero di telefono visibile.**

> Nota coerenza: nelle **chat private** in alto compare **solo il nome dell'altra persona** (non quello di chi fa lo screenshot). Nei **gruppi** compare il nome del gruppo e, dentro le bolle, il nome di ciascun mittente.

### screen_giulia_sara.png — chat privata (telefono di Giulia, contatto in alto: **Sara Bianchi**)
Rendi questa conversazione (Sara = bolle a sinistra, Giulia = bolle verdi a destra), orari serali plausibili:
```
Sara:  Giu scusa l'ora, posso chiederti una cosa al volo?
Giulia: Dimmi
Sara:  Ti rientrano quei 200 che mi avevi detto? Anche meno, giuro che te li ridò il 27.
Giulia: Questo mese non riesco, mi spiace. Tutto ok?
Sara:  Sì sì. Solo affitto e rata che si sono messi d'accordo per arrivare insieme.
Giulia: Domani fai chiusura?
Sara:  No, pranzo e poi metro. Per fortuna almeno quella non costa come la benzina.
Giulia: Ok. Ne parliamo domani senza gruppo.
```

### screen_silvia_elisa.png — chat privata (telefono di Silvia, contatto in alto: **Elisa Marini**)
```
Silvia: Eli io dopo Conti devo scappare. Ti lascio il foglio consegne sul mobiletto?
Elisa:  Sì, mettilo lì. Poi sistemo io quando chiudo.
Silvia: Anche il registro? Marco lo voleva aggiornato.
Elisa:  Sì. Tanto il giovedì finisce sempre a me, ormai lo sai.
Silvia: Ok. Le chiavi del retro?
Elisa:  Le tengo io. Ho lasciato la macchina dietro, così domani passo presto prima del pranzo.
```

### screen_sara_pietro.png — chat privata (telefono di Sara, contatto in alto: **Pietro Lombardi**)
```
Pietro: Domani riesci a passare dal retro prima del pranzo?
Sara:   Solo dieci minuti, poi devo andare in sala.
Pietro: Mi basta. Ti lascio due cassette vuote da mettere vicino al banco.
Sara:   Ok, ma scrivilo anche sul foglio o poi sembra sempre che sparisca qualcosa.
```

### cucina_sala.png — gruppo (nome in alto: **Stella - cucina/sala**)
Bolle con nome mittente in cima a ciascuna:
```
Diego:  Scusate, ieri sera ho ricontato il rosso della mensola bassa e non mi torna.
Pietro: Non spostate cartoni senza segnarlo, altrimenti poi sembra che manchi roba.
Matteo: Io ho preso solo due bottiglie per la sala grande, segnate sul foglio.
Elisa:  Evitiamo processi sul gruppo. Domani controllo io con Pietro.
Diego:  Ok, ma non è la prima volta. Anche le posate da sala erano contate diverse.
```

### compleanno_matteo.png — gruppo informale (nome in alto: **Compleanno Matteo**)
```
Giulia:  Domenica dopo servizio facciamo una tortina per Matteo?
Marta:   Io porto le candeline, ma niente casino in cucina.
Lorenzo: Confermo: niente casino in cucina.
Silvia:  Io ci sono dopo le 23. Tenetemi una fetta.
```
> Serve solo a rendere il set realistico: nessun indizio. **Usa "Lorenzo", non "Bruno".**

---

## 2. Foto magazzino

**Strumento consigliato:** image-gen fotorealistico. Formato **orizzontale 1600×1066**, luce da magazzino/retro cucina, stile foto da smartphone (leggermente imperfetta, non da catalogo). Eventuali note a mano devono essere **leggibili**.

### scaffale_vini_mancanti.png
> Foto di uno scaffale del magazzino vini, più ripiani. Sul **ripiano basso del vino rosso** alcune posizioni sono **vuote** e segnate a matita come dopo un controllo inventario. In basso un foglietto/nota a mano: **"Nota Pietro: mensola bassa del rosso incompleta rispetto al conteggio."** Realistico, non drammatizzato.

### cassa_fornitore_non_in_lista.png
> Area consegne del retro cucina. Diverse casse di fornitori noti con etichette leggibili: **Ortofrutta Conti**, **Dispense de la sora Lella**, **Caseificio Sabelli**. In primo piano, **separata e bordata di rosso**, una cassa con la scritta **"Cantina de Frascati – vino misto – 12 bt"**. Sotto, una nota: **"Cassa trovata nel retro senza bolla allegata. Da ricontrollare con gli ordini."**

### cassetto_posate_vuoti.png
> Cassetto portaposate di sala visto dall'alto: alcuni scomparti quasi pieni, altri con **vuoti evidenti**, soprattutto **cucchiai e coltelli**. Piccola didascalia interna: **"vuoti anomali in cucchiai e coltelli da sala"**.

### retro_notte_auto_giovedi.jpg
> Retro del locale **di notte**: porta di servizio, pavimento esterno bagnato, e la **sagoma di un'auto scura** parcheggiata nel **vicolo** dietro. Atmosfera notturna, poca luce, foto da telefono.
>
> ⚠️ **EXIF**: gli image-gen **non** producono metadati affidabili. Dopo aver generato l'immagine, re-inietta la data/ora con un tool (es. `exiftool`):
> ```
> exiftool "-DateTimeOriginal=2025:12:11 23:18:42" "-CreateDate=2025:12:11 23:18:42" retro_notte_auto_giovedi.jpg
> ```
> (giovedì 11 dicembre 2025, ore 23:18 — è una **pista bonus**: la soluzione non deve dipendere dall'EXIF perché molti tool lo rimuovono.)

---

## 3. Biglietto anonimo — `biglietto_anonimo.png`

**Strumento consigliato:** image-gen. **Versione pulita** (l'attuale ha testo "fantasma" sovrapposto). Formato **1200×860**, sfondo carta avorio leggermente texturizzata, calligrafia a mano **nitida e leggibile**, penna scura, tono concitato ma controllato. **Un solo livello di testo, niente doppioni/ombre di testo.** Testo esatto:

```
Non è giusto.
Controllate meglio chi chiude la cassa il giovedì sera —
i conti non tornano e sparisce pure la merce.
Un dipendente che non ci sta più.
```
> Indica "chi chiude la cassa il giovedì" (→ Elisa) senza fare nomi.

---

## 4. Vocali (TTS)

**Come si rigenerano:** script pronto `vocali/genera_vocali.mjs` — usa la **Realtime API di OpenAI** (`gpt-realtime`) con la cadenza **romanesca** guidata dal system prompt, una voce distinta per personaggio (Sara=coral, Giulia=shimmer, Elisa=sage). Richiede `OPENAI_API_KEY` nel `.env` di `gioco/`, Node ≥ 22 e `ffmpeg`.

```
cd gioco/fase2-indagine/vocali
node genera_vocali.mjs            # genera tutti e 3
node genera_vocali.mjs sara       # solo uno: sara | giulia | elisa
```

Come arriva l'accento: la cadenza romana vera non viene dalle sole istruzioni (il modello pronuncia ciò che è scritto), ma dal fatto che ogni personaggio nella mappa `VOCALI` ha due testi — `text` (italiano pulito = pista canonica, uguale a `script_vocali.md`) e `phonetic` (lo stesso testo riscritto in romanesco: "nun", "er/ar/ner/sur", "me/te/se", troncamenti come "chiede/caricà/preoccupà", raddoppiamenti come "robba/gnente"). Lo script dà al modello la versione `phonetic`, così l'accento si sente; il significato e le piste restano identici. Per ritoccare voce, tono o intensità del dialetto basta editare la mappa `VOCALI` in cima al file. Esporta in **.mp3** mono ~10–15 s. I testi (versione pulita):

### vocale_sara.mp3 — donna ~30 anni, tono **provato/in difficoltà**, voce bassa
```
Non ce la faccio più. Ho l'affitto, due rate indietro, e mi vergogno pure a chiedere.
Al locale faccio finta di niente, ma non so come pago fine mese.
```

### vocale_giulia.mp3 — donna giovane, tono **incerto, quasi riluttante** ("magari non è niente")
```
Ti dico una cosa, magari non è niente. L'altra sera dopo la chiusura ho visto una collega
caricare delle cose in macchina nel vicolo dietro. Si sentiva tipo tintinnio, bottiglie o posate. Boh.
```

### vocale_elisa.mp3 — donna ~35-40 anni, tono **calmo ma evasivo**, vuole chiudere il discorso
```
No no, quella roba l'ho già sistemata io. Non ti preoccupare.
Giovedì porto il resto e chiudiamo il discorso, va bene? Meglio non parlarne sul gruppo.
```

---

## Dopo la rigenerazione

- Mantieni gli **stessi nomi file** (sono referenziati da `index.html` e dalle descrizioni).
- Aggiorna, se serve, le didascalie in `descrizione_conversazioni.md` / `descrizione_foto.md`.
- Verifica leggibilità su schermo proiettato (i C-level li guarderanno da lontano): testo grande, contrasto alto.
