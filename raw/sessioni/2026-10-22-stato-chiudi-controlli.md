# Nota di fine chat — STATO.md, «chiudi» e controlli automatici

> Source: sessione Claude desktop (Code) locale sul PC di Matteo; link non disponibile
> Collected: 2026-10-22
> Published: 2026-10-22

- **Dove:** Claude desktop, scheda Code, sul PC; Opus 5.5 per le decisioni, un sotto-agente Sonnet per scrivere e provare i file.
- **Obiettivo di Matteo:** «Formato STATO.md per progetto, al massimo 40 righe, riscritto da capo a fine chat»; comando «chiudi»; «Script di controllo (lunghezza, data, link) che parte da solo prima di ogni salvataggio»; «Usa Sonnet per l'esecuzione, Opus solo per decisioni difficili».
- **Decisioni di Matteo:** «Sì, aggiungi cleanupPeriodDays: 1095 in ~/.claude/settings.json»; «in AGENTS.md e in ogni script o controllo scrivi il comando come `python` (su questo PC python3 non funziona)»; per il cloud Linux «uno script che provi prima `python` e poi `python3`».
- **Risultato:** skill `.claude/skills/chiudi/SKILL.md` (STATO.md vive nella repo del progetto, non in memory); `strumenti/controlla.py`, `strumenti/controlli.sh`, `.githooks/pre-commit` (anche `raw/` immutabile); `cleanupPeriodDays` a 1095 in `~/.claude/settings.json`.
- **Ha funzionato:** decisioni prese prima e passate a Sonnet in un solo brief, file e prove in un giro; prove con casi che devono fallire (41 righe, data futura, link rotto, modifica a raw/).
- **Non ha funzionato / attenzione:** il clone locale era indietro rispetto alla repo remota; senza `git pull` ho creduto che mancasse `raw/sessioni/` e ho scritto un formato di nota diverso da quello già in AGENTS.md (poi allineato). Su questo PC `python3` è l'alias vuoto del Microsoft Store.
- **Costo:** sotto-agente Sonnet 88.838 token; chat principale non letta.
- **Aperto (dipende da fatti non disponibili):** controlli e riga nel CLAUDE.md delle repo dei progetti, da fare quando Matteo apre un progetto.
