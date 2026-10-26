# Nota di fine chat — disegno del team di CalendarBackup-v2 e lavoro 0 affidato a Codex

> Source: sessione Claude desktop (Code) 3fb5083c-5e91-4058-ad74-ebaefb173602, cartella memory
> Collected: 2026-10-26
> Published: 2026-10-26

- **Dove:** Claude desktop (Code), Opus 5.5; nessun sotto-agente.
- **Obiettivo di Matteo:** «Agisci come senior e aiutami a pianificare al meglio il sistema <<progetta>>»; un metodo per le novità IA «anche da Instagram e social, a basso costo»; un sistema «che si migliora e revisiona monitorando il suo costo»; poi «fai in modo che se avvio codex nella repo lui sappia cosa iniziare a fare».
- **Decisioni di Matteo:** «Per il resto tutto come hai definito va bene»; l'esecutore «parte dopo che io in chat di reasoning con agente ho creato il lavoro da fare»; «qualche token in meno a disposizione degli esecutori e qualcuno in più a favore del reasoning e la revisione»; «Anticipo lavori di Claude su codex che ho token»; «agenti possono lavorare anche su prod. Hanno mio ok e io ho ok del bar»; «i merge delle PR preferisco li facciano agenti». Parole complete: `raw/conversazioni/2026-10-26-flusso-reasoning-manager-e-codex.md` e `raw/conversazioni/2026-10-26-prod-e-merge-agli-agenti.md`.
- **Risultato:** `CalendarBackup-v2/schede/2026-10-26-contesto-attivo.md` (0 errori; flusso, divisione 32/13/10/8/7, ricercatore, riordino, registro, brief per Codex con merge al passo 9), ingresso in cima a `CalendarBackup-v2/AGENTS.md`, `CalendarBackup-v2/STATO.md`, `strumenti/notebooklm-fonti-ricercatore.md`.
- **Ha funzionato:** leggere solo le tre fonti indicate da Matteo più `wiki/metodo/costi-e-quota.md` è bastato per il disegno; il numero dei 585.723 token dei ricercatori ha portato alla regola «prima lo script, il modello solo alla fine».
- **Non ha funzionato / attenzione:** il primo disegno non metteva Matteo e la chat di reasoning a monte del manager: lo ha corretto lui; il pre-commit MSS di `.husky` chiede di rilanciare lo stesso commit; i tag congelati salvano il codice, non i dati del DB di PROD.
- **Costo:** chat principale 5.229.198 token (cache letta 4.957.017, cache scritta 215.726, output 56.389); nessun sotto-agente.
- **Letti:** `raw/conversazioni/2026-10-26-team-ricercatore-e-riordino.md` (servito); scheda contesto-attivo, tutta (servito); `wiki/metodo/criteri-di-progetto.md` (servito); `wiki/metodo/costi-e-quota.md` (servito: 18.000 token per punto, fonti da seguire); `wiki/index.md` (non servito); `CalendarBackup-v2/STATO.md` e `AGENTS.md` (servito); skill progetta e chiudi (servito); `strumenti/controlla.py`, prime 40 righe, e `.githooks/pre-commit` (non servito); `raw/sessioni/2026-10-26-lavoro-0-progetto.md` (servito, formato); `codex --help` (servito: `--add-dir`).
- **Aperto:** lettura della quota in cloud (lavoro 1); certificabilità (professionista).
