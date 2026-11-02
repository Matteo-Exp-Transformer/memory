# Sessione — G1, cancelli e perimetro dei test
Data: 2026-10-29
Dove: Codex desktop, GPT-6, chat manuale; nessun sotto-agente.
Obiettivo di Matteo: «Esegui questo prompt : richieste/2026-10-29-prompt-g1-codex.md».
Decisioni nuove di Matteo: nessuna; domanda sulla deroga alle sole fixture ancora senza risposta.
Esito: branch codex/g1-cancelli-29-10, commit b78da39 pushato; PR non aperta, consegna incompleta.
Prove: 9/9 casi nuovi verdi, 4 mutazioni rilevate; validate 1363/1363 e controllo contesto verdi.
Limite: il blocco dei file PR illeggibili rende rosse 32 prove storiche senza campo files; solo le fixture aggiornate in copia temporanea danno 110/110.
Imparato: un perimetro che consente di cambiare un contratto ma vieta le sue fixture può impedire una consegna verde; rendere esplicita questa dipendenza nel brief.
Quota account prima 72%/36%, dopo 77%/37% (5 ore/settimana); differenze condivise, non costo esclusivo.
- **Costo:** snapshot 2017184 token, input 2007078 (cache 1927936), output 10106; nessun sotto-agente. Snapshot precedente alla chiusura.
- **Letti:** serviti: progetto AGENTS.md, STATO.md, team/costruttore.md, voce G1/G2 di LAVORI.md, richieste/2026-10-29-prompt-g1-codex.md; schede/2026-10-29-macchina-regole-e-cancelli.md e schede/2026-10-29-audit-macchine-esito.md.
Letti, serviti: scripts/catena/merge.mjs, soglie.mjs, verifica-catena.mjs, parte di verifica-chiusura.mjs; nuovi voce.mjs e verifica-cancelli.mjs; log locali di test e validate.
Letti Memory, serviti: AGENTS.md e .claude/skills/chiudi/SKILL.md; wiki/index.md non servito (nessun approfondimento necessario).
Aperto: autorizzazione delle sole fixture in verifica-catena.mjs, verifica-audit.mjs e verifica-chiusura.mjs; STATO.md intoccabile per mandato esplicito.
Sessione: 01a18724-6d49-7391-8706-e44df2982906, cartella iniziale CalendarBackup-v2; worktree C:/Users/matte.MIO/.codex/worktrees/g1-cancelli-29-10/CalendarBackup-v2.
