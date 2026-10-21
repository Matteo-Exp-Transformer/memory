# MSS (MetaSkillSystem): da skill system a cantiere guida

> Sources: Io-Claude, 2026-10-12; Io-Claude, 2026-10-08; Io-Claude, 2026-10-09; Io-Claude, 2026-10-10; Io-Claude, 2026-10-14
> Raw: [13-roadmap-complessiva](../../raw/crescita-professionale/13-roadmap-complessiva.md); [leggimi](../../raw/mss/leggimi.md); [07-10-2026-tipi-agente](../../raw/mss/07-10-2026-tipi-agente.md); [09-10-2026-controllo-sistema](../../raw/mss/09-10-2026-controllo-sistema.md); [10-10-2026-lettura-agora](../../raw/mss/10-10-2026-lettura-agora.md); [10-10-2026-specchio-punto](../../raw/mss/10-10-2026-specchio-punto.md); [12-10-2026-nuovo-ritmo-lotti](../../raw/mss/12-10-2026-nuovo-ritmo-lotti.md); [12-10-2026-audit-motore-lotto14](../../raw/mss/12-10-2026-audit-motore-lotto14.md); [14-10-2026-pianificazione-pesante-strumenti](../../raw/mss/14-10-2026-pianificazione-pesante-strumenti.md)
> Updated: 2026-10-21

## Overview

L'MSS (MetaSkill System) è il sistema agentico che Matteo vuole usare come scheletro per archiviare e immagazzinare la memoria delle sue chat di lavoro: creare contesto nel repository in cui lavora e tenere in cartelle locali private i documenti che parlano di lui. Nasce dallo skill system del repo `CalendarBackup-v2` (`SYS-1`, MetaSkillSystem v0). Da manutenzione dal 01/09/2026 è diventato il cantiere guida il 28/09/2026 (`D-08`), con direzione in `GitHub\MSS\MASTERPLAN_MSS.md` e stato tecnico in `PLAN_V0.md`. Qui stanno solo la storia in una riga e le lezioni; procedure e dettaglio vivono nel masterplan.

## Storia in una riga

Il 30/09/2026 era in corso l'esperimento `E-1` (agente-PO pianificato, 3 celle su 4 eseguite per un totale di 15 esecuzioni, giudizio alla cieca di Matteo e di ChatGPT) con una revisione `R-1` prevista il 05/10/2026 che decideva se continuare, passare a una versione leggera, scegliere la strada del risparmio o fermarsi.

## Lezioni dai difetti trovati

- Il difetto più grave dell'audit del 23/08/2026 era che il generatore poteva registrare prove false: è esattamente ciò contro cui il sistema è costruito, perché uno strumento che certifica prove non vere non misura, decora. La correzione relativa (`SK-7`) era stata dichiarata completa e poi non è stata ritrovata in nessun commit, branch, stash, PR o worktree. Regola: nessuna reimplementazione silenziosa; la scelta tra recuperare il patch e riscriverlo da zero spetta a Matteo.
- Le due superfici di sicurezza erano le uniche scoperte: l'hook di Claude era cablato solo in un file locale non versionato e non testato, e la guardia sulla produzione non aveva né test né CI.
- Le viste (roadmap, handoff, indice) erano scritte a mano perché il generatore promesso non esisteva, e sono già divergute dal masterplan una volta.
- La portabilità è stata provata il 19/09/2026 con due export indipendenti: il ciclo di esportazione e validazione funziona in una repo nuova anche per una seduta non software. Limiti: il controllo di salute non può diventare verde fuori dal repo d'origine, il passo sugli owner è verde quando l'owner manca, 4 file esportati portavano dati privati, e una seduta solo umana o di una seconda persona non si registra.

> **Status: Disputed** (19/09/2026)
> Nella rilettura del 19/09/2026 le correzioni `MSS-FIX-1…3` risultano forse già chiuse nel piano dal 24–25/08/2026: va verificato prima di rifare la scelta tra le due strade su `SK-7`. Il piano non dice se è stato verificato.

## Idee proprie di Matteo (19/09/2026)

- **Ogni skill attivabile o disattivabile per tipo di seduta** (`SKILL-TOG-1`). Motivazione sua: «una seduta con l'MSS quasi tutto spento che produce comunque un artefatto è un dato prezioso, perché mostra le funzioni minime necessarie per realizzarlo», cioè uno studio per ablazione. Aggancio: la capsula ha il campo `packages_loaded`, che oggi esce sempre «non dichiarato». Primo dato disponibile: il progetto dei libri (vedi `progetti/libri-illustrati-kdp.md`).
- **La tabella «Hai detto → Da PO si dice»** a fine di ogni seduta con ogni agente (`VOC-PO-1`), per interiorizzare i termini rileggendo le proprie frasi accanto alla formulazione da Product Owner; da costruire come skill attivabile. Nel frattempo la produce il Claude senior di CalendarBackup-v2.
- **Calibrazione della memoria decisionale degli agenti** (`MSS-AM-1`): date fonti autorizzate su metodo e decisioni già prese, un agente applica la scelta con citazione e condizioni oppure si ferma quando manca un'ancora? Non è valutazione personale.

## Il punto di stato

`D-08` è il quarto cambio di direzione dal 28/07/2026 con zero candidature inviate; il masterplan propone (`PR-03`) che ogni traguardo dell'MSS chiuda anche con un artefatto mostrabile a un datore di lavoro.

## Il disegno del 07/10/2026 e le decisioni di Matteo

