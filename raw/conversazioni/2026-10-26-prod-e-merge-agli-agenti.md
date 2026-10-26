# CalendarBackup-v2: agenti su PROD, merge delle PR agli agenti, Matteo solo reasoning

> Source: chat Claude desktop (Code), Opus, 26/10/2026, repo memory; messaggio di Matteo con la richiesta di «chiudi»
> Collected: 2026-10-26
> Published: 2026-10-26

Seguito di [2026-10-26-flusso-reasoning-manager-e-codex](2026-10-26-flusso-reasoning-manager-e-codex.md).

Messaggio di Matteo, alla lettera:

«Fai chiusura sessione ma annota che : agenti possono lavorare anche su prod. Hanno mio ok e io ho ok del bar. Quindi cancelliamo pure dati clienti quando sarà necessario permettiamo ad agenti di toccare prod per ora ( tanto abbiamo tag congelati. ) i merge delle PR preferisco li facciano agenti. Io vorrei fare solo chat reasoning con agente, e le azioni che non possono fare loro. 
Avvio chat codex quando è tutto aggiornato e chiuso. Dimmi quando lo posso avviare e con che cartelle di contesto. Il prompt uso quello che mi hai dato ( lo avvio da desktop app openai, con cartelle linkare )»

Claude ne ha ricavato: l'OK del ristorante alla cancellazione non è più aperto; il criterio 17 (collaudo a mano di Matteo su PROD) non si applica per ora; i merge in `env/test` e in `main` li fa il manager; i tag congelati salvano il codice, non i dati del DB, quindi prima di ogni modifica al DB di PROD l'agente salva lo schema e i conteggi aggregati.
