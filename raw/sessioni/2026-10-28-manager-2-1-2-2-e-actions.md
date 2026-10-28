# Nota di fine chat — manager: 2.1 unita, 2.2 costruita, analisi Actions

> Source: sessione Claude Code 7c17e71f-598d-48ca-89d0-3e212b85490d, CalendarBackup-v2 (terza parte)
> Collected: 2026-10-28
> Published: 2026-10-28

- **Dove:** Claude desktop (Code), Opus 5.5 manager + sub-agente Opus costruttore della 2.2; worktree propri da origin/env/test; PR #32, #33 (aperta), #34.
- **Obiettivo:** Matteo: «Test sui menu ok, sembra tutto uguale.» Account Classic dato in chat; «Codex ha finito. Proseguiamo.» Analisi del consumo di Actions: «Nessuna modifica richiesta in questa fase.» Poi: «No modificate voi i file. È tutto test tanto non ci sono dati. Potete accedere».
- **Decisioni:** 2.1 unita dopo tre corse rifatte. Account Classic scritto dal manager in `.env.local.test` (ignorato), valori mai in Git o note. 2.2 a sub-agente Opus (credenziali e permessi). Secret GitHub NON inseriti da agenti: li inserisce Matteo. Corse dopo l'unione tenute; «CI per rischio» proposta dopo la 2.2.
- **Risultato:** env/test 872c7e1 con 2.1; PR #33 della 2.2 con ci e Vercel verdi, e2e rosso alla guardia per 9 secret mancanti; #34 consegna manager e scheda `schede/2026-10-28-analisi-consumo-actions.md`.
- **Misure:** smoke 17/17 ×3, 55-63 s. Actions dal 26/10: 54 corse, ~375 min, 1 rossa; 8 PR su 17 solo documenti; `Unit tests` ~4 min su ~6. Proiezione: ottobre ~48%, un mese intero a questo ritmo ~3.750 min (sopra 2.000).
- **Ha funzionato:** leggere `.github/` e il log reale di `e2e` dal Git invece del rapporto del sub-agente; controllare valori di `.env` solo con conteggi (`grep -c`).
- **Attenzione:** una PR solo documenti NON prova l'assenza di `e2e` finché `e2e.yml` non è sulla base: errore mio corretto prima del merge. Lo smoke con CRLF fallisce solo nella copia Windows (`core.autocrlf`). I secret sono 9, non 6.
- **Quota Claude (sonda quota.mjs):** 5 ore 15% → 26%; settimana 14% → 16%. Codex 5 ore 32%, settimana 12% (lettura 15:43). Avvio manuale: nessuna soglia.
- **Costo:** sotto-agente Opus 133.261 subagent_tokens; chat principale cumulata nella nota precedente e nel costo della sessione.
- **Letti:** verbale 2.1, LAVORI 2.2, valutazione 2.2, ci.yml, e2e.yml e guardia della PR #33, `gh run list` (serviti).
- **Aperto:** 9 secret (Matteo); e2e verde, prova di blocco, unione della 2.2; conferma «CI per rischio»; `public-booking-smoke` intermittente; catena programmata mai provata.
