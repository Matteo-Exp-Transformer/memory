#!/usr/bin/env python3
"""Controllo della scheda di progetto (skill progetta): formato, livello, sezioni dei criteri.

Uso: python strumenti/controlla_scheda.py <scheda.md> [...]
     senza argomenti controlla schede/*.md nella cartella corrente
     dove python manca: sh strumenti/controlla-scheda.sh <scheda.md>
Esce con 1 se c'è almeno un errore, altrimenti 0.
Il modello della scheda è .claude/skills/progetta/scheda-modello.md.
"""
import re
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

OGGI = date.today()

NOMI = {
    1: "Valore", 2: "Pre-mortem", 3: "Fattibilità", 4: "Sostenibilità", 5: "Usabilità",
    6: "Finito verificabile", 7: "Brief senza decisioni", 8: "Fetta piccola", 9: "Confini",
    10: "Parallelizzabile", 11: "Costo d'uso", 12: "Aggiungere senza cancellare",
    13: "Leggibile in poco contesto", 14: "Niente duplicati", 15: "Sicurezza",
    16: "Reversibilità", 17: "Produzione",
}
R1 = {1, 6, 7, 8, 9, 11, 15}
R2 = R1 | {3, 4, 5, 12, 13, 14, 16}
R3 = R2 | {2, 17}

RE_SEGNAPOSTO = re.compile(r"<[^<>\n]+>")
RE_CODICE = re.compile(r"`([^`]*)`")
RE_CAMPO = re.compile(r"^([A-Za-zÀ-ÿ ]+?):\s*(.*)$")
RE_SEZIONE = re.compile(r"^##\s+(.*)$")
RE_SEZ_NUM = re.compile(r"^(\d+)\s+(\S.*)$")
RE_LIVELLO = re.compile(r"^R([123])\b", re.I)
RE_FONTE = re.compile(r"\((?:A|M|B)\)")
RE_NIENTE = re.compile(r"^niente\s*[—–-]+\s*(\S.*)$", re.I)

errori = 0


def segnala(percorso, riga, motivo):
    global errori
    errori += 1
    print(f"ERRORE {percorso}:{riga} — {motivo}")


def togli_commenti(riga, in_commento):
    """Toglie i commenti HTML (anche su più righe). Ritorna (testo, ancora_in_commento)."""
    fuori, i = "", 0
    while i < len(riga):
        if in_commento:
            j = riga.find("-->", i)
            if j < 0:
                return fuori, True
            i, in_commento = j + 3, False
        else:
            j = riga.find("<!--", i)
            if j < 0:
                fuori += riga[i:]
                break
            fuori += riga[i:j]
            i, in_commento = j + 4, True
    return fuori, in_commento


def prepara(righe):
    """Per ogni riga: (libera, visibile, pulita, ha_codice).
    libera = senza commenti; visibile = anche senza il contenuto dei blocchi ```;
    pulita = anche senza codice inline (serve per segnaposto e campi);
    ha_codice = c'è codice inline non vuoto oppure un blocco ```."""
    risultato, in_commento, in_blocco = [], False, False
    for r in righe:
        libera, in_commento = togli_commenti(r, in_commento)
        if libera.lstrip().startswith("```"):
            in_blocco = not in_blocco
            risultato.append((libera, "", "", True))
            continue
        if in_blocco:
            risultato.append((libera, "", "", True))
            continue
        inline = any(m.group(1).strip() for m in RE_CODICE.finditer(libera))
        risultato.append((libera, libera, RE_CODICE.sub("", libera), inline))
    return risultato


def controlla_data(testo, percorso, riga):
    try:
        d = date.fromisoformat(testo)
    except ValueError:
        segnala(percorso, riga, f"data non valida: {testo or '(vuota)'}")
        return
    if d > OGGI:
        segnala(percorso, riga, f"data nel futuro: {testo} (oggi è {OGGI})")


def elementi(prep, indici):
    """Elenco puntato '- ': ritorna [(riga_numero, testo)] con le righe di continuazione rientrate."""
    voci = []
    for i in indici:
        visibile = prep[i][1]
        if visibile.startswith("- "):
            voci.append([i + 1, visibile[2:].strip()])
        elif voci and visibile.strip() and visibile[0] in " \t":
            voci[-1][1] += " " + visibile.strip()
    return voci


