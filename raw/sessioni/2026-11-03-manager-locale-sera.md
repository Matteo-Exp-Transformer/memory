# 2026-11-03 — manager locale della sera: PROD controllata, SV1 e SV2 unite
Progetto: CalendarBackup-v2 / PrenotaZen · Ruolo: manager (Opus), avvio manuale di Matteo dal PC · 22:20-23:15

## Cosa è successo
- Controlli di PROD dopo il rilascio LG1+LG2: main e5aa72d, `ci` e Vercel verdi, bundle su rwuxgvld, login 200 in 0,5 s, nessun errore Vercel in 3 giorni. Tag `rilascio/2026-11-03` su 053290c, ramo segnaposto cancellato.
- Unite in env/test #150, #148, #145 (SV1), #149 (SV2, 072 su TEST con la checklist). Tipi generati uguali a quelli scritti a mano.
- Scoperta: la 069 non è in PROD (la valutazione del senior cloud diceva il contrario). SEC069 passa da «urgente in PROD» a «prima del rilascio di Servizio».
- Le prove `e2e-collaudo` di SV1 e SV2, scritte dal cloud senza anteprima, andavano in timeout: Servizio si apre in vista Lista. Corrette e provate rosse sul codice vecchio.
- Revisioni Sonnet su #142, #141, #148, #139-#140: 1 P1 vero (FX4: `merge.mjs` rifiuta la PR uscita dalla bozza senza commit nuovo), 3 P2 (RV1).

## Lezioni
- Una prova scritta senza poterla lanciare va lanciata prima di togliere la bozza: correggerla dopo è costata ~14 minuti di Actions (corsa cancellata + e2e in più).
- «Già in PROD» si verifica con `list_migrations` e `pg_proc` di PROD prima di decidere l'urgenza.
- Revisioni Sonnet a sub-agente: ~110-150 mila token l'una, rilievi utili; i P1 vanno sempre ricontrollati sul codice (qui il P1 era vero, ma pesa solo sulla catena).
- Sul PC manca un Postgres locale (Docker spento, niente `psql`): le prove SQL delle migrazioni oggi le fa solo il cloud.

## Costo e letture
- **Costo:** quota Claude 22:20 settimana 2%, 5 ore 16% → 23:08 settimana 7%, 5 ore 45%; Codex nessun record valido. Chat principale 17,3 M token, 272 mila non in cache (circa 1,7 punti con 156 mila per punto); sub-agenti Sonnet 113 mila + 108 mila + 151 mila. Actions ~59 minuti (previsti 49).
- **Letti:** team/manager.md, STATO e LAVORI dal ramo di #150, migrazione 072, spec di SV1 e SV2, merge.mjs, AdminAuthContext: serviti. Scheda della valutazione: poco servita (letta intera per 5 righe). Skill chiudi: servita.
