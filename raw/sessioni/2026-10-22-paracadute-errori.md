# Nota di fine chat — prima prova del metodo su PrenotaZen (paracadute errori)

> Source: sessione Claude desktop (Code), id f6177421-8cf1-4fb0-ad38-d5d293869b10
> Collected: 2026-10-22
> Published: 2026-10-22

- **Dove:** Claude desktop, chat di ragionamento Opus 5.5; esecutore Sonnet in una chat separata.
- **Obiettivo di Matteo:** «pianifichiamo : riparazione , sviluppo, completamento app prenotazen»; «realizziamo la prima task da svolgere e proviamo metodo della repo Memory su questa task».
- **Decisioni di Matteo:** «Le mie sono idee trattale come tali»; «No revisioni per ora lavoriamo sul test e prossima settimana al reset di token codex e Claude fare revisione e merge su main e production»; «In linea generale anche i test di navigazione attiva nell'app la fanno agenti. Se non riescono o richiede troppi token ( stimiamo in fase di Plan ) allora testo io , mi date procedura e link per testare nelle pr GitHub.»; anteprime Vercel: «Prova a farlo tu».
- **Risultato:** scheda `CalendarBackup-v2/schede/2026-10-22-paracadute-errori.md` (R3, 0 errori); PR https://github.com/Matteo-Exp-Transformer/CALENDARIO-V2/pull/14 aperta; variabili Vercel `VITE_SUPABASE_*` di `prenotazen-test` separate, Preview su DB di test; skill `progetta` aggiornata (commit 83afc7b).
- **Ha funzionato:** scheda con scelte già fatte, Sonnet ha consegnato in una sessione; link dell'anteprima Vercel nella PR, comodo per Matteo; il tasto Aiuto apre l'email compilata.
- **Non ha funzionato:** le anteprime erano sul DB di produzione, quindi le pagine di prova non c'erano e Matteo pensava di aver sbagliato; istruzioni della PR per Matteo poco chiare («guarda in orizzontale»); la cartella di lavoro separata non aveva `.env.local.test`, Sonnet non è entrato nell'app; `installa-hook-scheda.sh` avrebbe scritto in `.husky/pre-commit` (tracciato) un percorso del PC, non installato; il controllo MSS della repo chiede di rilanciare ogni commit.
- **Costo:** chat principale claude-opus-5-5 10.944.144 token (cache letta 10.609.003, output 55.305); chat di Sonnet non letta: separata, senza nota. Matteo: Codex esaurito, Claude «oltre 60 % utilizzo settimanale».
- **Letti:** `wiki/index.md` servito; `wiki/metodo/criteri-di-progetto.md` servito; `wiki/progetti/prenotazen-calendarbackup.md` non servito; `wiki/metodo/costi-e-quota.md` servito; skill `progetta`, `scheda-modello.md`, `controlla_scheda.py`, `installa-hook-scheda.sh`, `hook-scheda.sh` serviti; in CalendarBackup-v2: `src/router.tsx`, `AdminShell.tsx`, `devConsole.ts`, `logger.ts`, `TenantContext.tsx`, `features.ts`, `vercel.json`, `.husky/pre-commit` serviti; `docs/APP_CONTEXT_SKILL.md` (§1b, §4, §5b) servito; `AGENTS.md`, `.claude/CLAUDE.md` serviti; `AdminDashboard.tsx` (grep) servito; PR 14 servita.
- **Aperto:** quale progetto Vercel serve i clienti (`prenotazen-test`, `prenota-zen`, `calendario-alritrovo-prenotazioni`) → passo 0 del piano; tasto Aiuto su Classic a 375 px su DB di test → prova di un agente.
