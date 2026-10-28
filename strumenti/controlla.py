#!/usr/bin/env python3
"""Controlli sulla memoria e sui progetti: STATO.md, note di sessione, pagine wiki, link.

Uso: python strumenti/controlla.py [radice ...]   (default: .)
     nel cloud Linux: sh strumenti/controlli.sh
Esce con 1 se c'è almeno un errore, altrimenti 0.
"""
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote

sys.stdout.reconfigure(encoding="utf-8")

SALTA = {".git", "node_modules", ".venv", "dist", "build"}
OGGI = date.today()
RE_AGGIORNATO = re.compile(r"^Aggiornato: (\d{4}-\d{2}-\d{2})")
RE_UPDATED = re.compile(r"^> Updated: (\d{4}-\d{2}-\d{2})")
RE_NOME_NOTA = re.compile(r"^(\d{4}-\d{2}-\d{2})-")
RE_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
RE_INLINE_CODE = re.compile(r"`[^`]*`")

errori, avvisi = 0, 0


def segnala(tipo, percorso, riga, motivo):
    global errori, avvisi
    if tipo == "ERRORE":
        errori += 1
    else:
        avvisi += 1
    print(f"{tipo} {percorso}:{riga} — {motivo}")


def controlla_data(testo, percorso, riga):
    """Segnala data non valida o nel futuro. Ritorna True se tutto ok."""
    try:
        d = date.fromisoformat(testo)
    except ValueError:
        segnala("ERRORE", percorso, riga, f"data non valida: {testo}")
        return False
    if d > OGGI:
        segnala("ERRORE", percorso, riga, f"data nel futuro: {testo} (oggi è {OGGI})")
        return False
    return True


def controlla_link(file, righe):
    in_codice = False
    for n, riga in enumerate(righe, 1):
        if riga.lstrip().startswith("```"):
            in_codice = not in_codice
            continue
        if in_codice:
            continue
        for m in RE_LINK.finditer(RE_INLINE_CODE.sub("", riga)):
            dest = m.group(1)
            if re.match(r"^(https?://|mailto:|#)", dest, re.I):
                continue
            dest = unquote(re.split(r"[#?]", dest, maxsplit=1)[0])
            if dest and not (file.parent / dest).exists():
                segnala("ERRORE", file, n, f"link rotto: {m.group(1)}")


def leggi(file):
    return file.read_text(encoding="utf-8", errors="replace").splitlines()


def controlla_stato(file, righe):
    if len(righe) > 40:
        segnala("ERRORE", file, 41, f"STATO.md ha {len(righe)} righe (massimo 40)")
    m = RE_AGGIORNATO.match(righe[1]) if len(righe) > 1 else None
    if not m:
        segnala("ERRORE", file, 2, "la riga 2 deve iniziare con «Aggiornato: AAAA-MM-GG»")
    else:
        controlla_data(m.group(1), file, 2)


def controlla_nota(file, righe):
    m = RE_NOME_NOTA.match(file.name)
    if not m:
        segnala("ERRORE", file, 1, "il nome deve iniziare con AAAA-MM-GG-")
    else:
        controlla_data(m.group(1), file, 1)
    if len(righe) > 20:
        segnala("ERRORE", file, 21, f"nota di {len(righe)} righe (massimo 20, vedi AGENTS.md)")
    if gia_in_git(file):
        return  # raw/ è immutabile: le note già salvate restano come sono
    costo = next((n for n, r in enumerate(righe, 1) if r.startswith("- **Costo:**")), None)
    if not costo:
        segnala("ERRORE", file, 1, "manca la riga «- **Costo:**» (vedi AGENTS.md)")
    elif not re.search(r"\d", righe[costo - 1].removeprefix("- **Costo:**")):
        segnala("ERRORE", file, costo, "costo senza numeri: lancia strumenti/costo_sessione.py")
    if not any(r.startswith("- **Letti:**") for r in righe):
        segnala("ERRORE", file, 1, "manca la riga «- **Letti:**» con i file letti, serviti o no")


def gia_in_git(file):
    """True se il file è già nell'ultimo commit (allora è una nota vecchia, che non si tocca)."""
    try:
        # In un hook di un worktree collegato Git esporta metadati locali. Ereditandoli,
        # `git -C raw/sessioni` può considerare quella sottocartella il worktree intero.
        # Questa lettura di HEAD riscopre il repository dalla directory del file;
        # la guardia dell'hook sulle modifiche raw continua a usare l'indice originale.
        env = os.environ.copy()
        for nome in ("GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE", "GIT_PREFIX",
                     "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_GRAFT_FILE",
                     "GIT_SHALLOW_FILE", "GIT_IMPLICIT_WORK_TREE"):
            env.pop(nome, None)
        file = file.resolve()
        r = subprocess.run(["git", "-C", str(file.parent), "cat-file", "-e", f"HEAD:./{file.name}"],
                           capture_output=True, env=env)
        return r.returncode == 0
    except OSError:
        return True  # senza git non si distingue: non bloccare le note vecchie


def controlla_pagina_wiki(file, righe):
    trovata = None
    for n, riga in enumerate(righe, 1):
        m = RE_UPDATED.match(riga)
        if m:
            trovata = (n, m.group(1))
            break
    if not trovata:
        segnala("ERRORE", file, 1, "manca la riga «> Updated: AAAA-MM-GG»")
    else:
        controlla_data(trovata[1], file, trovata[0])
    if len(righe) > 150:
        segnala("AVVISO", file, 151, f"pagina lunga {len(righe)} righe (oltre 150)")


def file_da_controllare(radice):
    """Genera (file, tipo) saltando le cartelle escluse."""
    for p in sorted(radice.rglob("*.md")):
        rel = p.relative_to(radice)
        if SALTA & set(rel.parts[:-1]):
            continue
        parti = rel.parts
        if p.name == "STATO.md":
            yield p, "stato"
        elif len(parti) >= 3 and parti[-3:-1] == ("raw", "sessioni"):
            yield p, "nota"
        elif parti[0] == "wiki":
            if rel.as_posix() == "wiki/index.md":
                yield p, "indice"
            elif rel.as_posix() != "wiki/log.md":
                yield p, "wiki"


def main():
    radici = [Path(a) for a in sys.argv[1:]] or [Path(".")]
    for radice in radici:
        if not radice.is_dir():
            segnala("ERRORE", radice, 0, "la radice non esiste")
            continue
        for file, tipo in file_da_controllare(radice):
            righe = leggi(file)
            if tipo == "stato":
                controlla_stato(file, righe)
            elif tipo == "nota":
                controlla_nota(file, righe)
            elif tipo == "wiki":
                controlla_pagina_wiki(file, righe)
            controlla_link(file, righe)
    print(f"controlla: {errori} errori, {avvisi} avvisi")
    return 1 if errori else 0


if __name__ == "__main__":
    sys.exit(main())
