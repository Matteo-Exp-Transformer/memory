#!/usr/bin/env python3
"""Prova della vista «Lezioni archiviate» (da completare / completate). Aggiunta, non sostituisce prova_pagina.py.
Uso: python palestra/test/prova_lezioni.py"""
import json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

QUI = Path(__file__).resolve().parent
sys.argv = sys.argv[:1]
sys.path.insert(0, str(QUI))
import prova_pagina as P  # noqa: E402

C = P.CARTUCCE[P.CAMPO]
blocchi = C["blocchi"]
base = lambda fine, bl, esito=None: {"cartuccia": C["id"], "versione": C["versione"], "titolo": C["titolo"], "zona": C["zona"],
    "inizio": "2026-10-25T09:17:32.000Z", "fine": fine, "finito_condizione": "So spiegarlo", "finito_esito": esito, "blocchi": bl}
fatto = lambda: {"tipo": blocchi[0]["tipo"], "risposta": "ok", "fiducia": 3, "esito": "aperto", "quando": "2026-10-25T09:20:00.000Z"}
APERTA, APERTA2, CHIUSA = C["id"] + "__20261025-091732", C["id"] + "__20261025-093000", C["id"] + "__20261024-180000"
semina = [["cartucce", C["id"], C],
          ["sedute", APERTA, base(None, {})],
          ["sedute", APERTA2, base(None, {blocchi[0]["id"]: fatto()})],
          ["sedute", CHIUSA, base("2026-10-24T18:30:00.000Z", {b["id"]: fatto() for b in blocchi}, "si")]]

with sync_playwright() as pw:
    br = pw.chromium.launch()
    ctx, p, err = P.nuova_pagina(br, P.finto_db(semina))
    t = lambda n: P.t(p, n)
    expect(t("btn-lezioni")).to_be_visible()
    expect(t("cartuccia-" + C["id"])).to_contain_text("2 lezioni da completare")
    t("btn-lezioni").click()
    da, co = t("lezioni-da-completare"), t("lezioni-completate")
    expect(da).to_contain_text("Da completare (2)")
    expect(co).to_contain_text("Completate (1)")
    expect(da.get_by_test_id("lezione-" + APERTA)).to_be_visible()
    expect(da.get_by_test_id("lezione-" + APERTA2)).to_contain_text("Blocchi completati: 1 su %d" % len(blocchi))
    expect(co.get_by_test_id("lezione-" + CHIUSA)).to_be_visible()
    P.passo("elenco diviso in da completare (2) e completate (1)")
    P.senza_scroll_orizzontale(p, "lezioni")
    p.screenshot(path="/tmp/lezioni390.png", full_page=True)

    # consulta
    t("consulta-" + CHIUSA).click()
    expect(t("consulta")).to_contain_text(C["titolo"])
    expect(t("consulta-blocco-" + blocchi[1]["id"])).to_be_visible()
    t("btn-copia-risultati").click()
    expect(t("testo-risultati")).to_have_value(__import__("re").compile("PALESTRA"))
    P.passo("lezione completata rileggibile, con «Copia risultati»")
    t("btn-lezioni-indietro").click()

    # riprendi dall'inizio
    t("riprendi-" + APERTA).click()
    expect(p.locator("#vista")).to_contain_text(blocchi[0].get("titolo") or blocchi[0]["id"])
    P.passo("seduta senza blocchi: riparte dal primo blocco")
    p.screenshot(path="/tmp/ripresa390.png")
    doc_prima = p.evaluate("window.__FAKE_DB['sedute/%s']" % APERTA)
    assert doc_prima["fine"] is None and doc_prima["inizio"] == "2026-10-25T09:17:32.000Z"

    # riprendi a metà: stesso id, niente nuovo documento
    p.goto(P.URL)
    t("btn-lezioni").click()
    t("riprendi-" + APERTA2).click()
    expect(p.locator("#vista")).not_to_contain_text("Blocchi completati")
    nsed = p.evaluate("Object.keys(window.__FAKE_DB).filter(k => k.startsWith('sedute/')).length")
    assert nsed == 3, nsed
    P.passo("seduta a metà: riparte dal blocco successivo, stesso documento, nessun duplicato")
    assert not err, err
    br.close()
