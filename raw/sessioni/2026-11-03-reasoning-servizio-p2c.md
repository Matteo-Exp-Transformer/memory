# 2026-11-03 — Reasoning: analista, fetta 75/25 e pagina Servizio, PrenotaZen

- **Dove:** Claude desktop (Code), senior di reasoning Opus 5.5 avviato a mano da Matteo. Tipo per E1: reasoning.
- **Obiettivo di Matteo:** decidere P2C gruppo 1, fetta del 75/25 e pagina Servizio; decisioni in scheda e LAVORI.md.
- **Decisioni di Matteo:** «Rilasciamola. Lo scopo è intanto avere app completa con le funzionalità già iniziate. In seguito farò testare a ristoratori app intera e vediamo come va. Per ora però il criterio di sblocco non è un ristoratore, il criterio è che deve essere funzionale secondo me che in sala ci ho lavorato..poi raccogliamo feedback». «Farò io e altri utenti, e agenti serate finte su prod. (Con agenti ad app finita simuleremo dei test chiedendo ad agenti di agire con qi bassi in modo da identificare problemi.» «Ho testato prod sembra tutto ok. Anche aspetto delle pagine sembra ok.»
- **Risultato:** CalendarBackup-v2 `schede/2026-11-03-servizio-in-prod.md`, `richieste/2026-11-03-servizio-in-prod.md`, voce P2C1 in LAVORI.md. MG1b confermata, MG2 ferma, stash senza valore per Servizio.
- **Ha funzionato:** leggere i diff dei tag di stash e `decidiAnalisi` ha risolto da solo due punti senza chiedere a Matteo.
- **Imparato:** l'analista riceve solo le righe della corsa corrente anche alla quinta, quindi «dati insufficienti» è strutturale. Il collaudo Servizio del 26/8 è già 26/26 di Matteo: la domanda vera era il criterio di sblocco, non chi prova.
- **Non ha funzionato:** avevo proposto la persona esterna come cancello: Matteo l'ha tolto. Le mie opzioni partivano dalla formula del prompt invece che dal suo scopo, l'app completa.
- **Aperto:** accesso degli agenti a PROD per le serate finte: in questa app un agente non digita password su PROD, e AGENTS.md dice «Test automatici solo mock/TEST» → scheda ad app finita.
- **Quota:** Claude settimana 77% al 2/11 → 79%. Codex 70%, azzera 4/11 8:44. Punti previsti 2, reali 2.
- **Costo:** riga `costo-chat` in team/registro.jsonl, circa 1,5 punti stimati con 156 mila per punto; nessun sotto-agente.
- **Letti:** servizio-clienti, STATO, voci LAVORI, progetta, criteri, revisione Claude, corsa.mjs, FOLLOW_UP Servizio, collaudo: serviti. Memoria S4: servita per le decisioni del 6/8. Masterplan Servizio: poco.
