#!/usr/bin/env python3
"""Controlla che una o più cartucce della Palestra rispettino il formato (palestra/CARTUCCE.md).

Uso:   python palestra/strumenti/valida_cartuccia.py file1.json [file2.json ...]
       python palestra/strumenti/valida_cartuccia.py --json file.json   (stampa gli errori come lista JSON)
Esce con 1 se almeno una cartuccia ha errori.
La pagina (palestra.html) contiene la stessa logica in JavaScript: le due devono dare lo stesso esito.
"""
import json
import re
import sys
from datetime import date

sys.stdout.reconfigure(encoding="utf-8")

RE_ID = re.compile(r"^[a-z0-9][a-z0-9-]{1,59}$")
ZONE = {"banco", "campo"}
TIPI_CON_FIDUCIA = {"stima", "scelta", "duello", "ordina", "previsione"}
COMUNI = {"id", "tipo", "titolo", "testo", "dominio", "concetti"}
CAMPI = {
    "racconto": (set(), set()),
    "stima": ({"unita", "risposta", "tolleranza", "spiegazione"}, set()),
    "scelta": ({"opzioni", "giusta", "spiegazione"}, set()),
    "duello": ({"vincoli", "opzioni", "migliore", "spiegazione", "domanda_ribalta"}, set()),
    "ordina": ({"elementi", "spiegazione"}, set()),
    "previsione": ({"unita", "collegata_a", "tolleranza_percento"}, set()),
    "simulatore": ({"parametri", "uscite"}, {"nota"}),
    "mio_modello": ({"unita_riga", "uscite"}, {"righe_iniziali", "costanti"}),
    "spiega": ({"parole_chiave", "max_frasi"}, set()),
    "aperta": (set(), {"suggerimento"}),
    "carte": ({"carte", "ripasso"}, set()),
    "cronometro": ({"fasi", "consegna", "min_giri"}, set()),
    "fascicolo": ({"voci"}, set()),
}
RADICE_OBBL = {"formato", "id", "versione", "titolo", "zona", "creata", "autore", "concetti", "durata_minuti", "blocchi"}
RADICE_FAC = {"finito_suggerito", "note_per_agenti"}
FUNZIONI = {"min": -1, "max": -1, "ceil": 1, "floor": 1, "round": 1, "abs": 1, "se": 3}


# ---------- espressioni: stessa grammatica di motore/espressioni.js ----------
def tokenizza(testo):
    t, i = [], 0
    while i < len(testo):
        c = testo[i]
        if c in " \t\n":
            i += 1
            continue
        if c in "0123456789.":
            j = i
            while j < len(testo) and testo[j] in "0123456789.":
                j += 1
            s = testo[i:j]
            if not re.fullmatch(r"\d+\.?\d*|\.\d+", s):
                raise ValueError(f"numero non valido: {s}")
            t.append(("num", s))
            i = j
            continue
        if c.isascii() and (c.isalpha() or c == "_"):
            k = i
            while k < len(testo) and (testo[k].isalnum() or testo[k] == "_") and testo[k].isascii():
                k += 1
            t.append(("id", testo[i:k]))
            i = k
            continue
        due = testo[i:i + 2]
        if due in ("<=", ">=", "==", "!="):
            t.append(("op", due))
            i += 2
            continue
        if c in "+-*/(),<>":
            t.append(("op", c))
            i += 1
            continue
        raise ValueError(f"carattere non ammesso: «{c}»")
    return t


