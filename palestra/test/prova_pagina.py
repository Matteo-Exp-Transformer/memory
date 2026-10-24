#!/usr/bin/env python3
"""Prova automatica della Palestra. Controlla palestra.html contro SPECIFICA.md.

Uso:  python palestra/test/prova_pagina.py [percorso/palestra.html]
      (default: palestra/pagina/palestra.html)
Serve Playwright per Python con Chromium. Nel container cloud di Claude c'è già: NON reinstallarlo.
Altrove: pip install playwright && python -m playwright install chromium

Stampa «TUTTO OK» ed esce con 0 solo se ogni controllo passa.
Tre scenari: A) senza claude.ai (archivio locale), B) con un finto database claude.ai,
C) claude.ai presente ma senza database. Più: telefono 390 px, tema chiaro/scuro, errori JavaScript.
"""
import copy
import json
import re
import sys
from pathlib import Path

from playwright.sync_api import expect, sync_playwright

QUI = Path(__file__).resolve().parent
PALESTRA = QUI.parent
sys.path.insert(0, str(PALESTRA / "strumenti"))
from valida_cartuccia import valida as valida_py  # noqa: E402

PAGINA = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else PALESTRA / "pagina" / "palestra.html"
URL = PAGINA.as_uri()
CARTUCCE = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted((PALESTRA / "cartucce").glob("*.json"))}
NON_VALIDA = json.loads((QUI / "esempi" / "non-valida.json").read_text(encoding="utf-8"))
U1, CAMPO, MISSIONE = "u1-ripasso-collo-di-bottiglia", "campo-code-ovunque", "missione-cronometro-bar"
ORA = "2026-10-25T10:00:00"
TELEFONO = {"width": 390, "height": 844}

expect.set_options(timeout=6000)
passi = []


def passo(nome):
    passi.append(nome)
    print(f"  · {nome}", flush=True)


def finto_db(semina=None):
    """Script iniettato prima della pagina: finge window.claude con un db in memoria."""
    return """
(() => {
  const store = {};
  const ascolti = {};
  window.__FAKE_DB = store; window.__FAKE_DB_VIETATI = [];
  const clona = o => JSON.parse(JSON.stringify(o));
  const meta = {fromCache: false, hasPendingWrites: false};
  function fotoDoc(c, id) { const k = c + '/' + id; const c2 = k in store; const d = c2 ? clona(store[k]) : undefined;
    return {id, exists: c2, data: () => d, metadata: meta}; }
  function fotoColl(c) { const docs = Object.keys(store).filter(k => k.split('/')[0] === c).map(k => fotoDoc(c, k.split('/')[1]));
    return {docs, size: docs.length, empty: docs.length === 0,
      docChanges: () => docs.map((d, i) => ({type: 'added', doc: d, oldIndex: -1, newIndex: i})), metadata: meta}; }
  function avvisa(c) { (ascolti[c] || []).forEach(fn => setTimeout(() => fn(fotoColl(c)), 0)); }
  function vietato(n) { return () => { window.__FAKE_DB_VIETATI.push(n); throw new Error('SPECIFICA: ' + n + ' non ammesso'); }; }
  function rifDoc(c, id) {
    if (!/^[A-Za-z0-9_\\-.~:@+]+$/.test(id)) throw new TypeError('id non valido: ' + id);
    return {id, path: c + '/' + id,
      get: async () => fotoDoc(c, id),
      set: async (d) => { if (!d || typeof d !== 'object' || Array.isArray(d)) throw {code: 'invalid_argument', message: 'corpo'};
        store[c + '/' + id] = clona(d); avvisa(c); },
      update: vietato('update'), delete: vietato('delete'), onSnapshot: vietato('onSnapshot su documento'),
      collection: vietato('sottocollezioni'), acquire: vietato('acquire')};
  }
  function rifColl(c) {
    if (c.includes('/')) vietato('collezioni annidate')();
    return {path: c, doc: (id) => { if (!id) vietato('doc senza id')(); return rifDoc(c, id); },
      add: vietato('add'), get: async () => fotoColl(c),
      onSnapshot: (next, err) => { (ascolti[c] = ascolti[c] || []).push(next); setTimeout(() => next(fotoColl(c)), 0);
        return () => { ascolti[c] = ascolti[c].filter(f => f !== next); }; },
      where: vietato('where'), orderBy: vietato('orderBy'), limit: vietato('limit')};
  }
  const db = Object.freeze({collection: rifColl, doc: (p) => { const s = p.split('/'); return rifDoc(s[0], s[1]); }});
  window.claude = {use: async (n) => (n === 'db' ? db : null)};
  window.__SEMINA = (c, id, corpo) => { store[c + '/' + id] = clona(corpo); avvisa(c); };
  const semi = %s;
  for (const [c, id, corpo] of semi) store[c + '/' + id] = clona(corpo);
})();
""" % json.dumps(semina or [])


