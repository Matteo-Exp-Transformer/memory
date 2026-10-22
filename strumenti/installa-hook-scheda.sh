#!/bin/sh
# Installa nel pre-commit di una repo di progetto il controllo delle schede.
# Uso: sh strumenti/installa-hook-scheda.sh <repo progetto>
# Si può rilanciare: se la riga c'è già non fa niente.
if [ -z "$1" ] || ! git -C "$1" rev-parse --git-dir >/dev/null 2>&1; then
  echo "uso: sh strumenti/installa-hook-scheda.sh <repo progetto>  (deve essere una repo git)" >&2
  exit 1
fi
REPO="$(cd "$1" && pwd)"
M="$(cd "$(dirname "$0")/.." && pwd)"
MARCA="# scheda-progetto (memory)"
RIGA="sh \"$M/strumenti/hook-scheda.sh\" || exit 1  $MARCA"

HOOKS="$(git -C "$REPO" rev-parse --git-path hooks)"
case "$HOOKS" in
  /* | [A-Za-z]:*) ;;               # già assoluto (anche C:/ su Windows)
  *) HOOKS="$REPO/$HOOKS" ;;        # relativo alla radice della repo
esac
mkdir -p "$HOOKS"
PC="$HOOKS/pre-commit"

if [ ! -f "$PC" ]; then
  printf '#!/bin/sh\n%s\n' "$RIGA" > "$PC"
  chmod +x "$PC"
  echo "creato $PC con il controllo delle schede"
elif grep -qF "$MARCA" "$PC"; then
  echo "già installato in $PC: non cambio niente"
else
  TMP="$(mktemp)" || exit 1
  if head -n 1 "$PC" | grep -q '^#!'; then
    { head -n 1 "$PC"; printf '%s\n' "$RIGA"; tail -n +2 "$PC"; } > "$TMP"
    DOVE="subito dopo lo shebang"
  else
    { printf '%s\n' "$RIGA"; cat "$PC"; } > "$TMP"
    DOVE="in testa"
  fi
  cat "$TMP" > "$PC"
  rm -f "$TMP"
  chmod +x "$PC"
  echo "aggiunto il controllo delle schede a $PC ($DOVE)"
fi