def variabili_espressione(testo):
    """Analizza l'espressione e restituisce le variabili usate; ValueError se non è valida."""
    t = tokenizza(testo)
    p = [0]
    usate = []

    def guarda():
        return t[p[0]] if p[0] < len(t) else None

    def prendi(v):
        x = guarda()
        if not x or x[1] != v:
            raise ValueError(f"atteso «{v}»")
        p[0] += 1

    def confronto():
        somma()
        x = guarda()
        if x and x[0] == "op" and x[1] in ("<", "<=", ">", ">=", "==", "!="):
            p[0] += 1
            somma()

    def somma():
        prodotto()
        while (x := guarda()) and x[0] == "op" and x[1] in "+-" and len(x[1]) == 1:
            p[0] += 1
            prodotto()

    def prodotto():
        unario()
        while (x := guarda()) and x[0] == "op" and x[1] in ("*", "/"):
            p[0] += 1
            unario()

    def unario():
        x = guarda()
        if x and x == ("op", "-"):
            p[0] += 1
            unario()
        else:
            primario()

    def primario():
        x = guarda()
        if not x:
            raise ValueError("espressione incompleta")
        if x[0] == "num":
            p[0] += 1
            return
        if x[0] == "id":
            p[0] += 1
            y = guarda()
            if y and y[1] == "(":
                if x[1] not in FUNZIONI:
                    raise ValueError(f"funzione sconosciuta: {x[1]}")
                p[0] += 1
                n = 0
                if guarda() and guarda()[1] != ")":
                    confronto()
                    n = 1
                    while guarda() and guarda()[1] == ",":
                        p[0] += 1
                        confronto()
                        n += 1
                prendi(")")
                atteso = FUNZIONI[x[1]]
                if (atteso >= 0 and n != atteso) or (atteso < 0 and n < 1):
                    raise ValueError(f"numero di argomenti sbagliato per {x[1]}")
                return
            if x[1] in FUNZIONI:
                raise ValueError(f"{x[1]} è una funzione: usala con le parentesi")
            if x[1] not in usate:
                usate.append(x[1])
            return
        if x[1] == "(":
            p[0] += 1
            confronto()
            prendi(")")
            return
        raise ValueError(f"simbolo inatteso: «{x[1]}»")

    confronto()
    if p[0] < len(t):
        raise ValueError(f"simbolo in più: «{t[p[0]][1]}»")
    return usate


# ---------- controlli ----------
def testo_ok(v):
    return isinstance(v, str) and v.strip() != ""


def intero(v):
    return isinstance(v, int) and not isinstance(v, bool)