def nuova_pagina(browser, init=None, schema="light"):
    ctx = browser.new_context(viewport=TELEFONO, color_scheme=schema, is_mobile=True, has_touch=True)
    ctx.add_init_script(f"window.__PALESTRA_ORA = {json.dumps(ORA)};")
    if init:
        ctx.add_init_script(init)
    pagina = ctx.new_page()
    errori = []
    pagina.on("pageerror", lambda e: errori.append(str(e)))
    pagina.on("dialog", lambda d: (errori.append(f"dialog vietato: {d.message}"), d.dismiss()))
    pagina.goto(URL)
    return ctx, pagina, errori


def t(p, nome):
    return p.get_by_test_id(nome)


def archivio(p):
    """Restituisce {collezione: {id: corpo}} da qualunque archivio usi la pagina."""
    tipo = p.evaluate("window.Palestra.Archivio.tipo")
    if tipo == "locale":
        return p.evaluate("JSON.parse(localStorage.getItem('palestra:v1') || '{}')")
    if tipo == "db":
        piatto = p.evaluate("window.__FAKE_DB")
        out = {}
        for k, v in piatto.items():
            c, i = k.split("/")
            out.setdefault(c, {})[i] = v
        return out
    raise AssertionError(f"archivio inatteso: {tipo}")


def senza_scroll_orizzontale(p, dove):
    w = p.evaluate("[document.documentElement.scrollWidth, window.innerWidth]")
    assert w[0] <= w[1] + 1, f"{dove}: scorrimento orizzontale ({w[0]} px su {w[1]})"


def vai(p, nav):
    t(p, nav).click()


def importa(p, oggetto_o_testo, esito):
    vai(p, "nav-home")
    t(p, "btn-importa").click()
    testo = oggetto_o_testo if isinstance(oggetto_o_testo, str) else json.dumps(oggetto_o_testo, ensure_ascii=False)
    t(p, "campo-importa").fill(testo)
    t(p, "btn-importa-conferma").click()
    expect(t(p, "esito-importa")).to_have_attribute("data-esito", esito)


def scegli_fiducia(blocco, n, conferma):
    expect(conferma).to_be_disabled()
    blocco.get_by_test_id(f"fiducia-{n}").click()
    expect(blocco.get_by_test_id(f"fiducia-{n}")).to_have_attribute("aria-pressed", "true")
    expect(conferma).to_be_enabled()
    conferma.click()


