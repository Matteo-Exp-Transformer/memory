# Lezioni apprese costruendo il sistema di valutazione

> Sources: Io-Claude, 2026-10-12
> Raw: [13-roadmap-complessiva](../../raw/crescita-professionale/13-roadmap-complessiva.md)
> Updated: 2026-10-21

## Overview

Tra il 07/08/2026 e il 09/08/2026 il sistema di interrogazione e valutazione è stato costruito, usato e rotto più volte in pochi giorni. Le lezioni che reggono, tutte nate da un errore misurato, non dal ragionamento a tavolino.

## 1. Regge la struttura, non la diligenza

- **Il corpus comprime a favore della tesi.** Il contatore dei casi (`MET-2`) è arrivato a 14 in due giorni. Regola: nessuna domanda e nessuna citazione senza aver aperto la fonte primaria, e la regola vale anche sulle sintesi dello stesso giorno, comprese le nostre: due casi su due sono stati trovati puntandola contro un documento nostro.
- **Una copia diverge anche quando chi copia sta attento.** Il file nato per fermare il problema (la bussola) lo ha ereditato nelle sue prime due ore di vita: «Blocco 7: restano 11» era falso, erano 10. Un comando che avrebbe trovato la riga era scritto e non è stato rilanciato. Lo stesso valore viveva in tre forme e il pattern ne copriva una: il comando deve coprire tutte le forme, e l'elenco dei file si costruisce dal comando, non a memoria.
- **Lo stato dichiarato non è lo stato reale.** `WP-1` risultava ancora «prossimo eseguibile» mentre il registro esisteva già, con 49 righe: un agente che avesse aperto il piano l'avrebbe rifatto e sovrascritto. Si apre la cartella, non si legge lo stato scritto.

## 2. Un collaudo che non può fallire non è un collaudo

- Un test passato con 4 controlli su 5 già scritti nel riquadro che l'agente leggeva misura chi incontra per primo il riquadro, non la bussola: il quinto controllo, l'unico comportamentale, era già quello fallito. Un «passa» che non può più diventare un «fallisce» è una dichiarazione.
- La risposta che finisce in un file che il soggetto legge brucia la prova, in tre forme: dentro l'oggetto testato, dentro il file che progetta la prova, dentro i puntatori che nominano il collaudo. Disegno risultante: il disegno è pubblico, si sigilla l'istanza, non il criterio; chi scrive non somministra; l'agente in prova riceve un task vero.
- Il ramo «fallisce» deve avere un percorso scritto e un tetto di ripetizioni: senza, ogni test finisce in «passa». Il collaudo cieco di instradamento è fallito (1 controllo su 5), il cantiere `C9` è stato chiuso per abbandono il 09/08/2026, senza terza somministrazione.
- Il test set è fatto di casi al bordo: manca il controllo positivo, e senza un positivo noto una misura severa non si distingue da una misura rotta (vedi `progetti/strumento-interrogazione.md`).

## 3. Una descrizione è una sintesi, e le sintesi comprimono

Il materiale di un esercizio si consegna come «ROTTA + STATO» (URL o sequenza di schermate, con la fonte primaria), mai descritto a parole. Un conduttore aveva descritto a parole uno dei tre stati: incompleta, rilevata da Matteo, da lì è nata metà dei guai della seduta. Stato non raggiungibile dal vivo: fuori dal materiale, si cambia caso. È il «gate schermata+URL» del 31/05/2026 portato su un contesto nuovo. La chiave di un esercizio si spacca in materiale e chiave, perché in Cursor la lettura dell'agente mostra il file al soggetto.

## 4. Una catena di validazioni non sostituisce l'ultimo lettore

Il piano dello skill system del binario è nato da una catena a quattro passaggi con Matteo dentro (sessione con il senior, upgrade, validazione di un secondo modello in Cursor, validazione finale da un terzo). I quattro difetti trovati dopo erano passati attraverso due validazioni precedenti: la catena alza la qualità e non sostituisce l'ultimo lettore. Il permesso di spostare i file era già concesso: la decisione di non spostare ha retto su un argomento, non su un divieto.

## 5. Piccole regole di igiene

- Un file operativo temporaneo ha una data di morte scritta (quello per due giorni di agenti Cursor: il 10/08/2026), altrimenti diventa una copia stale.
- Il binario crescita aveva 14 file, due cartelle e un protocollo senza instradamento: per questo uno skill system contenuto per il binario (`IDEA-4`, tre file nuovi di al massimo 415 righe).
- Le promozioni arrivano dove si applica il protocollo giusto: lui dà l'ancora, il repo dà l'indirizzo.

## See Also

- [Strumento di interrogazione](../progetti/strumento-interrogazione.md)
- [Lavorare con gli agenti](../metodo/lavorare-con-agenti.md)
- [Eval HubSpot](../progetti/hubspot-pipeline-eval.md)
