# PIANO — costruire la Palestra (per l'agente esecutore, pensato per Sonnet)

Scritto da Claude (claude-opus-5-5) il 2026-10-25 su richiesta di Matteo:
«Scrivi il Plan […] e lascia che sia sonnet a farlo. Lo lancio io. Tu assicurati che non possa sbagliare
a costruirlo.» Lingua di lavoro: italiano, dai del tu a Matteo, frasi semplici, niente gergo non spiegato.

## Cosa costruisci, in una frase

Una pagina web (artefatto su claude.ai, usata soprattutto dal **telefono**) in cui Matteo gioca esercizi
chiamati **cartucce**. Gli agenti caricano le cartucce come dati nel database della pagina. Lui gioca,
la pagina salva, Claude rilegge i risultati e fa il debrief in chat.

## I file che contano (leggili TUTTI prima di scrivere codice, in quest'ordine)

1. `palestra/PIANO.md`: questo file, cioè cosa fare e in che ordine.
2. `palestra/SPECIFICA.md`: come deve comportarsi la pagina, con i `data-testid` obbligatori.
3. `palestra/CARTUCCE.md`: il formato degli esercizi e le regole didattiche.
4. `palestra/motore/espressioni.js`: il calcolatore delle formule, da copiare **tale e quale**.
5. `palestra/strumenti/valida_cartuccia.py`: il validatore. La pagina deve dare gli stessi esiti.
6. `palestra/test/prova_pagina.py`: il test che decide se hai finito.
7. `palestra/cartucce/*.json`: le tre cartucce vere da caricare.

**Non leggere** la repo `psychological-insight` né le pagine della wiki: non servono, costano token e
contengono materiale privato che non deve finire nella pagina.

## Regole che non si discutono

- **Non cambiare** `CARTUCCE.md`, `motore/espressioni.js`, `strumenti/valida_cartuccia.py`, le cartucce
  in `cartucce/`, né le regole di `SPECIFICA.md`. Se pensi che una cosa sia sbagliata, scrivilo in
  `palestra/STATO.md` sotto «Dubbi per Matteo» e vai avanti con quello che c'è scritto.
- **Il test** (`test/prova_pagina.py`) puoi correggerlo **solo** se un suo controllo contraddice
  `SPECIFICA.md` (il test era stato scritto prima che la pagina esistesse). Mai togliere o indebolire un
  controllo per far passare la pagina. Ogni modifica al test va in `STATO.md` sotto «Modifiche al test»,
  con la riga e il motivo citando la frase della specifica.
- **Non aggiungere funzioni** che la specifica non chiede: niente valutazione automatica con l'IA dentro la
  pagina (capability `sample`), niente attività pianificate, niente altre capability oltre a `db`,
  niente librerie esterne, niente login, niente grafici di librerie.
- **Niente cancellazioni**: la pagina non elimina mai dati.
- Repo `memory`: `raw/` è immutabile (si aggiungono solo file nuovi), commit sì, **push solo con l'OK di
  Matteo in chat**. Rispetta `AGENTS.md` della radice.

## Passo 0 — controlla l'ambiente (prima di tutto, 2 minuti)

1. Ti serve il tool **Artifact** (pubblica pagine su claude.ai) e il tool **ArtifactData** (scrive nel
   database di una pagina). Cerca ArtifactData con ToolSearch (`select:ArtifactData`).
   **Se Artifact non c'è, fermati subito**: scrivi in `STATO.md` «Ambiente senza tool Artifact» e di' a
   Matteo, con parole semplici, di rilanciarti da una sessione dell'app Claude in cloud (come quella in cui è
   stato scritto questo piano), con la repo `memory` collegata.
2. `node --version` e `python -c "import playwright"` (nel container cloud usa `python3` se `python`
   manca; Playwright e Chromium ci sono già: **non reinstallarli**). Se Playwright manca davvero:
   `pip install playwright --break-system-packages && python -m playwright install chromium`.
3. Dalla radice della repo: `git config core.hooksPath .githooks`.

## Passo 1 — prova i pezzi già pronti

```
node palestra/motore/prova_espressioni.mjs                      # → tutto ok
python palestra/strumenti/valida_cartuccia.py palestra/cartucce/*.json   # → tre righe OK
python palestra/strumenti/valida_cartuccia.py palestra/test/esempi/non-valida.json   # → NO (è giusto così)
```

Se uno di questi non va come scritto, fermati e scrivilo a Matteo: vuol dire che qualcuno ha toccato i file.

## Passo 2 — carica le skill per gli artefatti

Con il tool Skill: `artifact-design` (obbligatoria prima di scrivere la pagina) e `artifact-capabilities`
(obbligatoria per usare `db`). Leggi in quest'ultima il file `db.d.ts` indicato: la specifica usa solo una
parte di quelle funzioni (vedi SPECIFICA §2).

## Passo 3 — costruisci `palestra/pagina/palestra.html` a tappe

Un file solo. Costruisci a tappe e lancia il test dopo ogni tappa (fallirà sulle parti non ancora fatte:
guarda che il primo errore sia più avanti di prima).

