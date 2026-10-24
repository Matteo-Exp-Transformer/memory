# Cartucce della Palestra — formato e regole per chi le scrive

Una **cartuccia** è un esercizio scritto come dati (JSON), non come pagina. La Palestra è la console fissa
che la gioca. Chi la scrive (Claude, ChatGPT, Codex, un altro modello) produce **solo il JSON**.

Prima di caricarla, controllala sempre:

```
python palestra/strumenti/valida_cartuccia.py palestra/cartucce/<id>.json
```

Deve stampare `OK`. Se stampa `NO`, correggi e rilancia. Non caricare mai una cartuccia `NO`.

## 1. Regole didattiche (perché esiste la Palestra)

Vengono dalla wiki di `memory` (`wiki/persona/come-apprende.md`, `lettura-non-verbale.md`,
`difetto-chiave-e-forze.md`) e dalle richieste di Matteo. Valgono per ogni cartuccia.

1. **Pochi concetti per volta** (1–4 in `concetti`). Più profondità nella decisione, non più nozioni.
2. **Varia la forma.** Non ripetere la stessa sequenza di tipi dell'ultima cartuccia: leggi l'elenco
   delle cartucce già caricate e cambia ordine, tipi e ambientazione. Matteo: «permettiamo cartucce
   variabili, non sempre tutto ripetitivo».
3. **Porta i concetti fuori dalla ristorazione.** Ogni cartuccia `banco` deve avere blocchi in almeno
   **2 domini** (il validatore lo controlla). Usa la vita quotidiana, lo sport, la musica, la sanità,
   i trasporti, la burocrazia, i giochi, le storie di persone. Matteo: «agenti devono potermi trasportare
   concetti anche in casi di vita reale o che non c'entrano con la ristorazione. Anche esempi umani».
4. **Esempi umani inventati o pubblici, mai privati.** Personaggi inventati (es. «la dottoressa Ferri») o
   fatti pubblici (un pit stop di Formula 1). **Mai** materiale della repo `psychological-insight`, della
   vita privata di Matteo, della sua relazione o della sua famiglia: la Palestra è una pagina condivisibile.
5. **Niente domande ovvie.** Un `duello` mette in competizione opzioni **tutte plausibili**
   (`perche_plausibile` obbligatorio), dentro **vincoli** concreti (budget, tempo, persone), con dati
   incompleti. Matteo ha bocciato «lo consigli per tutte le pasticcerie?» come «ovvio che no».
   Se una opzione è chiaramente sbagliata, non è un duello: è una `scelta`.
6. **Il concetto si consegna come mossa.** Le carte dicono una cosa da fare domani («Prima di dire X, fai
   Y»), non una definizione astratta. Le distinzioni si perdono, le mosse restano.
7. **Chi dà torto è un numero.** Le `conseguenza` e le `spiegazione` descrivono cosa succede, con i conti.
   Niente «Bravo!» e niente rimproveri.
8. **Onestà sui numeri.** Se un numero è una stima, dillo nel testo. Se un modello è semplificato (es. la
   coda carico ÷ (1 − carico)), dillo. Ricontrolla ogni conto due volte prima di scriverlo.
9. **Fiducia prima della risposta.** I tipi `stima`, `scelta`, `duello`, `ordina`, `previsione` chiedono
   la fiducia da 1 a 5: almeno uno di questi è obbligatorio in una cartuccia `banco`.
10. **Due zone.** `campo` = esplorazione, nessun voto, serve a toccare un tema nuovo. `banco` = si misura.
    Un tema passa al banco quando ha acceso Matteo due volte.
11. **La spiegazione scritta la valuta l'agente in chat.** Le `parole_chiave` di `spiega` si accendono ma
    non danno punteggio.

## 2. Il formato (versione 1)

Campi sconosciuti = errore: il validatore è severo apposta, così un refuso non passa.
Gli `id` usano solo minuscole, cifre e trattini, da 2 a 60 caratteri (es. `u1-ripasso`).

### Radice

| Campo | Tipo | Note |
|---|---|---|
| `formato` | `1` | sempre 1 |
| `id` | testo | unico; non riusarlo per un'altra cartuccia |
| `versione` | intero ≥ 1 | per correggere una cartuccia già caricata alza la versione |
| `titolo` | testo | |
| `zona` | `"banco"` o `"campo"` | |
| `creata` | `"AAAA-MM-GG"` | |
| `autore` | testo | es. `"ChatGPT (GPT-6)"`, `"Claude (claude-sonnet-5-5)"` |
| `durata_minuti` | intero 1–120 | |
| `concetti` | lista di `{id, nome}` | almeno 1 |
| `blocchi` | lista di blocchi | da 1 a 25, giocati in ordine |
| `finito_suggerito` | testo, facoltativo | idea per la «condizione di finito»; la pagina NON la precompila |
| `note_per_agenti` | testo, facoltativo | contesto per chi farà il debrief; non viene mostrato |

### Campi comuni a ogni blocco

`id` (unico nella cartuccia), `tipo`, `testo` (obbligatorio), `dominio` (obbligatorio, es. `"ristorazione"`,
`"vita quotidiana"`, `"sport"`), `titolo` (facoltativo), `concetti` (facoltativo, id presi da `concetti`).

### I tipi di blocco