def gioca_blocco(p, blocco, b, c, attesi):
    tipo, zona = b["tipo"], c["zona"]
    g = blocco.get_by_test_id
    conferma = g("btn-conferma")
    if tipo == "racconto":
        return
    if tipo == "stima":
        g("stima-valore").fill(str(b["risposta"]).replace(".", ","))
        scegli_fiducia(blocco, 4, conferma)
        attesi[b["id"]] = ("giusto", 4)
    elif tipo == "scelta":
        sbagliata = next(o["id"] for o in b["opzioni"] if o["id"] != b["giusta"])
        g(f"opzione-{sbagliata}").click()
        scegli_fiducia(blocco, 5, conferma)
        attesi[b["id"]] = ("sbagliato", 5)
        giusta = next(o for o in b["opzioni"] if o["id"] == b["giusta"])
        expect(g("rivela")).to_contain_text(giusta["conseguenza"][:40])
    elif tipo == "duello":
        prima = b["opzioni"][0]["id"]
        g(f"opzione-{prima}").click()
        expect(blocco).to_contain_text(b["opzioni"][1]["perche_plausibile"][:30])
        g("duello-motivo").fill("Costa meno e si torna indietro.")
        expect(conferma).to_be_disabled()
        g("duello-ribalta").fill("Se i piattini pesano più di 10 secondi cambio.")
        scegli_fiducia(blocco, 2, conferma)
        esito = "aperto" if b["migliore"] is None else ("giusto" if prima == b["migliore"] else "sbagliato")
        attesi[b["id"]] = (esito, 2)
    elif tipo == "ordina":
        giusto = [e["id"] for e in b["elementi"]]
        iniziale = [e.get_attribute("data-id") for e in g("ordina-el").all()]
        assert sorted(iniziale) == sorted(giusto), "ordina: elementi mancanti"
        assert iniziale != giusto, "ordina: l'ordine iniziale non deve essere già quello giusto"
        for j, voluto in enumerate(giusto):
            for _ in range(len(giusto)):
                ora = [e.get_attribute("data-id") for e in g("ordina-el").all()]
                if ora.index(voluto) <= j:
                    break
                g(f"su-{voluto}").click()
        assert [e.get_attribute("data-id") for e in g("ordina-el").all()] == giusto, "ordina: su/giù non funzionano"
        scegli_fiducia(blocco, 3, conferma)
        attesi[b["id"]] = ("giusto", 3)
    elif tipo == "previsione":
        g("previsione-valore").fill("70")
        scegli_fiducia(blocco, 4, conferma)
        expect(g("rivela")).to_have_attribute("data-esito", "in_attesa")
        attesi[b["id"]] = ("in_attesa", 4)   # diventa «sbagliato» dopo il cronometro (giri di pochi ms)
        return
    elif tipo == "simulatore":
        q = b["parametri"][0]
        cursore = g(f"param-{q['id']}")
        cursore.evaluate("(el, v) => { el.value = v; el.dispatchEvent(new Event('input', {bubbles: true}));"
                         " el.dispatchEvent(new Event('change', {bubbles: true})); }", str(q["max"]))
        valori = {x["id"]: x["valore"] for x in b["parametri"]}
        valori[q["id"]] = q["max"]
        for u in b["uscite"]:
            atteso = p.evaluate("([f, v, d]) => Espressioni.formatta(Espressioni.calcola(f, v), d)",
                                [u["formula"], valori, u["decimali"]])
            expect(g(f"uscita-{u['id']}")).to_contain_text(atteso)
        return
    elif tipo == "mio_modello":
        n = len(b.get("righe_iniziali", []))
        if n == 0:
            g("btn-aggiungi-riga").click()
            g("riga-nome-0").fill("fase di prova")
        g("riga-valore-0").fill("30")
        valori = [30] + [r["valore"] for r in b.get("righe_iniziali", [])[1:]]
        variabili = {"somma": sum(valori), "righe": len(valori)}
        variabili.update({k["id"]: k["valore"] for k in b.get("costanti", [])})
        for u in b["uscite"]:
            atteso = p.evaluate("([f, v, d]) => Espressioni.formatta(Espressioni.calcola(f, v), d)",
                                [u["formula"], variabili, u["decimali"]])
            expect(g(f"uscita-{u['id']}")).to_contain_text(atteso)
        g("btn-aggiungi-riga").click()
        g(f"riga-nome-{len(valori)}").fill("fase aggiunta")
        g(f"riga-valore-{len(valori)}").fill("5")
        return
    elif tipo == "spiega":
        pk = b["parole_chiave"]
        g("spiega-testo").fill(f"Qui conta il {pk[0]}. Lo dico in due frasi.")
        expect(g("parola-0")).to_have_attribute("data-presente", "si")
        altra = next((i for i, x in enumerate(pk) if x.lower() not in f"qui conta il {pk[0]}".lower()), None)
        if altra is not None:
            expect(g(f"parola-{altra}")).to_have_attribute("data-presente", "no")
        expect(g("conta-frasi")).to_contain_text("2")
        return
    elif tipo == "aperta":
        g("aperta-testo").fill("Risposta di prova scritta dal test.")
        return
    elif tipo == "carte":
        for i, carta in enumerate(b["carte"]):
            expect(g("carta-fronte")).to_contain_text(carta["fronte"][:25])
            assert g("carta-retro").count() == 0 or not g("carta-retro").is_visible(), "il retro si vede prima di girare"
            g("btn-gira").click()
            expect(g("carta-retro")).to_contain_text(carta["retro"][:25])
            g("voto-si" if i == 0 else "voto-quasi").click()
        return
    elif tipo == "cronometro":
        expect(g("crono-fase-0")).to_be_disabled()
        g("crono-start").click()
        for giro in range(b["min_giri"]):
            for i in range(len(b["fasi"])):
                g(f"crono-fase-{i}").click()
            g("crono-fine-giro").click()
            expect(g("crono-conta-giri")).to_have_text(str(giro + 1))
        g("crono-stop").click()
        g("crono-nota").fill("Una brocca rifatta al secondo giro.")
        g("btn-crono-salva").click()
        for prev in (x for x in c["blocchi"] if x["tipo"] == "previsione" and x["collegata_a"] == b["id"]):
            expect(g("crono-confronto")).to_be_visible()
            attesi[prev["id"]] = ("sbagliato", 4)
        return
    elif tipo == "fascicolo":
        for i, v in enumerate(b["voci"]):
            k = f"{c['id']}__{v['id']}"
            if i == 0:
                g(f"sposta-{k}-1").click()
                g(f"prova-conferma-{k}").click()
                expect(g(f"errore-prova-{k}")).to_be_visible()
                g(f"prova-tipo-{k}").select_option("misura")
                g(f"prova-testo-{k}").fill("Cronometrato il 26/10, 3 giri")
                g(f"prova-conferma-{k}").click()
                expect(g("fascicolo-col-1").get_by_test_id(f"voce-{k}")).to_be_visible()
            else:
                g(f"sposta-{k}-2").click()
                expect(g("fascicolo-col-2").get_by_test_id(f"voce-{k}")).to_be_visible()
        return
    else:
        raise AssertionError(f"tipo non previsto dal test: {tipo}")
    # tipi con conferma: rivela con l'esito; in campo niente «Giusto»
    esito = attesi[b["id"]][0]
    expect(g("rivela")).to_have_attribute("data-esito", esito)
    if zona == "campo":
        assert "giusto" not in g("rivela").inner_text().lower(), "zona campo: niente giusto/sbagliato"
    for x in ("stima-valore", "previsione-valore"):
        if g(x).count():
            expect(g(x)).to_be_disabled()


