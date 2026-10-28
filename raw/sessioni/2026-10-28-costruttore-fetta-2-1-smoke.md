# 2026-10-28 — Costruttore Codex, fetta 2.1 smoke
Dove: Codex desktop Windows, chat 01a1831a-e429-71a2-a2ff-b357188df27e, progetto CalendarBackup-v2 / PrenotaZen.
Obiettivo di Matteo: «Consegna: PR con `ci` e `Vercel` verdi, non unire. Criteri di push, quota a «chiudi», STATO.md.»
Vincolo di Matteo: «File esclusivi: scripts/e2e-smoke.txt (LF, nessuna riga vuota) e il verbale schede/2026-10-28-lavoro-2-esito-fetta-2-1.md. Nessuno spec, nessun playwright.config.ts.»
Risultato: commit e8345af, PR https://github.com/Matteo-Exp-Transformer/CALENDARIO-V2/pull/32; lista cinque file, verbale nel percorso richiesto. Nessun merge; stato al manager secondo STATO.md di base, senza oltrepassare i due file esclusivi.
Funzionato: guardia TEST prima di ogni corsa, un worker, tre corse finali 17/17 senza salti in 53,251 / 55,648 / 56,690 s; validate 1360/1360; elenco completo ancora 118 casi.
Non funzionato: candidato public-booking-smoke intermittente, form assente entro 10 s a 375px nella seconda corsa; escluso. La corsa diagnostica con retries=2 passa subito, non annulla il rosso precedente.
Imparato: F2 legge tre nomi E2E_CLASSIC_* oltre ai sei secret iniziali; la futura 2.2 deve seguire gli spec attuali. Nessun valore riservato nella consegna; file ambiente temporaneo rimosso.
Quota iniziale Codex 5h 13%, settimana 9%; alla chiusura 5h 29%, settimana 11%. Avvio manuale, nessuna soglia.
- **Costo:** Alla stesura: 6.644.008 token totali, input 6.628.263 (cache 6.537.600), output 15.745; letti con costo_sessione.py codex dalla cartella originale della chat. Nessun sub-agente.
- **Letti:** (serviti) AGENTS.md, STATO.md (locale e origin/env/test), team/costruttore.md, LAVORI.md, schede/2026-10-28-lavoro-2-prove-automatiche-prima-dell-unione.md; playwright.config.ts, vite.config.ts, .gitignore, package.json, .husky/pre-commit, .github/workflows/ci.yml.
- **Letti:** (serviti) e2e/{admin-login,public-booking-smoke,admin-booking-mgmt,admin-menu-magazzino-ct,public-menu-qr,edition-classic-data-protection}.spec.ts; e2e/helpers/supabaseStaging.ts; verbale prodotto; skill Supabase; memory/AGENTS.md e .claude/skills/chiudi/SKILL.md.
- **Letti:** (non serviti) memory/wiki/index.md (nessuna decisione aggiuntiva), scripts/controlla-contesto.mjs (bastava eseguirlo).
Aperto: causa tecnica dell'intermittenza del form → indagine del senior/manager; aggiornamento STATO.md → manager, come già disposto nella base. Revisione della consegna prima del merge.
Sessione: codex://threads/01a1831a-e429-71a2-a2ff-b357188df27e.