def numero(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def valida(c):
    """Restituisce la lista degli errori (vuota = cartuccia valida)."""
    e = []
    if not isinstance(c, dict):
        return ["la cartuccia deve essere un oggetto JSON"]
    for k in RADICE_OBBL - c.keys():
        e.append(f"manca il campo «{k}»")
    for k in c.keys() - RADICE_OBBL - RADICE_FAC:
        e.append(f"campo sconosciuto «{k}»")
    if c.get("formato") != 1:
        e.append("«formato» deve essere 1")
    if not (isinstance(c.get("id"), str) and RE_ID.match(c["id"])):
        e.append("«id»: solo minuscole, cifre e trattini, da 2 a 60 caratteri")
    if not (intero(c.get("versione")) and c["versione"] >= 1):
        e.append("«versione» deve essere un intero ≥ 1")
    for k in ("titolo", "autore"):
        if k in c and not testo_ok(c[k]):
            e.append(f"«{k}» deve essere un testo non vuoto")
    if c.get("zona") not in ZONE:
        e.append("«zona» deve essere «banco» o «campo»")
    try:
        date.fromisoformat(c.get("creata", ""))
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", c.get("creata", "")):
            raise ValueError
    except (ValueError, TypeError):
        e.append("«creata» deve essere una data AAAA-MM-GG")
    if not (intero(c.get("durata_minuti")) and 1 <= c["durata_minuti"] <= 120):
        e.append("«durata_minuti» deve essere un intero tra 1 e 120")
    for k in ("finito_suggerito", "note_per_agenti"):
        if k in c and not testo_ok(c[k]):
            e.append(f"«{k}» deve essere un testo non vuoto")
    concetti = set()
    if not (isinstance(c.get("concetti"), list) and c["concetti"]):
        e.append("«concetti» deve essere una lista con almeno un concetto")
    else:
        for i, x in enumerate(c["concetti"]):
            if not (isinstance(x, dict) and set(x.keys()) == {"id", "nome"}
                    and isinstance(x["id"], str) and RE_ID.match(x["id"]) and testo_ok(x["nome"])):
                e.append(f"concetti[{i}]: serve {{\"id\", \"nome\"}} con id in minuscole e trattini")
            elif x["id"] in concetti:
                e.append(f"concetti[{i}]: id ripetuto «{x['id']}»")
            else:
                concetti.add(x["id"])
    blocchi = c.get("blocchi")
    if not (isinstance(blocchi, list) and 1 <= len(blocchi) <= 25):
        e.append("«blocchi» deve essere una lista da 1 a 25 blocchi")
        return e
    ids, domini, tipi = set(), set(), []
    cronometri = {b.get("id") for b in blocchi if isinstance(b, dict) and b.get("tipo") == "cronometro"}
    for i, b in enumerate(blocchi):
        dove = f"blocchi[{i}]"
        if not isinstance(b, dict):
            e.append(f"{dove}: deve essere un oggetto")
            continue
        tipo = b.get("tipo")
        if tipo not in CAMPI:
            e.append(f"{dove}: tipo sconosciuto «{tipo}»")
            continue
        tipi.append(tipo)
        dove = f"blocchi[{i}] ({tipo} «{b.get('id')}»)"
        obbl, fac = CAMPI[tipo]
        for k in (obbl | {"id", "tipo", "testo", "dominio"}) - b.keys():
            e.append(f"{dove}: manca «{k}»")
        for k in b.keys() - obbl - fac - COMUNI:
            e.append(f"{dove}: campo sconosciuto «{k}»")
        bid = b.get("id")
        if not (isinstance(bid, str) and RE_ID.match(bid)):
            e.append(f"{dove}: «id» in minuscole, cifre e trattini")
        elif bid in ids:
            e.append(f"{dove}: id ripetuto")
        else:
            ids.add(bid)
        for k in ("testo", "dominio"):
            if k in b and not testo_ok(b[k]):
                e.append(f"{dove}: «{k}» deve essere un testo non vuoto")
        if testo_ok(b.get("dominio")):
            domini.add(b["dominio"].strip().lower())
        if "titolo" in b and not testo_ok(b["titolo"]):
            e.append(f"{dove}: «titolo» deve essere un testo non vuoto")
        if "concetti" in b:
            if not (isinstance(b["concetti"], list) and all(x in concetti for x in b["concetti"])):
                e.append(f"{dove}: «concetti» deve elencare id presenti nei concetti della cartuccia")
        e.extend(controlla_tipo(tipo, b, dove, cronometri))
    if c.get("zona") == "banco":
        if len(domini) < 2:
            e.append("zona banco: servono blocchi in almeno 2 domini diversi (trasferimento)")
        if not TIPI_CON_FIDUCIA & set(tipi):
            e.append("zona banco: serve almeno un blocco stima, scelta, duello, ordina o previsione")
    return e


def lista_opzioni(b, dove, campi_obbl, e):
    ops = b.get("opzioni")
    if not (isinstance(ops, list) and len(ops) >= 2):
        e.append(f"{dove}: «opzioni» deve avere almeno 2 opzioni")
        return set()
    viste = set()
    for j, o in enumerate(ops):
        if not (isinstance(o, dict) and set(o.keys()) == campi_obbl):
            e.append(f"{dove}: opzioni[{j}] deve avere esattamente {sorted(campi_obbl)}")
            continue
        if not (isinstance(o["id"], str) and RE_ID.match(o["id"])):
            e.append(f"{dove}: opzioni[{j}].id in minuscole e trattini")
        elif o["id"] in viste:
            e.append(f"{dove}: opzioni[{j}].id ripetuto")
        viste.add(o["id"])
        for k in campi_obbl - {"id"}:
            if not testo_ok(o[k]):
                e.append(f"{dove}: opzioni[{j}].{k} deve essere un testo non vuoto")
    return viste


def controlla_uscite(b, dove, permesse, e):
    us = b.get("uscite")
    if not (isinstance(us, list) and us):
        e.append(f"{dove}: «uscite» deve avere almeno un'uscita")
        return
    viste = set()
    for j, u in enumerate(us):
        if not (isinstance(u, dict) and set(u.keys()) == {"id", "nome", "formula", "decimali", "unita"}):
            e.append(f"{dove}: uscite[{j}] deve avere id, nome, formula, decimali, unita")
            continue
        if not (isinstance(u["id"], str) and RE_ID.match(u["id"])) or u["id"] in viste:
            e.append(f"{dove}: uscite[{j}].id non valido o ripetuto")
        viste.add(u["id"])
        if not testo_ok(u["nome"]) or not isinstance(u["unita"], str):
            e.append(f"{dove}: uscite[{j}]: nome non vuoto, unita testo (anche vuoto)")
        if not (intero(u["decimali"]) and 0 <= u["decimali"] <= 4):
            e.append(f"{dove}: uscite[{j}].decimali tra 0 e 4")
        try:
            usate = variabili_espressione(u["formula"]) if isinstance(u["formula"], str) else None
            if usate is None:
                raise ValueError("la formula deve essere un testo")
            ignote = [v for v in usate if v not in permesse]
            if ignote:
                e.append(f"{dove}: uscite[{j}].formula usa variabili sconosciute {ignote}")
        except ValueError as err:
            e.append(f"{dove}: uscite[{j}].formula non valida: {err}")


def controlla_tipo(tipo, b, dove, cronometri):
    e = []
    if tipo == "stima":
        if not numero(b.get("risposta")):
            e.append(f"{dove}: «risposta» deve essere un numero")
        if not (numero(b.get("tolleranza")) and b["tolleranza"] >= 0):
            e.append(f"{dove}: «tolleranza» deve essere un numero ≥ 0")
        if not isinstance(b.get("unita"), str):
            e.append(f"{dove}: «unita» deve essere un testo (anche vuoto)")
        if not testo_ok(b.get("spiegazione")):
            e.append(f"{dove}: «spiegazione» non vuota")
    elif tipo == "scelta":
        ids = lista_opzioni(b, dove, {"id", "testo", "conseguenza"}, e)
        if b.get("giusta") not in ids:
            e.append(f"{dove}: «giusta» deve essere l'id di un'opzione")
        if not testo_ok(b.get("spiegazione")):
            e.append(f"{dove}: «spiegazione» non vuota")
    elif tipo == "duello":
        ids = lista_opzioni(b, dove, {"id", "testo", "perche_plausibile", "conseguenza"}, e)
        if not (b.get("migliore") is None or b.get("migliore") in ids):
            e.append(f"{dove}: «migliore» deve essere null o l'id di un'opzione")
        v = b.get("vincoli")
        if not (isinstance(v, list) and v and all(testo_ok(x) for x in v)):
            e.append(f"{dove}: «vincoli» deve avere almeno un vincolo testuale")
        for k in ("spiegazione", "domanda_ribalta"):
            if not testo_ok(b.get(k)):
                e.append(f"{dove}: «{k}» non vuota")
    elif tipo == "ordina":
        el = b.get("elementi")
        if not (isinstance(el, list) and len(el) >= 3):
            e.append(f"{dove}: «elementi» deve avere almeno 3 elementi, nell'ordine giusto")
        else:
            viste = set()
            for j, x in enumerate(el):
                if not (isinstance(x, dict) and set(x.keys()) == {"id", "testo"} and isinstance(x["id"], str)
                        and RE_ID.match(x["id"]) and testo_ok(x["testo"])) or x.get("id") in viste:
                    e.append(f"{dove}: elementi[{j}] deve essere {{id, testo}} con id unico")
                else:
                    viste.add(x["id"])
        if not testo_ok(b.get("spiegazione")):
            e.append(f"{dove}: «spiegazione» non vuota")
    elif tipo == "previsione":
        if b.get("collegata_a") not in cronometri:
            e.append(f"{dove}: «collegata_a» deve essere l'id di un blocco cronometro di questa cartuccia")
        if not (numero(b.get("tolleranza_percento")) and 0 < b["tolleranza_percento"] <= 100):
            e.append(f"{dove}: «tolleranza_percento» tra 0 e 100")
        if not isinstance(b.get("unita"), str):
            e.append(f"{dove}: «unita» deve essere un testo")
    elif tipo == "simulatore":
        ps = b.get("parametri")
        nomi = set()
        if not (isinstance(ps, list) and ps):
            e.append(f"{dove}: «parametri» deve avere almeno un parametro")
        else:
            for j, q in enumerate(ps):
                chiavi = {"id", "nome", "min", "max", "passo", "valore", "unita"}
                if not (isinstance(q, dict) and set(q.keys()) == chiavi):
                    e.append(f"{dove}: parametri[{j}] deve avere {sorted(chiavi)}")
                    continue
                if not (isinstance(q["id"], str) and re.fullmatch(r"[a-z_][a-z0-9_]*", q["id"])) or q["id"] in nomi \
                        or q["id"] in FUNZIONI:
                    e.append(f"{dove}: parametri[{j}].id: minuscole, cifre e _ (niente trattini: è una variabile)")
                nomi.add(q["id"])
                if not all(numero(q[k]) for k in ("min", "max", "passo", "valore")):
                    e.append(f"{dove}: parametri[{j}]: min, max, passo, valore numerici")
                elif not (q["min"] < q["max"] and q["passo"] > 0 and q["min"] <= q["valore"] <= q["max"]):
                    e.append(f"{dove}: parametri[{j}]: serve min < max, passo > 0, min ≤ valore ≤ max")
                if not testo_ok(q["nome"]) or not isinstance(q["unita"], str):
                    e.append(f"{dove}: parametri[{j}]: nome non vuoto, unita testo")
        controlla_uscite(b, dove, nomi, e)
        if "nota" in b and not testo_ok(b["nota"]):
            e.append(f"{dove}: «nota» non vuota")
    elif tipo == "mio_modello":
        permesse = {"somma", "righe"}
        for j, q in enumerate(b.get("costanti", [])):
            if not (isinstance(q, dict) and set(q.keys()) == {"id", "nome", "valore"}
                    and isinstance(q["id"], str) and re.fullmatch(r"[a-z_][a-z0-9_]*", q["id"])
                    and q["id"] not in permesse and numero(q["valore"]) and testo_ok(q["nome"])):
                e.append(f"{dove}: costanti[{j}] deve essere {{id (variabile), nome, valore numerico}}")
            else:
                permesse.add(q["id"])
        if not isinstance(b.get("costanti", []), list):
            e.append(f"{dove}: «costanti» deve essere una lista")
        ri = b.get("righe_iniziali", [])
        if not (isinstance(ri, list) and all(isinstance(r, dict) and set(r.keys()) == {"nome", "valore"}
                                             and testo_ok(r["nome"]) and numero(r["valore"]) for r in ri)):
            e.append(f"{dove}: «righe_iniziali» deve essere una lista di {{nome, valore numerico}}")
        if not testo_ok(b.get("unita_riga")):
            e.append(f"{dove}: «unita_riga» non vuota")
        controlla_uscite(b, dove, permesse, e)
    elif tipo == "spiega":
        pk = b.get("parole_chiave")
        if not (isinstance(pk, list) and pk and all(testo_ok(x) for x in pk)):
            e.append(f"{dove}: «parole_chiave» deve avere almeno una parola")
        if not (intero(b.get("max_frasi")) and 1 <= b["max_frasi"] <= 10):
            e.append(f"{dove}: «max_frasi» intero tra 1 e 10")
    elif tipo == "aperta":
        if "suggerimento" in b and not testo_ok(b["suggerimento"]):
            e.append(f"{dove}: «suggerimento» non vuoto")
    elif tipo == "carte":
        cs = b.get("carte")
        if not (isinstance(cs, list) and cs):
            e.append(f"{dove}: «carte» deve avere almeno una carta")
        else:
            viste = set()
            for j, x in enumerate(cs):
                if not (isinstance(x, dict) and set(x.keys()) == {"id", "fronte", "retro"} and isinstance(x["id"], str)
                        and RE_ID.match(x["id"]) and testo_ok(x["fronte"]) and testo_ok(x["retro"])) \
                        or x.get("id") in viste:
                    e.append(f"{dove}: carte[{j}] deve essere {{id unico, fronte, retro}}")
                else:
                    viste.add(x["id"])
        if not isinstance(b.get("ripasso"), bool):
            e.append(f"{dove}: «ripasso» deve essere true o false")
    elif tipo == "cronometro":
        f = b.get("fasi")
        if not (isinstance(f, list) and 1 <= len(f) <= 8 and all(testo_ok(x) for x in f) and len(set(f)) == len(f)):
            e.append(f"{dove}: «fasi» da 1 a 8 nomi diversi")
        if not testo_ok(b.get("consegna")):
            e.append(f"{dove}: «consegna» non vuota")
        if not (intero(b.get("min_giri")) and 1 <= b["min_giri"] <= 20):
            e.append(f"{dove}: «min_giri» intero tra 1 e 20")
    elif tipo == "fascicolo":
        vs = b.get("voci")
        if not (isinstance(vs, list) and vs):
            e.append(f"{dove}: «voci» deve avere almeno una voce")
        else:
            viste = set()
            for j, x in enumerate(vs):
                if not (isinstance(x, dict) and set(x.keys()) == {"id", "testo"} and isinstance(x["id"], str)
                        and RE_ID.match(x["id"]) and testo_ok(x["testo"])) or x.get("id") in viste:
                    e.append(f"{dove}: voci[{j}] deve essere {{id unico, testo}}")
                else:
                    viste.add(x["id"])
    return e


def main(argv):
    come_json = "--json" in argv
    file = [a for a in argv if a != "--json"]
    if not file:
        print(__doc__)
        return 2
    esito = 0
    for nome in file:
        try:
            with open(nome, encoding="utf-8") as fh:
                dati = json.load(fh)
            errori = valida(dati)
        except (OSError, json.JSONDecodeError) as err:
            errori = [f"file non leggibile o JSON non valido: {err}"]
        if come_json:
            print(json.dumps(errori, ensure_ascii=False))
        elif errori:
            print(f"NO  {nome}")
            for x in errori:
                print(f"    - {x}")
        else:
            print(f"OK  {nome}")
        esito |= 1 if errori else 0
    return esito


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
