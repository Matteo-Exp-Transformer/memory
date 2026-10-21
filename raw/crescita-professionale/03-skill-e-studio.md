# 03 Skill e Studio

> Source: Io-Claude/Crescita professionale/03_Skill_e_Studio.md (PC di Matteo)
> Collected: 2026-10-21
> Published: Unknown
> Ultima modifica originale: 2026-09-01

# Skill & Studio — Matteo Cavallaro
*Dove sono (albero skill) e cosa devo studiare (priorità). Aggiornare solo per: livelli skill e piano di studio.*
*v4 al 28/07/2026 (sessione 4: riordinata la sezione Certificazioni/Corsi sul criterio "gap degli annunci attivi"; aggiunta la sequenza doppio binario e il pacchetto candidatura tra gli artefatti target).*
*v3 al 13/07/2026 (sessione 3: evals spina concettuale + triage repo).*
 
---
 
## SCALA DEI LIVELLI
- **L0** Zero · **L1** Consapevole · **L2** Operativo con appoggio (AI/dev) · **L3** Autonomo · **L4** Avanzato (saprei insegnarlo)
---
 
## ALBERO SKILL — livelli reali
 
```
DOMINIO F&B & OPERATIONS
├─ Gestione sala/bancone (Italia, autonoma) ......... L4
├─ Gestione personale & turni ....................... L3
├─ Fornitori / scorte / ordini ...................... L3
├─ Banqueting & eventi alto livello (Londra) ........ L3 esecutivo (NON gestionale)
├─ Coinvolgimento in decisioni aziendali ............ L3
├─ Economia del locale (food cost, margini) ......... L1  ← non li gestivi tu
└─ HACCP (processo) ................................. L3 conoscenza + studio
 
PRODUCT THINKING
├─ Definizione requisiti ............................ L3
├─ Gap-finding / caccia alle falle .................. L3
├─ Workflow design .................................. L3
├─ Anticipazione errori utente ...................... L3
├─ User research (utenti reali) ..................... L1  ← pochi feedback finora
└─ Metriche di successo / definire "buono" .......... L1  ← priorità studio
 
AI-ASSISTED BUILDING
├─ Costruire con Cursor+Claude (leggo/modifico) ..... L2
├─ Deploy / messa online (Vercel, con login) ........ L3
├─ Prodotto in uso reale in produzione .............. SÌ — è il **calendario/prenotazioni**, non l'HACCP (corr. 01-09-26)
├─ Database (Supabase, query preparate da AI) ....... L2
├─ Integrazioni: env keys, account, permessi ........ L2–L3
├─ Sicurezza base (RLS, tipi di chiave, env) ........ L2–L3  ← salito dopo il quiz
├─ Git / versionamento .............................. da confermare
└─ Debug / test E2E ................................. L1–L2
 
DIFFERENZIATORE AI
├─ Prompt engineering applicato ..................... L3
├─ Skill system multi-step funzionanti (x2) ......... L2–L3 sul costruire
├─ Guardrail (difese input/output) .................. L2  ← lo sai fare
└─ Evals / soglie d'errore / criteri di "buono" ..... L1  ← IL buco chiave
 
UI / UX
├─ Curare e adattare UI da riferimenti + AI ......... L2–L3
└─ Design da zero / Figma ........................... L0
 
TRASVERSALI
├─ Inglese .......................................... L3 professionale
├─ Leadership ....................................... L3
└─ Autonomia / lavoro sotto pressione ............... L4
```
 
---
 
## PRINCIPIO DELLO STUDIO
Sei in disoccupazione: tempo pieno, ma è un **conto alla rovescia**. Ogni blocco di studio chiude con un **artefatto** (case study, eval scritta, checklist), non con "ho letto". Nemico = finire il cuscinetto con più nozioni e zero prove nuove.
 
**Metodo (tuo):** assorbi metodo → codifichi in istruzioni per un modello → impari eseguendo. Usa: modelli che ti interrogano, esercizi, materiale gratuito, applicato ai *tuoi* prodotti.
 
---
 
