# 2026-11-02 — Revisione-cancello chiusa, PrenotaZen
Chat manager avviata a mano da Matteo. Tipo per E1: manager. Punti Claude previsti 5 più i fix, reali 4 (settimana 66% → 70%, 5 ore 1% → 26%). Codex settimana 64% → 68%.

Imparato:
- Un rilievo va riprovato con un comando, non solo riletto: la prova ha allargato il P1 della guardia PROD; il connettore `supabase` raggiunge PROD e la guardia non scattava sul nome vero.
- Una memoria di 3 mesi su ambienti e connettori era falsa: `get_project_url` costa nulla e la smentisce.
- Il cancello bloccava i propri fix: una corsa ferma per 38 mila token prima di scrivere la riga in chiaro.
- Un'ipotesi mia sul conteggio di `message.id` è caduta alla misura su transcript veri.
- `costo-sessione --ultima` prende la sonda di quota appena lanciata, non la chat: serve `--file`.
- Una voce non deve chiedere a un costruttore ciò che il suo sandbox non può fare: SRC1 ha speso 3 rimandi su una mutazione impossibile.
- La prima corsa su `src/` ha prodotto codice buono al primo giro: il costo è venuto dalla prova richiesta, non dal lavoro.
- **Costo:** chat principale 538.073 token non in cache su 31,1 M totali, stima 3,4 punti con 156 mila per punto, reali 4; riga `costo-chat` in team/registro.jsonl. Righe aggiunte il 2/11 da un'altra chat, per Matteo: «Non voglio lasciare errori».
- **Letti:** non registrati da questa chat. Ingresso dal prompt: AGENTS, STATO, manager, revisore, servizio-clienti, elenco e revisione Codex del cancello; servito o no non noto.