def gioca(p, cid, correzione=False):
    c = CARTUCCE[cid]
    vai(p, "nav-home")
    t(p, f"apri-{cid}").click()
    if c["zona"] == "banco":
        expect(t(p, "btn-inizia")).to_be_disabled()
    t(p, "seduta-finito").fill("Ho finito quando ho risposto a tutto senza appunti.")
    t(p, "btn-inizia").click()
    attesi = {}
    for i, b in enumerate(c["blocchi"]):
        blocco = t(p, "blocco")
        expect(blocco).to_have_count(1)
        expect(blocco).to_have_attribute("data-id", b["id"])
        expect(blocco).to_have_attribute("data-tipo", b["tipo"])
        expect(t(p, "seduta-avanzamento")).to_contain_text(f"{i + 1} / {len(c['blocchi'])}")
        avanti = t(p, "btn-avanti")
        completo_subito = b["tipo"] in ("racconto", "simulatore") or (b["tipo"] == "mio_modello" and b.get("righe_iniziali"))
        if not completo_subito:
            expect(avanti).to_be_disabled()
        if correzione and i == 0:
            blocco.get_by_test_id("btn-correggi").click()
            blocco.get_by_test_id("campo-correzione").fill("Il testo non dice se il latte è intero.")
            blocco.get_by_test_id("btn-correzione-invia").click()
            expect(blocco.get_by_test_id("correzione-ok")).to_be_visible()
        gioca_blocco(p, blocco, b, c, attesi)
        senza_scroll_orizzontale(p, f"blocco {b['id']}")
        expect(avanti).to_be_enabled()
        avanti.click()
    expect(t(p, "fine-seduta")).to_be_visible()
    t(p, "btn-finito-si").click()
    expect(t(p, "riepilogo")).to_be_visible()
    t(p, "btn-copia-risultati").click()
    testo = t(p, "testo-risultati").input_value()
    assert c["titolo"] in testo and cid in testo, "Copia risultati: manca titolo o id"
    for b in c["blocchi"]:
        assert f"[{b['id']}]" in testo, f"Copia risultati: manca il blocco {b['id']}"
    # archivio
    a = archivio(p)
    sedute = [s for s in a.get("sedute", {}).values() if s["cartuccia"] == cid and s.get("fine")]
    assert sedute, f"{cid}: nessuna seduta chiusa salvata"
    s = sedute[-1]
    assert s["finito_esito"] == "si" and s["finito_condizione"].startswith("Ho finito quando")
    assert set(s["blocchi"].keys()) == {b["id"] for b in c["blocchi"]}, f"{cid}: blocchi salvati incompleti"
    for bid, (esito, fid) in attesi.items():
        assert s["blocchi"][bid]["esito"] == esito, f"{cid}/{bid}: esito {s['blocchi'][bid]['esito']} invece di {esito}"
        assert s["blocchi"][bid]["fiducia"] == fid, f"{cid}/{bid}: fiducia sbagliata"
    for b in c["blocchi"]:
        r = s["blocchi"][b["id"]]["risposta"]
        if b["tipo"] == "duello":
            assert r["motivo"] and r["ribalta"] and r["opzione"] == b["opzioni"][0]["id"]
        if b["tipo"] == "ordina":
            assert r == [e["id"] for e in b["elementi"]]
        if b["tipo"] == "cronometro":
            m = a["misure"][r]
            assert m["completa"] is True and len(m["giri"]) == b["min_giri"] and m["media_giro_ms"] >= 0
            assert m["nota"].startswith("Una brocca")
        if b["tipo"] == "carte" and b["ripasso"]:
            for carta in b["carte"]:
                k = f"{cid}__{b['id']}__{carta['id']}"
                assert k in a.get("ripassi", {}), f"ripasso mancante: {k}"
                assert a["ripassi"][k]["prossima"] == "2026-10-26" and a["ripassi"][k]["passo"] == 0
        if b["tipo"] == "fascicolo":
            k = f"{cid}__{b['voci'][0]['id']}"
            v = a["fascicolo"][k]
            assert v["colonna"] == 1 and v["prova"]["tipo"] == "misura" and v["prova"]["testo"]
    if correzione:
        cor = [x for x in a.get("correzioni", {}).values() if x["cartuccia"] == cid]
        assert cor and cor[0]["blocco"] == c["blocchi"][0]["id"], "correzione non salvata"
    return s


