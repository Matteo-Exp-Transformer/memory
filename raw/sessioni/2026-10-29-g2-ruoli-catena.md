# Nota di fine chat — costruttore Claude, fetta G2 (ruoli della catena)

> Source: sessione Claude Code desktop cf3de371-01b4-43a8-b823-282b0d401dda
> Collected: 2026-10-29
> Published: 2026-10-29

- **Dove:** Claude Code (app desktop), Sonnet 5.5, avvio manuale di Matteo, worktree wt-claude-g2-29-10, branch claude/g2-ruoli-29-10.
- **Obiettivo di Matteo:** eseguire il prompt `richieste/2026-10-29-prompt-g2-claude.md` come costruttore G2; poi «Accetta» sulle 3 righe toccate in verifica-catena.mjs e «fai chiudi, inanto avvio manager».
- **Decisioni di Matteo:** «Accetta» (3 righe di verifica-catena.mjs, vincolo violato per due test storici incompatibili con la voce G2).
- **Risultato:** PR bozza #62 verso env/test: R1 senza senior-piano, senior-controllo con Bash di sola lettura e prova, analista-sistema dopo la corsa; 124 test verdi, validate verde, mutazioni rosse. Non passa `ci` finché G1 non è unita (voce.mjs).
- **Ha funzionato:** test scritti prima (rossi sui sorgenti originali); prova reale della CLI con haiku in un repo di scarto: commit, Write e `--output` negati.
- **Non ha funzionato / attenzione:** quota «prima» non rilevata all'inizio; STATO.md non riscritto (era fuori dai confini di G2 e parte il manager).
- **Costo:** chat principale 7.575.586 token (cache letta 7.346.807, cache scritta 176.314, output 52.379); quota dopo: 5 ore 44%, settimana 33%.
- **Letti:** AGENTS.md (servito), team/costruttore.md (servito), LAVORI.md voci G1 e G2 (servito), schede/2026-10-29-macchina-regole-e-cancelli.md (servito), scripts/catena/coordinatore.mjs, corsa.mjs, chiusura.mjs e ruoli/*.md (serviti), verifica-catena.mjs e verifica-audit.mjs (serviti: hanno rivelato i due test incompatibili), merge.mjs (servito), voce.mjs del branch G1 (servito), skill progetta (servito per le cinque regole), skill chiudi (servito), STATO.md (non servito: non riscritto).
- **Aperto (dipende da fatti non disponibili):** unione di G1 → poi riallineo di #62 e unione da parte del manager; unificare `fettaConfermata` storica con voce.mjs.
