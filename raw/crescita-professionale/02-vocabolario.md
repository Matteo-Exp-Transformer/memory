# 02 Vocabolario

> Source: Io-Claude/Crescita professionale/02_Vocabolario.md (PC di Matteo)
> Collected: 2026-10-21
> Published: Unknown
> Ultima modifica originale: 2026-07-30

# Vocabolario da Conoscere — Matteo Cavallaro
*Ogni parola specifica che uso, pronta al "ma cosa vuol dire?". Per ognuna: cosa dici · esempio · trappola.*
*Aggiornare solo per: definizioni di termini. v2 al 13/07/2026 (sessione 3: concetti evals per testo libero).*
 
---
 
### Product specialist
- **Dici:** "Chi porta competenza profonda di un dominio dentro le decisioni di prodotto: capisco il settore F&B e lo uso per definire cosa il software deve fare."
- **Perché non "manager":** il manager possiede roadmap e strategia con un team — non l'ho ancora fatto. "Specialist" mette davanti la mia forza vera (il dominio).
- **Trappola:** non dire "product manager" finché non ho gestito una roadmap con un team reale.
### Food & Beverage (F&B)
- **Dici:** "Ristorazione e somministrazione: ristoranti, bar, catering, hospitality."
- **Trappola:** se vedi facce perplesse, traduci subito in "ristorazione".
### Definire i requisiti
- **Dici:** "Trasformo un bisogno vago dell'operatore in istruzioni precise e costruibili per chi sviluppa."
- **Esempio:** "non voglio prenotazioni doppie" → *quando un cliente prenota una fascia, il sistema blocca il tavolo per tutta la durata, impedisce riassegnazioni, invia conferma.*
- **Metafora:** "Come dare una ricetta a un cuoco mai stato nella mia cucina: non basta 'fallo buono', servono grammi e passaggi."
- **Trappola:** scrivo il *cosa* e il *perché*, non le specifiche ingegneristiche profonde (il *come*).
### Workflow (flusso)
- **Dici:** "La sequenza di passi che utente e sistema fanno per completare un'azione. Progettarlo = decidere quei passi e l'ordine perché siano veloci e a prova d'errore."
- **Esempio (HACCP):** addetto apre l'app → sceglie il frigo → inserisce temperatura → se fuori soglia l'app segnala e registra → il responsabile riceve notifica.
- **Trappola:** non confonderlo con "disegnare le schermate" (quello è UI design). Il flusso è la *logica dei passi*.
### AI-in-the-loop
- **Dici:** "Processi dove l'AI fa la parte ripetitiva — bozze, riordino, segnalazioni — e la persona mantiene la decisione finale, dove conta."
- **Esempio:** l'AI legge le fatture fornitori e pre-compila magazzino e scadenze; il gestore controlla e conferma.
- **Trappola:** se **non** c'è decisione umana finale NON è in-the-loop → è **automazione autonoma** (human-out-of-the-loop), un'altra cosa, più rischiosa da promettere. Mai dire che "l'AI gestisce da sola" conformità o sicurezza alimentare.
### AI-assisted development *(la più delicata — a memoria)*
- **Dici:** "Definisco requisiti e architettura, poi costruisco iterando con Cursor e Claude, che generano e mi aiutano a modificare il codice. So leggere, capire e modificare codice; non scrivo da zero codice complesso senza supporto. La fattibilità tecnica profonda la valido con un dev."
- **Trappola:** NON dire "full-stack developer" né "programmo in React/Node". Una domanda tecnica e cadi.
### HACCP
- **Dici:** "Sistema obbligatorio UE per prevenire i rischi igienico-sanitari: individui i punti critici (temperature, cotture, scadenze), li tieni sotto controllo e documenti. Il mio gestionale ti *aiuta* a compilare correttamente e in tempo la documentazione. Lo conosco da operativo e l'ho studiato a fondo per costruirlo."
- **Trappola:** la parola-mina è "**garantisce la conformità**". Il software aiuta la documentazione; la conformità dipende da come gestisci davvero il locale, e nessuna app può rispecchiarlo. Non spacciarti per consulente HACCP certificato.
### Skill system / workflow AI strutturati *(il differenziatore)*
- **Dici:** "Codifico un metodo in istruzioni strutturate che un modello esegue. Ne ho due funzionanti: uno per gestire e navigare repository con agenti che scrivono codice, uno che in un'app di trading risponde seguendo il metodo di lettura dei grafici del cliente."
- **Trappola onesta (dilla tu prima):** "So costruirli; sto imparando a **valutarli in modo sistematico** — criteri e soglie d'errore per dire se funzionano *bene*, non solo se funzionano."
### Guardrail vs Evals *(distinzione appresa — non confonderle)*
- **Guardrail:** filtri/difese su input e output del modello — *cosa succede quando sbaglia*. (Questo lo sai fare.)
- **Evals:** misura di *quanto spesso ha ragione*, su un insieme di casi rappresentativi (test set), con un criterio deciso prima (ground truth) e una metrica. (Questo lo stai imparando.)
- **Trappola:** "ha azzeccato 8 volte su 8" NON è una eval (campione minuscolo, scelto da te, nessun criterio, nessun baseline).
### Metrica (negli evals)
- **Dici:** "Un numero che trasforma 'funziona' da sensazione in misura confrontabile e difendibile: dice quanto *spesso* il sistema ha ragione, non se ha funzionato una volta."
- **Metafora (tua):** come la temperatura in HACCP — "il frigo va bene?" è una sensazione; "4°C, soglia max 8°C" è una metrica con soglia: registrabile, confrontabile, mostrabile all'ispettore. La metrica sta all'AI come la temperatura sta al frigo.
- **Poggia su tre mattoni:** *test set* (insieme fisso di casi rappresentativi, riprovati a ogni modifica) · *ground truth* (la risposta giusta decisa prima da chi se ne intende) · *metrica* (la regola che confronta output vs ground truth e produce un numero).
- **Le principali (sistemi che classificano, es. il tuo trading):**
  - *Accuratezza:* % di casi azzeccati. **Trappola:** se una risposta è molto più frequente (es. "aspetta"), un sistema che dice sempre quella segna altissimo ed è inutile. Da sola mente.
  - *Precisione:* quando dice "sì", quante volte è davvero sì (pochi falsi allarmi). *Recall:* dei "sì" veri esistenti, quanti ne ha colti (poche occasioni perse).
  - *Metafora rilevatore di fumo:* suona a ogni toast = recall alto, precisione bassa; suona solo per incendi veri ma può perdere un fuoco lento = precisione alta, recall basso. **Tirano in direzioni opposte:** scegli quale errore ti fa più male — ed è una scelta di *dominio*, non tecnica.
  - *F1:* un solo numero che bilancia precisione e recall.
