#!/usr/bin/env python3
"""Prova che il controllo delle schede funzioni: una scheda giusta passa, tre sbagliate falliscono ciascuna con il suo errore.

Uso: python strumenti/prova_scheda.py
Esce con 1 se almeno una prova fallisce, altrimenti 0.
"""
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

QUI = Path(__file__).resolve().parent
CONTROLLO = QUI / "controlla_scheda.py"
PROVE = QUI / "prove-scheda"

# file -> testo che deve comparire nell'unico errore (None = deve passare)
ATTESE = {
    "giusta.md": None,
    "manca-campo-r2.md": "criterio 12",
    "senza-livello.md": "livello assente",
    "finito-senza-comando.md": "finito senza comando",
}


def lancia(scheda):
    r = subprocess.run([sys.executable, str(CONTROLLO), str(scheda)],
                       capture_output=True, text=True, encoding="utf-8")
    return r.returncode, [r_ for r_ in r.stdout.splitlines() if r_.startswith("ERRORE")]


def main():
    falliti = 0
    for nome, atteso in ATTESE.items():
        codice, errori = lancia(PROVE / nome)
        if atteso is None:
            perche = None if codice == 0 and not errori else f"doveva passare, invece exit {codice} e {len(errori)} errori"
        elif codice != 1:
            perche = f"doveva fallire con exit 1, invece exit {codice}"
        elif len(errori) != 1:
            perche = f"doveva dare esattamente 1 errore, ne ha dati {len(errori)}"
        elif atteso not in errori[0]:
            perche = f"l'errore non contiene «{atteso}»: {errori[0]}"
        else:
            perche = None
        if perche:
            falliti += 1
            print(f"FALLITO {nome} — {perche}")
        else:
            print(f"OK {nome}")
    print(f"prova_scheda: {falliti} fallite su {len(ATTESE)}")
    return 1 if falliti else 0


if __name__ == "__main__":
    sys.exit(main())