## PRIORITÀ DI STUDIO
 
### 1. Evals — valutare i sistemi AI *(n.1, confermata dal quiz)*
È la linea che separa l'AI PM vero dalla trappola. Al quiz hai coperto i *guardrail* (difesa) ma non gli *evals* (misura): sono due gambe diverse, ti manca la seconda.
**Devi saper rispondere a:** test set e ground truth; differenza tra "funziona" e "funziona bene, misurato"; precisione vs recall in parole semplici; come si sceglie una soglia d'errore accettabile e cosa fa il fallback.
 
**STATO post-sessione 3 — spina concettuale COPERTA (in sessione guidata), livello NON promosso.** Padroneggiati a voce, applicati al caso brand-fidelity del cliente trading: quali sistemi hanno bisogno di eval (probabilistico vs deterministico); output vs ground truth; guardrail (legale, avvocato, zero sforamenti) ≠ eval (fidelity, cliente, graduabile); circolarità del ground truth; **eval a rubrica** per testo libero; **binari vs graduati**; **scala ancorata** con esempi-timbro; **per-criterio vs aggregata**; **estrazione del ground truth da un esperto che non sei tu** (l'esperto timbra esempi, non scrive regole → è "definire i requisiti" puntato sull'eval). → *Tutto nel vocabolario v2.*
**Ancora APERTO (ultima fondazione):** il **test set** — quali grafici dai in pasto al sistema per generare gli output da timbrare, e *perché quei casi* (rappresentatività, casi limite, non solo quelli facili).
**Il livello sale a L2/L3 solo dopo:** produrre l'artefatto E reggere un interrogatorio su casi **non pilotati** (test severo, non sessione guidata).
 
**Artefatto (ridefinito, più preciso):** un **protocollo di intake + ground truth** per il cliente trading — il documento che gli metteresti davvero in mano. Contiene: le specifiche brand/tono/lingua/ruolo/legale; la **rubrica** (criteri binari + criteri graduati con scala ancorata); la procedura di **timbratura** degli esempi (5 "mia voce" / 5 "no"); come si calcola il numero per-criterio. Poi si applica al codice della repo (Trading-Platform — privata: serve accesso o file-chiave incollati).
**Gratis:** doc evals di Anthropic e OpenAI; "The Batch" di DeepLearning.AI; cerca "LLM evaluation basics", "rubric-based / LLM-as-judge evaluation".
 
### 2. Stima della fattibilità tecnica *(colma la dipendenza dal dev)*
Non diventare ingegnere: saper dire "semplice / medio / probabilmente complicato" con un ragionamento, prima di chiedere conferma.
**Riconoscere:** feature "solo CRUD" vs complessità nascosta (tempo reale, concorrenza, integrazioni, stato condiviso); perché "sembra facile" ≠ "è facile" (casi limite).
**Artefatto:** stima la complessità di una feature *prima* di chiedere al dev di Genova, poi confronta. Ripeti per calibrare il fiuto.
 
### 3. Sicurezza — consolidare *(scesa dopo il quiz: la maneggi già)*
Resta da fissare il legame **anon key ↔ RLS**: la anon key è pubblica per definizione, quindi è sicura da esporre *solo perché* le RLS fanno da serratura. Spegni le RLS e la chiave pubblica diventa un passe-partout.
**Artefatto:** checklist di sicurezza applicata ai tuoi due prodotti.
 
### 4. Economia del locale *(opzionale, alza il tetto)*
Oggi "capisco il business" regge solo sul lato operativo. Impara food cost, margini, budget acquisti → parli coi ristoratori da pari.
**Artefatto:** ricostruisci a posteriori il food cost del locale che gestivi, con numeri realistici.
 
---
 
## COSA NON STUDIARE (per proteggere il cuscinetto)
- Framework di programmazione da zero (React/Node "a mano"): l'AI copre quel livello.
- Design UI da zero / Figma avanzato: non è la tua sedia.
- Architetture enterprise scalabili: fuori dal posizionamento attuale.
---
 
## SEQUENZA SUL CUSCINETTO