def controlla_validatore(p):
    casi = list(CARTUCCE.values()) + [NON_VALIDA]
    base = CARTUCCE[U1]
    def rotta(f):
        x = copy.deepcopy(base)
        f(x)
        return x
    casi += [
        rotta(lambda x: x.update(zona="banco", blocchi=[b for b in x["blocchi"] if b["dominio"] == "ristorazione"])),
        rotta(lambda x: x["blocchi"][4]["opzioni"][0].update(perche_plausibile="")),
        rotta(lambda x: x.update(campo_sbagliato=1)),
        rotta(lambda x: x["blocchi"][2].update(risposta="79")),
        rotta(lambda x: x["blocchi"][3].update(giusta="non-esiste")),
        rotta(lambda x: x["blocchi"].append({"id": "sim", "tipo": "simulatore", "dominio": "x", "testo": "t",
              "parametri": [{"id": "a", "nome": "A", "min": 0, "max": 2, "passo": 1, "valore": 1, "unita": ""}],
              "uscite": [{"id": "u1", "nome": "U", "formula": "a * b", "decimali": 0, "unita": ""}]})),
        rotta(lambda x: x["blocchi"].append({"id": "prev", "tipo": "previsione", "dominio": "x", "testo": "t",
              "unita": "s", "collegata_a": "nessuno", "tolleranza_percento": 10})),
        rotta(lambda x: x.update(versione=2)),   # questa resta valida
    ]
    for i, caso in enumerate(casi):
        py = valida_py(caso)
        js = p.evaluate("(o) => window.Palestra.valida(o)", caso)
        assert isinstance(js, list), "Palestra.valida deve restituire una lista"
        assert (len(py) == 0) == (len(js) == 0), (
            f"validatore JS e Python non concordano sul caso {i}: python={py[:3]} js={js[:3]}")
    return len(casi)


