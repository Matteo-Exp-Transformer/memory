# Nota di fine chat — quale app vedono i clienti e prova del tasto Aiuto (PrenotaZen)

> Source: sessione Claude desktop (Code) avviata dal telefono, girata sul PC, id 74db1d8b-1105-42a1-bc32-a10206cfe9a3
> Collected: 2026-10-22
> Published: 2026-10-22

- **Dove:** Claude desktop (Code), sessione creata dal telefono ma in esecuzione sul PC, cartella `Io-Claude`; Opus 5.5.
- **Obiettivo di Matteo:** «Pianifichiamo task : l'app è accesa? In calendarbackup. Recupera info da repo Memory e poi progettiamo il lavoro.»; e se avviare dal telefono costa più token che dal PC.
- **Decisioni di Matteo:** «intanto svolgiamo zero A più 1. Svolgerò in altra chat anche 0B e 2»; «Non avviare server se non serve»; «Hai mio ok per file vuoto» (`.git/HEAD.lock` del 03/09); «Al ritrovo usa questo link : https://calendario-v2.vercel.app/login»; «Hai ok al push».
- **Risultato:** siti → DB: `calendario-v2.vercel.app` (progetto `prenotazen-test`, `main` di CALENDARIO-V2) e `prenota-zen.vercel.app` su DB prod `rwuxgvld`; `calendario-alritrovo-prenotazioni.vercel.app` (v1) su `dphuttzg`; anteprima PR 14 su DB test `docnnernvp`. PR 14: tasto Aiuto Classic spostato in basso a sinistra (commit 4bb5aa6, pushato). `CalendarBackup-v2-paracadute/STATO.md` riscritto. Commit 173eca4 e a66e0b5 su `feat/cloud-bootstrap`. 40 processi node di Codex chiusi da Matteo.
- **Ha funzionato:** la sessione avviata dal telefono gira sul PC, quindi lo stesso costo d'avvio di una chat locale (smentisce `docs/MOBILE_BOOTSTRAP.md` §0); leggere l'URL Supabase nei pacchetti JS pubblici dice su che DB sta ogni sito; Playwright con `--env-file` fa il login di prova senza che le credenziali passino dalla chat.
- **Non ha funzionato:** lettura diretta delle credenziali di test negata dal classificatore; MCP Vercel vede 2 progetti su 4 e le variabili danno 403; `.git/HEAD.lock` vuoto del 03/09 bloccava i commit; l'hook MSS chiede di rilanciare ogni commit; la sessione aperta in `Io-Claude` invece che in `CalendarBackup-v2` ha obbligato a ricostruire il contesto a mano.
- **Costo:** chat principale claude-opus-5-5 7.305.657 token (cache letta 7.058.449, cache scritta 208.748, output 38.372), letto prima della chiusura; nessun sotto-agente.
- **Letti:** `memory/AGENTS.md` servito; `wiki/index.md` servito; `wiki/metodo/costi-e-quota.md` servito; `wiki/progetti/prenotazen-calendarbackup.md` non servito; `raw/sessioni/2026-10-22-paracadute-errori.md` servito; skill `chiudi` servito; `Io-Claude/Esplorazione/LETTURA_MATTEO.md` (In 30 secondi) servito; in CalendarBackup-v2: `docs/MOBILE_BOOTSTRAP.md` servito, `package.json` non servito, `schede/2026-10-22-paracadute-errori.md` servito, `STATO.md` servito, `e2e/pro/pro-login.spec.ts` servito, `HelpButton.test.tsx` servito, `vite.config.ts` non servito; `MSS/docs/pilota-prenotazen/LEGGIMI.md` servito.
- **Aperto:** spegnere la v1 `calendario-alritrovo-prenotazioni` → Matteo; a cosa serve `prenota-zen.vercel.app` → Matteo; Sentry o Supabase + Brevo per l'allarme errori → Matteo, chat del lavoro 2; permessi MCP Vercel → collegamento Vercel.
- **Sessione:** 74db1d8b-1105-42a1-bc32-a10206cfe9a3