| Tipo | Campi propri | Cosa fa Matteo |
|---|---|---|
| `racconto` | — | legge una storia o un contesto |
| `stima` | `unita` (testo), `risposta` (numero), `tolleranza` (numero ≥ 0), `spiegazione` | scrive un numero + fiducia; giusto se \|valore − risposta\| ≤ tolleranza |
| `scelta` | `opzioni` [{`id`,`testo`,`conseguenza`}] ≥ 2, `giusta` (id), `spiegazione` | sceglie + fiducia |
| `duello` | `vincoli` [testo] ≥ 1, `opzioni` [{`id`,`testo`,`perche_plausibile`,`conseguenza`}] ≥ 2, `migliore` (id o `null`), `domanda_ribalta`, `spiegazione` | sceglie, motiva, scrive cosa gli farebbe cambiare idea, + fiducia. Con `migliore: null` non c'è giusto/sbagliato: valuta l'agente nel debrief |
| `ordina` | `elementi` [{`id`,`testo`}] ≥ 3 **già nell'ordine giusto**, `spiegazione` | rimette in ordine (la pagina li mescola) + fiducia |
| `previsione` | `unita`, `collegata_a` (id di un `cronometro` della stessa cartuccia), `tolleranza_percento` (0–100) | scommette un numero prima di misurare; giusto se entro la tolleranza dalla media dei giri misurati |
| `simulatore` | `parametri` [{`id`,`nome`,`min`,`max`,`passo`,`valore`,`unita`}] ≥ 1, `uscite` [{`id`,`nome`,`formula`,`decimali` 0–4,`unita`}] ≥ 1, `nota` (facoltativa) | muove cursori e guarda i numeri |
| `mio_modello` | `unita_riga`, `uscite` (come sopra), `righe_iniziali` [{`nome`,`valore`}] (facolt.), `costanti` [{`id`,`nome`,`valore`}] (facolt.) | costruisce il suo modello riga per riga (fase + tempo) |
| `spiega` | `parole_chiave` [testo] ≥ 1, `max_frasi` (1–10) | spiega con parole sue |
| `aperta` | `suggerimento` (facoltativo) | risponde per iscritto |
| `carte` | `carte` [{`id`,`fronte`,`retro`}] ≥ 1, `ripasso` (true/false) | gira e si giudica (sì / quasi / no); con `ripasso: true` le carte entrano nelle Scale a 1, 3, 7, 14 giorni |
| `cronometro` | `fasi` [testo] 1–8, `consegna`, `min_giri` (1–20) | misura giri veri toccando le fasi |
| `fascicolo` | `voci` [{`id`,`testo`}] ≥ 1 | mette ogni voce in una delle tre colonne; la colonna 1 vuole una prova |

### Formule (`simulatore`, `mio_modello`)

Linguaggio piccolo e sicuro (niente codice): numeri, variabili, `+ - * / ( )`, confronti
`< <= > >= == !=` (danno 1 o 0), funzioni `min max ceil floor round abs se(cond, a, b)`.
Divisione per zero = ∞. Gli `id` dei parametri e delle costanti sono variabili: solo minuscole, cifre e `_`
(niente trattini). In `mio_modello` ci sono anche `somma` (somma dei valori delle righe) e `righe`
(quante righe). Un'uscita **non** può usare un'altra uscita: riscrivi la formula per intero.

## 3. Come si carica una cartuccia

**Claude (o un agente con il tool ArtifactData) — il modo normale:**
1. Scrivi il file in `palestra/cartucce/<id>.json` e lancia il validatore: deve dare `OK`.
2. Leggi le cartucce già caricate: `ArtifactData` → `list`, collezione `cartucce`, url della Palestra
   (lo trovi in `palestra/STATO.md`). Controlla che il tuo `id` non esista già (o alza `versione`).
3. Carica: `ArtifactData` → `set`, collezione `cartucce`, `doc_id` = id della cartuccia, `data` = il JSON
   intero (oppure `file_path` = il file). La Palestra aperta la mostra da sola.
4. Fai commit del file in `palestra/cartucce/` (push solo con l'OK di Matteo).

**ChatGPT o un modello senza accesso al database:** produci il JSON in un blocco di codice e di' a Matteo
di incollarlo in Palestra → «Importa cartuccia». La pagina lo controlla con le stesse regole.

## 4. Come si fa il debrief

Quando Matteo scrive «debrief Palestra» (o simile):
1. `ArtifactData` → `list` della collezione `sedute` (e, se servono, `fascicolo`, `ripassi`, `misure`,
   `correzioni`). Leggi la cartuccia della seduta per sapere le risposte attese.
2. Valuta **sul significato**: le spiegazioni (`spiega`), le motivazioni dei `duello` e il numero scritto
   in `domanda_ribalta`. Il contatore delle parole non vale come voto.
3. Rispondi in chat: cosa regge, cosa no, con le sue parole tra virgolette. Calibrazione: fiducia contro esito.
4. Le `correzioni` sono segnalazioni di Matteo sul gioco: se ha ragione, prepara la cartuccia con
   `versione` + 1 e dillo.
5. Aggiorna i voti 1–5 in `wiki/carriera/formazione-operations-food-ai.md` solo con prove nuove,
   seguendo le regole della wiki (fonte nuova in `raw/`, mai modificare `raw/`).

ChatGPT riceve gli stessi dati col pulsante «Copia risultati» della pagina: Matteo li incolla in chat.
