#!/usr/bin/env node
/**
 * Genera i 3 vocali della Fase 3 con la Realtime API di OpenAI (gpt-realtime),
 * con voce e cadenza ROMANESCA guidate dal system prompt (instructions).
 *
 * Requisiti: Node >= 22 (WebSocket nativo), ffmpeg nel PATH, OPENAI_API_KEY nel .env di gioco/.
 * Uso:   node genera_vocali.mjs            (genera tutti e 3)
 *        node genera_vocali.mjs sara       (solo uno: sara | giulia | elisa)
 *
 * Output: vocale_sara.mp3, vocale_giulia.mp3, vocale_elisa.mp3 in questa cartella.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ENV_PATH = path.resolve(__dirname, "../../.env");
const MODEL = "gpt-realtime";
const RATE = 24000; // PCM16 mono in uscita dalla Realtime API

// ── chiave ────────────────────────────────────────────────────────────────
const env = fs.readFileSync(ENV_PATH, "utf8");
const KEY = (env.match(/^OPENAI_API_KEY=(.+)$/m) || [])[1]?.trim();
if (!KEY) { console.error("OPENAI_API_KEY non trovata in", ENV_PATH); process.exit(1); }

// ── persona comune + regola verbatim ────────────────────────────────────────
const BASE = `Sei una persona NATA E CRESCIUTA A ROMA (quartiere Testaccio) che registra una nota vocale di WhatsApp. Parli in DIALETTO ROMANESCO con accento MARCATO e inconfondibile, come un vero romano de Roma: deve sentirsi forte fin dalla prima parola.
Il testo che ricevi è GIÀ SCRITTO in romanesco: pronuncialo ESATTAMENTE come è scritto, parola per parola, senza correggerlo verso l'italiano standard e senza aggiungere, togliere o annunciare nulla. In particolare rispetta:
- il raddoppiamento delle consonanti dove scritto: "robba", "gnente", "be'";
- i troncamenti degli infiniti e dei verbi: "chiede", "caricà", "preoccupà", "fa'", "sta'";
- "nun" al posto di "non"; "er / ar / ner / sur / der" al posto di "il / al / nel / sul / del";
- "me / te / se" al posto di "mi / ti / si"; "'na / 'sto / 'sta" per "una / questo / questa";
- la musicalità calante e strascicata tipica romana, le vocali aperte.
Tono: nota vocale spontanea da telefono, ritmo parlato e realistico, qualche micro-esitazione naturale. Accento romano deciso e credibile, da persona reale — non una macchietta da film.`;

// ── i 3 personaggi ──────────────────────────────────────────────────────────
const VOCALI = {
  sara: {
    voice: "coral",
    instructions: `${BASE}
Personaggio: Sara, donna sui 30 anni. Tono PROVATO e in difficoltà, avvilita, voce bassa e stanca, sull'orlo del pianto trattenuto. Parla piano, come chi si confida con vergogna.`,
    // testo "pulito" = pista canonica (uguale a script_vocali.md)
    text: "Non ce la faccio più. Ho l'affitto, due rate indietro, e mi vergogno pure a chiedere. Al locale faccio finta di niente, ma non so come pago fine mese.",
    // testo dato al modello: stesso significato, scritto in romanesco per l'accento
    phonetic: "Nun ce la faccio più. C'ho l'affitto, du' rate indietro, e me vergogno pure a chiede. Ar locale faccio finta de gnente, ma nun so come pago fine mese.",
  },
  giulia: {
    voice: "shimmer",
    instructions: `${BASE}
Personaggio: Giulia, donna giovane. Tono INCERTO e riluttante, come chi non sa se sta facendo bene a parlare: esita, va un po' a tentoni, e abbassa la voce verso la fine sul "Boh", quasi a minimizzare.`,
    text: "Ti dico una cosa, magari non è niente. L'altra sera dopo la chiusura ho visto una collega caricare delle cose in macchina nel vicolo dietro. Si sentiva tipo tintinnio, bottiglie o posate. Boh.",
    phonetic: "Te dico 'na cosa, magari nun è gnente. L'antra sera dopo la chiusura ho visto 'na collega caricà delle cose in macchina ner vicolo dietro. Se sentiva tipo tintinnìo, bottije o posate. Boh.",
  },
  elisa: {
    voice: "sage",
    instructions: `${BASE}
Personaggio: Elisa, donna sui 35-40 anni. Tono CALMO ma EVASIVO: vuole chiudere il discorso in fretta, suona rassicurante in superficie ma sfuggente, leggermente infastidita dalla domanda. Controllata, non emotiva.`,
    text: "No no, quella roba l'ho già sistemata io. Non ti preoccupare. Giovedì porto il resto e chiudiamo il discorso, va bene? Meglio non parlarne sul gruppo.",
    phonetic: "No no, quella robba l'ho già sistemata io. Nun te preoccupà. Giovedì porto er resto e chiudemo 'sto discorso, va be'? Mejo nun parlanne sur gruppo.",
  },
};

// ── una generazione su WebSocket ─────────────────────────────────────────────
function genera(nome, cfg) {
  return new Promise((resolve, reject) => {
    const url = `wss://api.openai.com/v1/realtime?model=${MODEL}`;
    // Auth via subprotocol (il WebSocket nativo non permette header custom)
    const ws = new WebSocket(url, [
      "realtime",
      "openai-insecure-api-key." + KEY,
    ]);

    const chunks = [];
    let done = false;
    const fail = (e) => { if (!done) { done = true; try { ws.close(); } catch {} reject(e); } };
    const timer = setTimeout(() => fail(new Error("timeout (60s)")), 60000);

    ws.onerror = (e) => fail(new Error("WebSocket error: " + (e?.message || e)));

    ws.onopen = () => {
      ws.send(JSON.stringify({
        type: "session.update",
        session: {
          type: "realtime",
          output_modalities: ["audio"],
          audio: { output: { voice: cfg.voice, format: { type: "audio/pcm", rate: RATE } } },
          instructions: cfg.instructions,
        },
      }));
    };

    ws.onmessage = (ev) => {
      let m; try { m = JSON.parse(ev.data); } catch { return; }
      switch (m.type) {
        case "session.updated":
          // invia il testo da leggere e chiede la risposta audio
          ws.send(JSON.stringify({
            type: "conversation.item.create",
            item: { type: "message", role: "user", content: [{ type: "input_text", text: cfg.phonetic || cfg.text }] },
          }));
          ws.send(JSON.stringify({ type: "response.create" }));
          break;
        case "response.output_audio.delta":
        case "response.audio.delta":
          if (m.delta) chunks.push(Buffer.from(m.delta, "base64"));
          break;
        case "response.done": {
          clearTimeout(timer);
          done = true;
          try { ws.close(); } catch {}
          if (!chunks.length) return reject(new Error("nessun audio ricevuto. Risposta: " + JSON.stringify(m).slice(0, 500)));
          resolve(Buffer.concat(chunks));
          break;
        }
        case "error":
          fail(new Error("API error: " + JSON.stringify(m.error || m)));
          break;
      }
    };
  });
}

// ── PCM16 → mp3 con ffmpeg ───────────────────────────────────────────────────
function pcmToMp3(pcm, outPath) {
  const r = spawnSync("ffmpeg", [
    "-y", "-f", "s16le", "-ar", String(RATE), "-ac", "1", "-i", "pipe:0",
    "-codec:a", "libmp3lame", "-q:a", "4", outPath,
  ], { input: pcm });
  if (r.status !== 0) throw new Error("ffmpeg fallito: " + (r.stderr?.toString().slice(-400) || r.error));
}

// ── main ─────────────────────────────────────────────────────────────────────
const only = process.argv[2];
const targets = only ? [only] : Object.keys(VOCALI);
for (const nome of targets) {
  const cfg = VOCALI[nome];
  if (!cfg) { console.error(`Personaggio sconosciuto: ${nome} (usa: ${Object.keys(VOCALI).join(", ")})`); continue; }
  process.stdout.write(`▶ ${nome} (voce ${cfg.voice})… `);
  try {
    const pcm = await genera(nome, cfg);
    const out = path.join(__dirname, `vocale_${nome}.mp3`);
    pcmToMp3(pcm, out);
    const sec = (pcm.length / 2 / RATE).toFixed(1);
    console.log(`ok → ${path.basename(out)} (${sec}s)`);
  } catch (e) {
    console.log("ERRORE");
    console.error("  ", e.message);
  }
}
