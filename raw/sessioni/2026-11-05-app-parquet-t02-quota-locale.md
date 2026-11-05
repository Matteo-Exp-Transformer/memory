# Nota di fine chat — app-parquet: T-02 scheletro e quota letta da locale

> Source: sessione Claude Code 5c69a8a6-d0b9-46b4-8edd-c6d67e7dcfc5, app-parquet
> Collected: 2026-11-05
> Published: 2026-11-05

- **Dove:** Claude desktop (Code), Opus 5.5, cartella locale `app-parquet` (prima vuota, clonata in chat), branch t-02-scheletro-app, PR #2.
- **Obiettivo:** «Leggi solo AGENTS.md e STATO.md, poi esegui la task T-02 (scheletro app)»; «Controlla se da locale a differenza della chat precedente riesce a leggere la tua quota».
- **Decisioni di Matteo:** backup «iniziamo da 1 giorno, cerchiamo di mantenere account gratis supabase e provider in generale»; «Hai ok per le task proposte in generale».
- **Risultato:** React + Vite + TypeScript, PWA installabile, `npm run validate` verde al primo giro, CI su ogni PR; D-12 decisa; T-08 backup gratuito aggiunta.
- **Quota:** da locale si legge con lo strumento `get_usage` dell'app desktop: 5 ore 12% → 14%, settimana 35% → 36%. Dalla chat cloud del 4/11 non si leggeva (registro di app-parquet: «nessuno strumento la legge»).
- **Ha funzionato:** la quota letta da locale dà prima→dopo nel registro senza chiedere a Matteo.
- **Attenzione:** in locale la chat carica circa 20.000 token di strumenti MCP (Vercel, marketing, nimble) a ogni turno anche se non servono.
- **Costo:** chat principale 2.623.538 token (input 50, cache scritta 83.178, cache letta 2.524.557, output 15.753), costo_sessione.py; nessun sotto-agente.
- **Letti:** AGENTS, STATO, REGISTRO di app-parquet (serviti); paragrafo D-12 di DECISIONI (servito); wiki costi-e-quota e una nota del 28/10 di memory (serviti).
- **Aperto:** se un'attività programmata legge la quota (T-01); hosting gratuito ammesso per uso di lavoro.