> 🔴 **SUPERATA IL 01-09-26. In caso di conflitto vale `13_Roadmap_Complessiva.md` §9.**
> Il doppio binario A/B qui sotto resta come storia della decisione, ma la sequenza operativa
> corrente è il **piano a 6 settimane (01/09 → 12/10)**: guida `C2`/Fase 3, 20–25 h/settimana,
> scadenza dura **06/10 = prima candidatura inviata**. ⛔ In quelle sei settimane **non si aprono**
> corsi, PSPO I, l'artefatto evals sul cliente trading, né MSS oltre la manutenzione.
*Aggiornata in sessione 4: **due binari in parallelo**, non uno. Il binario A serve le candidature attive (orizzonte: settimane); il binario B serve la competenza e Genova (orizzonte: mesi). Le priorità di studio qui sopra (P1–P4) restano il binario B.*

**BINARIO A — candidature (prevale in caso di conflitto di tempo)**
1. **Sett. 1–2:** HubSpot Academy (Sales Hub → Customer Success) + apertura account CRM gratuito con **la mia ricerca di lavoro caricata come pipeline reale**. Chiusura del corso AI Act → headline LinkedIn allineata.
2. **Sempre, prioritario su tutto:** il **pacchetto candidatura** (CV 1 pagina Hospitality Tech, video-demo 60–90s, 2 case study, tabella 5 metriche, esempio situazione–azione–risultato). Nessuno dei 5 pezzi esiste ancora.

**BINARIO B — competenza (studio di fondo)**
3. **Sett. 1–4:** Evals (P1) in parallelo all'avvio Genova → artefatto sul trading system.
4. **Sett. 2–4:** Sicurezza (P3, veloce) + Fattibilità (P2) sul campo dentro Genova.
5. **In sottofondo:** IBM AI Product Manager, senza mai rubare tempo al binario A.
6. **Quando ho fiato:** economia del locale (P4).
---
 
## CERTIFICAZIONI / CORSI
> **⚠️ SEZIONE RIVISTA IL 28/07/2026 (sessione 4). La classifica operativa completa sta nel file 06_Piano_Corsi_e_LinkedIn — questa ne è la sintesi. In caso di conflitto vale il 06.**

**Cosa è cambiato e perché.** L'ordine precedente era costruito su un criterio implicito — *"cosa mi insegna la sostanza che mi manca per diventare AI Product Specialist"* — cioè sulla **destinazione**. Incrociandolo con la mappa candidature (file 08) è emerso che **su 6 candidature prioritarie, 5 nominano CRM, disciplina commerciale o metriche Customer Success, e zero nominano evals o AI product management**. La vecchia lista non era sbagliata: era **fuori tempo**. Serviva la scala, non la chiave della porta.

**Nuovo criterio di ordinamento (esplicito):**
> **rendimento = (gap chiuso su un annuncio attivo × verificabilità della credenziale) / (ore + €)**

Un corso che non chiude una riga scritta nella colonna "Gap da gestire" del file 08 **non è prioritario**, per quanto interessante sia.

**Budget confermato: €500 TOTALI su 3 mesi** (non più €500 per corso).

