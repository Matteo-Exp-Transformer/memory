#!/bin/sh
# Controllo della scheda di progetto, da qualunque cartella.
# Prova prima python, poi python3: su questo PC python3 è l'alias vuoto del
# Microsoft Store, nel cloud Linux spesso c'è solo python3.
# Uso: sh strumenti/controlla-scheda.sh <scheda.md> [...]   (senza argomenti: schede/*.md)
M="$(dirname "$0")/.."
PY=
for c in python python3; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(sys.version_info[0] < 3)' >/dev/null 2>&1; then
    PY=$c
    break
  fi
done
if [ -z "$PY" ]; then
  echo "controlla-scheda: python non trovato (provati python e python3)" >&2
  exit 1
fi

exec "$PY" "$M/strumenti/controlla_scheda.py" "$@"
