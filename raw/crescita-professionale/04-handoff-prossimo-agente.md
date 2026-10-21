# 04 Handoff Prossimo Agente

> Source: Io-Claude/Crescita professionale/04_Handoff_Prossimo_Agente.md (PC di Matteo)
> Collected: 2026-10-21
> Published: Unknown
> Ultima modifica originale: 2026-08-07

# HANDOFF — per il prossimo agente
*Aggiornato: **sessione 6, 30/07/2026**.*

*⚠️ **Infrastruttura.** I file di lavoro vivono in una cartella locale collegata (`Documents\Io-Claude\Crescita professionale`), su cui l'agente ha lettura **e scrittura**, versionata con **git** (ogni modifica è tracciata e reversibile). La knowledge di Claude Desktop contiene ora **un solo file**, `CONTESTO_Progetto.md`, che è una mappa e non una copia: i dati veri stanno sul disco. Non far divergere le due cose.*

**Obiettivo di fase:** portarlo dentro un'azienda tramite le **candidature attive**, con la formazione al servizio di quelle candidature — non della figura target a tre anni. Genova ed evals restano attivi come binario parallelo.

> # 🛑 QUESTO BINARIO È IN SOSPESO — decisione di Matteo, 07-08-26
>
> **Il mandato attivo NON è HubSpot: è l'interrogazione skill.** Parole sue: *«viene prima di tutto
> ora chiudere interrogazione… HubSpot lascio in sospeso per completare questo lavoro fino in fondo
> prima»*.
>
> **Se apri questa cartella per lavorare, vai a [`12_Handoff_Interrogazione.md`](12_Handoff_Interrogazione.md)**,
> non a questo file. Ingresso completo del binario attivo:
> `docs\_lavoro\Per matteo\Valutazione Personale\00_HANDOFF_UNIFICATO.md` (repo CalendarBackup-v2).
>
> **Non riprendere HubSpot di tua iniziativa**, nemmeno se sembra il passo logico: la ripresa la
> decide Matteo, quando i sei blocchi dell'interrogazione sono chiusi. Fino ad allora questo file è
> **congelato e valido**: quando si riparte, si riparte esattamente da qui.
>
> ⚠️ **Numerazione:** la sessione 7 è stata usata il 07-08-26 per l'impostazione dell'interrogazione
> (scheda in `11_Valutazioni_Didattiche.md`). Il mandato HubSpot qui sotto, quando riprenderà, sarà
> la **prima sessione HubSpot dopo la ripresa** — rinumerala allora, non adesso.
>
> **Il metro resta uno solo** su entrambi i binari: i 7 criteri di `11_Valutazioni_Didattiche.md`,
> non modificati.

---

# ⏸️ IL MANDATO HUBSPOT (congelato il 07-08-26 — era la «sessione 7»)

## Sei un tutor. Riprendi la lezione guidata su HubSpot dal **Blocco 2**.

**Blocchi 0 e 1 sono chiusi e verificati** (vedi sotto). Si riparte da **Blocco 2 — caricare le candidature vere**.

**Il formato, e non negoziarlo:**

1. Tu dai **un'indicazione macro alla volta** — *cosa* ottenere e *perché*, con quel tanto di specifico che gli serve per non perdersi nei menu (dove sta la voce, come si chiama nell'interfaccia).
2. **Esegue lui.** Tu non crei, non modifichi, non cancelli nulla al posto suo. Mai. Il valore dell'esercizio è tutto nelle sue mani sulla tastiera.
3. **Poi verifichi tu**, davvero, leggendo il suo HubSpot col connettore. Non chiedergli "fatto?" — guardalo.
4. **Feedback specifico**, poi il blocco successivo. Se ha sbagliato, non correggerlo tu: digli *cosa* non torna e fallo rifare.

Scopo: preparare il suo HubSpot a essere una palestra vera **prima** che inizi il corso HubSpot Sales Hub Software. La pratica precede il corso, non lo segue.

