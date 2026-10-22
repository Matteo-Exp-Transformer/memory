#!/bin/sh
# Tutti i controlli della repo memory, da qualunque cartella.
# Prova prima python, poi python3: su questo PC python3 è l'alias vuoto del
# Microsoft Store, nel cloud Linux spesso c'è solo python3.
# Uso: sh strumenti/controlli.sh               controlla la memoria
#      sh strumenti/controlli.sh <progetto>    controlla anche lo STATO.md di un progetto
M="$(dirname "$0")/.."
PY=
for c in python python3; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(sys.version_info[0] < 3)' >/dev/null 2>&1; then
    PY=$c
    break
  fi
done
if [ -z "$PY" ]; then
  echo "controlli: python non trovato (provati python e python3)" >&2
  exit 1
fi

# lunghezza, date e link
"$PY" "$M/strumenti/controlla.py" "$M" "$@" || exit 1
# numeri e citazioni devono comparire alla lettera nei raw (esce 0 anche con soli "sospetti")
"$PY" "$M/.claude/skills/karpathy-llm-wiki/scripts/check_evidence.py" "$M" || exit 1
