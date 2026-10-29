---
name: progetta
description: Usa questa skill quando Matteo vuole progettare un lavoro prima di affidarlo a un agente («progetta», «chat di ragionamento», «prepariamo il brief»): guida il ragionamento, compila la scheda di progetto nella repo del progetto e scrive il brief per l'esecutore solo dopo che il controllo della scheda passa.
---

# progetta — dalla chat di ragionamento al brief

La chat di ragionamento decide; l'esecutore esegue senza dover scegliere. Il ponte è la **scheda di
progetto**: un file nella repo del progetto (mai in `memory`), controllato da uno script. Finché il
controllo non passa, il brief non si scrive.

`<memory>` = `C:\Users\matte.MIO\Documents\GitHub\memory` (nel cloud: dove è clonata la repo `memory`).

## Le cinque regole del ragionamento

1. **Manca sempre qualcosa.** Cercalo attivamente e classifica ogni mancanza o incognita nella sezione
   «Mancanze e incognite»:
   - `[blocca]` — senza questo il brief costringerebbe l'esecutore a scegliere o a indovinare;
   - `[non blocca]` — con il motivo per cui si parte lo stesso;
   - `[aperta]` — con `→` e il fatto che la sblocca (un fatto o un evento, non una data).
   La sezione non può essere vuota: se non trovi niente, non hai cercato abbastanza.
2. **I fatti si cercano, non si chiedono e non si suppongono.** Se un fatto si può trovare (documentazione,
   codice, prezzi, limiti), programma una ricerca con un agente: domanda precisa, chi la fa (di solito un
   agente leggero), cosa deve riportare. Ogni fonte nella sezione «Ricerche» porta un segno:
   - `(A)` primaria e verificata: documentazione ufficiale, codice, dato misurato da noi;
   - `(M)` seria ma di seconda mano: articolo tecnico, issue con conferma, risposta citata;
   - `(B)` non verificata: forum, blog, memoria del modello.
   Una decisione che poggia solo su fonti `(B)` ha stima bassa.
3. **Le incognite restano aperte con il loro sblocco.** Non inventare una risposta per chiuderle. Se
   un'incognita impedisce di scrivere il «finito», diventa `[blocca]`.
4. **Le soluzioni hanno una stima.** Proponi la soluzione con `Stima: alta | media | bassa`, `Perché:` e
   `Cambia se:` (il fatto che la cambierebbe). Le alternative scartate stanno in una riga ciascuna.
5. **Premortem: immagina che sia già andata male e ragiona a ritroso.** Prima di chiudere la scheda
   scrivi almeno tre esiti sbagliati concreti (consegna sbagliata, falso «finito», quota o soldi spesi
   per niente, dati o PROD toccati, agenti che si pestano i piedi). Per ognuno risali alla causa e al
   controllo che manca, poi scegli: un controllo nel «finito» o nelle prove, oppure una voce in
   «Mancanze e incognite» con il suo segno. Separa fatti, deduzioni e incognite. Per R1 bastano
   tre righe; da R2 ogni esito ha anche come lo si scopre e come si torna indietro.

Le scelte tecniche le fai tu (decisione `0012`): a Matteo chiedi solo ciò che può giudicare lui (valore,
utenti, soldi, produzione: criteri 1, 2, 4, 5, 17). Una domanda rimandata «per sicurezza» è lavoro non fatto.

## Procedura

1. Leggi `<memory>/wiki/metodo/criteri-di-progetto.md` (livelli e criteri) e, se c'è, lo `STATO.md` del
   progetto. Nient'altro della memoria, salvo che il compito lo chieda.
2. Copia `scheda-modello.md` (stessa cartella di questa skill) in
   `<repo progetto>/schede/AAAA-MM-GG-<argomento>.md`. Una scheda per lavoro.
3. Decidi il livello R1/R2/R3 e scrivilo con il motivo; nel dubbio si sale.
4. Ragiona con Matteo con le cinque regole, aggiornando la scheda mentre procedi. Lancia le ricerche
   quando servono, senza aspettare la fine.
5. Compila i criteri del livello. I numeri e i nomi delle sezioni sono quelli della pagina dei criteri:
   - R1: 1, 6, 7, 8, 9, 11, 15;
   - R2: in più 3, 4, 5, 12, 13, 14, 16 (scritto), e 2 se `Inizio progetto: sì`;
   - R3: in più 2, 17, e 16 con il comando che prova il ritorno indietro;
   - 10 se `Agenti in parallelo` è più di 1.
   Il criterio 6 ha sempre un comando tra backtick e cosa «deve uscire».
6. Controlla: `python <memory>/strumenti/controlla_scheda.py <scheda>`
   (dove `python` manca: `sh <memory>/strumenti/controlla-scheda.sh <scheda>`).
   Finché esce con errori **non scrivere il brief**: correggi la scheda o torna a ragionare con Matteo.
   Una mancanza `[blocca]` fa fallire il controllo: si risolve, o si declassa scrivendo perché.
7. La prima volta in quella repo installa il blocco al commit:
   `sh <memory>/strumenti/installa-hook-scheda.sh <repo progetto>`, ma **non** se la repo ha
   `core.hooksPath` su una cartella tracciata (es. `.husky`): la riga col percorso di questo PC
   bloccherebbe i commit nel cloud. Lì si lancia il controllo a mano (passo 6). Poi commit locale
   della scheda; push solo con l'OK di Matteo in chat.
8. Scrivi il brief in chat, pronto da incollare nella chat dell'esecutore. Prima rileggilo come se fossi
   l'esecutore (criterio 7): se deve scegliere qualcosa che non è scritto, torna alla scheda.

## Formato del brief

```
<Lavoro> — livello Rx. Scheda: <repo>/schede/<file>.md
Leggi solo: <file, in ordine>
Fai: <cosa, in passi se servono>
Confini: sempre <…>; chiedi <…>; mai <…>
Finito quando: `<comando>` → <cosa deve uscire>
Prova nell'app: <la fa l'agente con l'account di prova | la fa Matteo, perché …>
Aperto: <aperta → fatto che la sblocca>, oppure «niente»
A fine chat: «chiudi».
Decide <modello della chat di ragionamento>, esegue <modello dell'esecutore>.
```

Il brief non ripete la scheda: prende solo ciò che serve all'esecutore. Di solito decide Opus ed esegue
Sonnet.

## Prova nell'app (regola di Matteo, 22/10/2026)

La navigazione nell'app la fanno gli agenti, sull'anteprima collegata al DB di test e con l'account di
prova della repo (dove sta lo dice la repo; in una cartella di lavoro separata il file va copiato dalla
principale). Nella scheda (criterio 11) si stima se costa troppo: allora la fa Matteo. In quel caso la PR
ha la sezione «Prova per Matteo»: link completi e cliccabili, un passo per riga, cosa deve vedere,
nessun sottinteso («gira il telefono», non «guarda in orizzontale»).