print("LEZIONI OK")

# --- Tornare ai passi precedenti: pagina intera, non riassunto (aggiunto 25/10/2026)
with sync_playwright() as pw:
    br = pw.chromium.launch()
    ctx, p, err = P.nuova_pagina(br, P.finto_db(semina))
    t = lambda n: P.t(p, n)
    t("apri-" + C["id"]).click()
    t("seduta-finito").fill("So spiegarlo")
    t("btn-inizia").click()
    expect(t("btn-precedente")).to_have_count(0)            # primo passo: niente prima
    t("btn-avanti").click()                                  # racconto
    sim = blocchi[1]; q = sim["parametri"][0]
    t("param-" + q["id"]).evaluate("(el, v) => { el.value = v; el.dispatchEvent(new Event('input', {bubbles: true})); el.dispatchEvent(new Event('change', {bubbles: true})); }", str(q["max"]))
    t("btn-avanti").click()                                  # simulatore
    t("aperta-testo").fill("La coda nasce dove il lavoro si accumula.")
    t("btn-avanti").click()                                  # aperta
    d = blocchi[3]
    t("opzione-" + d["opzioni"][0]["id"]).click()
    t("duello-motivo").fill("Costa meno.")
    t("duello-ribalta").fill("Se pesa troppo cambio.")
    t("fiducia-2").click(); t("btn-conferma").click()
    expect(t("rivela")).to_be_visible()
    t("btn-avanti").click()                                  # duello
    expect(t("blocco")).to_have_attribute("data-id", blocchi[4]["id"])
    # sul passo vivo (carte) scrivo qualcosa che non deve perdersi: giro la prima carta
    t("btn-gira").click()
    # indietro: duello com'era (opzione scelta, testi, fiducia, rivelazione), non un riassunto
    t("btn-precedente").click()
    expect(t("blocco")).to_have_attribute("data-id", d["id"])
    expect(t("duello-motivo")).to_have_value("Costa meno.")
    expect(t("duello-ribalta")).to_have_value("Se pesa troppo cambio.")
    expect(t("opzione-" + d["opzioni"][0]["id"])).to_have_attribute("aria-pressed", "true")
    expect(t("rivela")).to_be_visible()
    expect(t("btn-conferma")).to_have_count(0)
    P.passo("indietro: il duello riappare intero, con le tue risposte e la rivelazione")
    t("btn-precedente").click(); t("btn-precedente").click()  # aperta, poi simulatore
    expect(t("blocco")).to_have_attribute("data-id", sim["id"])
    expect(t("param-" + q["id"])).to_have_value(str(q["max"]))
    P.passo("indietro: il cursore del simulatore è dov'era")
    # modifico il cursore e riparto: deve salvare
    minimo = str(q["min"])
    t("param-" + q["id"]).evaluate("(el, v) => { el.value = v; el.dispatchEvent(new Event('input', {bubbles: true})); el.dispatchEvent(new Event('change', {bubbles: true})); }", minimo)
    t("btn-successivo").click()
    expect(t("aperta-testo")).to_have_value("La coda nasce dove il lavoro si accumula.")
    saved = [v for k, v in P.archivio(p)["sedute"].items() if v["fine"] is None and sim["id"] in v["blocchi"] and k.startswith(C["id"] + "__20261025-1")]
    assert saved and saved[0]["blocchi"][sim["id"]]["risposta"]["parametri"][q["id"]] == q["min"], saved
    P.passo("modifica di un passo rivisto salvata")
    t("btn-successivo").click(); t("btn-successivo").click()
    expect(t("blocco")).to_have_attribute("data-id", blocchi[4]["id"])
    expect(t("btn-gira")).to_have_count(0)                   # la carta girata è ancora girata
    expect(t("carta-retro")).to_be_visible()
    P.passo("ritorno al passo in corso: lo trovi com'era (carta già girata)")
    P.senza_scroll_orizzontale(p, "passi")
    assert not err, err
    br.close()
print("INDIETRO OK")
