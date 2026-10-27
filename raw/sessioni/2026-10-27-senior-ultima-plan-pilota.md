# Nota di fine chat — plan del pilota della catena ultimato
> Source: Claude Code desktop, sessione 9226736f-8235-49f3-a26f-9a026a1d95cc, repo CalendarBackup-v2
> Collected: 2026-10-27
> Published: 2026-10-27
- **Dove:** Claude Code desktop, Claude Opus 5.5, avvio manuale di Matteo come senior che ultima il plan del pilota; worktree proprio wt-senior-pilota sul branch piano/lavoro-1a-quota-codex; nessun sotto-agente; una prova con Claude haiku.
- **Obiettivo di Matteo:** «Il tuo compito è ultimare e definire il plan per provare UN caso pilota, non costruirlo»; «Parlami in italiano semplice: io valuto l'uso, non le scelte tecniche».
- **Decisioni di Matteo:** nessuna nuova; applicata la scelta già data «Proviamo la 1, ma teniamo le altre possibilità da valutare. Poi capiremo modo migliore usandolo.» e «il team si studierà attivamente tramite agente manager per capire questo genere di decisioni da migliorare prendere o proporre».
- **Risultato:** in CalendarBackup-v2 schede/2026-10-27-pilota-catena-agenti.md con «Misure prima e dopo», «Autovalutazione del manager», «Controllo del mandato» (controlla_scheda 0 errori); valutazione critica §7; team/senior-sistema-agenti.md punto 6; STATO.md.
- **Ha funzionato:** una misura sola ha cambiato il disegno: una chiamata Claude dà una sola riga rate_limit anche con 3 turni (18:57Z, 83,7 k token, 66,9 k da cache), quindi l'esecutore rilegge la quota con una sonda a ogni commit. Le opzioni 2 e 3 si calcolano su ogni tentativo senza applicarle: dati per confrontarle senza cambiare le soglie.
- **Attenzione:** la cartella principale era sul branch audit/frontend-performance di un'altra chat; lavoro fatto solo nel worktree proprio. CI della corsa B: 4 corse, non 2. Mancava cosa succede dopo 7 tentativi rifiutati.
- **Quota:** Claude 18:57Z 5h 24% / settimana 2% → 19:01Z 27% / 2%; Codex 19:01Z 56% / 20% (non usato da questa chat, uso parallelo); avvio manuale, nessuna soglia applicata.
- **Costo:** costo_sessione.py: chat principale claude-opus-5-5 2.664.566 token (input 38, cache scritta 119.009, cache letta 2.513.005, output 32.514); prove: haiku circa 0,008 $ in 2 chiamate.
- **Letti:** serviti, progetto: STATO.md, team/{senior-sistema-agenti,manager,revisore,costruttore}.md, LAVORI.md, schede/2026-10-27-{sistema-agenti-valutazione-critica,pilota-catena-agenti}.md, richieste/2026-10-27-autonomia-tecnica-e-ciclo-agenti.md (coda), esperimenti/catena-minima/catena.mjs (righe quota e uso), scripts/quota.mjs di 1a.
- **Letti:** serviti, memory: .claude/skills/{progetta,chiudi}/SKILL.md, wiki/metodo/criteri-di-progetto.md, strumenti/controlla_scheda.py (nomi funzioni), AGENTS.md (Note di fine chat), raw/sessioni/2026-10-27-senior-critica-e-pilota.md; non servito: niente.
- **Aperto:** peso di 1 M token per modello in punti di settimana → registro della corsa B; conferma del manager in LAVORI.md dopo #17, #18 e la revisione Codex del piano di A.
- **Sessione:** Claude Code 9226736f-8235-49f3-a26f-9a026a1d95cc
