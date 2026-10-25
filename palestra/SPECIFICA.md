# La Palestra — specifica della pagina

Una sola pagina HTML (`palestra/pagina/palestra.html`), pubblicata come artefatto su claude.ai.
Si usa **soprattutto dal telefono**. Il formato degli esercizi (cartucce) è in `CARTUCCE.md`.
Il test automatico `test/prova_pagina.py` controlla questa specifica: gli attributi `data-testid`
elencati qui sono **obbligatori e con questi nomi esatti**.

## 1. Vincoli tecnici (non negoziabili)

1. **Un file solo**: HTML, CSS e JavaScript nello stesso file. Niente framework, niente build, niente
   librerie esterne (eccetto, se vuoi, un font da Google Fonts). JavaScript semplice (ES2020), niente moduli.
2. **Il calcolatore** `motore/espressioni.js` va copiato **tale e quale** in un `<script>` prima del codice
   della pagina. Mai usare `eval`, `new Function`, `innerHTML` con testi delle cartucce o di Matteo
   (usa `textContent`): le cartucce arrivano anche da altri modelli e vanno trattate come dati.
3. **Telefono prima**: larghezza 360–430 px, margini laterali 16 px, nessuno scorrimento orizzontale,
   pulsanti alti almeno 44 px, testo almeno 16 px nei campi (iOS non zooma). Funziona anche su PC.
4. **Tema chiaro e scuro**: colori come variabili su `:root`; scuro sotto
   `@media (prefers-color-scheme: dark)` con `:root:not([data-theme="light"])`, e di nuovo sotto
   `:root[data-theme="dark"]`. `body` ha uno sfondo esplicito.
5. **`<title>La Palestra</title>`**.
6. Niente `alert`, `confirm`, `prompt`.
7. Esponi per i test: `window.Palestra = { valida, adesso, Archivio }` (vedi sotto). `valida(oggetto)`
   restituisce la lista degli errori (vuota = valida) con **le stesse regole** di
   `strumenti/valida_cartuccia.py`: il test confronta i due su cartucce buone e rotte.
   Anche `window.Espressioni` resta globale (lo definisce il calcolatore).
8. **Una vista alla volta nel DOM.** Le viste non attive e i blocchi già giocati vanno **tolti** dal DOM
   (non solo nascosti): ogni `data-testid` compare una sola volta in pagina. Fa eccezione solo la barra
   di navigazione, sempre presente.

## 2. L'archivio (dove si salvano i dati)

All'avvio la pagina si disegna subito e mostra `banner-archivio` con «Collegamento all'archivio…».
Poi:

- se `window.claude` esiste e ha `use`, fa `const db = await window.claude.use("db")`;
- se `db` non è `null` → archivio **db**; altrimenti → archivio **locale** (`localStorage`, chiave
  `palestra:v1`, un oggetto `{ "<collezione>": { "<id>": { ...corpo } } }`);
- se anche `localStorage` lancia errori → archivio **memoria** (solo variabili, perso alla chiusura).

`banner-archivio` riceve l'attributo `data-backend="db" | "locale" | "memoria"` e un testo chiaro:
db = «Archivio su claude.ai: Claude può leggere i tuoi risultati»; locale = «Solo su questo dispositivo:
per il debrief usa "Copia risultati"»; memoria = «Attenzione: i dati si perdono chiudendo la pagina».

`window.Palestra.Archivio` ha esattamente questi metodi (tutti restituiscono Promise):

| Metodo | Cosa fa |
|---|---|
| `leggiTutti(collezione)` | lista di `{ id, ...corpo }` |
| `leggi(collezione, id)` | corpo o `null` |
| `scrivi(collezione, id, corpo)` | scrive il documento intero |
| `tipo` | proprietà: `"db"`, `"locale"` o `"memoria"` |

Regole per il db (dalla documentazione della piattaforma, `db.d.ts`):
- usa **solo** `db.collection(nome).doc(id).set(corpo)`, `.get()` (→ `snap.exists`, `snap.data()`),
  `db.collection(nome).get()` (→ `snap.docs`) e `db.collection("cartucce").onSnapshot(next, errore)`;
