# 2026-11-02 — Collaudo RNS eseguito da Sonnet, PrenotaZen

- **Dove:** Claude desktop (Code), chat di reasoning Opus 5.5 avviata a mano da Matteo; sottoagente Sonnet 5.5. Tipo per E1: reasoning.
- **Obiettivo di Matteo:** «vorrei che i test che sono da fare sull'app venissero organizzati con Playwright per Sonnet, che eseguirà i test al posto mio di verifica. Voglio provare questo tipo di task con intelligenza artificiale.»
- **Decisioni di Matteo:** «Hai il mio ok per prod e rns.» «autorizzo agenti a girare su prod per valutare effetti dei fix se serve.»
- **Risultato:** CalendarBackup-v2 `e2e-collaudo/`, `rapporti/collaudo-rns-2026-11-02/RAPPORTO.md`, voce CR1. 6 prove verdi, due corse 9/9, nessun difetto dell'app. PROD non toccata in questa chat.
- **Ha funzionato:** Sonnet con un brief preciso ha scritto prove vere e ha dichiarato da solo il punto debole (prova 2, soglia a occhio, non provata sul codice vecchio). Il controllo opposto, guasto di 3 s, ha mostrato che il login regge 1,2 s, non «qualche secondo».
- **Imparato:** un `e2e` rosso sul ramo di rilascio non era un difetto: spec vecchi; stesso codice con spec di env/test, 18/18. Un rosso va riprovato cambiando una cosa sola. La 406 viene solo da uno slug inesistente.
- **Non ha funzionato:** il limite di create-booking (6 in 10 minuti, blacklist 24 ore) ha allungato una corsa da 1,3 a 9,2 minuti. Le righe di prova cancellate lasciano il contatore `tenant_usage` cresciuto: riportato a mano dal sottoagente.
- **Quota:** Claude settimana 71% → 74%, 5 ore 30% → 49%; Codex 68% invariato (lettura delle 14:13 UTC). Punti previsti 3, reali 3.
- **Costo:** sottoagente Sonnet 316.000 token (avviso di fine), 29 minuti; chat principale Opus nel registro team/registro.jsonl, riga costo-chat del 2/11.
- **Letti:** STATO, servizio-clienti, scheda di rilascio, voci RNS e P2C, memoria connettori: serviti. Skill chiudi: servita.
- **Aperto:** connettori da Matteo, RNS passi 3-5 col manager, pagina Servizio, fetta 75/25, gruppi P2C. `GLOSSARIO_VIVO.md` non trovato: tabella in chat.
- **Hai detto → Da PO si dice:** «i test che sono da fare sull'app» → «il collaudo di accettazione»; «girare su prod per valutare effetti dei fix» → «verifica post-rilascio in produzione».
