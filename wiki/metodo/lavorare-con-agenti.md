# Lavorare con gli agenti: regole di Matteo

> Sources: Io-Claude, 2026-10-12; Io-Claude, 2026-09-25; Io-Claude, 2026-10-09; Io-Claude, 2026-10-08
> Raw: [2026-10-22-autorizzazioni-insieme](../../raw/conversazioni/2026-10-22-autorizzazioni-insieme.md); [2026-10-22-vercel-e-prova-aiuto](../../raw/sessioni/2026-10-22-vercel-e-prova-aiuto.md); [2026-10-22-stato-chiudi-controlli](../../raw/sessioni/2026-10-22-stato-chiudi-controlli.md); [2026-10-22-skill-progetta](../../raw/sessioni/2026-10-22-skill-progetta.md); [2026-10-22-criteri-di-progetto](../../raw/sessioni/2026-10-22-criteri-di-progetto.md); [12-handoff-interrogazione](../../raw/crescita-professionale/12-handoff-interrogazione.md); [13-roadmap-complessiva](../../raw/crescita-professionale/13-roadmap-complessiva.md); [contesto-progetto](../../raw/crescita-professionale/contesto-progetto.md); [12-10-2026-nuovo-ritmo-lotti](../../raw/mss/12-10-2026-nuovo-ritmo-lotti.md); [09-10-2026-controllo-sistema](../../raw/mss/09-10-2026-controllo-sistema.md); [07-10-2026-tipi-agente](../../raw/mss/07-10-2026-tipi-agente.md)
> Updated: 2026-10-22

## Overview

Matteo dirige agenti che producono i materiali (documenti, CV, verbali), e le regole di conduzione nascono dai passaggi di consegne tra un agente e il successivo. Qui stanno le regole ricorrenti, non le procedure dei singoli lavori.

## Regole

- **Decidi e scrivi la decisione con il criterio accanto.** Lascia aperto solo ciò che dipende da un fatto mancante, e di ogni aperto di questo tipo scrivi quale fatto manca (un trigger, non una data).
- **Le decisioni chiuse non si riaprono.** Il passaggio di consegne elenca le decisioni con il criterio e un divieto esplicito di riaprirle (per esempio: la claim «AI Act in progress» non deve ricomparire da nessuna parte).
- **Una domanda rimandata «per sicurezza» è lavoro non fatto, non prudenza.** Non chiedergli di scegliere tra opzioni che l'agente sa già valutare al posto suo.
- **Niente consulenza legale o fiscale** (AI Act, NASpI): i fatti, poi il rimando a un professionista.
- **Ricerca web:** si usa quando serve e si dice sempre cosa si è trovato e da quale fonte.
- **Ogni lavoro ha una condizione di chiusura e una data.** Se un lavoro rallenta quello decisivo, si taglia il lavoro, non la data.
- **Un binario attivo alla volta.** Quando due binari erano aperti (interrogazione skill e HubSpot), Matteo ne ha chiuso uno; l'handoff dell'altro è congelato, non cancellato, e si riparte esattamente da lì. Un handoff dello storico è segnalato come «non si esegue».
- **Il passaggio di consegne dice cosa leggere, in ordine, e solo quello.** Un file che non serve a quel binario si dichiara non necessario (per le candidature non serve la bussola della valutazione).
- **Nomina i divari:** quando Matteo fa una mossa e non la nomina, nominagliela tu nella lingua del contesto (vedi `persona/rubrica-e-valutazioni.md`).
- **A fine seduta:** una riga di log nella roadmap e nel profilo, e il file di contesto allineato su disco e nel progetto claude.ai.

## Chi decide cosa (12/10/2026)

Matteo ha detto: «mi sento inutile in queste chat perchè mi limito a seguire il filo dei tuoi ragionamenti e non posso che fidarmi perchè non ho le competenze per prendere decisioni di prodotto tecniche». La divisione che ne è uscita (decisione `0012`): le scelte tecniche (strumenti, codice, struttura) sono degli agenti; a lui spettano la direzione e i conflitti che richiedono il parere di un utente o di un owner; in chat si parla di risultati, non di numeri di issue, merge e conflitti. Se un errore degli agenti produce un grosso bug, alla peggio si ricostruisce con più esperti; ma bisogna accelerare il ritmo. È l'episodio dietro la proposta TIMONE (vedi `persona/lettura-non-verbale.md`).

Altre regole che Matteo ha fissato sul lavoro con gli agenti:

- Le segnalazioni devono dire cosa fare: il 09/10/2026 ha unito dal telefono una proposta mentre il parere del revisore era «DA CORREGGERE», perché il titolo («TOCCA A TE», senza un «non unire ancora») ha contato più del verdetto. L'errore di segnalazione era dell'agente, ma è anche un dato sul suo modo di usare i pareri.
- Quando lavorano due agenti sulla stessa repo servono regole per prevenire e risolvere i conflitti, e per le interruzioni; Matteo le ha chieste come schema generale, non come correzione puntuale del caso.
- Matteo detta a voce: refusi e parole storpiate vanno letti per il contesto («coda di tabù» voleva dire «Codex»).
- Gli agenti devono sapere come comportarsi in base al ruolo; una regola «citami le righe» (quando una decisione dipende da un file, riportare le parti su cui deve decidere) va nelle istruzioni personalizzate delle piattaforme, non nei file personali.

