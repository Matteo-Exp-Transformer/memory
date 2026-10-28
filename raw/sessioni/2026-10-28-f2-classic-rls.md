# Nota di fine chat — F2 Classic RLS
> Source: sessione Codex 01a18254-b721-78b1-80ad-b6b618da9b29
> Collected: 2026-10-28
> Published: 2026-10-28

- **Dove:** Codex desktop locale, costruttore Codex, avvio manuale; CalendarBackup-v2, worktree f2-classic-rls.
- **Obiettivo di Matteo:** «Niente asserzioni condizionali; i dati di prova li crea e li rimuove il test.»
- **Decisioni di Matteo:** «Consegna: PR verso env/test, aspetta `ci` e `Vercel` verdi, non unire.»; «registra le percentuali di quota a «chiudi» e aggiorna STATO.md».
- **Risultato:** PR https://github.com/Matteo-Exp-Transformer/CALENDARIO-V2/pull/27; verbale rosso/verde nella descrizione; stato nel progetto, STATO.md. Commit test c785563 con ci/Vercel verdi; chiusura aebac7f in attesa dei nuovi check finali. Nessun merge.
- **Ha funzionato:** fixture UUID isolata, sessione reale Classic verificata per lo stesso tenant, pulizia obbligatoria; togliere temporaneamente il seed ha prodotto il rosso atteso prima del login.
- **Non ha funzionato / attenzione:** costo_sessione dal nuovo worktree non trova la chat; eseguito dalla cartella iniziale della chat. La CI ha impiegato 8m6s, contro 57,51s dei test locali.
- **Quota Codex prima/dopo le modifiche:** 5h 0% → 8%; settimana 7% → 8% (misura 28/10 12:00:18 UTC). Nessuna soglia per avvio manuale.
- **Costo:** 3.859.821 token chat (input 3.848.094, cache 3.729.024, output 11.727), misurati prima della nota e dell'attesa finale; nessun sotto-agente.
- **Letti:** servito — progetto AGENTS.md, team/costruttore.md, LAVORI.md (F2), STATO.md di origin/env/test; spec F2, e2e/helpers/supabaseStaging.ts, playwright.config.ts, e2e/edition-classic.spec.ts (inizio), src/types/database.ts (customers), src/contexts/TenantContext.tsx, package.json, .gitignore, .husky/pre-commit, .github/workflows/ci.yml; skill supabase/SKILL.md e docs sicurezza/changelog Supabase; memory AGENTS.md, skill chiudi/SKILL.md, esempio raw/sessioni/2026-10-21-avvio-memoria.md.
- **Non servito:** STATO.md della cartella iniziale, superato dal remoto; docs Supabase Generating TypeScript Types (non occorre rigenerare tipi).
- **Aperto:** revisione e decisione del manager sulla PR; gli E2E restano locali fino alla fetta CI prevista. I nuovi check del commit documentale sono attesi nella stessa chat.