1. **Ossatura**: stili con i colori su `:root` (chiaro/scuro), barra di navigazione in basso, un solo
   contenitore delle viste (una vista alla volta nel DOM), `window.Palestra` con `adesso`, `Archivio`
   (db / locale / memoria) e `valida` (traduzione in JavaScript di `valida_cartuccia.py`: stessi controlli,
   nello stesso ordine). Copia `motore/espressioni.js` tale e quale in un `<script>`.
2. **Home e importazione**: banner dell'archivio, elenco cartucce (con iscrizione unica a `cartucce`),
   pannello «Importa cartuccia».
3. **La seduta**: avvio con la condizione di finito, un blocco alla volta, fiducia, rivelazione, correzioni,
   fine seduta, riepilogo e «Copia risultati». Tutti i tipi di blocco tranne il cronometro.
4. **Cronometro** con previsione collegata, wake lock e bozza.
5. **Scale, Sensore, Fascicolo, Quaderno**, modalità ripresa.
6. **Rifinitura visiva** secondo `artifact-design`: telefono prima, pulsanti grandi, stati chiari.

Consigli pratici:
- Disegna ogni vista con una funzione `mostraX()` che svuota il contenitore e lo ricrea; costruisci gli
  elementi con `document.createElement` e `textContent`.
- Tieni lo stato della seduta in un oggetto; dopo ogni blocco completato scrivi la seduta intera.
- Le scritture vanno in coda: una alla volta, aspettando la precedente.
- Le date `AAAA-MM-GG` sono locali: costruiscile con `getFullYear/getMonth/getDate`, non con `toISOString`.

## Passo 4 — il test deve passare

```
python palestra/test/prova_pagina.py      # → TUTTO OK (N controlli)
```

Non andare avanti finché non stampa `TUTTO OK`. Se un errore sembra un difetto del test, rileggi la frase
della specifica: quasi sempre è la pagina a sbagliare. Vale la regola sul test scritta sopra.

## Passo 5 — guarda la pagina con i tuoi occhi

Fai screenshot con Playwright a 390×844, in tema chiaro e scuro, di: Home con le 3 cartucce importate, un
blocco `duello`, il cronometro mentre gira, il Fascicolo, il Sensore. Aprili con Read e correggi ciò che è
brutto, illeggibile, troppo piccolo per un pollice o che esce dallo schermo. Poi rilancia il test.

## Passo 6 — pubblica

1. Segui le istruzioni del tool Artifact per una pagina nuova (se chiede prima `quickstart`, usa
   `intent: "other"`: è una piccola app costruita a mano, non un tipo pronto).
2. Pubblica `palestra/pagina/palestra.html` con `capabilities: {"db": {}}`, `icon: "dumbbell"`,
   descrizione: «Palestra personale di Matteo: esercizi caricati dagli agenti, da giocare dal telefono».
3. Carica le tre cartucce con **una** chiamata `ArtifactData` `batch`: tre `set` nella collezione
   `cartucce`, `doc_id` = id della cartuccia, `data` = il contenuto del file JSON.
4. Verifica: `ArtifactData` `list` della collezione `cartucce` → 3 documenti con gli id giusti.
   Poi un `list` di `sedute` (vuoto: è normale). Non giocare tu le cartucce sulla pagina vera.

## Passo 7 — chiudi

1. Riscrivi `palestra/STATO.md` (massimo 40 righe, riga 2 `Aggiornato: AAAA-MM-GG`): url della pagina,
   esito del test, cosa funziona, «Dubbi per Matteo», «Modifiche al test».
2. Nota di fine chat in `raw/sessioni/AAAA-MM-GG-palestra-costruzione.md` secondo `AGENTS.md` (massimo 20
   righe, con le righe «- **Costo:**» con i numeri di `python strumenti/costo_sessione.py` e
   «- **Letti:**»).
3. `git add palestra raw/sessioni/<la tua nota>` e commit con un messaggio chiaro. **Non fare push**:
   chiedi l'OK a Matteo.
4. Scrivi a Matteo, corto e semplice:
   - la pagina è pronta (la card col link la vede già);
   - da dove partire: «Ripasso a distanza — il picco al bancone» oggi; «Missione sul campo» al bar
     questa settimana, col telefono appoggiato; il «Campo giochi» quando ha voglia di esplorare;
   - per il debrief basta scrivere a Claude «debrief Palestra» con il link;
   - con ChatGPT: incolla la cartuccia in «Importa» e i risultati con «Copia risultati»;
   - la soglia scelta da lui: almeno 6–7 ripassi a distanza in 14 giorni, altrimenti la Palestra si spegne
     e si torna agli artefatti singoli;
   - chiedi l'OK per il push.

## Quando hai finito (tutte vere)

- [ ] `prova_pagina.py` stampa `TUTTO OK`
- [ ] screenshot guardati a 390 px, chiaro e scuro, e difetti corretti
- [ ] pagina pubblicata con `db`, tre cartucce nel database (verificato con `list`)
- [ ] `STATO.md` e nota di sessione scritti, commit fatto, push non fatto
- [ ] nessun file vietato modificato (`git diff --stat` lo mostra)
