# Nota di fine chat — senior: lavori degli audit come pilota

> Source: sessione Claude Code d660e51e-b711-4969-87fd-c82c7193a74e, CalendarBackup-v2
> Collected: 2026-10-28
> Published: 2026-10-28

- **Dove:** Claude desktop (Code), Sonnet 5.5, worktree proprio `CalendarBackup-v2-audit`, branch piano/lavori-audit-come-pilota, PR verso env/test.
- **Obiettivo di Matteo:** «Partiamo con lavoro 1 e poi lavoro 2 . Usiamolo come pilota.» Poi: «Lasciamo tutto pronto per [il] manager che analizzerà e smisterà la situazione e mi darà prompt per agente esecutore.»
- **Decisioni:** lettura confermata in chat (lavoro 1 = menu/prenotazione più veloci, lavoro 2 = prove automatiche); fetta della corsa B = immagini pubbliche più leggere, senza src/; fette di codice dopo il lavoro 2.
- **Risultato:** richiesta, due schede (0 errori), Corsa B riscritta, STATO; PR #19 con `ci` e `Vercel` verdi.
- **Misure:** PNG a palette −85/−95% sui 4 campioni; build 88 s; CI ottobre 24 corse, 156 minuti; sharp provato fuori dal repo.
- **Ha funzionato:** misurare prima (il test dei nomi nell'e2e ha escluso WebP); fare la fetta 1.1 provabile solo con controlli su file nel check `ci`.
- **Attenzione:** i secret di GitHub li inserisce Matteo; limite per IP dei runner e minuti gratuiti non verificati (fonte B).
- **Quota Claude (get_usage):** 5 ore 9% → 16%; settimana 8% → 9%. Avvio manuale: nessuna soglia.
- **Costo:** chat principale 4.590.309 token (cache letta 4.378.236, output 47.885); nessun sotto-agente.
- **Letti:** AGENTS.md, STATO.md, servizio-clienti, senior-sistema-agenti, LAVORI, revisore, costruttore, skill progetta e criteri (serviti); unione, due audit Codex, scheda del pilota (serviti: hanno deciso fette e criterio); ci.yml, playwright.config, helper e2e, vite.config, menuThemes (serviti).
- **Aperto:** chiavi TEST su GitHub; prova di aspetto di Matteo; PSNR su tutti i 13 file.
