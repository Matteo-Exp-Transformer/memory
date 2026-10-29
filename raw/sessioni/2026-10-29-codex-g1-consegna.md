# Sessione — G1, deroga alle fixture e consegna
Data: 2026-10-29
Dove: Codex desktop, GPT-6, chat manuale; nessun sotto-agente.
Obiettivo di Matteo: proseguire «Esegui questo prompt : richieste/2026-10-29-prompt-g1-codex.md».
Decisione di Matteo: «Sì, aggiorna le sole fixture»; domanda esplicita sui dati finti di gh senza files, con asserzioni invariate.
Risultato: PR https://github.com/Matteo-Exp-Transformer/CALENDARIO-V2/pull/61, branch codex/g1-cancelli-29-10, SHA b051580d5879f6dca3ec759a266a124a0ec6f70f; nessun merge.
Prove: 110/110 test catena, validate 1363/1363, contesto e diff check verdi; quattro mutazioni rilevate nel primo segmento della stessa chat e ripristinate.
Check alla scrittura: Vercel e Preview Comments SUCCESS, ci IN_PROGRESS; nessun e2e richiesto dal diff scripts/catena/.
Imparato: la deroga precisa sulle fixture risolve la dipendenza del contratto senza allargare l'implementazione o cambiare le asserzioni storiche.
Ha funzionato: prova preventiva in copia temporanea, poi applicazione limitata alle fixture dopo risposta esplicita; nessuna richiesta duplicata di autorizzazione.
Vincolo: STATO.md resta intoccabile per prompt G1; chiusura in Memory su branch proprio, senza modificare lo staging della cartella condivisa.
Quota account: ingresso chat 72%/36%, ripresa 78%/37%, snapshot chiusura 80%/37% (5 ore/settimana), uso condiviso, avvio manuale senza soglie.
- **Costo:** snapshot 3413917 token, input 3399789 (cache 3308416), output 14128; nessun sotto-agente; stesso totale cumulativo della chat, non sommare alla nota precedente.
- **Letti:** serviti STATO.md e AGENTS.md del progetto, fixture in scripts/catena/verifica-catena.mjs, verifica-audit.mjs e verifica-chiusura.mjs, patch temporanea, log catena/validate e check PR; Memory .claude/skills/chiudi/SKILL.md e AGENTS.md già letti nel segmento precedente. Nessuna rilettura dell'archivio.
Aperto: esito finale ci sulla PR #61, poi valutazione e merge del manager.
Sessione: 01a18724-6d49-7391-8706-e44df2982906, iniziata in CalendarBackup-v2 e proseguita nel worktree g1-cancelli-29-10.