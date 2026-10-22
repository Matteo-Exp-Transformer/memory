# Nota di fine chat — avvio della memoria e del metodo

> Source: sessione Claude cloud https://claude.ai/code/session_01Yb193umzKAMZ9SjmY4tvUk
> Collected: 2026-10-21
> Published: 2026-10-21

- **Dove:** Claude (sessione cloud collegata al PC), modello principale Opus 5.5, ricercatori Sonnet.
- **Obiettivo di Matteo:** «raccogliere il contesto minimo per capire come creare quello che mi serve»; costi eccessivi, contesto macchinoso, lavoro sul sistema invece che sul prodotto.
- **Decisioni di Matteo:** congelare l'MSS e partire dal contesto; soglia di definizione «dipende dal rischio ( valuto insieme ad agente )» con prototipi fino a un minimo accettabile; contesto in una LLM wiki; «Quasi tutto» l'abbonamento a ricerca e definizione per ora; spegne lui le attività pianificate dell'MSS; repo privata `memory`; si parte dalla wiki.
- **Risultato:** repo `memory` con 31 documenti di Io-Claude in raw/, 25 pagine wiki, skill karpathy-llm-wiki; ricerca iniziale in `raw/metodo-ia/`.
- **Ha funzionato:** domande a scelta prima di lanciare agenti; ricercatori Sonnet in parallelo con fonti e affidabilità; controllo automatico delle citazioni (0 errori).
- **Non ha funzionato / attenzione:** dal cloud non si crea una repo GitHub (la crea Matteo); il nome scelto è `memory`, non `memoria`; i documenti totali sono ~4,6 milioni di parole, troppi da caricare tutti.
- **Costo:** sotto-agenti Sonnet 131.237 + 169.660 + 156.602 + 152.151 token; chat principale non letta.
- **Aperto (dipende da fatti non disponibili):** spegnimento delle attività MSS (lo fa Matteo); quanto pesano davvero le attività pianificate sulla quota (non misurato).
