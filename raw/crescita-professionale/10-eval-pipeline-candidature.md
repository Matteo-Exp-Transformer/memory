# 10 Eval Pipeline Candidature

> Source: Io-Claude/Crescita professionale/10_Eval_Pipeline_Candidature.md (PC di Matteo)
> Collected: 2026-10-21
> Published: Unknown
> Ultima modifica originale: 2026-07-30

# Eval n.1 — Pipeline candidature in HubSpot
*Predizione congelata il **30/07/2026** (sessione 6).*
*Misurazione: **30 giorni dopo l'invio della prima candidatura**. Data non ancora determinata — vedi sotto.*

> ### 📌 Revisione della scadenza — 30/07/2026, stessa sessione
> La data fissa del 30/08 è stata **sostituita da un trigger** perché Matteo ha deciso di non candidarsi ancora. Senza candidature inviate non esistono dati, e un eval che scade su un denominatore vuoto non si "misura male": **non si misura affatto.**
>
> **Nuova regola:** il conteggio parte dal giorno in cui il primo deal entra nello stage *Candidatura inviata*. Da lì, 30 giorni.
>
> ⚠️ **La predizione sotto NON è stata toccata** — e non va toccata. È cambiata la data della misura, non il contenuto della stima. Se un giorno la predizione risultasse modificata, questo file va considerato invalido.
>
> ⚠️ **Rischio da sorvegliare:** un trigger senza data può essere rimandato all'infinito. Il trigger vale solo se l'evento che lo attiva ha a sua volta una condizione osservabile — vedi `04_Handoff`, punto sul rinvio delle candidature.
*⚠️ **Questo file non si modifica nella parte "Stima".** Congelare la predizione prima di vedere i dati è ciò che rende questo un eval e non un ricordo. Si compila solo la colonna "Reale" e la sezione Debrief, a misurazione avvenuta.*

---

## PERCHÉ QUESTO FILE ESISTE

Gli evals sono il buco n.1 in scheda (**L1**: spina concettuale coperta in sessione guidata, mai testata su un caso non pilotato). Questo è il primo caso non pilotato, e non è stato costruito a tavolino: è emerso configurando la pipeline di candidature su HubSpot.

**La forma è quella di un eval vero:**
- **ground truth** → i dati reali della pipeline al 30/08/2026;
- **predizione** → le percentuali stimate sotto, congelate *prima* di vedere qualsiasi dato;
- **metrica** → lo **scarto** fra stima e reale, per-stage;
- **il "prima" è tempistica**, non fonte: la stima è un'opinione, e va detta come tale finché non è misurata.

---

## LA PIPELINE (configurata il 29–30/07/2026)

`Candidature pipeline` — piano free, **una sola pipeline per oggetto** (scelta consapevole: candidature, non clienti, perché è sulle candidature che si producono i dati).

| # | Stage | Chiave tecnica | Probabilità stimata |
|---|---|---|---|
| 1 | Azienda Trovata | `appointmentscheduled` | 1% |
| 2 | Candidatura Pronta | `presentationscheduled` | 1% |
| 3 | Candidatura inviata | `decisionmakerboughtin` | **5%** |
| 4 | Ricevuta risposta | `qualifiedtobuy` | **6%** *(1/17 = 5,9%, arrotondato: HubSpot accetta solo interi)* |
| 5 | Colloquio | `contractsent` | **33%** |
| 6 | Assunto | `closedwon` | Won (100%) |
| 7 | Rifiutato | `closedlost` | Lost (0%) |

*Nota: 1% sui primi due stage è un workaround — HubSpot riserva 0% e 100% alle designazioni Lost/Won.*

---

## ⛔ LA PREDIZIONE — CONGELATA, NON TOCCARE

**Catena stimata su 20 candidature inviate:**

> 20 inviate → **17 risposte** → **3 colloqui** → **1 assunzione**

| Passaggio | Stima (30/07/2026) | Reale (30/08/2026) | Scarto |
|---|---|---|---|
| risposte / inviate | 17/20 = **85%** | | |
| colloqui / risposte | 3/17 = **18%** | | |
| assunzioni / colloqui | 1/3 = **33%** | | |
| assunzioni / inviate | 1/20 = **5%** | | |
| tempo medio di riscontro | *(non stimato — da fissare al Blocco 4)* | | |

### Ipotesi dichiarata come debole
L'**85% di tasso di risposta è molto ottimistico** e lo sapevo al momento di scriverlo: nelle candidature spontanee il tasso osservato è normalmente molto più basso (ordine di grandezza, non misura verificata sul mio segmento). **La stima è stata lasciata invariata di proposito.** Correggerla avrebbe distrutto l'eval; lo scarto su questa riga è il dato più informativo dell'esercizio.

### Regola di decadenza (fissata prima)
**21 giorni di silenzio → il deal passa a "Rifiutato".** Sul piano free non ci sono automazioni: la close date non chiude niente. La regola la eseguo **io, a mano, a cadenza fissa** (pipeline hygiene). Serve la proprietà *data di invio* per poterla applicare.

### Denominatore dichiarato
Il tasso di risposta si calcola su **"Candidatura inviata"**, non su "Azienda Trovata". I primi due stage sono attività mie e non appartengono al denominatore. L'esclusione si fa **nel filtro del report**, non abbassando la probabilità dello stage.

---

## DEBRIEF — da compilare 30 giorni dopo la prima candidatura inviata

1. Quale riga ha lo scarto più grande, e **perché**?
2. Lo scarto è dovuto a una **stima sbagliata** o a un **processo sbagliato**? *(Sono due conclusioni diverse e portano ad azioni diverse.)*
3. Cosa cambio nel processo di candidatura, sulla base di questo?
4. Le probabilità di stage vanno **ricalcolate sul reale**: da opinioni diventano dati.
5. Solo a questo punto si valuta se il livello evals in `03_Skill_e_Studio` si muove da L1.

## COSA SI PUÒ DIRE, E COSA NO — finché questo file non è compilato

✅ *"Sto costruendo il mio primo eval su un caso mio: ho congelato una predizione sulla mia pipeline il 30 luglio e la misuro a 30 giorni dalla prima candidatura, confrontando lo scarto."*

❌ *"Conosco gli evals."* · ❌ Qualsiasi percentuale detta come misurazione. Oggi sono **opinioni mie**.