- **niente** `where`, `orderBy`, `limit`, `update`, `delete`: le collezioni sono piccole, filtra in JS;
- una scrittura alla volta per documento (accoda e attendi); mai scrivere dal rendering o da un timer;
- iscriviti **una volta sola** a `cartucce` all'avvio (così le cartucce caricate dagli agenti compaiono
  da sole); le altre collezioni si leggono con `get()` quando apri una vista;
- errori: `unavailable` → riprova una volta dopo 1–2 s; `quota_exceeded` → messaggio a Matteo;
  altri → messaggio breve in `banner-archivio`, la pagina continua a funzionare.
- **La pagina non cancella mai nulla**, in nessun archivio.

### Le collezioni

| Collezione | id del documento | Corpo |
|---|---|---|
| `cartucce` | id della cartuccia | la cartuccia JSON così com'è |
| `sedute` | `<idCartuccia>__<AAAAMMGG-HHMMSS>` (ora locale di inizio) | `{cartuccia, versione, titolo, zona, inizio, fine, finito_condizione, finito_esito, blocchi}` |
| `ripassi` | `<idCartuccia>__<idBlocco>__<idCarta>` | `{cartuccia, blocco, carta, fronte, retro, passo, prossima, storia}` |
| `fascicolo` | `<idCartuccia>__<idVoce>` oppure `mia-<AAAAMMGG-HHMMSS>` | `{testo, colonna, prova, origine, creata, aggiornata, segnata, storia}` |
| `quaderno` | `q-<AAAAMMGG-HHMMSS>-<3 cifre a caso>` | `{tipo, materia, testo, termine_tecnico, creata}` |
| `misure` | `<idSeduta>__<idBlocco>` | `{cartuccia, seduta, blocco, fasi, tocchi, giri, media_giro_ms, completa, nota, quando}` |
| `correzioni` | `c-<AAAAMMGG-HHMMSS>-<3 cifre a caso>` | `{cartuccia, versione, blocco, testo, quando}` |

Dettagli:
- `inizio`, `fine`, `quando`, `creata`, `aggiornata`: testo ISO 8601 (`adesso().toISOString()`).
- `sedute.blocchi`: oggetto `{ "<idBlocco>": { tipo, risposta, fiducia, esito, quando } }`.
  `fiducia` 1–5 o `null`. `esito`: `"giusto"`, `"sbagliato"`, `"aperto"` (duello senza migliore),
  `"in_attesa"` (previsione senza misura completa) oppure `null` (blocchi senza esito).
  `risposta` dipende dal tipo: stima/previsione → numero; scelta → id; duello →
  `{opzione, motivo, ribalta}`; ordina → lista di id; simulatore → `{parametri: {id: valore}}`;
  mio_modello → `{righe: [{nome, valore}], uscite: {id: numero}}`; spiega/aperta → testo;
  carte → `{idCarta: "si"|"quasi"|"no"}`; cronometro → id del documento in `misure`;
  fascicolo → `{idVoce: colonna}`; racconto → `null`.
- La seduta si scrive all'inizio (`fine: null`) e di nuovo **dopo ogni blocco completato** (documento intero).
- `finito_esito`: `"si"`, `"no"` o `null`.
- `fascicolo.colonna`: `1` = «Posso provarlo», `2` = «Lo spiego, non lo provo», `3` = «Non lo so ancora».
  `prova`: `{tipo: "misura"|"ripasso_distanza"|"artefatto", testo}` oppure `null`. `origine`: id della
  cartuccia o `"mia"`. `storia`: lista `{data, colonna}`.
