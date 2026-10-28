# 2026-10-28 — Fetta 2.1, esito CI e quota dopo attesa
Dove: Codex desktop Windows, chat 01a1831a-e429-71a2-a2ff-b357188df27e; integrazione immutabile della nota 2026-10-28-costruttore-fetta-2-1-smoke.md.
Obiettivo di Matteo: «Consegna: PR con `ci` e `Vercel` verdi, non unire.»
Risultato verificato: https://github.com/Matteo-Exp-Transformer/CALENDARIO-V2/pull/32 aperta, mergedAt null; SHA e8345afb95d2df9d783870eb0d2cd5007b77cd28 con ci success (8m14s), Vercel success e Vercel Preview Comments success. Worktree pulito, solo i due file autorizzati nel diff.
Quota Codex prima 5h 13% / settimana 9%; dopo l'attesa CI, misura finale 5h 32% / settimana 12%. Nessuna soglia per l'avvio manuale.
Funzionato: attesa dei check sullo SHA consegnato senza duplicare le corse; CI precedenti duravano 5m39s–8m13s, confronto utile per interpretare l'attesa.
- **Costo:** 8.353.650 token totali, input 8.334.566 (cache 8.236.672), output 19.084, cumulativi della stessa chat; costo_sessione.py codex dalla cartella originale, nessun sub-agente.
- **Letti:** file e utilità come nella nota principale (serviti/non serviti già distinti); nessun nuovo file di contesto letto dopo la nota, solo stati dei check e Git.
Aperto: revisione base e STATO.md al manager; causa tecnica del timeout intermittente da accertare. Nessun merge effettuato.
Sessione: codex://threads/01a1831a-e429-71a2-a2ff-b357188df27e.
