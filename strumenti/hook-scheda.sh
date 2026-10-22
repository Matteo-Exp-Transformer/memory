#!/bin/sh
# Blocca il commit se una scheda in stage (schede/*.md) non passa il controllo.
# Si lancia dalla radice della repo di un progetto, dentro il suo pre-commit
# (lo mette installa-hook-scheda.sh). Controlla la versione IN STAGE, non quella su disco.
M="$(cd "$(dirname "$0")/.." && pwd)"
FILES="$(git diff --cached --name-only --diff-filter=ACMR -- 'schede/*.md')"
[ -z "$FILES" ] && exit 0

TMP="$(mktemp -d)" || exit 1
trap 'rm -rf "$TMP"' EXIT

# nomi con spazi non gestiti: le schede hanno nome AAAA-MM-GG-argomento.md
LISTA=
for f in $FILES; do
  git checkout-index --prefix="$TMP/" -- "$f" || exit 1
  LISTA="$LISTA $TMP/$f"
done

# shellcheck disable=SC2086
if ! sh "$M/strumenti/controlla-scheda.sh" $LISTA; then
  echo "commit bloccato: la scheda non passa il controllo (vedi skill progetta)" >&2
  exit 1
fi
