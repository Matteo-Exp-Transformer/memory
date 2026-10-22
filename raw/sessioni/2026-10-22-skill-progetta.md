# Nota di fine chat — skill progetta e controllo della scheda

> Source: sessione Claude desktop (Code) locale sul PC di Matteo; link non disponibile
> Collected: 2026-10-22
> Published: 2026-10-22

- **Dove:** Claude desktop, scheda Code, sul PC; Opus 5.5 per decisioni e testo della skill, un sotto-agente Sonnet per script, hook e prove; prova finale con Codex CLI 0.162.0.
- **Obiettivo di Matteo:** «Chat 2: la skill progetta nella repo memory», con quattro regole (mancanze classificate, ricerche con fonti A, M o B, incognite con lo sblocco, soluzioni con stima); «Finito quando: la skill funziona sia in Claude sia in Codex, e lo script fallisce su tre schede sbagliate preparate apposta (un campo R2 mancante, un livello assente, un finito senza comando) e passa su una giusta».
- **Decisioni di Matteo:** «Decide Opus, esegue Sonnet»; «Ottimo fai chiusura». Le scelte tecniche le ha prese Claude: una scheda per lavoro in `schede/` della repo del progetto; brief solo in chat, non salvato; una mancanza `[blocca]` fa fallire il controllo.
- **Risultato:** `.claude/skills/progetta/` (SKILL.md e scheda-modello.md), `.agents/skills/progetta/SKILL.md` (rimando), `strumenti/controlla_scheda.py`, `controlla-scheda.sh`, `hook-scheda.sh`, `installa-hook-scheda.sh`, `prova_scheda.py`, `prove-scheda/`; commit `4bc9092`.
- **Ha funzionato:** decisioni prima, poi un solo brief a Sonnet; prove con casi che devono fallire (ogni scheda sbagliata dà un solo errore); hook provato su una repo nuova (3 commit bloccati, 1 passato); Codex ha trovato la skill dal rimando e lanciato il controllo.
- **Non ha funzionato / attenzione:** in `codex exec --sandbox read-only` la shell PowerShell non parte («helper_unknown_error: setup refresh had errors») e Codex ripiega su node_repl; l'hook ha scritto dentro il percorso assoluto di memory (se la repo si sposta, si reinstalla); un commit bloccato mostra il percorso di una cartella temporanea.
- **Costo:** sotto-agente Sonnet 107.472 token; Codex 18.105 token; chat principale non letta.
- **Aperto (dipende da fatti non disponibili):** la skill non è ancora stata usata su un lavoro vero; l'hook non è installato in nessuna repo di progetto (si installa alla prima scheda).