def scenario_a(browser):
    print("Scenario A — archivio locale")
    ctx, p, errori = nuova_pagina(browser)
    expect(t(p, "banner-archivio")).to_have_attribute("data-backend", "locale")
    expect(t(p, "lista-cartucce")).to_be_visible()
    senza_scroll_orizzontale(p, "home")
    passo("avvio senza claude.ai: archivio locale")
    n_casi = controlla_validatore(p)
    passo(f"validatore della pagina = validatore Python ({n_casi} casi)")
    for cid in (U1, CAMPO, MISSIONE):
        importa(p, CARTUCCE[cid], "ok")
        expect(t(p, f"cartuccia-{cid}")).to_have_attribute("data-valida", "si")
    expect(t(p, f"cartuccia-{CAMPO}")).to_have_attribute("data-zona", "campo")
    importa(p, NON_VALIDA, "errore")
    importa(p, CARTUCCE[U1], "errore")                       # stessa versione
    importa(p, "{ questo non è json", "errore")
    v2 = copy.deepcopy(CARTUCCE[U1]); v2["versione"] = 2
    importa(p, v2, "ok")
    expect(t(p, f"cartuccia-{U1}")).to_have_count(1)
    passo("importa: 3 buone ok; non valida, doppione, JSON rotto rifiutati; versione 2 sostituisce")

    gioca(p, U1, correzione=True)
    passo("seduta completa U1 (carte, stima, scelta, duello, ordina, spiega, fascicolo) + correzione")
    gioca(p, MISSIONE)
    passo("seduta completa missione (previsione, cronometro, mio_modello)")
    gioca(p, CAMPO)
    passo("seduta completa campo giochi (simulatore, niente giusto/sbagliato)")

    # Sensore
    a = archivio(p)
    righe = {n: [0, 0] for n in range(1, 6)}
    for s in a["sedute"].values():
        if s["zona"] != "banco":
            continue
        for x in s["blocchi"].values():
            if x.get("fiducia") and x.get("esito") in ("giusto", "sbagliato"):
                righe[x["fiducia"]][0] += 1
                righe[x["fiducia"]][1] += x["esito"] == "giusto"
    vai(p, "nav-sensore")
    for n, (tent, giusti) in righe.items():
        expect(t(p, f"sensore-riga-{n}")).to_have_attribute("data-tentativi", str(tent))
        expect(t(p, f"sensore-riga-{n}")).to_have_attribute("data-giusti", str(giusti))
    eccesso = sum(1 for s in a["sedute"].values() if s["zona"] == "banco" for x in s["blocchi"].values()
                  if (x.get("fiducia") or 0) >= 4 and x.get("esito") == "sbagliato")
    expect(t(p, "sensore-eccesso")).to_have_attribute("data-valore", str(eccesso))
    expect(t(p, "sensore-storia")).to_be_visible()
    senza_scroll_orizzontale(p, "sensore")
    passo(f"sensore coerente con le sedute ({sum(r[0] for r in righe.values())} tentativi, {eccesso} sicuri e sbagliati)")

    # Scale: oggi niente, domani tutte le carte con ripasso
    n_carte = sum(len(b["carte"]) for cid in (U1, CAMPO) for b in CARTUCCE[cid]["blocchi"]
                  if b["tipo"] == "carte" and b["ripasso"])
    vai(p, "nav-home")
    expect(t(p, "conta-scale-oggi")).to_have_text("0")
    p.evaluate("window.__PALESTRA_ORA = '2026-10-26T10:00:00'")
    vai(p, "nav-scale")
    vai(p, "nav-home")
    expect(t(p, "conta-scale-oggi")).to_have_text(str(n_carte))
    vai(p, "nav-scale")
    for i in range(n_carte):
        expect(t(p, "scala-fronte")).to_be_visible()
        t(p, "scala-gira").click()
        expect(t(p, "scala-retro")).to_be_visible()
        t(p, "scala-si" if i else "scala-no").click()
    expect(t(p, "scala-vuota")).to_be_visible()
    senza_scroll_orizzontale(p, "scale")
    vai(p, "nav-home")
    expect(t(p, "conta-scale-oggi")).to_have_text("0")
    rip = archivio(p)["ripassi"]
    assert sorted(r["prossima"] for r in rip.values()).count("2026-10-29") == n_carte - 1, "sì → +3 giorni"
    assert sum(1 for r in rip.values() if r["prossima"] == "2026-10-27" and r["passo"] == 0) == 1, "no → domani, passo 0"
    passo(f"scale: {n_carte} carte in scadenza il giorno dopo, sì → +3 giorni, no → domani")

    # Ripresa dopo l'una
    p.evaluate("window.__PALESTRA_ORA = '2026-10-27T01:30:00'")
    vai(p, "nav-scale")
    vai(p, "nav-home")
    expect(t(p, "banner-ripresa")).to_be_visible()
    expect(t(p, f"apri-{U1}")).to_be_disabled()
    t(p, "btn-ripresa-ignora").click()
    expect(t(p, f"apri-{U1}")).to_be_enabled()
    p.evaluate("window.__PALESTRA_ORA = '2026-10-27T10:00:00'")
    passo("modalità ripresa dopo l'una, con «Ho deciso io»")

    # Fascicolo
    vai(p, "nav-fascicolo")
    k1 = f"{U1}__{CARTUCCE[U1]['blocchi'][-1]['voci'][0]['id']}"
    expect(t(p, "fascicolo-col-1").get_by_test_id(f"voce-{k1}")).to_be_visible()
    t(p, "fascicolo-nuova-testo").fill("Leggo un conto economico di un bar")
    t(p, "fascicolo-nuova-aggiungi").click()
    mia = t(p, "fascicolo-col-3").locator('[data-testid^="voce-mia-"]')
    expect(mia).to_have_count(1)
    chiave = mia.get_attribute("data-testid").removeprefix("voce-")
    t(p, f"sposta-{chiave}-1").click()
    t(p, f"prova-conferma-{chiave}").click()
    expect(t(p, f"errore-prova-{chiave}")).to_be_visible()
    t(p, f"sposta-{chiave}-2").click()
    expect(t(p, "fascicolo-col-2").get_by_test_id(f"voce-{chiave}")).to_be_visible()
    t(p, f"btn-segna-{chiave}").click()
    t(p, "btn-copia-fascicolo").click()
    testo = t(p, "testo-fascicolo").input_value()
    assert "Cronometrato il 26/10" in testo and "conto economico" not in testo, "copia fascicolo: solo colonna 1"
    assert p.get_by_role("button", name=re.compile(r"elimina|cancella", re.I)).count() == 0, "niente pulsanti elimina"
    f = archivio(p)["fascicolo"][chiave]
    assert f["colonna"] == 2 and f["segnata"] is True and f["prova"] is None and len(f["storia"]) >= 1
    senza_scroll_orizzontale(p, "fascicolo")
    passo("fascicolo: colonna 1 solo con prova, voce mia, segna, copia per colloquio, niente elimina")

    # Quaderno
    vai(p, "nav-quaderno")
    t(p, "quaderno-tipo").select_option("parola")
    t(p, "quaderno-materia").fill("Operations")
    t(p, "quaderno-testo").fill("il giro del bancone")
    t(p, "quaderno-termine").fill("ciclo di servizio")
    t(p, "quaderno-salva").click()
    voce = p.locator('[data-testid^="quaderno-voce-"]')
    expect(voce).to_have_count(1)
    expect(voce).to_contain_text("il giro del bancone")
    expect(voce).to_contain_text("ciclo di servizio")
    q = list(archivio(p)["quaderno"].values())[0]
    assert q["tipo"] == "parola" and q["materia"] == "Operations" and q["termine_tecnico"] == "ciclo di servizio"
    senza_scroll_orizzontale(p, "quaderno")
    passo("quaderno: parola mia → termine tecnico")

    # Persistenza
    p.reload()
    expect(t(p, f"cartuccia-{MISSIONE}")).to_be_visible()
    assert len(archivio(p)["sedute"]) == 3
    passo("dopo il ricaricamento i dati restano")
    assert not errori, f"errori JavaScript o dialog: {errori}"
    ctx.close()