| # | Corso | Costo | Tempo | Perché lì |
|---|---|---|---|---|
| **P0** | **HubSpot Academy** — Sales Hub Software → Customer Success → Service Hub | €0 | 4–8h + esame ciascuno | Chiude **testualmente** i gap degli annunci (churn, retention, health score, NPS, time-to-value, CRM, pipeline). Credential ID verificabile su LinkedIn. Vero valore: smette di dover improvvisare quel lessico in colloquio → **prevenzione del difetto-chiave**. |
| **P1** | **AI Act** (corso certificato breve) | ~€60–200 | 2–20h | **È già dichiarato sul profilo LinkedIn** ("AI Act in progress") senza nulla dietro: va chiuso o cancellato. Timing: dal 2 agosto 2026 scattano controlli e sanzioni sull'art. 4. |
| **P2** | **IBM AI Product Manager** (Coursera) | ~$49/mese × 4–6 | ~120h | Resta il pilastro della destinazione, ma **cambia ruolo: gira in sottofondo e non blocca mai le candidature né gli artefatti**. |
| **P3** | **Evals** (short course DeepLearning.AI) | €0 | — | Priorità **n.1 per la competenza**, n.4 per la credibilità delle candidature. Le due cose non coincidono. **Va sul CV come artefatto, non come corso.** |
| **P4** | **Ergonomia Cognitiva e Neuroergonomia** (DLI) | ~€60 | 3h14m | Opzionale. Dà il linguaggio per *"perché un ristoratore non adotta una funzione"* (errore umano = indice di progettazione inadeguata) e copre l'unico L0 dichiarato (UX). |
| **P5** | Generative AI (DLI) | — | — | **Rimandare.** Costruisco con l'AI ogni giorno: certificato senza sostanza nuova. |
| **P6** | Legal Tech Professional (DLI) | — | ~44h | **Tagliato per ora.** Pubblico avvocati, accreditamento CNF non applicabile a me, peggior rapporto ore/impatto della lista. |
| **P7** | AIPMM CPM | — | — | **Non ora.** Serve a salire, non a entrare: dopo l'IBM e dopo essere entrato in azienda. |

*Fuori budget, solo da sapere:* "AI Evals for Engineers & PMs" (Maven, ~$3.750) è il gold standard sugli evals. Salto.
*Salesforce:* è lo standard enterprise e **TheFork lo chiede esplicitamente**. Copertura decisa: qualche modulo **Trailhead (gratuito)**; certificazione Associate ($75) **non ora**. Principio: non ottimizzare la piattaforma, ottimizza il vocabolario.

**Regola anti-mio-difetto:** UNA alla volta, finita e raccontabile. Niente stack di acronimi (i recruiter diffidano di chi colleziona). Saper spiegare *cosa ho imparato* > elencare sigle.

**⭐ REGOLA DI CONFLITTO (sessione 4, sopra tutte):**
> Se in una settimana devo scegliere tra avanzare un corso e produrre un artefatto, **produco l'artefatto. Sempre.**
> Il corso è il timbro. Il prodotto in uso reale è la cosa rara — e ce l'ho già.
 
---
 
## LE TRE REPO COME PALESTRE (triage sessione 3)
Ogni repo allena un artefatto diverso — nessuna è sprecata:
- **Trading-Platform** (privata) → **evals**: unico sistema con output probabilistico/giudizio. È *lì* che gli evals hanno senso.
- **BHM-Zen** (HACCP) e **PrenotaZen** (prenotazioni) → output deterministici (niente da valutare statisticamente): servono per **case study** (problema→decisione→soluzione→risultato), **checklist di sicurezza** (entrambe su Supabase → RLS/anon key), **stima di fattibilità**.
## ARTEFATTI TARGET (cosa devi avere in mano a fine cuscinetto)

**Pacchetto candidatura — priorità massima, nessun pezzo esiste ancora (sessione 4):**
- [ ] CV di **una pagina orientato Hospitality Tech** (non il CV da ristorazione tradotto)
- [ ] Video-demo di **60–90 secondi**: problema, utente, soluzione, beneficio
- [ ] 2 **case study** di prodotto (prenotazioni + HACCP): contesto, problema, scelte, demo, feedback, prossima iterazione
- [ ] Tabella delle **5 metriche** che saprei migliorare (onboarding completion, time-to-value, adozione, retention, crescita)
- [ ] 1 esempio di **ristoratore difficile** in formato situazione–azione–risultato
- [ ] Metriche vere dalla **pipeline CRM della mia ricerca di lavoro** (candidature gestite, tasso di risposta, tempo medio di riscontro)

**Competenza / Genova:**
- [ ] 1–2 lavori concreti da Genova
- [ ] 1 eval scritta di uno skill system → **protocollo intake + ground truth** per il cliente trading (test set ancora da chiudere, poi applicare al codice)
- [ ] 1 checklist di sicurezza sui tuoi prodotti