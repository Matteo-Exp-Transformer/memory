# Definire un progetto e tenere la memoria: letture del 21/10/2026

> Sources: Io-Claude, 2026-10-21; chat Claude cloud, 2026-10-21
> Raw: [2026-10-21-ricerca-iniziale](../../raw/metodo-ia/2026-10-21-ricerca-iniziale.md); [2026-10-21-avvio-memoria](../../raw/sessioni/2026-10-21-avvio-memoria.md)
> Updated: 2026-10-22

## Overview

Il 21/10/2026 tre ricercatori (Sonnet) e una sintesi della chat principale hanno raccolto materiale grezzo per questa wiki: come definire un progetto, come tenere memoria e contesto, quanto costano gli agenti. Affidabilità dichiarata dei punti: A fonte ufficiale o primaria, M README o blog di esperti, B casi singoli. Nulla è stato provato sul campo: sono letture, non prove. Qui stanno solo le conclusioni che toccano Matteo; i link sono nel raw.

## Il contesto misurato

- L'MSS ha prodotto 8 blocchi «Direzione nuova» nel file di passaggio tra il 12/10 e il 21/10, e due decisioni diverse numerate `0027`.
- Documenti di testo: MSS 358 file e 660k parole (senza worktree); CalendarBackup circa 2.300 file e 3,8M parole (840 report di sessione, 972 in Archives); `Io-Claude` 30 file e 76k parole. Totale circa 4,6M parole, circa 11 volte la scala della wiki di Karpathy.

## Come definire un progetto

- Gli strumenti «spec-driven» (Spec Kit, Kiro, BMAD, OpenSpec, Agent OS, Tessl) producono molta documentazione: BMAD vuol dire 12–16 h di piano prima del codice, e secondo Böckeler e Fowler Kiro trasforma un bug piccolo in 4 user story e 16 criteri. Il Thoughtworks Radar li tiene in «Assess». Rischio: rifare l'errore dell'MSS (troppa struttura prima dell'uso).
- Il nativo e gratuito basta: il plan mode di Claude Code con un'intervista che scrive `SPEC.md` e poi una sessione nuova; il plan mode di Codex con `PLANS.md`.
- Criteri pronti: ISO/IEC 25010:2023 (9 caratteristiche) e i quattro rischi di Cagan (valore, usabilità, fattibilità, sostenibilità). I criteri di Matteo hanno un nome tecnico: «parallelizzabile» è modularità e basso accoppiamento; «aggiungere senza cancellare» è il principio aperto/chiuso. Altri criteri utili con agenti: verificabilità (un controllo eseguibile), leggibilità in poco contesto, interfacce esplicite, fetta piccola, niente duplicati, recuperabilità, confini sempre/chiedi/mai, file di istruzioni corto, costo d'uso, reversibilità.
- Pre-mortem di Klein: 20–30 minuti con la domanda «è fallito, perché?».
- Contro l'overplanning: «spec-first è waterfall con battitura migliore; non puoi specificare un ignoto» (Butler). E sul prototipo: «il prototipo è il tuo documento dei requisiti, non la prima versione» (McGuinness): si tiene ciò che ha validato (regole, casi limite, flusso), il codice si butta.
- Non esiste un modello pronto per «a tre livelli di rischio»: è una costruzione di Matteo.

## Memoria e contesto

- Il gist di Karpathy (aprile 2026): `raw/` immutabile, `wiki/` scritta dall'LLM, un file di regole, operazioni di ingest, query e lint, `index.md` e `log.md`; regge circa 100 fonti. Esistono implementazioni (una skill MIT, server MCP, hook automatici con rischio di note vecchie).
- Anthropic: nel context engineering conta «il più piccolo insieme di token ad alto segnale»; riferimenti leggeri e caricamento a richiesta; i sotto-agenti restituiscono 1–2k token. In Claude Code `CLAUDE.md` sta sotto le 200 righe e gli `@import` non riducono il costo; meglio `CLAUDE.md` nelle sottocartelle e le skill. In Codex gli `AGENTS.md` si concatenano con un tetto di 32 KiB: «corto e preciso batte lungo e vago»; regole aggiunte solo dopo errori ripetuti.
- Uno studio ETH (arXiv 2602.11988) dice che i file di contesto spesso non aumentano il successo e alzano i costi oltre il 20%; quelli generati dall'LLM vanno peggio. Servono solo informazioni non deducibili.
- Rischio di deriva: i riassunti perdono dettagli e vengono riletti come fonti. Contromisure: raw immutabile, ogni pagina con data e fonte, ricostruzione dagli originali quando conta.
- Architettura proposta: un repo privato «memoria» con `raw/` e `wiki/`; un solo `AGENTS.md` (con `CLAUDE.md` che lo richiama); un puntatore cortissimo da ogni repo; skill in `.claude/skills/` e `.agents/skills/`; partire da 20–30 documenti; Matteo rivede il diff.

## Le scelte di Matteo all'avvio (21/10/2026)

Lo scopo, nelle sue parole: «raccogliere il contesto minimo per capire come creare quello che mi serve». Il disagio di partenza: costi eccessivi, contesto macchinoso, lavoro sul sistema invece che sul prodotto. Decisioni:

- Congelare l'MSS e partire dal contesto; le attività pianificate dell'MSS le spegne lui.
- Soglia di definizione di un progetto: «dipende dal rischio ( valuto insieme ad agente )», con prototipi fino a un minimo accettabile. Da qui i livelli di [Criteri di progetto](criteri-di-progetto.md).
- Contesto in una LLM wiki, in una repo privata chiamata `memory` (non `memoria`); si parte dalla wiki.
- Quota: «Quasi tutto» l'abbonamento a ricerca e definizione, per ora.

Cosa ha funzionato: domande a scelta prima di lanciare agenti; ricercatori Sonnet in parallelo, ognuno con fonti e affidabilità; controllo automatico delle citazioni (0 errori). Cosa no: dal cloud non si crea una repo GitHub, la crea Matteo; i documenti totali sono circa 4,6 milioni di parole, troppi da caricare tutti. Costo dei ricercatori in [Costi e quota](costi-e-quota.md). Aperto: quanto pesano davvero le attività pianificate sulla quota, non misurato.

## Non verificato

I moltiplicatori di quota tra Opus e Sonnet su Pro; se le attività pianificate pesano sulla stessa quota (probabile); gli hook bash su Windows; Codex da telefono che legge la repo; le licenze di Kiro, Tessl e Agent OS. Nessuno strumento è stato provato.

## See Also

- [Costi e quota](../metodo/costi-e-quota.md)
- [File, cartelle e contesto](../metodo/gestione-file-e-contesto.md)
- [MSS](../progetti/mss-metaskillsystem.md)
