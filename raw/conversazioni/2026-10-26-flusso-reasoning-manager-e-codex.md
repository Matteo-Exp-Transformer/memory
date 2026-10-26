# Team di CalendarBackup-v2: disegno del sistema, flusso reasoning → manager, lavoro 0 a Codex

> Source: chat Claude desktop (Code), Opus, 26/10/2026, repo memory; tre messaggi di Matteo
> Collected: 2026-10-26
> Published: 2026-10-26

Seguito di [2026-10-26-team-ricercatore-e-riordino](2026-10-26-team-ricercatore-e-riordino.md).

Primo messaggio (incollato, con il testo preparato per l'agente del lavoro 1), le frasi di Matteo alla lettera:

«Agisci come senior e aiutami a pianificare al meglio il sistema <<progetta>> : Nel sistema avremo : ricerca  - reasoning e Plan - costruzione- revisione - git - decisioni manager app in sviluppo - manutenzioni programmate - raccolta dati quando app in produzione - riordino repository  di lavori attivi nei progetti e Memory ( se necessario e fa risparmiare se no script , materiale da capire) . 
 Ricerche anche per news IA : ci serve un  metodo per scovare novità IA (repo, tool, workflow) anche da Instagram e social, a basso costo.»

«Poi dimmi come immagini tu un sistema adeguato autonomo e che si migliora e revisiona monitorando il suo costo e progettando le esecuzioni di conseguenza ( e misurando dove avvengono costi maggiori e problemi, e raccoglie dati per ricercatore che analizza online come migliorare i parametri del sistema che lavora.»

Claude ha proposto: prima lo script, il modello solo alla fine; ricercatore con `DOMANDE.md` (priorità P1-P3, stati `[aperta]`, `[veglia]` risvegliata da un evento, `[proposta]` confermata dal manager, `[chiusa]`), filtri di licenza, manutenzione e sicurezza fatti da script, giornale di circa 40 righe, «niente di nuovo» valido; riordino come passo del manager con `scripts/controlla-contesto.mjs`, ruolo a sé solo se il manager sfora la sua parte di quota; novità dai social nella repo memory: feed a zero token, segnalazioni di Matteo dal telefono come issue GitHub con etichetta `segnalazione`, nessuno strumento a pagamento; registro `team/registro.jsonl` a ogni «chiudi», cruscotto settimanale, un parametro cambiato alla settimana in `team/parametri.md`, guardrail che il sistema non cambia da solo (70%, 60%, soldi, produzione, push, script di misura); divisione del 70%: costruttori 40%, manager e revisioni 15%, ricercatore 8%, riordino e manutenzioni 7%.

Secondo messaggio, alla lettera:

«Carico file in chat lavorato da NotebookLM ad hoc. Dammi un file .MD che spiega a notebook cosa voglio che faccia con le immagini che gli passo . ( Fonti per ricercatore ) E mi crea un file .MD che do in chat ad agente senior. L'unica cosa che non hai considerato nel flusso di lavoro che hai definito è che esecutore parte dopo che io in chat di reasoning con agente ho creato il lavoro da fare, da mandare ad agente manager che dirige poi il team di sviluppo con sotto agente senior e tutto. Partirei con qualche token in meno a disposizione degli esecutori e qualcuno in più a favore del reasoning e la revisione. E dimmi quando il setup sarà pronto, per cui da lì io farò una chat di avvio dei lavori dopo essermi confrontato con modello senior customer service. 
Quindi aggiungi il mio agente allo schema ( creo il lavoro da fare ) , e agente pianifica. Poi apro agente manager nella repo di lavoro e lui è manager del team di agenti. 
Tutto chiaro? Se è tutto chiaro aggiorna la documentazione e fai in modo che se avvio codex nella repo lui sappia cosa iniziare a fare. Anticipo lavori di Claude su codex che ho token. Lascia ingresso per agente chiaro per permettergli di lavorare. Poi dammi prompt e dimmi se basta cartella calendarbackup per avviare chat lavori codex.»

Terzo messaggio, alla lettera:

«Per il resto tutto come hai definito va bene»

Claude ne ha ricavato: nuova divisione del 70% (costruttori 32%, reasoning e plan 13%, revisioni 10%, ricercatore 8%, riordino e manutenzioni 7%); lavoro 0 eseguito da Codex invece che da Opus; ingresso per Codex in cima ad `AGENTS.md` di CalendarBackup-v2.