- `ripassi.passo` 0–3, `prossima` `"AAAA-MM-GG"` (data locale), `storia` lista `{data, voto}`.
- `misure.tocchi`: lista `{fase, ms}` (ms dall'avvio); `giri`: lista `{totale_ms, fasi: {nomeFase: ms}}`.

## 3. Il tempo

`window.Palestra.adesso()` = `window.__PALESTRA_ORA ? new Date(window.__PALESTRA_ORA) : new Date()`.
**Ogni** lettura dell'ora passa da qui (date delle sedute, scadenze delle Scale, modalità ripresa).
Le date `"AAAA-MM-GG"` sono **locali** (non UTC). Ogni vista ricalcola l'ora quando viene aperta.

**Modalità ripresa** (regola di Matteo: dopo l'una solo brevi riprese): se l'ora locale è tra 01:00 e
05:59, la Home mostra `banner-ripresa` («È passata l'una: solo Scale, al massimo 5 carte»); i pulsanti
`apri-<id>` sono disabilitati; le Scale mostrano al massimo 5 carte. Il pulsante `btn-ripresa-ignora`
(«Ho deciso io: è urgente») toglie il blocco fino al ricaricamento della pagina.

## 4. Navigazione

Barra fissa in basso (comoda col pollice) con 5 voci: `nav-home` (Palestra), `nav-scale` (Scale),
`nav-sensore` (Sensore), `nav-fascicolo` (Fascicolo), `nav-quaderno` (Quaderno). Una vista alla volta.
Durante una seduta la barra resta; uscire dalla seduta la lascia salvata fin dove era arrivata
(modifica del 25/10/2026, su richiesta di Matteo: una seduta lasciata a metà si può riprendere dal menù «Lezioni archiviate», vedi sotto).

**Lezioni archiviate** (aggiunta 25/10/2026). Pulsante `btn-lezioni` nella Home. Elenca le sedute in due sezioni:
`lezioni-da-completare` (seduta con `fine` vuoto) e `lezioni-completate` (con `fine`). Ogni seduta è `lezione-<idSeduta>`.
- Da completare: `riprendi-<idSeduta>` riparte dal primo blocco non ancora completato, sullo stesso documento (nessun duplicato).
  Le risposte a un blocco non ancora confermato non erano salvate e si rifanno.
- Completate: `consulta-<idSeduta>` apre la lettura (risposte, fiducia, esito) con «Copia risultati».
- Se la cartuccia non c'è più o non è valida, il pulsante è disattivato; se ha cambiato versione, la scheda lo dice.
- La Home segnala sulla cartuccia quante lezioni ha da completare. Nessun dato viene cancellato.
- Prova: `test/prova_lezioni.py` (aggiunta, non tocca `prova_pagina.py`).

## 5. Home

- `banner-archivio` (vedi sopra), `banner-ripresa` (solo in ripresa).
- `conta-scale-oggi`: numero di carte delle Scale in scadenza oggi o prima (solo il numero come testo).
- `lista-cartucce`: un elemento `cartuccia-<id>` per cartuccia, con `data-valida="si"|"no"` e
  `data-zona="banco"|"campo"`; mostra titolo, zona («Banco» / «Campo giochi»), durata, data dell'ultima
  seduta. Pulsante `apri-<id>`. Senza cartucce, `lista-cartucce` contiene il testo «Nessuna cartuccia:
  importane una o chiedi a Claude di caricarla» (così è visibile anche vuota). Una cartuccia non valida (controllata con `valida`) mostra il primo
  errore e il pulsante `apri-<id>` è disabilitato. Ordine: le non ancora giocate prima, poi per data.
- `btn-importa` apre il pannello di importazione (se è già aperto resta aperto e svuota il campo):
  `campo-importa` (textarea), `btn-importa-conferma`, `esito-importa` con `data-esito="ok"|"errore"` e il
  testo degli errori (uno per riga). `esito-importa` sparisce quando si riapre il pannello o si cambia il testo.
  Importazione: JSON non leggibile → errore; `valida` con errori → errore; esiste già una cartuccia con
  lo stesso `id` e `versione` maggiore o uguale → errore «Versione già presente: alza "versione"»;
  altrimenti `scrivi("cartucce", id, cartuccia)` → ok e la lista si aggiorna.

## 6. La seduta (il giocatore)

`apri-<id>` apre la schermata di avvio:
- titolo, durata, concetti; campo `seduta-finito` («Ho finito quando…») vuoto, con il segnaposto
  `finito_suggerito` se presente; `btn-inizia`. In zona `banco` `btn-inizia` è disabilitato finché
  `seduta-finito` è vuoto; in zona `campo` è sempre attivo.
- `btn-inizia` crea la seduta, la scrive e mostra il primo blocco.

Un blocco alla volta, dentro un contenitore `blocco` con `data-tipo` e `data-id`. Barra di avanzamento
`seduta-avanzamento` («3 / 9»). Pulsante `btn-avanti`, **disabilitato finché il blocco non è completo**
(regole sotto). Non si torna indietro: una scommessa data non si cambia.

Ogni blocco ha `btn-correggi` («Il gioco sbaglia?») che apre `campo-correzione` e
`btn-correzione-invia`: scrive in `correzioni` e mostra `correzione-ok` («Segnalato: Claude lo vedrà
nel debrief»).

**Fiducia** (componente comune ai tipi stima, scelta, duello, ordina, previsione): cinque pulsanti
`fiducia-1` … `fiducia-5` con `aria-pressed`, etichetta «Quanto sei sicuro?» (1 = tiro a indovinare,
5 = ci scommetto). Poi `btn-conferma`, attivo solo quando la risposta e la fiducia ci sono.
Dopo la conferma gli input si bloccano e compare `rivela` con `data-esito`
(`giusto`/`sbagliato`/`aperto`/`in_attesa`). In zona **banco** `rivela` scrive anche «Giusto» o
«Non ancora»; in zona **campo** non scrive mai giusto/sbagliato (solo «Ecco cosa succede»), ma
`data-esito` c'è lo stesso.

| Tipo | Elementi | Completo quando |
|---|---|---|
| `racconto` | testo | subito |
| `stima` | `stima-valore` (numero, tastiera numerica, accetta la virgola), fiducia, `btn-conferma`; `rivela` mostra la risposta, l'esito e la `spiegazione` | dopo la conferma |
| `scelta` | `opzione-<id>` (pulsanti, uno solo attivo), fiducia, `btn-conferma`; `rivela` mostra la `conseguenza` di **ogni** opzione e la `spiegazione` | dopo la conferma |
| `duello` | `vincoli` in elenco, `opzione-<id>` con il `perche_plausibile` visibile, `duello-motivo` («Perché questa?»), `duello-ribalta` (etichetta = `domanda_ribalta`), fiducia, `btn-conferma` (serve anche testo nei due campi); `rivela` come `scelta` | dopo la conferma |
| `ordina` | `ordina-lista` con figli `ordina-el` (`data-id`), pulsanti `su-<id>` e `giu-<id>`; ordine iniziale: elementi ordinati per `id` alfabetico, e se coincide con quello giusto, al contrario; fiducia, `btn-conferma`; `rivela` mostra l'ordine giusto | dopo la conferma |
| `previsione` | `previsione-valore`, fiducia, `btn-conferma`; `rivela` con `data-esito="in_attesa"` («Il confronto arriva dopo la misura») | dopo la conferma |
| `simulatore` | per parametro: `param-<id>` (`input type=range`), `valore-<id>`; per uscita: `uscita-<id>` = `Espressioni.formatta(valore, decimali)` + unità (errore → «—»); `nota` se presente | subito |
| `mio_modello` | righe `riga-nome-<n>`, `riga-valore-<n>` (n da 0), `btn-aggiungi-riga`, `btn-togli-riga-<n>`; parte da `righe_iniziali`; `uscita-<id>` ricalcolate a ogni modifica con `somma`, `righe` e le costanti | almeno una riga con valore numerico |
| `spiega` | `spiega-testo`; `parola-<i>` per ogni parola chiave con `data-presente="si"|"no"` (contiene la parola, senza maiuscole/minuscole); `conta-frasi` (frasi separate da `.`, `!`, `?`); se supera `max_frasi` avviso, non blocca | testo non vuoto |
| `aperta` | `aperta-testo`, `suggerimento` se presente | testo non vuoto |
| `carte` | `carta-fronte`, `btn-gira`, `carta-retro` (visibile dopo il giro), `voto-si` / `voto-quasi` / `voto-no`, `carte-progresso` («2 / 4») | tutte votate |
| `cronometro` | vedi sotto | dopo `btn-crono-salva` |
| `fascicolo` | per voce: `voce-<chiave>` con `sposta-<chiave>-1/2/3` (vedi §8) | ogni voce ha una colonna |

**Esiti**: stima giusta se `|valore − risposta| ≤ tolleranza`; scelta se l'id = `giusta`; duello
`aperto` se `migliore` è `null`, altrimenti giusto/sbagliato; ordina giusto solo se l'ordine è identico;
previsione `in_attesa` fino alla misura (§7).

**Carte con `ripasso: true`**: dopo il voto di ogni carta, crea (se non esiste) il documento `ripassi`
con `passo: 0`, `prossima` = domani, `storia: [{data: oggi, voto}]`. Se esiste già non lo tocca.

**Fine seduta** (dopo l'ultimo blocco): `fine-seduta` mostra la condizione di finito scritta all'inizio e
chiede «L'hai rispettata?» con `btn-finito-si` / `btn-finito-no`; scrive `fine` e `finito_esito`, poi
mostra `riepilogo`: per ogni blocco con fiducia, fiducia ed esito (fatti, niente complimenti);
`btn-copia-risultati` riempie `testo-risultati` (textarea in sola lettura, sempre visibile dopo il clic)
e prova a copiarlo negli appunti (dentro try/catch; se fallisce scrive «Seleziona e copia a mano»).

**Formato di «Copia risultati»** (testo semplice, per ChatGPT):
```
PALESTRA — <titolo> (<id> v<versione>, zona <zona>)
Seduta: <inizio locale AAAA-MM-GG HH:MM> → <fine>
Ho finito quando: <finito_condizione> — rispettata: <sì/no>
[<idBlocco>] <tipo> · fiducia <n o —> · esito <esito o —>
  risposta: <risposta in testo leggibile>
...
```

## 7. Il cronometro

Elementi: `crono-consegna`, `crono-start` («Via»), un pulsante grande per fase `crono-fase-<i>`
(i = posizione nella lista `fasi`, da 0) con il nome della fase, `crono-fine-giro`, `crono-stop`,
`crono-conta-giri` (numero di giri chiusi, solo il numero), `crono-tempo` (tempo che scorre),
`crono-giri` (elenco dei giri: totale e tempo per fase), `crono-nota`, `btn-crono-salva`.

- `crono-start` avvia; i pulsanti di fase e `crono-fine-giro` si attivano. Ogni tocco registra
  `{fase, ms}` (ms dall'avvio, da `performance.now()`). La durata di una fase = tempo dal tocco precedente
  (o dall'inizio del giro). Le fasi si possono toccare in qualunque ordine e anche più volte (si sommano).
  `crono-fine-giro` chiude il giro: `totale_ms` = tempo dalla fine del giro precedente (o dall'avvio).
- `crono-stop` ferma. `btn-crono-salva` (attivo dopo lo stop) scrive `misure` con `media_giro_ms`
  (media dei `totale_ms`) e `completa` = giri chiusi ≥ `min_giri`. Con meno giri salva lo stesso e lo dice.
- Mentre gira: prova `navigator.wakeLock.request("screen")` (try/catch) per tenere acceso lo schermo.
- Bozza: a ogni tocco salva la bozza in `localStorage` (try/catch, chiave `palestra:bozza-crono`), così
  un ricaricamento per errore non perde i giri; all'apertura del blocco, se c'è una bozza della stessa
  seduta e blocco, offre `crono-riprendi`.
- **Previsione collegata**: al salvataggio, per ogni blocco `previsione` con `collegata_a` = questo blocco,
  se `completa`: giusto se `|previsione − media_giro_ms/1000| ≤ media_giro_ms/1000 × tolleranza_percento/100`,
  altrimenti sbagliato; aggiorna l'`esito` nella seduta e mostra il confronto in `crono-confronto`
  («Avevi detto 75 s con fiducia 4: misurato 82,3 s»). Se non `completa` resta `in_attesa`.

## 8. Fascicolo (il registro a tre colonne)

Vista `nav-fascicolo`: tre colonne una sotto l'altra sul telefono, `fascicolo-col-1` («Posso provarlo»),
`fascicolo-col-2` («Lo spiego, non lo provo»), `fascicolo-col-3` («Non lo so ancora»). Ogni voce
`voce-<chiave>` (chiave = id del documento) mostra testo, origine, prova, ultima data, e i pulsanti
`sposta-<chiave>-1`, `sposta-<chiave>-2`, `sposta-<chiave>-3`, `btn-segna-<chiave>` («Da rivedere»).

- Spostare in colonna 1 apre `prova-tipo-<chiave>` (select: `misura`, `ripasso_distanza`, `artefatto`) e
  `prova-testo-<chiave>` con `prova-conferma-<chiave>`. Con il testo vuoto mostra
  `errore-prova-<chiave>` («Serve una prova: una misura, un ripasso a distanza superato o un tuo
  artefatto») e **non** sposta. Testo sotto: «Una stima, anche tua, sta in "Lo spiego, non lo provo"».
- Spostare in 2 o 3 è immediato e azzera `prova`. Ogni spostamento aggiunge a `storia`.
- **Nessun pulsante elimina.** «Da rivedere» mette solo `segnata: true/false`.
- `fascicolo-nuova-testo` + `fascicolo-nuova-aggiungi` aggiungono una voce mia in colonna 3.
- `btn-copia-fascicolo` riempie `testo-fascicolo` con le sole voci in colonna 1 e la loro prova (per
  colloqui) e prova a copiarlo.
- Nel blocco `fascicolo` di una seduta si usa lo stesso componente, **con gli stessi `data-testid`**
  (`fascicolo-col-1/2/3`, `voce-…`, `sposta-…`, `prova-…`, `errore-prova-…`), limitato alle voci della
  cartuccia (chiave `<idCartuccia>__<idVoce>`). Una voce nuova parte fuori dalle colonne, in un elenco
  «Da sistemare»; se esiste già nel fascicolo parte dalla sua colonna attuale. Senza `btn-copia-fascicolo`
  e senza voce nuova.

## 9. Scale (il ripasso quotidiano)

Vista `nav-scale`: le carte di `ripassi` con `prossima` ≤ oggi, una alla volta (in ripresa al massimo 5):
`scala-fronte`, `scala-gira`, `scala-retro`, `scala-si`, `scala-quasi`, `scala-no`, `scala-progresso`.
Nessuna carta → `scala-vuota` («Niente in scadenza oggi»). Intervalli `[1, 3, 7, 14]` giorni:
- `sì`: `passo` = min(passo + 1, 3), `prossima` = oggi + intervallo[passo nuovo];
- `quasi`: passo uguale, `prossima` = domani;
- `no`: `passo` = 0, `prossima` = domani.
Ogni voto aggiunge `{data, voto}` a `storia`. Il conteggio `conta-scale-oggi` della Home si aggiorna.

## 10. Sensore (fiducia contro esito)

Vista `nav-sensore`. Considera **solo** le sedute di zona `banco` e i blocchi con `fiducia` e `esito`
`giusto` o `sbagliato`.
- `sensore-tabella` con 5 righe `sensore-riga-1` … `sensore-riga-5` (`data-tentativi`, `data-giusti`):
  «Fiducia 5 — 3 tentativi, 1 giusto (33%)».
- `sensore-eccesso`: quanti con fiducia ≥ 4 e sbagliati («sicuro e sbagliato»);
  `sensore-difetto`: quanti con fiducia ≤ 2 e giusti («ti sei sottovalutato»). Entrambi con il numero
  anche nell'attributo `data-valore`.
- `sensore-storia`: gli ultimi 20 tentativi, con data, titolo della cartuccia, fiducia, esito. Sono fatti
  con data: niente frasi di incoraggiamento generiche.
- Nessun dato → `sensore-vuoto`.

## 11. Quaderno

Vista `nav-quaderno`: `quaderno-tipo` (select `nota` / `parola`), `quaderno-materia` (testo, con
suggerimenti dalle materie già usate), `quaderno-testo` (la nota, o per una parola: la parola **sua**),
`quaderno-termine` (solo per `parola`: il termine tecnico corrispondente), `quaderno-salva`.
Elenco `quaderno-voce-<id>`, dal più recente, filtrabile per materia con `quaderno-filtro`.
Le parole mostrano «parola tua → termine tecnico». Niente eliminazione.

## 12. Aspetto

Sobrio e caldo, da quaderno di lavoro, non da gioco per bambini. Tipografia leggibile, un colore
d'accento, stati chiari (attivo, bloccato, giusto, non ancora). Animazioni brevi o nessuna.
Rispetta la skill `artifact-design` per tutto ciò che questa specifica non dice.