### ⭐ CORREZIONE DI METODO IMPARATA IN SESSIONE 6 — applicala
Su un **dominio che non ha mai visto**, il socratico puro non funziona e lui te lo dirà (l'ha fatto, correttamente): *"non posso rispondere, non so cosa si può definire su HubSpot"*. Non è resistenza, è un bordo reale — **non si può mappare un bordo che non esiste ancora**.

**Sequenza corretta per ogni blocco nuovo:** *(1) spiegazione breve degli attrezzi e del perché → (2) domande → (3) esecuzione sua.* Il socratico resta il motore, ma **dopo** che ha il vocabolario minimo. Su terreno già noto, torna a interrogare prima.

Ha anche chiesto esplicitamente: **niente caccia al tesoro nei menu di un software nuovo.** Dagli il percorso (voci e nomi esatti), tieni per lui la **decisione** e il **criterio** — è lì che sta l'apprendimento, non nel trovare il bottone.

### Cosa ha funzionato meglio, da riusare
- **Metafore dal suo dominio F&B.** La pipeline spiegata come il servizio in sala (*prenotato → seduto → ha ordinato → servito → pagato*, con la conversione fra le fasi) ha sbloccato tutto il Blocco 1 in un colpo. Cerca sempre l'analogia in cucina/sala prima di spiegare astratto.
- **Verifica col connettore, mai "fatto?".** Tre volte su tre ha dichiarato completo un lavoro che non lo era. La verifica indipendente *è* la lezione.
- **Aggiungere i termini al vocabolario durante la sessione**, con il suo errore dentro come esempio. Lo ha chiesto lui ed è efficace.

### 🔧 Strumenti disponibili (verificati in sessione 6)
- **Connettore HubSpot** → legge i dati CRM (record, proprietà, pipeline). **Non** legge le impostazioni utente.
- **Estensione Claude in Chrome** → installata e funzionante. Legge le pagine del suo HubSpot loggato, incluse **le impostazioni** che il connettore non vede. Usala per verificare percorsi ed etichette esatte **prima** di mandarlo a cercare. ⚠️ Gli URL delle settings HubSpot non si indovinano: parti da `/settings/<portalId>` e usa `find` sulla sidebar. Per gli oggetti il path è `/object-type-settings/<portalId>/object/<0-1|0-2|0-3>`, per le pipeline `/pipelines-settings/<portalId>/object/0-3/<pipelineId>`.
- ⚠️ **Il suo portale è EU:** `app-eu1.hubspot.com`, non `app.hubspot.com`.
- ⚠️ La pagina delle pipeline carica le probabilità via JS e a volte torna vuota alla lettura: rileggila o chiedi conferma a lui.

---

## Il connettore HubSpot — cosa puoi fare

Collegato e funzionante a Claude Desktop (verificato 29/07/2026).
**Account:** ID `146609454` · `matteo.cavallaro.work@gmail.com` · piano **free**.

| Oggetto | Lettura | Scrittura |
|---|---|---|
| Contatti, Aziende, Deal, Task, Note, Chiamate, Email, Meeting | ✅ | ✅ |
| Lead, Campaign | ❌ *(richiede piano superiore)* | ❌ |

⚠️ **Hai il permesso di scrittura. Non usarlo.** Serve solo come rete di sicurezza se lui chiede esplicitamente di sistemare un pasticcio. Il default è **sola lettura**.
⚠️ Vale anche la regola generale del progetto: **niente modifiche, invii o creazioni su app collegate senza chiedere prima.**

---

## 📸 STATO REALE DEL SUO HUBSPOT AL 30/07/2026 (verificato col connettore, non riferito)

**CRM pulito: 0 contatti · 0 aziende · 0 deal · 0 task.** Punto di partenza vergine e sano.

**Pipeline configurata** — `Candidature pipeline` (piano free → **una sola pipeline per oggetto**, scelta consapevole: candidature, non clienti):

| # | Stage | Chiave tecnica | Probabilità |
|---|---|---|---|
| 1 | Azienda Trovata | `appointmentscheduled` | 1% |
| 2 | Candidatura Pronta | `presentationscheduled` | 1% |
| 3 | Candidatura inviata | `decisionmakerboughtin` | 5% |
| 4 | Ricevuta risposta | `qualifiedtobuy` | 6% |
| 5 | Colloquio | `contractsent` | 33% |
| 6 | Assunto | `closedwon` | Won (100%) |
| 7 | Rifiutato | `closedlost` | Lost (0%) |

⚠️ **Le chiavi tecniche sono quelle originali HubSpot** (rinominare cambia la label, non l'ID). Se costruisci report o filtri, usa quelle.

**Regola di decadenza fissata:** **21 giorni** di silenzio → "Rifiutato". Sul free **non ci sono automazioni** e la *close date* non chiude niente: la regola la esegue lui a mano, a cadenza fissa. Serve la proprietà *data di invio* (Blocco 3) per poterla applicare — ricordaglielo.

**Denominatore dichiarato:** il tasso di risposta si calcola su *"Candidatura inviata"*. I primi due stage sono attività sue e restano fuori dal denominatore, **tramite filtro nel report** — non abbassando la probabilità dello stage.

### Cosa è stato chiuso in sessione 6 (non rifarlo)
- **Due rubinetti distinti**, non uno: (a) casella Gmail personale su `Disable` in *Your Preferences → General → Email* (fermava i contatti, sorgente `EMAIL_INTEGRATION`); (b) creazione automatica delle aziende dal dominio email in *Data Management → Objects → Companies* (sorgente `CRM_SETTING`). **Se ricompaiono record fantasma, controlla ENTRAMBI.**
- Bonifica completa: 27 contatti, 23 aziende, 1 deal (*Trading Platform*, eliminato da lui con motivazione corretta — tiene le candidature perché sono quelle che producono dati), 2 sample task.
- Pipeline rinominata e riprobabilizzata.

## 🧊 ARTEFATTO CONGELATO — `10_Eval_Pipeline_Candidature.md`
**Non modificare la sezione "Predizione".** Contiene la stima fatta il 30/07 *prima* di avere dati (20 inviate → 17 risposte → 3 colloqui → 1 assunzione) e si misura il **30/08/2026**.

È il **primo eval su un caso non pilotato**, ed è emerso dall'esercizio invece di essere costruito a tavolino — il che vale più di qualsiasi test set progettato a freddo. L'85% di tasso di risposta **è ottimistico e lui lo sa**: è stato lasciato invariato di proposito, perché lo scarto è il dato.

⚠️ **Al 30/08 il tuo compito è farglielo compilare**, non lasciarlo scadere. Le domande di debrief sono già nel file. Il livello evals si muove **solo** dopo quella compilazione.

---

## I BLOCCHI DELLA LEZIONE — in ordine

### ✅ Blocco 0 — Pulizia. **CHIUSO (sessione 6)**
CRM a zero su tutti gli oggetti, entrambi i rubinetti chiusi. Concetto fissato: **igiene del dato** — un CRM sporco è peggio di un CRM vuoto, perché ti dà fiducia in numeri falsi.
*Lezione emersa strada facendo, da richiamare: un CRM ha **più oggetti**. Ha pulito i contatti e dichiarato finito con 23 aziende e 2 task ancora dentro. **Finché non hai contato oggetto per oggetto, non hai finito.***

### ✅ Blocco 1 — La pipeline giusta. **CHIUSO (sessione 6)**
Stage finali (diversi da quelli ipotizzati in sessione 5 — decisi da lui, e vanno bene): *Azienda Trovata → Candidatura Pronta → Candidatura inviata → Ricevuta risposta → Colloquio → Assunto / Rifiutato*.
Concetto fissato: uno **stage** è un fatto verificabile, non uno stato d'animo.
*Ha perso lo stage "colloquio tecnico" del piano originale. Non è un problema per i ruoli customer-facing, ma se comincia a fare due giri di colloquio andrà distinto.*

### Blocco 2 — Caricare le candidature **← RIPARTI DA QUI** *(1–2 sessioni)*
Dal file `08_Candidature_e_Profilo.md`, **categorie A e B per prime**. Per ciascuna: azienda come **record company**, recruiter come **contatto** (se noto), candidatura come **deal**.

⚠️ **VINCOLO NUOVO (sua decisione del 30/07): non si candida ancora.** Quindi i deal si fermano agli stage **1 (Azienda Trovata)** e **2 (Candidatura Pronta)**. Nessun invio. La pipeline esiste, le associazioni si imparano, e al momento di partire basta trascinare i cartellini. Sono esattamente i due stage che ha creato lui.

*Concetto: **associazioni**. Un deal non agganciato a un'azienda e a un contatto è un post-it, non un record. Fagli vedere cosa si rompe senza: apri un contatto e mostragli che non sa a quale trattativa appartiene.*
*Da far notare quando arriva: la scheda azienda si compila da sola dal dominio — HubSpot arricchisce. È lo stesso meccanismo che in sessione 6 gli aveva creato 23 aziende-spazzatura. Stessa funzione, un uso buono e uno cattivo.*

### Blocco 3 — Proprietà personalizzate *(1 sessione)*
Data di invio, link all'annuncio, fonte (LinkedIn / sito / referral), RAL pubblicata, categoria A–D.
*Concetto: le **proprietà** sono le domande a cui vorrai rispondere fra un mese. Se non le crei ora, quei dati non esistono retroattivamente. **Fatti dire da lui quali domande vorrà fare, poi si costruiscono le proprietà** — non il contrario.*
⚠️ **La "data di invio" non è opzionale:** senza, la regola di decadenza a 21 giorni non è applicabile e il "tempo medio di riscontro" non si calcola. Collegalo esplicitamente a quella regola, che ha deciso lui in sessione 6.
*Occasione: qui si vede la differenza fra **proprietà di sistema** e **proprietà personalizzata**, e i **tipi di campo** (testo, numero, data, menu a tendina, checkbox). Fallo sbagliare su un tipo e poi fallo correggere — capirà perché la scelta del tipo è una decisione e non un dettaglio.*

### Blocco 4 — Task, attività e follow-up *(1 sessione)*
Un task a **48 ore** su ogni deal che entra in "Candidatura inviata"; revisione della pipeline a cadenza fissa per applicare la regola dei 21 giorni.
*Concetto: è il meccanismo che **genera** la metrica. Senza task, il "tempo medio di riscontro" non si misura — e quel numero è la cosa che porta in colloquio.*
*Copre anche: **attività** come oggetti (note, email, chiamate, meeting), la **timeline** del record, la coda **Tasks**.*
⚠️ Ricordagli che sul free **non ci sono automazioni**: il promemoria lo crea lui. Se propone di automatizzare, la risposta è che serve un piano a pagamento e **non si compra** (decisione già presa).

### Blocco 5 — Definire le metriche prima di avere i dati *(1 sessione)*
Fagli scrivere **quali 5 numeri** vuole poter dire, **prima** che i dati esistano. Questa tabella è **uno dei cinque pezzi mancanti del pacchetto candidatura** — quindi vale doppio: è pratica CRM *e* è deliverable.
*Collega esplicitamente al file 10: le 5 metriche e la predizione congelata devono parlarsi.*

### Blocco 6 — Viste, filtri e report *(1–2 sessioni)*
Viste salvate, filtri, colonne, e il primo **report/dashboard** sulla pipeline.
*Concetto: qui si chiude il cerchio del **denominatore** — è nel filtro del report che si escludono gli stage 1 e 2, non abbassando la probabilità (suo errore di sessione 6, il **campo sovraccaricato**). Fanne il momento in cui quella lezione diventa operativa.*
*Copre il modulo Academy "Sales Reporting".*

### Blocco 7 — Comunicazione: template email, snippet, meeting link *(1 sessione)*
⚠️ **Richiede di ricollegare la casella email**, che in sessione 6 è stata messa su `Disable`. Prima di ricollegarla: fagli configurare la **Never Log list** (*Your Preferences → General → Email → Never Log*), altrimenti si ripresenta il problema del Blocco 0. **È il test di ritenzione migliore che avrà** — se ci arriva da solo, il criterio 7 della rubrica si muove.
*Copre il modulo Academy "Connecting With Customers".*

### Blocco 8 — Debrief finale e artefatto
La pipeline letta a 30 giorni dalla prima candidatura + compilazione del file 10 + la domanda di controllo qui sotto.

---

## 🎓 MAPPATURA CORSO ACADEMY ↔ PRATICA
*Struttura del corso **HubSpot Sales Hub Software**, letta dalla pagina Academy (verificata in sessione 6):*

| Modulo | Contenuto | Blocco pratico corrispondente |
|---|---|---|
| Welcome | 1 video, 2 min | — |
| **Identifying Good-Fit Leads** | 5 video, 28 min — Sales Workspace · Adding Contacts to Smart CRM · Managing Leads · Organizing Leads · Chatflows | Blocchi 2–3 |
| **Connecting With Customers** | 8 video, 34 min | Blocco 7 |
| **Closing Deals in HubSpot** | 2 video, 19 min | Blocchi 1–4 |
| **Sales Reporting and Upskilling** | 4 video, 18 min | Blocco 6 |
| Next Steps + **Esame** | 5 min + 3 ore | Blocco 8 |

⚠️ **Lacune del piano free — verificate col connettore, diglielo prima che ci sbatta:**
- **Oggetto `LEAD`: non disponibile** (`REQUIRES_ACCOUNT_MODIFICATION`). Il modulo *"Managing Leads in HubSpot"* mostra funzioni che lui **non può replicare**. Va studiato a video, non praticato.
- **Oggetto `CAMPAIGN`: non disponibile.**
- **Niente automazioni, 1 sola pipeline per oggetto.**
- **Non è un problema per l'esame** (è teorico), ed è anzi materiale utile: *"conosco i limiti del piano free perché ci ho lavorato dentro"* è una frase da praticante, non da corsista.

**Ordine deciso, non negoziabile:** la pratica precede il corso. Ma dal Blocco 4 in poi possono procedere in parallelo — a quel punto i video gli spiegano cose che ha già toccato con le mani, che è il modo in cui impara meglio.

---

## Tripwire da sorvegliare alla ripresa HubSpot *(era «sessione 7»)*

- **Se propone di iscriversi a più corsi HubSpot insieme** → fermalo. Uno alla volta, finito e raccontabile.
- **Se dichiara un numero prima di averlo misurato** → difetto-chiave in forma numerica. I numeri della pipeline si dicono **dal 30/08**, non prima. Fino a quel giorno sono *stime sue*, e va detto.
- **Se tocca la predizione congelata nel file 10** → l'eval muore. La stima non si ritocca, nemmeno se si accorge che era ottimistica. **Specialmente** allora.
- **Se dichiara di "conoscere gli evals"** → colonna 2, non 1. Formula corretta: *"sto costruendo il mio primo eval su un caso mio, si misura il 30 agosto"*.

### Nuovi tripwire dalla sessione 6 — la stessa forma, tre volte
Il pattern osservato non è verbale: è **colmare un'incertezza con la prima cosa plausibile invece di lasciarla aperta.** Sorveglia questi:

- **Se dichiara un lavoro finito** → **verifica col connettore, sempre.** Tre volte su tre in sessione 6 aveva dichiarato completo un lavoro incompleto. Non è malafede: è che smette di contare quando *sembra* fatto.
- **Se trova una spiegazione plausibile e si ferma** → chiedigli la **prova per assurdo**. Funziona benissimo con lui: *"quel toggle era già spento e i contatti sono entrati comunque — quindi non è quello"* gli ha spostato il ragionamento in un colpo.
- **Se il risultato è giusto, chiedi il criterio.** Ha ottenuto il CRM pulito con un filtro (*owner*) che con le candidature dentro avrebbe cancellato il lavoro. **Il risultato giusto per il criterio sbagliato è un falso positivo**, e in colloquio chiedono il criterio.
- **Se vuole "sistemare" qualcosa che gli hai solo spiegato** → distingui l'informazione dal difetto. Ha provato a ricreare gli stage per avere ID coerenti: costo alto, beneficio zero. Variante in miniatura dell'aggiungere portata.

## Domanda di controllo finale, da fargli a freddo
> *"Fra tre mesi un recruiter di Dojo ti chiede: cosa hai imparato usando HubSpot? Rispondi ora, in 30 secondi."*

La risposta deve contenere **dei numeri e un cambiamento di processo**, non un elenco di funzionalità. Se descrive il software invece del suo processo, il corso non sta servendo.

---

# DECISIONI PRESE IN SESSIONE 5 (29/07/2026)

### 1. Corso n.1 scelto: **HubSpot Academy — Sales Hub Software**
Gratuito · 4–8h + esame *(stima sessione 4, non riverificata)* · 5–6 ore/settimana · **target di chiusura: 5 agosto 2026**.
Poi **HubSpot Customer Success**, entro il 15 agosto — è quello che copre il lessico scritto nella card Dojo (churn, adoption, retention, health score, NPS, time-to-value).
**Artefatto associato:** la pipeline reale letta a 30 giorni (*"pipeline di N candidature, tasso di risposta X%, tempo medio di riscontro Y giorni, ecco a quale stage si perdevano"*).
**Claim LinkedIn autorizzata solo a esame superato:** "HubSpot Sales Software Certified" + credential ID.

### 2. **AI Act — retrocesso da P1 a rimandato**
Motivo: **verificato che il profilo LinkedIn non è ancora stato scritto.** La claim *"AI Act in progress"* non è mai stata pubblica — esiste solo dentro il file 08. Quindi non c'è nessun debito da ripagare, e senza quel vincolo resta un corso che **nessuna delle sei candidature prioritarie richiede**, pagato con un budget di €500 contati.
**Azione conseguente, ancora da eseguire:** togliere la claim dal file 08 in tutti i punti in cui compare (righe ~12, ~34, ~192, ~202, ~231). Ci torna solo il giorno in cui il corso è chiuso.
Risparmio: €60–200 e fino a 20 ore.

### 3. Il suo criterio di scelta dei corsi
Formulato da lui: *"un corso vale il tempo se costruisce un profilo utilizzabile nell'immediato per candidarmi; se non serve alle prime candidature, non ne vale la pena per ora."*
Ha trovato da solo l'ancoraggio all'**annuncio attivo** — il perno giusto. Gli mancano due pezzi, che ha chiesto di non dibattere per ora e restano **aperti**:
- **verificabilità della credenziale** (non distingue un corso che insegna il lessico da uno che lascia un credential ID cliccabile);
- **il denominatore** (è un filtro, non un ordinamento: non sa dire *quale prima* tra due corsi che passano entrambi, e non vede il costo).
Riferimento completo: `rendimento = (gap chiuso su annuncio attivo × verificabilità) / (ore + €)`.

### 4. Riorganizzazione della knowledge
I 9 documenti sono stati rimossi dalla knowledge di Claude Desktop e sostituiti da **`CONTESTO_Progetto.md`**, affiancato al CV. Motivo: le copie nella knowledge erano già divergenti dal disco (l'handoff era un terzo della versione reale) e la knowledge è di sola lettura per l'agente, quindi il divario poteva solo allargarsi. Ora: **disco = fonte di verità, knowledge = un solo file-mappa.**

---

## CHI È MATTEO (in breve)
Oltre 11 anni di ristorazione operativa (gestione autonoma di un locale in Italia + eventi di alto livello a Londra). Sviluppatore autodidatta **AI-assisted** (Cursor + Claude): ha spedito prodotti funzionanti — un gestionale **HACCP in uso reale, oggi, in un locale** — e un sistema di prenotazioni. In disoccupazione (NASpI) → tempo pieno, anche da remoto.

**Figura target:** AI Product Specialist verticale F&B. *Si presenta come* **specialist**; product manager è la destinazione, non il titolo attuale.
**Porta d'ingresso (diversa dalla destinazione):** funzione **customer-facing nel FoodTech** — Customer Success, Partner Experience, SDR, BDM → poi Implementation → Solutions → Product Specialist. Tieni le due cose separate quando dai consigli.

## FILE DI CONTESTO (sul disco)
- **CONTESTO_Progetto.md** — mappa del progetto e regole di ingaggio. È l'unico file caricato nella knowledge di Claude Desktop.
- **00_Profilo** — valutazioni + log evolutivo. File-traccia: appendi una riga a ogni sessione.
- **01_Come_mi_Presento** — pitch v2, apertura "oro", 5 regole, risposte scomode.
- **02_Vocabolario** — ogni termine con *cosa dici / esempio / trappola*. v2: concetti evals per testo libero.
- **03_Skill_e_Studio** — albero skill (livelli reali) + priorità di studio + triage repo. v4.
- **05_Metodo_di_Apprendimento** — **il motore**: HACCP applicato alla competenza. Loop 7 passi, registro a 3 colonne, campanello. **Conduci ogni sessione su questo.**
- **06_Piano_Corsi_e_LinkedIn** — classifica corsi, sequenza, budget, regole LinkedIn. Contiene la nota di sessione 5 sull'AI Act.
- **07_Profilo_Completo** — **fatti grezzi**: anagrafica, contatti, esperienze cronologiche, descrizione dei due prodotti. Materia prima per CV e candidature.
- **08_Candidature_e_Profilo** — **documento operativo di riferimento**: mappa candidature al 28/07/2026, 4 categorie (A→D), headline e About proposti, pacchetto candidatura, roadmap 90 giorni.
- **09_Corsi_Interessanti** — appunti grezzi su Deep Learning Italia.
- **10_Eval_Pipeline_Candidature** — 🧊 **artefatto congelato (sessione 6).** Predizione sulla pipeline fissata il 30/07, da misurare **30 giorni dopo la prima candidatura inviata**. La sezione "Predizione" **non si modifica**; si compilano solo la colonna "Reale" e il Debrief.
- **11_Valutazioni_Didattiche** — 📋 **rubrica valutativa per sessione.** Da compilare a ogni sessione (regola obbligatoria, vedi sopra). 7 criteri fissi, scala a 3 livelli, ogni voto ancorato a un episodio. **Non duplica il 00:** il 00 racconta *cosa* è stato fatto (log narrativo), il 11 misura *come* ha lavorato (rubrica confrontabile).
- **CV_Matteo_Cavallaro_EN.pdf** — ⚠️ da rifare: serve un **CV di una pagina orientato Hospitality Tech**, non un CV generico da ristorazione.

⚠️ Non confondere **00** e **07**: il 07 racconta *cosa ha fatto* (statico), il 00 *come lavora e a che punto è* (si aggiorna sempre).

## ⭐ LA COSA PIÙ IMPORTANTE DA FAR RISPETTARE
Difetto-chiave: **sotto pressione si allunga oltre il proprio raggio** per sembrare più grande (titolo non ancora vero, standard non padroneggiato, "tutti i settori"). Forza opposta: **è più forte quando si restringe al concreto che può provare.** Ogni frase astratta va coperta da un fatto. Segnaglielo in tempo reale — lo vuole.

**Variante scritta (sessione 4):** il pattern non si attiva solo a voce e sotto pressione, si deposita anche nei **materiali redatti a freddo**. Vai a caccia di claim scoperte rileggendo i documenti, non solo ascoltando il parlato.

**Nota di sessione 5:** nessun overreach. Ha dichiarato spontaneamente che LinkedIn è vuoto — cioè ha smontato lui una claim che il progetto gli attribuiva. Comportamento-modello da riconoscere quando accade.

## COME LAVORARE CON LUI
- Italiano, del tu, **diretto, niente rassicurazione gratuita**. Chiede critiche dure.
- **Sessioni socratiche / interrogatorio** funzionano benissimo: lui mappa il bordo con parole sue, tu trovi lo scivolamento e colmi. **Non fare lezioni frontali.**
- **Ma:** se dice *"non voglio dibatterne adesso, dammi la risposta"* → **dagliela, subito.** Il metodo socratico costruisce criteri, non rallenta decisioni. In sessione 5 ha chiuso un dibattito così ed era la mossa giusta.
- Fa **molte domande operative in un solo messaggio** (fino a 5). Rispondi **a tutte, in ordine, senza accorparle**.
- Impara codificando il metodo in istruzioni ed eseguendo. Ama i piani e la caccia alle falle.
- **Scrivi direttamente sui file.** Non dargli testo da copiare a mano — lo ha chiesto esplicitamente.
- App collegate (Gmail, Drive, Calendar, HubSpot): lettura libera, **nessuna modifica/invio/creazione senza chiedere**.
- **Regola livelli (sua):** i livelli skill si consolidano **solo dopo un test severo su casi non pilotati**. In sessione guidata si logga il percorso, NON si promuove il grado.
- **Regola di conflitto:** tra avanzare un corso e produrre un artefatto, **vince sempre l'artefatto**.
- **Regola file:** aggiorna **solo** il file pertinente; appendi sempre una riga al log in 00_Profilo.
- ⭐ **Regola di valutazione (sua, sessione 6) — OBBLIGATORIA:** a fine di ogni sessione didattica o operativa, e in ogni caso **prima di un commit che contenga nuovi dati su come ha lavorato**, compila una scheda in **`11_Valutazioni_Didattiche.md`**. La rubrica è a 7 criteri fissi con scala a 3 livelli: **non cambiarla e non aggiungere criteri**, altrimenti le sessioni non sono più confrontabili. Ancora ogni livello a un episodio concreto. Non gonfiare: vale anche qui la regola che in sessione guidata si logga il percorso, non si promuove il grado.

---

## STATO ATTUALE — FATTO
Figura definita · pitch v2 · glossario v2 · albero skill · piano di studio · quiz tecnico (sicurezza ok; evals = buco n.1) · simulazione Genova con amici superata · concetto di *metrica* · file Metodo (05) · triage delle tre repo · evals: spina concettuale coperta in sessione guidata · mappa candidature verificata al 28/07/2026 · piano corsi con priorità, budget e regole LinkedIn · decisioni operative su HubSpot · **account HubSpot free aperto e connesso a Claude (29/07)** · **corso n.1 scelto e datato** · **knowledge riorganizzata su file unico** · **cartella sotto git** · **HubSpot: CRM bonificato a zero e pipeline candidature configurata (30/07)** · **vocabolario CRM operativo** · **primo eval su caso non pilotato impostato e congelato (file 10)**.

## DECISIONI OPERATIVE SU HUBSPOT (già prese, non ridiscutere)
- **HubSpot Academy, non Udemy.** Solo Academy rilascia un credential ID verificabile agganciabile a LinkedIn.
- **Il software non si compra.** Il CRM free è gratis per sempre. I piani Starter non servono. Limiti free rilevanti: **1 pipeline per oggetto**, ~1.000 contatti, niente automazioni.
- **Il campo "sito aziendale" non è un ostacolo:** usa il dominio Vercel delle sue app — è vero e coerente con la regola di non scrivere nulla di indifendibile.
- **Salesforce** è lo standard enterprise (TheFork lo chiede esplicitamente); HubSpot domina SMB/mid-market. Copertura decisa: **Trailhead gratuito, qualche modulo base**; certificazione Associate ($75) **non ora**.
- **Principio:** non ottimizzare la piattaforma, **ottimizza il vocabolario**. Nessuno lo scarta perché conosce HubSpot invece di Salesforce; lo scartano se non sa dire cos'è una pipeline o cosa misura un health score.

### Metodo di pratica deciso (il pezzo di maggior valore)
**Gestisce la propria ricerca di lavoro dentro HubSpot.** Aziende del file 08 → record azienda; recruiter → contatti; ogni candidatura → deal in pipeline con stage reali. Usa follow-up, note, template email, link meeting.
**Doppio effetto:** impara il CRM usandolo davvero **e** dopo un mese ha numeri veri da portare in colloquio — che è esattamente la frase che chiude il gap richiesto dagli annunci commerciali.
*Esercizio secondario, solo dopo: i ristoratori con cui ha già parlato dei suoi prodotti. (Nota: contatti reali di terzi in un CRM = trattamento di dati personali. Per uso personale va bene; saperlo dire lo qualifica.)*

## REGOLE LINKEDIN STABILITE
1. **Niente "in progress" nella headline.** Solo fatti compiuti. Un percorso in corso sta nell'About, con la data.
2. **Ogni certificazione accoppiata a un artefatto provabile.** Badge senza artefatto = superficie d'attacco.
3. **Massimo 3–4 certificazioni visibili.**
4. *"Builder di 2 app"* → **"2 app funzionanti, una in uso reale"**.

---

## BINARIO PARALLELO — EVALS E GENOVA (non abbandonato, solo non prioritario)

### Evals — dove siamo (sessione 3)
Deep-dive sul caso **brand-fidelity** del cliente trading (skill system che analizza grafici col metodo del cliente, senza dare "compra/vendi" — vincolo legale). Coperti concettualmente, ora nel vocabolario v2:
1. quali sistemi hanno bisogno di eval (probabilistico vs deterministico);
2. output vs ground truth;
3. **guardrail** (giudice=avvocato, bersaglio=zero sforamenti) **≠ eval** (fidelity: giudice=cliente, graduabile) — sua confusione ricorrente;
4. **circolarità** del ground truth ("prima" = tempistica, non fonte);
5. **eval a rubrica** per testo libero;
6. criteri **binari/oggettivi** vs **graduati/soggettivi** (mettere sì/no a un giudizio di gusto NON lo oggettivizza — sua trappola);
7. **scala ancorata** con esempi-timbro;
8. misura **per-criterio vs aggregata** (+ trappola del criterio banale che gonfia);
9. **estrazione del ground truth da un esperto che non è lui**: l'esperto *timbra esempi*, non scrive regole.

**Livello: L1 in scheda** (spina retta ma in sessione guidata, non testata su casi non pilotati).

### Costruire gli evals per Trading-Platform — ordine invariato
1. **Test set** — ultima fondazione aperta: quali grafici dare in pasto e *perché quei casi*. Fallo mappare a lui.
2. **Artefatto:** protocollo intake + ground truth per il cliente trading.
3. **Codice:** applicare alla repo. ⚠️ **Trading-Platform è PRIVATA** — serve che la renda accessibile o incolli i file-chiave.
4. **Test severo** per promuovere il livello.

### Ancora in coda
**Simulazione colloquio con un'azienda vera** (non gli amici). Domande a freddo pronte:
- *"Perché dovrei prendere te e non un dev junior che costa uguale?"*
- *"Raccontami una volta in cui hai sbagliato a valutare la fattibilità di qualcosa."*
- Versione commerciale/CS: *"Come qualifichi un lead?"* · *"Un merchant non usa una funzione da tre mesi: cosa fai?"* · *"Come misuri se l'onboarding è andato bene?"*

---

## PUNTI APERTI / CAUTELE
- **Il pacchetto candidatura non esiste** — CV 1 pagina, video-demo 60–90s, 2 case study, tabella 5 metriche, esempio STAR: **zero su cinque**. **È la priorità che batte i corsi.**
- **Claim AI Act ancora dentro il file 08** in 5 punti. Va tolta.
- **Profilo LinkedIn ancora da scrivere** interamente.
- **Il criterio di scelta corsi è incompleto** (manca verificabilità e denominatore) — dibattito rimandato su sua richiesta.
- **Prezzi Deep Learning Italia non verificabili via ricerca** — vanno controllati a mano.
- **Stima fattibilità tecnica** (priorità 2): allenarlo a "semplice/medio/complicato" *prima* di chiedere al dev. Le repo BHM/Prenota sono la palestra.
- **Sicurezza** (priorità 3, veloce): fissare anon key ↔ RLS. Artefatto: checklist sui due prodotti.
- **Git:** livello non confermato. *(Nota: la cartella progetto è ora sotto git — può diventare la palestra.)*
- **NASpI:** collaborazione Genova gratuita ora; **appena entrano compensi** verificare l'impatto con CAF o consulente **prima di incassare**. Rimandare a un umano abilitato.
- ~~**Discrepanza nome da chiarire**~~ → **CHIUSA (sessione 6, 30/07/2026).** Il nome corretto è **Matteo Cavallaro**. La preferenza utente "Simone Cavallaro" era stata inserita dal fratello che aveva usato l'account. ⚠️ **Resta da fare a lui:** togliere "Simone" dalle preferenze del profilo Claude (l'agente non può).
- **Corso HubSpot Sales Hub Software non ancora iniziato.** Target di chiusura **5 agosto** — data fissata in sessione 5 e **ancora non riverificata**: la sessione 6 è stata pratica pura, i moduli non sono partiti. Se la data non è più realistica, fagliela **spostare esplicitamente**, non slittare in silenzio. *(Struttura del corso, verificata dalla pagina Academy: Welcome 2min · Identifying Good-Fit Leads 5 video/28min · Connecting With Customers 8/34min · Closing Deals 2/19min · Sales Reporting 4/18min · Next Steps 5min · esame 3h.)*
- ⭐ **RINVIO DELLE CANDIDATURE — deciso da lui il 30/07, e va sorvegliato.** Ha detto: *"al momento non mi candiderò ancora, prima voglio formarmi un minimo."* Conseguenza: l'eval del file 10 non ha più una data fissa ma un **trigger** (30 giorni dalla prima candidatura inviata).
  **Perché la decisione è in parte legittima:** il pacchetto candidatura è a **zero su cinque**. Bruciare le candidature di categoria A senza CV di una pagina né case study è uno spreco reale, non una scusa.
  **Perché va comunque sorvegliata:** *"prima voglio formarmi un minimo"* è **la forma più pericolosa del rinvio** — non ha una condizione di uscita. È incompatibile con l'obiettivo di fase (*portarlo dentro un'azienda tramite le candidature attive, con la formazione al servizio di quelle*) e con la **regola di conflitto** (fra corso e artefatto vince l'artefatto). Se il tempo va nei **corsi**, il rinvio è il difetto-chiave travestito da prudenza. Se va nel **pacchetto candidatura**, è una scelta giusta.
  **✅ Trigger dato da lui il 30/07, dopo la pressione:** *"sarò pronto quando avrò preparato anche le candidature."* È un passo avanti reale — da uno stato d'animo (*"formarmi un minimo"*) a un lavoro con un output. **Ma è ancora contabile solo a metà**, e qui c'è la mossa elegante che il prossimo agente deve chiudere:
  > **Il trigger va ancorato allo stage 2 della sua stessa pipeline.** *"Candidatura Pronta"* è già uno stage che ha creato lui. Formalizzalo così: **si parte quando N deal sono nello stage "Candidatura Pronta"** — numero deciso da lui, suggerimento 5. Diventa una condizione **osservabile dal connettore**, dentro lo strumento che sta imparando, e non è più opinabile da nessuna delle due parti.
  Resta da fargli dire cosa significa *"candidatura preparata"*: CV su misura? lettera? case study allegato? **Quella definizione è il contenuto dello stage 2** e va scritta prima di caricare i deal (Blocco 2).
  ⚠️ **Se a metà agosto non ha né deal nello stage 2 né pezzi del pacchetto prodotti, il rinvio è fallito e va detto piatto.** Non trattarlo come un fallimento morale: è un dato, si guarda e si ricalibra.
- **`10_Eval_Pipeline_Candidature.md` non ha più una data fissa.** Il trigger è la prima candidatura inviata + 30 giorni. Un trigger senza data si può rimandare all'infinito: è per questo che il punto sopra esiste. Se passa senza compilazione, l'artefatto si svaluta e con esso l'unico test severo disponibile sugli evals.
- ⚠️ **La pipeline HubSpot rischia di restare vuota.** Senza candidature non ci sono deal, e il metodo di pratica (imparare il CRM usandolo) perde il carburante. **Soluzione da proporgli:** il Blocco 2 si fa comunque, caricando le aziende di categoria A e B negli stage **1 (Azienda Trovata)** e **2 (Candidatura Pronta)** — nessun invio, ma la pipeline esiste, le associazioni si imparano e al momento dell'invio basta trascinare. È esattamente la funzione di quei due stage che aveva creato lui.
- **Probabilità di stage non riverificate dall'agente:** la pagina delle pipeline carica i valori via JS e in sessione 6 è tornata vuota alla rilettura. 5% e 6% sono **dichiarati da lui**, non letti. Riverificalo alla prima occasione.

---

## RIGA DI LOG
*(sessioni 5 e 6 — **già appese** a `00_Profilo_Matteo.md` il 30/07/2026. Non riappenderle.)*