## Chi esegue (22/10/2026)

Matteo ha fissato il riparto tra i modelli: «Usa Sonnet per l'esecuzione, Opus solo per decisioni difficili», poi «Decide Opus, esegue Sonnet». Nelle sessioni che hanno funzionato le decisioni sono state prese prima e passate a Sonnet in un solo brief, con file e prove in un giro. Le scelte puramente tecniche le prende l'agente (coerente con `0012`); Matteo conferma con frasi come «Confermo procedi pure e fai chiusura» o «Ottimo fai chiusura». Dettagli e lezioni in [Il ciclo progetta, brief, chiudi](ciclo-progetta-brief-chiudi.md).

**Autorizzazioni tutte insieme (22/10/2026).** L'agente senior Opus, in chat di lavoro come queste, non chiede le autorizzazioni una alla volta: le raccoglie, le valuta tutte insieme quando può e le chiede in un solo messaggio (push, cancellazioni, file in `.git`, server da avviare). Parole di Matteo: «Deve valutarle tutte insieme quando può e chiedermele insieme. Per evitare di continuare a ricaricare contesto per rispondere.» Ogni turno in più rimanda tutto il contesto: nella chat del 22/10 la cache riletta era 7.058.449 token su 7.305.657.

Un errore da non ripetere: il clone locale era indietro rispetto alla repo remota e, senza `git pull`, un agente ha creduto che mancasse `raw/sessioni/` e ha scritto un formato di nota diverso da quello già in AGENTS.md.

## Come si tiene la roadmap (regole del 07/08/2026 e del 01/09/2026)

- Una riga per movimento, con la data; niente riscritture silenziose.
- Niente entra senza stato e senza condizione di chiusura verificabile: se non si sa dire quando è finito, è un'idea e va nel backlog.
- I numeri si scrivono veri: se si dichiara una copertura, si dà il conto senza aspettare che lo chieda (14 file su 16, non 16).
- Al datore di lavoro esce solo `PROVATO`.
- Regola di Matteo del 01/09/2026: «non voglio lasciare nei file decisioni da prendere dove agenti parlano con me». Quando un agente aggiorna i file, annota già le decisioni che lui può e sa prendere; chi legge le esegue e riapre solo se ha un fatto nuovo che contraddice il criterio, non perché preferisce un'altra opzione. Scopo dichiarato: chiudere più lavoro possibile mentre se ne apre di nuovo.
- Una cosa alla volta, finita e raccontabile: i cantieri sospesi non si riaprono di iniziativa dell'agente, nemmeno se sembrano il passo logico.
- Il disco è la fonte di verità: si scrive nella cartella `Io-Claude\Crescita professionale\`, mai sulla copia in `docs\Archives\`.
- Ogni agente che tocca il metodo di interrogazione lavora sotto il vincolo della visione dello strumento (vedi `persona/valori-e-visione.md`).
- All'inizio di ogni chat del binario crescita e valutazione va linkata o aperta la bussola: senza un path esplicito l'instradamento non è garantito.

## Cowork e git, dal 25/09/2026

Ogni `git add` o `commit` crea e poi cancella `.git/index.lock`; nella sandbox Cowork cancellare è vietato finché Matteo non concede il permesso di cancellazione sulla cartella, una volta per sessione. Per leggere lo stato si usa `git --no-optional-locks status`. Verificato il 25/09/2026 che non esiste un'impostazione permanente da attivare: il gesto giusto è cliccare «Allow» sulla richiesta, e non mandare Matteo a cercarla nelle impostazioni. Dal PC di Matteo, fuori da Cowork, git funziona normalmente.

## Il CV è generato

Il CV Customer Success si rigenera con `strumenti/build_cv_customer_success.js` (Node e libreria `docx`; A4, Calibri 9,5 pt, una pagina), poi conversione in PDF con LibreOffice. Se cambia il testo si ricontrolla che stia in una pagina e si rigenerano entrambe le lingue. La cartella `Claude outputs/` è tracciata su richiesta di Matteo (25/09/2026) e contiene copie identiche dei PDF: se il CV si rigenera, si aggiornano anche quelle copie o si tolgono, per non avere due versioni diverse con lo stesso nome.

## See Also

- [Il ciclo progetta, brief, chiudi](ciclo-progetta-brief-chiudi.md)
- [File, cartelle e contesto](../metodo/gestione-file-e-contesto.md)
- [Come comunicare](../persona/come-comunicare.md)
- [Lezioni apprese](../metodo/lezioni-apprese.md)
- [MSS](../progetti/mss-metaskillsystem.md)
