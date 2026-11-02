# 2026-11-02 — Rilascio RNS in PROD, PrenotaZen

- **Dove:** Claude desktop (Code), manager Opus 5.5 avviato a mano da Matteo. Tipo per E1: manager.
- **Obiettivo di Matteo:** passi 3-5 di RNS, con «Hai il mio ok per prod e rns.» e «autorizzo agenti a girare su prod per valutare effetti dei fix se serve.»
- **Decisioni di Matteo:** sul connettore, «se proprio nom funziona usiamo quello dell app fisso». Per il prossimo manager: deve dire «se abbiamo ulteriori dati per valutare come si sta comportando il sistema a livello di costo ed efficienza».
- **Risultato:** CalendarBackup-v2 `rapporti/rilascio-rns-2026-11-02/RAPPORTO.md`. 067 e 071 su PROD, `create-booking` v23, #70 unita in main (053290c), tag su fc4d648; #124 e #125 in env/test.
- **Ha funzionato:** il controllo incrociato dei connettori ha fermato la chat prima di scrivere. Misurare su PROD la convenzione dell'ora (50 righe, scarto 0) ha chiuso il rischio principale della 071 prima di applicarla. Il sorgente salvato e il confronto byte per byte col ramo si possono ricavare dal transcript, senza riscrivere nulla a mano.
- **Imparato:** il connettore dell'app con `project_ref` ha strumenti senza `project_id`: non può sbagliare progetto. Il nome di un connettore non dice l'ambiente. Sul Pranzo di da-tommaso la 071 ha corretto un errore reale, da 0 a 8 orari.
- **Non ha funzionato:** la #124 aveva `ci` rosso, Vitest raccoglieva `e2e-collaudo/`; i salvataggi `.ts` in `rapporti/` hanno fatto rossa la #125, ora sono `.txt`. La prima risposta si è fermata solo perché il controllo chiesto non tornava: Matteo l'ha sbloccata in chat.
- **Quota:** Claude settimana 74% → 76%, 5 ore azzerata durante la chat; Codex non letta, `no_valid_record`. Punti previsti 3, reali 2.
- **Costo:** chat principale 334.297 token non in cache su 9,3 M totali, stima 2,1 punti con 156 mila per punto; riga `costo-chat` in team/registro.jsonl. Nessun sotto-agente. Primo turno 98 mila; soglia 247 mila superata alla fine, per le due letture e la pubblicazione della funzione.
- **Letti:** AGENTS, manager, scheda RNS, rapporto CR1, memoria connettori, migrazioni, codice di AdminAuthContext: serviti. Voce RNS in LAVORI: servita. Skill chiudi: servita.
- **Aperto:** giudizio di Matteo su login e aspetto; gestionale dopo il login su PROD non provato; «Configura la pagina Prenota» nel form; connettore TEST da riprovare in chat nuova; Codex non misurato.
- **Hai detto → Da PO si dice:** tabella in `docs/_lavoro/Per matteo/GLOSSARIO_VIVO.md`, seduta del 02-11-26.
