# Eval n.1: la pipeline candidature in HubSpot

> Sources: Io-Claude, 2026-07-30; Io-Claude, 2026-10-12; Io-Claude, 2026-08-07
> Raw: [10-eval-pipeline-candidature](../../raw/crescita-professionale/10-eval-pipeline-candidature.md); [13-roadmap-complessiva](../../raw/crescita-professionale/13-roadmap-complessiva.md); [04-handoff-prossimo-agente](../../raw/crescita-professionale/04-handoff-prossimo-agente.md)
> Updated: 2026-10-21

## Overview

Il primo eval non pilotato di Matteo, emerso configurando su HubSpot (piano free, una sola pipeline per oggetto) la pipeline delle candidature, il 29–30/07/2026. Gli evals sono il buco n.1 in scheda (L1: concetti coperti in sessione guidata, mai testati su un caso non pilotato). Ha la forma di un eval vero: ground truth (i dati reali della pipeline), predizione congelata prima di vedere i dati, metrica (lo scarto per stage).

## La predizione congelata il 30/07/2026

Catena stimata su 20 candidature inviate: 20 inviate, 17 risposte, 3 colloqui, 1 assunzione. Cioè 85% di risposte sulle inviate, 18% di colloqui sulle risposte, 33% di assunzioni sui colloqui, 5% di assunzioni sulle inviate. La parte «Stima» del file non si modifica: se risultasse modificata, il file è da considerare invalido. Si compilano solo la colonna «Reale» e il debrief.

Matteo ha dichiarato lui stesso debole l'85%: nelle candidature spontanee il tasso osservato è normalmente molto più basso, e la stima è stata lasciata invariata di proposito, perché lo scarto su quella riga è il dato più informativo dell'esercizio.

## Regole fissate prima

- **Trigger al posto della data:** la misura a 30 giorni, prima fissata al 30/08, parte dal giorno in cui il primo deal entra nello stage «Candidatura inviata», perché Matteo aveva deciso di non candidarsi ancora e un eval su un denominatore vuoto non si misura affatto. Rischio dichiarato: un trigger senza data può essere rimandato all'infinito.
- **Denominatore:** il tasso di risposta si calcola su «Candidatura inviata», non su «Azienda Trovata»; l'esclusione si fa nel filtro del report, non abbassando la probabilità dello stage.
- **Decadenza:** 21 giorni di silenzio e il deal passa a «Rifiutato»; sul piano free non ci sono automazioni, la regola la esegue lui a mano a cadenza fissa e serve la proprietà data di invio.
- **Stage:** Azienda Trovata, Candidatura Pronta, Candidatura inviata, Ricevuta risposta, Colloquio, Assunto, Rifiutato; le probabilità dei primi due sono 1% per un vincolo tecnico di HubSpot (0% e 100% riservati a Lost e Won).

## Debrief previsto

Quale riga ha lo scarto più grande e perché; se è una stima sbagliata o un processo sbagliato (conclusioni diverse, azioni diverse); cosa cambia nel processo di candidatura; ricalcolare le probabilità di stage sul reale; solo dopo, valutare se il livello evals si muove da L1.

## Cosa si può dire

Finché il file non è compilato: «Sto costruendo il mio primo eval su un caso mio: ho congelato una predizione sulla mia pipeline il 30 luglio e la misuro a 30 giorni dalla prima candidatura, confrontando lo scarto.» Non si dice «Conosco gli evals» e nessuna percentuale è una misura: sono opinioni sue.

> **Status: Outdated** (28/09/2026)
> Il contatore a 30 giorni parte dalla prima candidatura inviata. Il piano era di spedire entro il 06/10/2026, ma con `D-08` (28/09/2026) le candidature sono rinviate senza nuova data e le candidature inviate restano zero: il contatore non è partito, e l'eval, con la predizione ancora intatta, non ha dati. HubSpot resta, per `D-03`, solo come strumento di tracciamento.

## Cosa ha insegnato la bonifica del CRM (30/07/2026)

Matteo ha ripulito un CRM sporco: 27 contatti, 23 aziende, 1 deal (Trading Platform, eliminato da lui con motivazione corretta: tiene le candidature perché sono quelle che producono dati) e 2 task di esempio. I record fantasma avevano due rubinetti distinti, non uno: l'integrazione della casella Gmail personale e la creazione automatica delle aziende dal dominio email. Lezioni fissate:

- Igiene del dato: un CRM sporco è peggio di un CRM vuoto, perché dà fiducia in numeri falsi. Finché non hai contato oggetto per oggetto, non hai finito.
- Uno stage è un fatto verificabile, non uno stato d'animo.
- Le proprietà sono le domande a cui vorrai rispondere fra un mese: se non le crei ora quei dati non esistono retroattivamente. La data di invio non è opzionale, senza non si applica la decadenza a 21 giorni né si calcola il tempo di riscontro.
- Il piano free ha limiti che si sanno solo lavorandoci dentro (una sola pipeline per oggetto, niente automazioni, oggetti Lead e Campaign non disponibili): «conosco i limiti del piano free perché ci ho lavorato dentro» è una frase da praticante, non da corsista.
- Decisioni operative: HubSpot Academy e non Udemy, perché solo Academy rilascia un credential ID verificabile; il software non si compra.

Domanda di controllo a freddo prevista: «Fra tre mesi un recruiter di Dojo ti chiede: cosa hai imparato usando HubSpot? Rispondi ora, in 30 secondi.» La risposta deve contenere dei numeri e un cambiamento di processo, non un elenco di funzionalità.

## See Also

- [Candidature, ricerca e vincoli](../carriera/candidature-e-ricerca.md)
- [Trading-Platform e evals](../progetti/trading-platform-evals.md)
- [Lezioni apprese](../metodo/lezioni-apprese.md)
