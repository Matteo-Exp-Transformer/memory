# Il ciclo progetta, brief, chiudi

> Sources: chat Claude desktop, 2026-10-22
> Raw: [2026-10-22-stato-chiudi-controlli](../../raw/sessioni/2026-10-22-stato-chiudi-controlli.md); [2026-10-22-skill-progetta](../../raw/sessioni/2026-10-22-skill-progetta.md)
> Updated: 2026-10-22

## Overview

Il 22/10/2026 sono state costruite due chat di seguito: la prima per «chiudi» (stato del lavoro e controlli automatici), la seconda per la skill `progetta`. Insieme formano il ciclo con cui Matteo vuole lavorare: ragiona con un agente e compila la scheda (`progetta`), l'esecutore riceve un brief, a fine chat «chiudi» riscrive lo stato. Cosa fanno gli script sta nella repo; qui stanno le richieste di Matteo, le scelte e le lezioni. Il ciclo non è ancora stato usato su un lavoro vero.

## Cosa ha chiesto Matteo

Chat «chiudi»:

- «Formato STATO.md per progetto, al massimo 40 righe, riscritto da capo a fine chat»; comando «chiudi».
- «Script di controllo (lunghezza, data, link) che parte da solo prima di ogni salvataggio».
- «Usa Sonnet per l'esecuzione, Opus solo per decisioni difficili».

Chat `progetta` («Chat 2: la skill progetta nella repo memory»): quattro regole (mancanze classificate, ricerche con fonti A, M o B, incognite con lo sblocco, soluzioni con stima). Condizione di chiusura: «Finito quando: la skill funziona sia in Claude sia in Codex, e lo script fallisce su tre schede sbagliate preparate apposta (un campo R2 mancante, un livello assente, un finito senza comando) e passa su una giusta».

## Decisioni

Di Matteo:

- «Sì, aggiungi cleanupPeriodDays: 1095 in ~/.claude/settings.json».
- «in AGENTS.md e in ogni script o controllo scrivi il comando come `python` (su questo PC python3 non funziona)»; per il cloud Linux «uno script che provi prima `python` e poi `python3`».
- «Decide Opus, esegue Sonnet»; «Ottimo fai chiusura».

Prese da Claude, non da Matteo: lo `STATO.md` vive nella repo del progetto, non in `memory`; una scheda per lavoro in `schede/` della repo del progetto; il brief solo in chat, non salvato; una mancanza `[blocca]` fa fallire il controllo.

## Cosa ha funzionato

- Decisioni prese prima e passate a Sonnet in un solo brief: file e prove in un giro.
- Prove con casi che devono fallire (41 righe, data futura, link rotto, modifica a `raw/`; per le schede, ogni scheda sbagliata dà un solo errore).
- L'hook provato su una repo nuova: 3 commit bloccati, 1 passato.
- Codex ha trovato la skill dal rimando e ha lanciato il controllo.

## Cosa no

- Il clone locale era indietro rispetto alla remota: serve `git pull` a inizio sessione.
- Su questo PC `python3` è l'alias vuoto del Microsoft Store.
- In `codex exec --sandbox read-only` la shell PowerShell non parte («helper_unknown_error: setup refresh had errors») e Codex ripiega su node_repl.
- L'hook ha scritto dentro il percorso assoluto di `memory`: se la repo si sposta, si reinstalla. Un commit bloccato mostra il percorso di una cartella temporanea.

## Aperto

- La skill `progetta` non è ancora stata usata su un lavoro vero; l'hook non è installato in nessuna repo di progetto, si installa alla prima scheda.
- Controlli e riga nel CLAUDE.md delle repo dei progetti: da fare quando Matteo apre un progetto.

Costi di queste chat in [Costi e quota](costi-e-quota.md).

## See Also

- [Criteri di progetto](criteri-di-progetto.md)
- [Lavorare con gli agenti](lavorare-con-agenti.md)
- [Costi e quota](costi-e-quota.md)
