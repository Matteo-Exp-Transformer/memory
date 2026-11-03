# 2026-11-03 — Sessione cloud a PC spento: LG2 e INV, PrenotaZen

- **Dove:** sessione cloud Claude Code (branch `ccr-0357a516-lhvugr`), Opus 5.5, avvio manuale di Matteo, 3/11 mattina con il PC spento, fuori dalla catena. Nota scritta dopo, dalla chat manager del 3/11 (memory stava sul PC).
- **Obiettivo di Matteo:** portare avanti la lista del 3/11 senza il PC: LG2, poi INV.
- **Risultato:** LG2 unita in env/test con PR #139 (27/27, `npm run test` 1379/1379, mutazioni rosse, ci, e2e e Vercel verdi); INV fatta con PR #140 ([scheda](https://github.com/Matteo-Exp-Transformer/CALENDARIO-V2/blob/env/test/schede/2026-11-03-inventario-funzionalita.md)), 10 proposte «rilascio» per Matteo; richiesta sulla CI scritta per il manager.
- **Parole di Matteo:** sulla CI «Cerchiamo di fare in modo che basti per tutto il mese [...] Facciamola girare a gate. Lascia indicazioni in merito a questo per il prossimo agente manager.»; su LG2 revisione Codex dalle Actions o dal connettore, altrimenti unione a controlli verdi con nota.
- **Scoperta:** `@codex review` in un commento della PR fa la revisione Codex in circa 1 minuto senza minuti di Actions; dal cloud non c'è `codex exec`.
- **Errore:** un commit di soli documenti sopra la PR di LG2 ha rifatto ci ed e2e completi (~13 minuti di Actions). Da qui la regola «mai documenti sopra una PR con codice».
- **Imparato:** a PC spento mancano memory, `codex exec`, la quota Codex e il lettore dei costi: la sessione lascia registro e nota da completare. Le mutazioni le ha fatte chi ha costruito: le ha rifatte il manager il 3/11, tutte rosse come previsto.
- **Quota:** non misurata nella sessione. Lettura successiva (chat manager, 3/11 8:44): Claude settimana 87%, 5 ore 23%; Codex non misurabile dal cloud.
- **Costo:** token non misurati (nessun `costo_sessione.py` nel cloud). Actions: ~35 minuti per LG2 e ~2 per INV, stime dagli orari delle corse.
- **Letti:** file letti dalla sessione cloud non noti (nota scritta dopo). Fonti di questa nota: STATO.md e LAVORI.md di env/test 82de499, corse Actions di #139 e #140: servite.
