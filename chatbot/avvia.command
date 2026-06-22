#!/bin/bash
# Avvio dell'Assistente Dati del Ristorante.
# Doppio click su questo file: prepara tutto da solo e apre il browser.

# Vai nella cartella di questo script (così funziona da qualunque punto)
cd "$(dirname "$0")" || exit 1

echo "============================================"
echo "  Assistente Dati del Ristorante"
echo "============================================"
echo

# 1) Serve Python 3.10 o più recente. Cerchiamo il primo disponibile.
PY=""
for cand in python3.13 python3.12 python3.11 python3.10 python3; do
  if command -v "$cand" >/dev/null 2>&1; then
    if "$cand" -c 'import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)' 2>/dev/null; then
      PY="$cand"; break
    fi
  fi
done
if [ -z "$PY" ]; then
  echo "ERRORE: serve Python 3.10 o più recente e non l'ho trovato."
  echo "Installa Python da https://www.python.org/downloads/ e riprova."
  echo
  read -r -p "Premi Invio per chiudere."
  exit 1
fi
echo "Uso $PY ($($PY --version 2>&1))."

# 2) Crea l'ambiente isolato .venv la prima volta (o se è rotto/incompleto)
if [ ! -x ".venv/bin/python" ]; then
  echo "Preparo l'ambiente (ci vuole un minuto)..."
  rm -rf .venv   # rimuove eventuale .venv incompleto copiato da un altro computer
  "$PY" -m venv .venv || { echo "Non riesco a creare .venv"; read -r -p "Premi Invio."; exit 1; }
  ./.venv/bin/python -m pip install --quiet --upgrade pip
  ./.venv/bin/python -m pip install --quiet -r requirements.txt || {
    echo "Errore nell'installazione degli strumenti."; read -r -p "Premi Invio."; exit 1;
  }
  echo "Ambiente pronto."
  echo
fi

# 3) Apri il browser tra qualche secondo (in parallelo all'avvio del server)
( sleep 3; open "http://localhost:8000" ) &

# 4) Avvia il server (resta in ascolto finché non chiudi questa finestra)
echo "Avvio in corso... lascia aperta questa finestra."
echo "Per spegnere l'assistente: chiudi questa finestra."
echo
./.venv/bin/python server.py

echo
read -r -p "Server fermato. Premi Invio per chiudere."