def scenario_b(browser):
    print("Scenario B — finto database di claude.ai")
    ctx, p, errori = nuova_pagina(browser, finto_db([["cartucce", CAMPO, CARTUCCE[CAMPO]]]))
    expect(t(p, "banner-archivio")).to_have_attribute("data-backend", "db")
    expect(t(p, f"cartuccia-{CAMPO}")).to_be_visible()
    passo("cartuccia caricata da un agente prima dell'apertura: visibile")
    p.evaluate("([id, c]) => window.__SEMINA('cartucce', id, c)", [U1, CARTUCCE[U1]])
    expect(t(p, f"cartuccia-{U1}")).to_be_visible()
    passo("cartuccia caricata da un agente con la pagina aperta: compare da sola")
    importa(p, CARTUCCE[MISSIONE], "ok")
    assert f"cartucce/{MISSIONE}" in p.evaluate("window.__FAKE_DB")
    gioca(p, CAMPO, correzione=True)
    gioca(p, U1)
    db = p.evaluate("window.__FAKE_DB")
    assert any(k.startswith("sedute/") for k in db) and any(k.startswith("ripassi/") for k in db)
    vietati = p.evaluate("window.__FAKE_DB_VIETATI")
    assert not vietati, f"la pagina usa funzioni del db vietate dalla SPECIFICA: {vietati}"
    passo("sedute, ripassi, correzioni scritti nel db; nessuna funzione vietata (where, update, delete…)")
    assert not errori, f"errori JavaScript o dialog: {errori}"
    ctx.close()