def controlla_mancanze(prep, indici, percorso, riga_titolo):
    voci = elementi(prep, indici)
    if not voci:
        segnala(percorso, riga_titolo, "«Mancanze e incognite» senza elementi: se non trovi niente, non hai cercato abbastanza")
    for n, testo in voci:
        if testo.startswith("[blocca]"):
            segnala(percorso, n, "mancanza che blocca: niente brief finché non è risolta o declassata")
        elif testo.startswith("[non blocca]"):
            pass
        elif testo.startswith("[aperta]"):
            m = re.search(r"→\s*(\S.*)$", testo)
            if not m:
                segnala(percorso, n, "mancanza [aperta] senza «→» e il fatto che la sblocca")
        else:
            segnala(percorso, n, "mancanza senza classificazione: deve iniziare con [blocca], [non blocca] o [aperta]")


def controlla_ricerche(prep, indici, percorso, riga_titolo):
    piene = [i for i in indici if prep[i][0].strip()]
    if not piene:
        segnala(percorso, riga_titolo, "«Ricerche» vuota: elenca le ricerche con il segno (A), (M) o (B), oppure «niente — motivo»")
        return
    prima = prep[piene[0]][1].strip()
    if len(piene) == 1 and prima.lower().startswith("niente"):
        if not RE_NIENTE.match(prima):
            segnala(percorso, piene[0] + 1, "«niente» senza motivo: scrivi «niente — perché non serve cercare»")
        return
    voci = elementi(prep, indici)
    if not voci:
        segnala(percorso, piene[0] + 1, "nessuna ricerca come elemento «- » (né «niente — motivo»)")
    for n, testo in voci:
        if not RE_FONTE.search(testo):
            segnala(percorso, n, "ricerca senza segno di fonte: aggiungi (A), (M) o (B)")


def controlla_soluzione(prep, indici, percorso, riga_titolo):
    trovati = {}
    for i in indici:
        m = re.match(r"^(Stima|Perché|Cambia se):\s*(.*)$", prep[i][1].strip())
        if m and m.group(1) not in trovati:
            trovati[m.group(1)] = (i + 1, m.group(2).strip())
    for campo in ("Stima", "Perché", "Cambia se"):
        if campo not in trovati:
            segnala(percorso, riga_titolo, f"Soluzione senza «{campo}:»")
            continue
        n, valore = trovati[campo]
        if not valore:
            segnala(percorso, n, f"«{campo}:» vuoto")
        elif campo == "Stima" and not re.match(r"^(alta|media|bassa)\b", valore, re.I):
            segnala(percorso, n, f"Stima non valida: {valore} (alta, media o bassa)")


