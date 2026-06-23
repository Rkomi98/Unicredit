// Esempio del file segreto richiesto dal gioco (indizio Fase 2).
// COPIA questo file in "secret.local.js" (stessa cartella) e incolla la passphrase reale.
// secret.local.js è gitignored e NON va committato.
//
// La passphrase serve a decifrare GEMINI_BLOB dentro restaurant_game.html.
// Se cambi la passphrase devi rigenerare anche GEMINI_BLOB (XOR+base64 della stringa
// "GEMINI_API_KEY=...." con la nuova passphrase).
window.__SECRET_PASS = "incolla-qui-la-passphrase";