def scenario_c(browser):
    print("Scenario C — claude.ai senza database, tema scuro")
    ctx, p, errori = nuova_pagina(browser, "window.claude = {use: async () => null};", schema="dark")
    expect(t(p, "banner-archivio")).to_have_attribute("data-backend", "locale")
    scuro = p.evaluate("getComputedStyle(document.body).backgroundColor")
    ctx.close()
    ctx, p2, errori2 = nuova_pagina(browser, schema="light")
    chiaro = p2.evaluate("getComputedStyle(document.body).backgroundColor")
    assert scuro != chiaro and "rgba(0, 0, 0, 0)" not in (scuro, chiaro), f"tema: chiaro {chiaro}, scuro {scuro}"
    assert p2.title() == "La Palestra", f"titolo: {p2.title()}"
    passo("senza database → locale; sfondo diverso in chiaro e scuro; titolo «La Palestra»")
    html = PAGINA.read_text(encoding="utf-8")
    for vietato in ("eval(", "new Function", "alert(", "confirm(", "prompt("):
        assert vietato not in html, f"nel file c'è {vietato!r}"
    calcolatore = (PALESTRA / "motore" / "espressioni.js").read_text(encoding="utf-8").replace("\r\n", "\n")
    assert calcolatore.strip() in html.replace("\r\n", "\n"), "motore/espressioni.js non è copiato tale e quale nella pagina"
    assert not re.search(r"<script[^>]+src=", html), "niente script esterni"
    passo("niente eval/alert, calcolatore copiato tale e quale, niente script esterni")
    assert not errori and not errori2, f"errori JavaScript: {errori + errori2}"
    ctx.close()


def main():
    if not PAGINA.exists():
        print(f"Manca la pagina: {PAGINA}")
        return 1
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        try:
            scenario_a(browser)
            scenario_b(browser)
            scenario_c(browser)
        finally:
            browser.close()
    print(f"TUTTO OK ({len(passi)} controlli)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
