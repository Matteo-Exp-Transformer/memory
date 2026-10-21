# Skill tecniche e livelli: cosa sa fare, cosa no, cosa è provato

> Sources: Io-Claude, 2026-10-12; Io-Claude, 2026-07-30; Io-Claude, 2026-09-01
> Raw: [00-profilo-matteo](../../raw/crescita-professionale/00-profilo-matteo.md); [02-vocabolario](../../raw/crescita-professionale/02-vocabolario.md); [03-skill-e-studio](../../raw/crescita-professionale/03-skill-e-studio.md); [13-roadmap-complessiva](../../raw/crescita-professionale/13-roadmap-complessiva.md)
> Updated: 2026-10-21

## Overview

Il profilo tecnico di Matteo è onesto e più stretto di quanto lui tenda a dire sotto pressione. Sa costruire e chiudere prodotti con Cursor e Claude, ma non scrive da zero codice complesso senza AI e ha un buco chiave sulla valutazione sistematica dei sistemi AI (evals). I livelli in scheda non si promuovono senza un test severo su casi non pilotati.

## Sa fare

- Costruire e chiudere prodotti funzionanti con Cursor e Claude (L2 sul codice).
- Deploy reale su Vercel con login (L3); Supabase con query preparate da AI (L2).
- Wiring di integrazioni, chiavi e permessi dei provider (L2–L3).
- Prompt engineering applicato (L3); skill system multi-step funzionanti, due (L2–L3 sul costruire).

## Non fa (ancora)

- Codice complesso da zero senza AI; debug e test E2E (L1–L2).
- Stima autonoma della fattibilità tecnica profonda: la valida accanto a un dev.
- Valutazione sistematica dei sistemi AI (evals): L1, il buco chiave.

## Albero dei livelli (scala: L0 zero · L1 consapevole · L2 operativo con appoggio · L3 autonomo · L4 avanzato, saprebbe insegnarlo)

| Area | Livelli reali |
|---|---|
| Dominio F&B | sala e bancone L4; personale, fornitori, banqueting a Londra (esecutivo, non gestionale), coinvolgimento nelle decisioni aziendali L3; HACCP come processo L3 di conoscenza più studio; economia del locale (food cost, margini) L1, perché non li gestiva lui |
| Product thinking | definire i requisiti, caccia alle falle, workflow, anticipazione degli errori utente L3; user research L1 (pochi feedback); metriche di successo L1 |
| Costruire con AI | Cursor e Claude L2; deploy L3; database L2; integrazioni L2–L3; sicurezza base L2–L3 (salita dopo un quiz); Git da confermare; debug e test E2E L1–L2 |
| Differenziatore AI | prompt engineering L3; skill system L2–L3 sul costruire; guardrail L2; evals L1 |
| UI/UX | adattare UI da riferimenti L2–L3; design da zero o Figma L0 |
| Trasversali | inglese L3; leadership L3; autonomia sotto pressione L4 |

## Guardrail e evals sono due gambe diverse

Sa costruire guardrail (difesa quando il modello sbaglia). Sulla misura (evals) ha la spina concettuale (rubrica per testo libero, criteri binari contro graduati, scala ancorata, misura per criterio, estrazione del ground truth da un esperto) ma non l'ha provata su un artefatto reale. Resta L1 in scheda finché non produce l'eval e regge un test non guidato. Il 13/07/2026 ha di nuovo confuso e ri-separato guardrail ed eval.

## Concetti evals che sa spiegare (vocabolario al 30/07/2026)

Test set, ground truth e metrica sono i tre mattoni. Accuratezza da sola mente se una risposta è molto più frequente delle altre. Precisione e recall tirano in direzioni opposte e la scelta di quale errore costa di più è di dominio, non tecnica. Per testo libero serve una rubrica con criteri decisi prima; i criteri binari danno un numero pulito, quelli graduati vogliono una scala ancorata a esempi; si tiene la riga per criterio perché un criterio quasi sempre superato gonfia l'aggregato. Il ground truth non è mai l'output del modello: «prima» vuol dire tempistica (congelato prima di guardare i nuovi output), non «lo so io in anticipo». L'esperto riconosce esempi anche quando non sa scrivere la regola: gli si fa timbrare output veri, e questo è «definire i requisiti» puntato sull'eval.

## Regola sui livelli

I livelli non sono stati aggiornati in nessuna sessione guidata, per regola: la spina concettuale retta in sessione guidata non è un test severo. Una skill si dichiara a un datore di lavoro solo con prova pratica, artefatto o prova tangibile in app (stato `PROVATO`): vincolo aggiunto da lui il 07/08/2026, non presente tra le opzioni che gli erano state offerte.

## Formazione

In valutazione a luglio: il bundle Deep Learning Italia (Ergonomia Cognitiva, Generative AI, AI Act, Legal Tech) e il Google UX Design Certificate. Nota: i corsi sono input per posizionarsi, non il prodotto; i software sono gli asset reali.

## Buchi, dominio e cosa è provato (esiti dell'interrogazione)

- **I quattro buchi trovati due volte, in modo indipendente:** stima dei tempi, user research, economia, design generativo. Non servono conferme: serve decidere quali chiudere e in che ordine. La user research è stata riformulata nel blocco «Al Ritrovo» in modo che stringa invece di assolvere: n=1, non casuale, l'utente è il suo ex datore di lavoro; accettata da lui alla lettera. Il buco sulle stime si è spostato: non è il tempo, è il metro di «finito».
- **Previsione di organico:** «al pranzo bastano tre», tenuta per anni contro tutti e validata da un test che non ha scelto lui, con il nuovo assetto rimasto. È l'unica candidata `PROVA` del dominio ristorazione, confermabile da Paolo. Ma la ragione che ha dato è da proprietario d'azienda, non da persona di sala: gli undici anni non sono ancora dimostrati a monte del prodotto.
- **Gli undici anni al Ritrovo** non compaiono in nessuna riga dell'albero e non sono verificati da nulla, eppure reggono l'asset n.3. Si chiudono con contratto o buste paga, la verifica più economica del cantiere, che non dipende da Paolo.
- **Stato dell'albero a T1:** tutte e 153 le righe L3 e L4 nascono `ANNOTATO`; al 09/08/2026 sono chiusi i sei blocchi, con 0 livelli alzati e una sola `PROVA` su 43 domande (vedi `progetti/strumento-interrogazione.md`).

## See Also

- [La rubrica e le valutazioni](../persona/rubrica-e-valutazioni.md)
- [Studio, corsi e budget](../carriera/corsi-e-formazione.md)
- [PrenotaZen e BHM](../progetti/prenotazen-calendarbackup.md)