def controlla(file):
    percorso = str(file)
    try:
        righe = Path(file).read_text(encoding="utf-8-sig", errors="replace").splitlines()
    except OSError as e:
        segnala(percorso, 0, f"file non leggibile: {e.strerror or e}")
        return
    prep = prepara(righe)

    # segnaposto non compilati (fuori da commenti e codice)
    for n, (_, _, pulita, _) in enumerate(prep, 1):
        for m in RE_SEGNAPOSTO.finditer(pulita):
            segnala(percorso, n, f"segnaposto non compilato: {m.group(0)}")

    # sezioni e intestazione
    titoli = []  # (indice_riga, titolo)
    for i, (_, visibile, _, _) in enumerate(prep):
        m = RE_SEZIONE.match(visibile)
        if m:
            titoli.append((i, m.group(1).strip()))
    fine_intestazione = titoli[0][0] if titoli else len(prep)

    campi = {}
    for i in range(fine_intestazione):
        m = RE_CAMPO.match(prep[i][2].strip())
        if m:
            campi.setdefault(m.group(1).strip().lower(), (i + 1, m.group(2).strip()))

    riga_livello = campi.get("livello", (1, ""))[0]

    # Progetto
    if not campi.get("progetto", (0, ""))[1]:
        segnala(percorso, campi.get("progetto", (1,))[0], "«Progetto:» assente o vuoto")

    # Data
    if "data" not in campi:
        segnala(percorso, 1, "«Data:» assente")
    else:
        controlla_data(campi["data"][1], percorso, campi["data"][0])

    # Livello
    livello = None
    if not campi.get("livello", (0, ""))[1]:
        segnala(percorso, 1, "livello assente: scrivi «Livello: R1», «R2» o «R3» con il motivo")
    else:
        m = RE_LIVELLO.match(campi["livello"][1])
        if m:
            livello = int(m.group(1))
        else:
            segnala(percorso, riga_livello, f"livello non valido: {campi['livello'][1]} (deve iniziare con R1, R2 o R3)")

    # Inizio progetto
    inizio_si = False
    if "inizio progetto" in campi:
        n, v = campi["inizio progetto"]
        if v.lower() in ("sì", "si"):
            inizio_si = True
        elif v.lower() != "no":
            segnala(percorso, n, f"«Inizio progetto:» deve essere sì o no, non «{v}»")
    elif livello == 2:
        segnala(percorso, 1, "«Inizio progetto:» assente (obbligatorio a R2: sì o no)")

    # Agenti in parallelo
    agenti = 1
    if "agenti in parallelo" in campi:
        n, v = campi["agenti in parallelo"]
        if re.fullmatch(r"\d+", v) and int(v) >= 1:
            agenti = int(v)
        else:
            segnala(percorso, n, f"«Agenti in parallelo:» deve essere un intero da 1 in su, non «{v}»")

    # contenuto delle sezioni
    sezioni = {}  # chiave -> (riga_titolo, [indici])
    criteri = {}  # numero -> (riga_titolo, [indici])
    for k, (i, titolo) in enumerate(titoli):
        fine = titoli[k + 1][0] if k + 1 < len(titoli) else len(prep)
        corpo = list(range(i + 1, fine))
        m = RE_SEZ_NUM.match(titolo)
        if m and 1 <= int(m.group(1)) <= 17:
            criteri.setdefault(int(m.group(1)), (i + 1, corpo))
        else:
            for nome in ("mancanze", "ricerche", "soluzione"):
                if titolo.lower().startswith(nome):
                    sezioni.setdefault(nome, (i + 1, corpo))

    def vuota(corpo):
        return not any(prep[j][0].strip() for j in corpo)

    # sezioni sempre richieste
    for nome, controllo in (("mancanze", controlla_mancanze), ("ricerche", controlla_ricerche),
                            ("soluzione", controlla_soluzione)):
        if nome not in sezioni:
            segnala(percorso, riga_livello, f"manca la sezione «## {nome.capitalize()}»")
        elif vuota(sezioni[nome][1]):
            segnala(percorso, sezioni[nome][0], f"sezione «{nome.capitalize()}» vuota")
        else:
            controllo(prep, sezioni[nome][1], percorso, sezioni[nome][0])

    # criteri richiesti per livello (senza livello valido non si controllano, tranne il 10)
    richiesti = {}  # numero -> motivo
    if livello:
        base = {1: R1, 2: R2, 3: R3}[livello]
        for n in base:
            richiesti[n] = f"R{livello}"
        if livello == 2 and inizio_si:
            richiesti[2] = "R2 a inizio progetto"
    if agenti > 1:
        richiesti[10] = "Agenti in parallelo > 1"
    for n in sorted(richiesti):
        if n not in criteri or vuota(criteri[n][1]):
            riga = criteri[n][0] if n in criteri else riga_livello
            segnala(percorso, riga, f"criterio {n} ({NOMI[n]}) richiesto a {richiesti[n]}")

    # contenuto di alcuni criteri
    if 6 in criteri and not vuota(criteri[6][1]):
        riga, corpo = criteri[6]
        if not any(prep[j][3] for j in corpo):
            segnala(percorso, riga, "finito senza comando: scrivi il comando tra backtick")
        if not any("deve uscire" in prep[j][0].lower() for j in corpo):
            segnala(percorso, riga, "finito senza cosa deve uscire: scrivi «deve uscire: …»")
    if livello == 3 and 16 in criteri and not vuota(criteri[16][1]):
        riga, corpo = criteri[16]
        if not any(prep[j][3] for j in corpo):
            segnala(percorso, riga, "a R3 il ritorno indietro va provato con un comando")


def main():
    argomenti = sys.argv[1:]
    if argomenti:
        schede = [Path(a) for a in argomenti]
    else:
        schede = sorted(Path("schede").glob("*.md")) if Path("schede").is_dir() else []
        if not schede:
            print("controlla_scheda: nessuna scheda in schede/*.md")
            return 0
    for scheda in schede:
        controlla(scheda)
    print(f"controlla_scheda: {errori} errori su {len(schede)} schede")
    return 1 if errori else 0


if __name__ == "__main__":
    sys.exit(main())
