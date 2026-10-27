# Studio dei miglioramenti del pilota — 2026-10-27
Dove: Codex desktop, GPT-6; avvio manuale, worktree propri per progetto e nota, senza altri agenti.
Obiettivo di Matteo: «Non fare il Plan»; «Segui questo prompt solo per cercare ulteriori miglioramenti all'idea».
Decisione conservata: «Proviamo la 1, ma teniamo le altre possibilità da valutare. Poi capiremo modo migliore usandolo.»
Mandato: «il team si studierà attivamente tramite agente manager per capire questo genere di decisioni da migliorare prendere o proporre».
Risultato: aggiornate scheda pilota, valutazione critica e STATO in CalendarBackup-v2; controlla_scheda 0 errori, contesto OK, validate:docs 0 path rotti; commit 1d215e9 sul branch studio/pilota-misure-2026-10-27, da acquisire nella PR 18 dal manager.
Funzionato: distinguere quota condivisa da costo attribuibile, registrare anche stop e dati mancanti; una sola prova offline quota-assente, uscita 2 senza modelli.
Corretto: cache scritta e singola scrittura negata non provano convenienza o isolamento; sette appuntamenti senza consegna chiudono con «non concluso».
Uso: Matteo deve poter distinguere consegna, quota insufficiente e PC assente dal rapporto; nessuna nuova scelta richiesta ora.
- **Costo:** costo_sessione.py codex dalla cartella iniziale: 1.025.901 token, input 1.015.103 (cache 930.176), output 10.798; rilevazione prima della chiusura amministrativa, nessun sotto-agente.
Quota Codex intero conto: prima 18:57:13Z cinque ore 53%, settimana 19%; dopo 19:01:16Z 56% e 20%, reset futuri; timestamp più recente, non mtime. Delta non attribuibile alla sola chat, uso parallelo possibile. Claude non usato né sondato: quota non misurata.
- **Letti:** servito: AGENTS fornito, STATO iniziale e aggiornato; team/senior-sistema-agenti.md, costruttore.md, manager.md, revisore.md; LAVORI.md: mandato, letture e limiti.
- **Letti:** servito: richieste/2026-10-27-autonomia-tecnica-e-ciclo-agenti.md; schede del 27/10 sistema-agenti-allineamento-decisioni-e-prove, sistema-agenti-autonomia-tecnica, sistema-agenti-premortem-e-costi, sistema-agenti-valutazione-critica, pilota-catena-agenti: confronto critico e modifiche.
- **Letti:** servito: esperimenti/catena-minima/catena.mjs, .github/workflows/ci.yml, package.json, scripts/controlla-contesto.mjs, .husky/pre-commit: limiti della prova e verifiche documentali; nessuna modifica all’app.
- **Letti:** servito in memory: AGENTS.md, wiki/index.md, wiki/metodo/criteri-di-progetto.md, .claude/skills/progetta/SKILL.md, .claude/skills/chiudi/SKILL.md, strumenti/costo_sessione.py (parziale), strumenti/controlla_scheda.py (parziale): scheda, costo e chiusura. Letti anche .githooks/pre-commit, strumenti/controlli.sh e funzione gia_in_git di controlla.py: serviti a distinguere controllo manuale e hook; causa non risolta nel mandato.
Aperto: autenticazione programmata, git/sandbox e cache lunga aspettano A/B; confronto delle opzioni 2/3 richiede dati attribuibili. Conferma e revisioni del manager restano da fare; nessuna automazione avviata.
Pubblicazione: progetto pushato (1d215e9); nota locale nel worktree memory-studio-pilota, commit/push bloccati dall’hook su sei errori di note storiche. Controlli manuali verdi; nessun bypass e nessuna nota storica modificata.
Sessione: 01a17eb8-8ef9-7c12-b93e-a697a1c2565c; workspace iniziale CalendarBackup-v2.
