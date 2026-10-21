# Trading-Platform e il caso evals del cliente trading

> Sources: Io-Claude, 2026-10-12; Io-Claude, 2026-07-30; Io-Claude, 2026-09-01
> Raw: [00-profilo-matteo](../../raw/crescita-professionale/00-profilo-matteo.md); [02-vocabolario](../../raw/crescita-professionale/02-vocabolario.md); [03-skill-e-studio](../../raw/crescita-professionale/03-skill-e-studio.md); [13-roadmap-complessiva](../../raw/crescita-professionale/13-roadmap-complessiva.md)
> Updated: 2026-10-21

## Overview

Trading-Platform (repo privata, non clonabile) è l'unica delle tre app più sviluppate di Matteo con un sistema dal giudizio probabilistico: uno skill system che, in un'app di trading, risponde seguendo il metodo di lettura dei grafici del cliente. Per questo è il bersaglio giusto per costruire il primo eval vero. Le altre due app (BHM-Zen e PrenotaZen) hanno output deterministici e non sono candidate a eval.

## Il caso: fedeltà al brand del cliente

Triage del 13/07/2026. Il caso su cui si è lavorato è la fedeltà al brand: l'output deve rispettare tono, lingua, ruolo e, per legge, non dare indicazioni mirate di compra o vendi. Due misure diverse, che Matteo tende a confondere (la sua confusione ricorrente):

- **Guardrail legale:** giudice è l'avvocato, bersaglio è zero sforamenti.
- **Eval di fedeltà:** giudice è il cliente, il criterio è graduabile (tono in tre livelli, con esempi-timbro).

Il ground truth non può essere l'output del modello e non lo scrive Matteo: lo timbra il cliente su esempi reali, 3–5 output «mia voce» e 3–5 «non mia voce», congelati prima. La difficoltà che Matteo ha sciolto: non deve essere l'esperto del dominio per fissare il ground truth, deve strutturare l'assaggio.

## Cosa manca e cosa è aperto

- Il test set è l'ultima fondazione aperta: quali grafici dare in pasto al sistema e perché quei casi (rappresentatività, casi limite, non solo i facili).
- L'artefatto previsto è un protocollo di intake e ground truth per il cliente trading: specifiche brand, tono, lingua, ruolo, legale; rubrica con criteri binari e graduati; procedura di timbratura; calcolo per criterio. Solo dopo si applica al codice.
- La repo è privata: serve accesso o file-chiave incollati.
- L'8/08/2026 Matteo ha detto di aver creato su Trade-Analyst «un sistema per testare gli agenti e lo skill system»: da verificare, perché se regge tocca il buco evals, oggi L1 (vedi `carriera/skill-e-livelli.md`).

## MILE-1 e lo stato dopo le decisioni di settembre

Il 07/08/2026 è stata definita la prima milestone di prova pratica: un eval di aderenza al brand su output multi-tenant. L'admin compila un form che modifica solo lo skill system, legato al tenant slug; si misura se l'output rispetta le istruzioni del brand. Condizione di chiusura con due bordi, messi da Matteo: il cliente timbra anche i negativi (3–5 «mia voce» e 3–5 «non mia voce», congelati prima) ed esiste un denominatore, «su cento richieste nuove, quante volte passa».

Il 01/09/2026 `D-03` ha deciso: evals sul trading agent sì, ma non ora, apertura il 13/10/2026, perché sono il buco n.1 e testualmente il requisito degli annunci («definire metriche di successo per feature AI-powered»). Nel frattempo `ES-4` allena lo stesso muscolo su un caso più piccolo.

> **Status: Disputed** (28/09/2026)
> L'apertura del 13/10/2026 non è confermata: `D-08` (28/09/2026) ha sospeso le candidature e portato il focus sull'MSS, e nessun file dice cosa succede ai cantieri evals. Il test set resta l'ultima fondazione aperta.

## See Also

- [Eval HubSpot](../progetti/hubspot-pipeline-eval.md)
- [Lezioni apprese](../metodo/lezioni-apprese.md)
- [Direzione professionale](../carriera/direzione-professionale.md)
