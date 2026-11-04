# 2026-11-04 — Senior della catena («Senior · catena»), SV5, PrenotaZen

- **Dove:** chat locale sul PC, Sonnet 5.5, avvio manuale. Prompt di Matteo: lavoro 1 = SV5 con la catena (prima corsa vera di FX6), lavoro 2 = progettare il confronto macchina contro chat Opus con sotto-agenti, allineare SV8, budget 3 punti Claude.
- **Corsa SV5 (09-00-03, Claude):** costruita, `prova.collaudo` verde sull'anteprima del commit (codice 0, nessun errore): FX6 chiusa. Bloccata però con `file_fuori_fetta`: l'apertura su Mappa rompe 4 test di `ServizioPage.deleteTableOccupato.test.tsx`, file fuori dalla fetta; il controllore l'aveva ammesso, lo script no. Il senior ha portato la correzione dell'esecutore sul ramo (`npm run validate` 1412/1412, hook attivi), #163 unita con `ci`, `e2e`, Vercel verdi. Diff letto contro i sette casi: tutti coperti. Limite noto: «prossima prenotazione» senza timer.
- **Causa vera:** le voci SV elencano i file di test della fetta ma non quelli che il cambio di comportamento rompe. Da fare per SV6-SV7 (cercare i test che dipendono dal default cambiato).
- **Documenti (#165):** FX6 chiusa, SV5 unita, casi limite di SV6 (7) e SV7 (9) nel Finito, SV6 con ShiftBriefingModal e helper estratto nei file esclusivi, SV8 allineata a codex.
- **Lavoro 2:** non costruito; proposta data a Matteo in chat, scheda e voce dopo la sua risposta.
- **Errori:** `python3` è l'alias del Microsoft Store su questo PC: usare Node. Nessun `--no-verify`.
- **Quota:** Claude 8:59 settimana 16%, 5 ore 55% → 9:31 settimana 18%, 5 ore 62% (2 punti su 3). Codex 2%/12% invariata.
- **Actions:** ~25 minuti (due giri di ci+e2e su #163) più la PR documenti; giornata ~93, sopra il tetto di 60, accettato da Matteo nel prompt.
- **Costo:** punti Claude della chat 2 (la corsa SV5 e questa chat insieme; la corsa da sola: quinta 55→61%, settimana 16→17%); nessun sotto-agente.
- **Letti:** STATO, LAVORI (piano, FX6, SV5-SV8), scheda Servizio Blocco 1-2, `useTableStatuses.ts`, `shiftBriefingPdf.ts`, `ShiftBriefingModal.tsx`, registro e stato della corsa, diff di #163: tutti serviti.
