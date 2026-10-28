# Nota di fine chat — manager: prima corsa della catena osservata (M1)

> Source: sessione Claude Code b327f78f-7356-4793-a6d3-a8df5acc0db0, CalendarBackup-v2
> Collected: 2026-10-28
> Published: 2026-10-28

- **Dove:** Claude desktop (Code), Opus 5.5, worktree `wt-manager-corsa`; PR #39 (unita, fde3ec7) e #40 di chiusura, verso env/test.
- **Obiettivo:** Matteo: «codex lavora in parallelo su 1.2 - tu intanto agisci come manager della repo e responsabile del sistema agenti»; rivedere la PR #37 e provare la catena programmata osservandola.
- **Decisioni:** difetto dell'identità git dei figli aggirato nella voce M1 (non nello script); corsa non forzata a mano né con scorciatoie dopo la causa trovata; M1 NON CONCLUSA; task rimosso.
- **Risultato:** corsa mai partita. 4 tentativi del pianificatore usciti «nessun_programma» senza riga. Causa: `programma.json` scritto dall'app desktop finisce in `AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Local\`, che il task non vede. Rapporto con 6 fix in `rapporti/2026-10-28.md`.
- **Misure:** node del task partito +577 ms e +805 ms dopo l'appuntamento, quindi l'ipotesi del task in anticipo è smentita; osservatore dei file: nessun file toccato; uscita del task salvata su file: `nessun_programma`; lettura dal task: ENOENT. Validate 1360/1360, albero pulito dopo `npm ci`.
- **Ha funzionato:** eliminare i rami del codice uno alla volta (anticipo, blocco, lettura) con prove dal pianificatore stesso, invece di fidarsi di `LastTaskResult 0`.
- **Non ha funzionato:** la prima ipotesi (anticipo di millisecondi) non era misurata, e ha richiesto un tentativo in più.
- **Attenzione:** tutto ciò che un agente nell'app desktop scrive in `%LOCALAPPDATA%` (anche dal terminale dell'app) è invisibile ai processi fuori dall'app, mentre le letture vedono entrambe le copie. La sonda della fetta A funzionava perché non legge il programma.
- **Quota Claude (sonda):** 5 ore 17% → 24%; settimana 19% → 20% (giorno 2, soglia 20%: stasera nessun avvio possibile). Codex non letto (in uso sulla 1.2).
- **Costo:** chat principale 9.180.433 token (cache letta 8.954.598, output 51.752); nessun sotto-agente; nessun modello della catena avviato.
- **Letti:** AGENTS, manager, STATO, LAVORI, scheda pilota, revisione Codex 1.2, coordinatore, corsa, soglie, scadenza, blocco, misure, merge, ruoli, pianifica.ps1 (serviti); verbale A (servito: identità non provata, sonda senza programma); nota del manager precedente (servita).
- **Aperto:** fix 1 (cartella dati) e 2 (tentativo senza riga) da scrivere e assegnare; poi riconfermare M1.
