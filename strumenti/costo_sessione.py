#!/usr/bin/env python3
"""Token consumati da una sessione, letti dai registri locali: serve alla riga «Costo» della nota di fine chat.

Uso: python strumenti/costo_sessione.py [claude|codex] [id]
     claude (default): la sessione Claude Code più recente della cartella corrente, con i sotto-agenti
     codex: la sessione Codex più recente avviata nella cartella corrente
     id: un pezzo dell'id della sessione, per sceglierne una diversa dalla più recente
Registri: ~/.claude/projects/<cartella>/<id>.jsonl (+ <id>/subagents/) e ~/.codex/sessions/AAAA/MM/GG/.
Esce con 1 se non trova la sessione.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

CASA = Path.home()


def numero(n):
    return f"{n:,}".replace(",", ".")


def scegli(files, pezzo_id):
    files = [f for f in files if not pezzo_id or pezzo_id in f.name]
    return max(files, key=lambda f: f.stat().st_mtime) if files else None


def somma_claude(file):
    """Somma l'uso per modello. Il registro ripete un messaggio dell'API per ogni blocco, e solo
    l'ultima copia ha l'output completo: per ogni id si tiene l'ultima."""
    ultimi = {}
    for riga in file.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            m = json.loads(riga).get("message") or {}
        except (json.JSONDecodeError, AttributeError):
            continue
        if isinstance(m, dict) and m.get("usage"):
            ultimi[m.get("id") or len(ultimi)] = m
    per_modello = {}
    for m in ultimi.values():
        uso = m["usage"]
        t = per_modello.setdefault(m.get("model", "?"), [0, 0, 0, 0])
        t[0] += uso.get("input_tokens", 0)
        t[1] += uso.get("cache_creation_input_tokens", 0)
        t[2] += uso.get("cache_read_input_tokens", 0)
        t[3] += uso.get("output_tokens", 0)
    return per_modello


def riga_claude(nome, per_modello):
    parti = []
    for modello, (i, cw, cr, o) in per_modello.items():
        parti.append(f"{modello} {numero(i + cw + cr + o)} token "
                     f"(input {numero(i)}, cache scritta {numero(cw)}, cache letta {numero(cr)}, output {numero(o)})")
    return f"{nome}: " + ("; ".join(parti) if parti else "nessun uso registrato")


def claude(pezzo_id):
    cartella = CASA / ".claude" / "projects" / re.sub(r"[^A-Za-z0-9]", "-", str(Path.cwd()))
    file = scegli(list(cartella.glob("*.jsonl")), pezzo_id)
    if not file:
        print(f"costo_sessione: nessuna sessione Claude in {cartella}")
        return 1
    print(f"sessione Claude {file.stem}")
    print(riga_claude("chat principale", somma_claude(file)))
    agenti = sorted((cartella / file.stem / "subagents").glob("*.jsonl"))
    for agente in agenti:
        print(riga_claude(f"sotto-agente {agente.stem}", somma_claude(agente)))
    if agenti:
        # il registro dei sotto-agenti salva l'uso a inizio risposta: l'input è giusto, l'output no
        print("nota: l'output dei sotto-agenti è sottostimato; il totale giusto è «subagent_tokens» "
              "nell'avviso di fine sotto-agente")
    return 0


def codex(pezzo_id):
    qui = str(Path.cwd()).lower()
    candidati = []
    for f in (CASA / ".codex" / "sessions").glob("*/*/*/*.jsonl"):
        try:
            with f.open(encoding="utf-8", errors="replace") as h:
                meta = json.loads(h.readline()).get("payload", {})
        except (OSError, json.JSONDecodeError):
            continue
        if str(meta.get("cwd", "")).lower() == qui:
            candidati.append(f)
    file = scegli(candidati, pezzo_id)
    if not file:
        print(f"costo_sessione: nessuna sessione Codex avviata in {Path.cwd()}")
        return 1
    ultimo = None
    for riga in file.read_text(encoding="utf-8", errors="replace").splitlines():
        if '"token_count"' in riga:
            try:
                ultimo = json.loads(riga)["payload"]
            except (json.JSONDecodeError, KeyError):
                pass
    print(f"sessione Codex {file.stem}")
    totale = ((ultimo or {}).get("info") or {}).get("total_token_usage")
    if not totale:
        print("chat: nessun uso registrato")
        return 0
    print(f"chat: {numero(totale['total_tokens'])} token (input {numero(totale['input_tokens'])}, "
          f"di cui in cache {numero(totale.get('cached_input_tokens', 0))}, output {numero(totale['output_tokens'])})")
    limiti = ultimo.get("rate_limits") or {}
    for chiave, nome in (("primary", "finestra"), ("secondary", "settimana")):
        lim = limiti.get(chiave)
        if lim:
            print(f"quota Codex {nome} ({lim['window_minutes']} min): {lim['used_percent']}% usata")
    return 0


def main():
    args = sys.argv[1:]
    tipo = args.pop(0) if args and args[0] in ("claude", "codex") else "claude"
    pezzo_id = args[0] if args else ""
    return claude(pezzo_id) if tipo == "claude" else codex(pezzo_id)


if __name__ == "__main__":
    sys.exit(main())
