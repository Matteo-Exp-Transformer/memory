# Nota di fine chat — costruttore Claude, fetta A del pilota della catena
> Source: sessione Claude 22b3817e-8692-40f7-b646-27ea6b1063c4
> Collected: 2026-10-28
> Published: 2026-10-28

- **Dove:** Claude desktop Windows (Code), Sonnet 5.5, avvio manuale, worktree wt-catena-a.
- **Obiettivo di Matteo:** costruire la fetta A di LAVORI.md; «non legare il coordinatore alla fetta della corsa B» (B farà «pagine pubbliche più leggere»); «Non avviare la corsa B».
- **Decisioni di Matteo:** push e PR verso env/test con i criteri di team/costruttore.md, «senza chiedere».
- **Risultato:** PR #20 su CALENDARIO-V2 (branch claude/pilota-catena-a): scripts/catena/, scripts/quota-claude.mjs, verbale schede/2026-10-27-pilota-catena-esito-a.md; 31 prove verdi, validate verde (1360 test).
- **Ha funzionato:** ruoli e gh finti per provare la sequenza; `--tools` con elenco chiuso; sonda dal pianificatore (esito 0); push dry-run per le prove negative.
- **Non ha funzionato / attenzione:** il divieto di Bash lasciava PowerShell; nome repo sbagliato (CALENDARIO-V2); un test di 1a rifiutava `claude`; corsa intera con modelli veri non provata.
- **Quota Claude:** prima 5 ore 3%, settimana 6% (2026-10-28T06:06Z); dopo 15% e 8% (06:19Z); conto intero, nessuna soglia (avvio manuale). Codex: lettura assente, prova sandbox circa 0,1 M token.
- **Costo:** chat principale claude-sonnet-5-5 9.482.015 token (input 100, cache scritta 196.466, cache letta 9.196.239, output 89.210); misura prima della nota; prove haiku circa 0,2 M a parte.
- **Letti:** serviti: AGENTS.md, team/costruttore.md, LAVORI.md, scheda del pilota, STATO.md, scripts/quota-codex.mjs, scripts/verifica-quota.mjs, esperimenti/catena-minima/catena.mjs; non servito: team/manager.md; memory chiudi/SKILL.md e AGENTS.md serviti.
- **Aperto:** corsa B (prima esecuzione reale), risveglio del PC alle 22:00.
- **Sessione:** https://claude.ai/code/session_22b3817e-8692-40f7-b646-27ea6b1063c4