- **Soglia:** il taglio deciso *prima*, in base a quanto costa sbagliare (come gli 8°C), con un *fallback* (es. sotto soglia → conferma umana).
- **Se l'output è testo libero:** criterio verificabile (contiene i dati obbligatori? sì/no), valutazione umana con griglia, o modello-giudice; più metriche operative (latenza, costo, tasso di fallimento).
- **Trappola:** decidere cosa significa "buono" *dopo* aver visto i risultati = spostare i pali della porta. Si decide prima.
### Eval a rubrica (per testo libero) *(sessione 3)*
- **Dici:** "Quando l'output è testo libero — un'analisi, non un'etichetta — non esiste *una* risposta perfetta da confrontare parola per parola. Allora voto ogni output contro una **checklist di criteri decisi prima**: la rubrica. Il ground truth non è un testo-modello, è il **metro**."
- **Perché conta:** risolve la circolarità. Non confronto output-vs-output, confronto output-vs-criteri-fissati-prima.
- **Trappola:** una rubrica vale solo se i criteri sono verificabili da due giudici diversi allo stesso modo. Se un criterio richiede "interpretazione", non è ancora un metro (vedi scala ancorata).
### Criteri binari/oggettivi vs graduati/soggettivi *(sessione 3)*
- **Binari/oggettivi:** rispondono sì/no in modo quasi deterministico — "c'è il nome del brand? è nella lingua richiesta? contiene un compra/vendi mirato?". Due giudici non litigano → numero pulito gratis.
- **Graduati/soggettivi:** hanno un *quanto*, non un sì/no onesto — tono, "rispecchia lo stile". Mettere "sì/no" accanto NON li rende oggettivi: nasconde la sensazione, non la elimina.
- **Trappola (mia, ricorrente):** binarizzare a forza un criterio graduato. È lo stesso "il frigo va bene?" con una casella accanto. Campanello: se sto mettendo sì/no a un giudizio di gusto, mi sto ingannando.
### Scala ancorata (anchored scale) *(sessione 3 — lo strumento per i graduati)*
- **Dici:** "Per un criterio graduato lo strumento non è la casella, è una **scala con esempi concreti attaccati a ogni livello**, decisi prima. Sono gli esempi-ancora a far convergere due giudici sullo stesso voto."
- **Esempio (tono, cliente trading):** L1 fuori voce (freddo/robotico) · L2 tiepido (corretto ma piatto) · L3 in voce (competente e caldo, *come parla lui alla community*). Il ground truth vero = **3–5 output reali che il cliente timbra "mia voce" e 3–5 "non mia voce"**, congelati prima.
- **Metafora:** gli esempi-ancora stanno al tono come "8°C" sta al frigo: fanno convergere due persone sullo stesso verdetto.
### Misura per-criterio vs aggregata *(sessione 3)*
- **Dici:** "Da tanti output tiro *un* numero come nell'accuratezza (% che passa). Ma non collasso tutto in un numero solo troppo presto: tengo la **riga per-criterio** (brand-name 100%, tono 55%), perché l'aggregato dice *se* peggiora, il per-criterio dice *dove*."
- **Trappola:** un criterio quasi sempre superato (il nome del brand c'è sempre) gonfia l'aggregato e ti fa sembrare bravo dove non conta. Il per-criterio lo smaschera. (Peso diverso tra criteri = piano successivo, non subito.)
### Circolarità del ground truth (trappola) *(sessione 3)*
- **Cos'è:** definire "la risposta giusta = l'output che risulta allineato". È definire *giusto con giusto*: non misuri niente.
- **Regola:** il ground truth è deciso **prima e a parte**, non è mai l'output del modello. "Prima" = **tempistica** (congelato prima di guardare i nuovi output), non "lo so io in anticipo".
### Estrazione del ground truth da un esperto (che non sono io) *(sessione 3 — la chiave)*
- **Dici:** "Non devo essere l'esperto del dominio per fissare il ground truth. L'esperto **riconosce esempi** anche quando non sa scrivere la regola (sapere tacito): gli metto davanti output veri e lui **timbra** 'mia voce / non mia voce'. Quei verdetti congelati SONO il ground truth. Io conduco l'assaggio in modo strutturato e scrivo i verdetti."
- **Metafora (cuoco):** un grande cuoco spesso non ti scrive il risotto in grammi, ma assaggia due piatti e ti dice subito quale è giusto. Il suo palato è il ground truth; il mio mestiere è strutturare l'assaggio.
- **Collegamento forte:** questo è **"definire i requisiti" (L3 già mio)** puntato sull'eval — trasformo un bisogno/standard tacito in qualcosa di testabile. Stesso muscolo del bancone.
- **Trappola:** chiedere all'esperto di *descrivere* la sua voce ("formale o informale?") dà solo la *bozza* delle ancore. Diventa ground truth solo quando timbra **esempi reali**.
### "Capisco il business" *(ricalibrato)*
- **Dici:** "Parto dalle operations reali e dalle decisioni di un locale. Ero coinvolto nelle decisioni importanti dell'azienda."
- **Esempio:** "Uno sviluppatore ti fa un'interfaccia di prenotazione bellissima ma non sa che il sabato accetti overbooking perché una quota non si presenta. Io lo so dalla sala."
- **Trappola:** NON rivendicare la gestione dei conti (food cost, margini, budget): li teneva il titolare. Il tuo "business" è operativo e decisionale, non finanziario.
### Prodotto funzionante (vs prototipo)
- **Dici:** "Il prototipo dimostra un'idea; il prodotto funzionante viene usato per fare davvero il lavoro. I miei lo fanno."
- **Trappola:** non dire "production-grade" o "scalabile enterprise". Di': "funzionante e in uso per il compito reale, non ancora indurito per grandi volumi".
### Termini tecnici che ora sai difendere
- **RLS (Row Level Security):** policy che "chiudono" le tabelle del DB. Se spente, chiunque abbia la anon key (pubblica, estraibile dal browser) legge/scrive l'intera tabella. Sono la vera serratura.
- **anon key vs service_role key:** la anon va nel frontend; la service_role **mai** — ignora le RLS e agisce da super-admin, sta solo lato server.
- **Variabili d'ambiente:** i segreti non vanno versionati su git né esposti nel frontend, e vanno reinseriti nel pannello di deploy (Vercel), perché il file locale non viene caricato.

---

## CRM — lessico operativo *(sessione 6, 29/07/2026 — appreso facendo, su HubSpot)*
*Questi non sono termini HubSpot: sono termini CRM. Valgono identici su Salesforce, Pipedrive, Zoho. È il "vocabolario" della regola di progetto — non ottimizzare la piattaforma, ottimizza il lessico.*

### Oggetto (*object*)
- **Dici:** "Un CRM non ha una tabella sola: ha **tipi di record diversi** — contatti, aziende, deal, ticket, attività. Ognuno è un oggetto, con le sue proprietà e le sue liste."
- **Metafora:** sono archivi separati nello stesso magazzino. Svuotare lo scaffale dei contatti non svuota quello delle aziende.
- **Trappola (mia, vissuta):** ho pulito i contatti e ho creduto di aver finito il CRM. Erano rimaste 23 aziende. **Una pulizia si dichiara finita solo dopo aver contato oggetto per oggetto.**

### Record
- **Dici:** "La singola scheda dentro un oggetto. Un contatto è un record, un'azienda è un record."
- **Trappola:** non dire "contatto" per intendere "scheda". Sono cose di livello diverso.

### Proprietà (*property*)
- **Dici:** "Un campo dentro il record: nome, email, data di creazione, sorgente."
- **Metafora:** il record è la scheda del prodotto, la proprietà è una riga di quella scheda.
- **Perché conta:** le proprietà sono **le domande a cui potrai rispondere fra un mese**. Se non le crei oggi, quei dati non esistono retroattivamente.

### Sorgente del record (*record source*)
- **Dici:** "La proprietà che dice **da dove è arrivato** quel record: inserito a mano, creato dall'integrazione email, importato da file, creato da un'impostazione del CRM."
- **Esempio (mio):** i 25 contatti-rumore avevano sorgente *integrazione email*; le 23 aziende avevano sorgente *impostazione CRM* — due rubinetti diversi, non uno.
- **Trappola:** confonderla con il **proprietario** (*owner*). L'owner dice *chi è responsabile*, la sorgente dice *da dove viene*. Sono domande diverse.

### Filtrare per la proprietà giusta *(la lezione, non il termine)*
- **Il principio:** un filtro non va scelto perché funziona **oggi**, ma perché continua a separare rumore da segnale **domani**.
- **Esempio (mio errore):** ho cancellato i contatti-rumore filtrando per *owner = Matteo Cavallaro*. Ha funzionato solo perché in quel momento il CRM conteneva **solo** rumore. Con le candidature vere dentro — anche quelle assegnate a me — lo stesso filtro avrebbe cancellato il lavoro insieme alla spazzatura.
- **Da dire in una stanza:** "Ho filtrato per sorgente del record, non per proprietario: volevo un criterio che distinguesse l'origine, non la responsabilità."

### Azione in blocco (*bulk action*)
- **Dici:** "Filtro la lista, seleziono il gruppo, agisco una volta sola su tutti."
- **Il metodo, valido ovunque:** **filtra → seleziona → agisci in blocco**.
- **Campanello:** se in un software mainstream ti ritrovi a fare 200 volte la stessa operazione a mano, non è il software: stai usando lo strumento sbagliato. Fermati e ricontrolla.

### Igiene del dato (*data hygiene*)
- **Dici:** "La disciplina di tenere il CRM privo di rumore, duplicati e record morti — perché le metriche si calcolano su quello che c'è dentro."
- **Metafora (mia, F&B):** è la stessa logica dell'HACCP. Un frigo che *sembra* pulito e un frigo *verificato* pulito non sono la stessa cosa; la differenza la vedi solo quando arriva l'ispettore — o il recruiter.
- **La frase che vale in colloquio:** "Un CRM sporco è peggio di un CRM vuoto: quello vuoto non ti dà numeri, quello sporco te ne dà di falsi e ti ci fa contare sopra."
- **Trappola:** dichiarare un tasso di risposta calcolato su un denominatore che contiene rumore. Non è una metrica: è un numero inventato — e crolla alla prima domanda.

### Soft delete / cestino (*recycle bin*)
- **Dici:** "Il record cancellato non sparisce subito: resta recuperabile per un periodo (~90 giorni su HubSpot)."
- **Perché conta:** puoi essere deciso nella pulizia senza rischiare l'irreversibile.

### "Non è retroattivo"
- **Dici:** "Cambiare un'impostazione blocca quello che verrà, non ripulisce quello che c'è già."
- **Il concetto in due lavori distinti:** **chiudere il rubinetto** (prevenzione: impostazioni) e **asciugare il pavimento** (bonifica: cancellazione dei record già entrati). Sono separati, e nessuno dei due sostituisce l'altro.

### Pipeline e stage
- **Dici:** "La pipeline è la sequenza ordinata di fasi che una pratica attraversa dall'apertura alla chiusura. Lo stage è la singola fase, e deve corrispondere a **un fatto verificabile**, non a uno stato d'animo."
- **Metafora (mia, sala):** un tavolo passa da *prenotato → seduto → ha ordinato → servito → pagato*. "Ha ordinato" significa che la comanda è partita, non che sembrava intenzionato. E se dieci si siedono e tre ordinano, il problema non è nelle prenotazioni: è fra il tavolo e la comanda. La pipeline serve a vedere **dove si intasa**, non a fare l'elenco.
- **Trappola:** spostare un deal avanti perché ti senti ottimista. È il CRM sporco in un'altra forma — i numeri restano inventati.
- **Dettaglio che ti qualifica:** rinominare uno stage cambia **l'etichetta**, non **l'ID interno**. Nella mia pipeline lo stage "Colloquio" ha ID `contractsent`, "Candidatura inviata" ha `decisionmakerboughtin`. Si vede negli export, nei report e via API. Chi ha lavorato davvero su un CRM lo sa.

### Indicatore anticipatore vs ritardato (*leading vs lagging indicator*)
- **Dici:** "Il **lagging** misura il risultato finale: fatturato chiuso, assunzione ottenuta. È quello che conta ma arriva tardi e raro. Il **leading** misura i comportamenti che lo precedono: risposte ricevute, colloqui fissati. Arriva presto e spesso, ed è l'unico su cui puoi correggere il tiro mentre sei in corsa."
- **Esempio (mio):** se definisco il successo solo come "assunto", in 30 giorni avrò 0 su 25 e nessuna metrica da raccontare. Il numero che vive dentro la mia finestra di osservazione è il **tasso di risposta** — leading.
- **Metafora (HACCP):** l'intossicazione alimentare è il lagging indicator. La temperatura del frigo è il leading. Non aspetti il primo per capire che qualcosa non va.
- **Trappola:** costruire un cruscotto fatto solo di lagging indicator. Sembra serio e non è azionabile.

### Probabilità di stage
- **Dici:** "La percentuale attaccata a uno stage risponde a una domanda sola: *dei deal che arrivano fin qui, quanti si chiudono vinti?* Cresce lungo la pipeline, perché chi è arrivato allo stage successivo è già stato filtrato."
- **Trappola (mio errore):** dividere 100 per il numero di fasi. Le probabilità **non sono fette di una torta** e **non sommano a 100**: sono indipendenti l'una dall'altra e crescenti. Non è una torta, è un imbuto.
- **E soprattutto:** al primo giro quei numeri sono **opinioni**, non dati. Diventano dati solo dopo che la pipeline ha girato abbastanza da poterli ricalcolare sul reale.

### Decadenza del deal / pipeline hygiene (*aging*)
- **Dici:** "Un deal a cui nessuno risponde non si chiude da solo. Decido **prima** dopo quanti giorni di silenzio lo dichiaro perso, e passo la pipeline a intervalli fissi per applicare la regola."
- **Attenzione (piano free):** la **close date** è solo una *data prevista*. Non sposta niente, non chiude niente, non fa scattare nulla. Le automazioni non ci sono sul piano gratuito: la regola la eseguo **io, a mano, a cadenza fissa**.
- **Perché conta:** senza regola di decadenza la pipeline si riempie di zombie, e ogni tasso di conversione calcolato sopra è gonfiato.
- **Metafora:** è la stessa logica delle scadenze in cella frigo. La data non butta via niente da sola: qualcuno deve passare a controllare.

### Denominatore (di una metrica)
- **Dici:** "Prima di dire una percentuale devo poter dire **su cosa** l'ho calcolata. Cambiare il denominatore cambia il numero senza che nulla sia cambiato nella realtà."
- **Esempio (mio):** "tasso di risposta" su *tutte le aziende individuate* è un numero diverso da quello su *sole candidature effettivamente inviate*. Entrambi legittimi, uno solo onesto rispetto alla domanda che mi fanno.
- **Trappola:** dire la percentuale senza dichiarare il denominatore. È la forma numerica dell'allungarsi oltre il raggio.

### Chiave tecnica vs label
- **Dici:** "In un CRM ogni voce ha due strati: un **identificatore interno stabile e muto** (la chiave tecnica) e un'**etichetta leggibile e modificabile** (la label). Rinominare cambia solo la seconda."
- **Perché è progettato così:** un identificatore serve a puntare a una cosa in modo stabile, quindi **non deve avere significato**. Se cambiasse a ogni rename, report e integrazioni si romperebbero.
- **Esempio (mio):** nella mia pipeline lo stage "Colloquio" ha chiave `contractsent`, "Candidatura inviata" ha `decisionmakerboughtin`. Restano quelli dei nomi originali HubSpot.
- **Metafora:** il codice a barre di una bottiglia non cambia se cambi il nome del vino sul menù. È proprio il punto del codice a barre.
- **Trappola (mia, sessione 6):** aver voluto "sistemare" gli ID ricreando gli stage. Sarebbe costato la migrazione dei deal e lo storico, per un problema estetico. Era un'informazione da sapere, non un difetto da correggere.

### Campo sovraccaricato (*overloaded field*)
- **Dici:** "Usare un campo per due significati diversi. Funziona finché non devi filtrare o calcolare — poi produce numeri sbagliati e non capisci perché."
- **Esempio (mio errore, sessione 6):** ho messo l'1% di probabilità allo stage "Candidatura inviata" non perché fosse la mia stima (era il 5%), ma per **escluderlo dal denominatore**. Due lavori sullo stesso campo: la previsione della pipeline ne usciva falsata.
- **La regola:** un campo, un significato. L'esclusione dai conti si fa **nel filtro del report**, non nel valore del dato.
- **Metafora (F&B):** usare la colonna "note" del registro temperature per segnare anche chi era in turno. Funziona finché non devi filtrare per turno.

### Falsa precisione (*false precision*)
- **Dici:** "Dare a una stima più cifre di quante l'incertezza ne sopporti. Se il numero è un'ipotesi, scriverlo con i decimali non lo rende più vero — lo fa solo sembrare misurato."
- **Esempio (mio):** 1/17 = 5,9%, ma HubSpot accetta solo interi → 6%. Irrilevante: l'errore della *stima* è di molti punti, non di un decimale.
- **Trappola:** i decimali sono un segnale di autorevolezza mal riposto. In colloquio "circa il 6%, è una mia stima da verificare" batte "5,88%".