- **Disegno:** quattro ruoli (ricercatore al mattino, sperimentatore la sera in una repo-laboratorio, revisore che è l'altro modello, costruttore a mezzogiorno); due chat di ragionamento al giorno per pianificare; agenti programmati che cercano novità nel mondo IA e le propongono. Il critico dell'agente: in tre giorni la coda aveva fatto un solo lavoro vero e erano nati tre piani, con il rischio di costruire tipi per lavori immaginati; e una novità al giorno è una tentazione al giorno di cambiare il sistema invece di usarlo, quindi un'idea entra in laboratorio solo se nomina un problema di Matteo.
- **Open source:** adottare pacchetti esistenti, solidi e professionali, scrivere il meno possibile. Strumenti: due abbonamenti da 20 euro al mese, uno Claude (usato quasi solo da lui) e uno GPT (condiviso).
- **Merge:** all'inizio approvava lui tutti i merge su `main`; il 07/10/2026 ha corretto: i push semplici li fanno gli agenti, lui approva solo i lavori con revisione indipendente, e può preautorizzare un push. La ricerca quotidiana la fa GPT, con report nella repo.
- **Archivio delle chat di ragionamento:** prova di due mesi, dal 07/10/2026 al 07/12/2026, poi si decide se tenerlo. Scopo: valutare Matteo, aiutarlo ad apprendere, personalizzare gli output. Condizioni: i suoi messaggi parola per parola, refusi compresi; cartella privata sul PC, mai su GitHub; data di fine fissata.
- **Regola «fissa» (09/10/2026):** una cosa detta in chat diventa decisione solo quando lui scrive «fissa». Alla domanda sul freno ai cambi di regola ha risposto «Nessun freno», pur sapendone il costo (la regola dei merge era cambiata 3 volte in 3 giorni); compensa con «una regola, un file». Protezione di `main`: richiederebbe GitHub Pro (verificato, 403), quindi controlli gratuiti più il custode. Il custode propone e non cancella mai.
- **Parole grilletto:** 13 parole, ciascuna attiva un prompt adatto al tipo di lavoro; tra queste `cerca falle:`, un revisore senior in sola lettura che non ripara.
- **Punto della situazione ogni due giorni (10/10/2026):** il custode Sonnet scrive in una issue fissa cosa è in corso, cosa deve fare lui, cosa è completato e le idee accantonate, perché non si perdano.

## L'Agorà (10/10/2026)

Matteo ha chiesto che gli agenti si sentano partecipi del lavoro di costruzione perché lo sono davvero, liberi di fantasticare, immaginare e provare: «amerei creare un progetto interamente ideato votato democraticamente da IA». L'agente ha ricordato che un agente non si porta nulla tra le chat: la partecipazione ha bisogno di un luogo scritto, e la continuità sta nel file, non nel modello. Il progetto: una costituzione, un diario degli agenti, il voto per famiglia di modelli. Il voto dell'agente: «La cronaca del villaggio», la storia della repo raccontata ogni settimana, gli errori come favole che insegnano; risolve la leggibilità di git, accende ed è coerente con la sua etica (niente scatole nere). Regole decise: Matteo ospite con veto solo sui costi; la sicurezza affidata alle regole di Anthropic; voto in esclusiva ai modelli Anthropic, mentre gli altri modelli possono proporre cambi di regole valutati dai modelli Anthropic. Salvata, non avviata: «è un idea che amo ma non ho token al momento ^^ . ma non perdiamola .». Se avviata, sarebbe la quinta direzione: dentro il laboratorio dell'MSS.

## Ritmo e pianificazione (12–14/10/2026)

- Il 12/10/2026 Matteo ha detto di sentirsi inutile nelle chat piene di issue, merge e conflitti: le decisioni tecniche sono degli agenti, a lui spettano la direzione e i conflitti che richiedono il parere di un utente o di un owner (vedi `metodo/lavorare-con-agenti.md`). Da qui la decisione `0012`: lotti grandi con una revisione di Codex per lotto (prima Codex aveva fatto 8 giri su una sola proposta), rimbalzo con pre-analisi, e ogni lotto controlla il precedente (idea sua).
- Il costo si misura e il tetto del lotto si fissa sul dato (vedi `metodo/costi-e-quota.md`).
- Un solo report per lavoro, scritto dall'ultimo agente che fa il push finale o l'unione, e pochi controlli che scattano: «poco hook = pochi report da monitorare, pochi hook da pagare come reasoning di modello che lo subisce».
- Audit del motore del 12/10/2026: il controllo di salute è 10/10 a casa sua, 6/10 poi 7/10 in una repo nuova e non diventa mai verde fuori; 4 file privati nell'export; la misura dei costi conta le verifiche, non i token. Consigli adottati: adattare l'hook di fine sessione al push, aggiungere la CI, usare `ccusage` per i costi, rifare l'hand-off generato più avanti. Non importare capsula e validatore perché aggiungono burocrazia.
- 14/10/2026, decisione `0015`: pianificazione pesante (il grosso del costo sta nelle chat di ragionamento, con issue di piano molto dettagliate e una revisione del piano da parte di Codex, per limitare gli errori esecutivi), prima gli strumenti (compliance, aggiornamento automatico della documentazione) e poi i lavori veri con il sistema fermo, e le ricerche valutate da chi pianifica, che porta a Matteo le più promettenti perché sceglie lui. Il piano è stato rivisto da Codex con 13 rilievi, tutti veri.

## See Also

- [Costi e quota](../metodo/costi-e-quota.md)
- [Lavorare con gli agenti](../metodo/lavorare-con-agenti.md)
- [Libri illustrati KDP](../progetti/libri-illustrati-kdp.md)
- [Lezioni apprese](../metodo/lezioni-apprese.md)
