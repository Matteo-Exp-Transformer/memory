# Palestra — stato
Aggiornato: 2026-10-25

## Dove siamo
- Piano, specifica, formato delle cartucce, calcolatore, validatore, test e 3 cartucce: scritti da
  Claude (claude-opus-5-5) il 2026-10-25.
- Pagina: **non ancora costruita**. La costruisce Sonnet seguendo `PIANO.md`.
- Url della pagina pubblicata: — (lo scrive l'esecutore).

## Decisioni di Matteo (25/10/2026)
- Soglia: «6 o 7 almeno» ripassi a distanza in 14 giorni; sotto, la Palestra si spegne.
- Cronometro: «Si lo faccio questa settimana al bar».
- Dispositivo: «Soprattutto telefono».
- «Permettiamo cartucce variabili non sempre tutto ripetitivo. Agenti devono potermi trasportare
  concetti anche in casi di vita reale o che non c'entrano con la ristorazione.»

## Controlli già fatti
- `node motore/prova_espressioni.mjs` → tutto ok.
- `valida_cartuccia.py` → le 3 cartucce OK, `test/esempi/non-valida.json` NO (atteso).
- `test/prova_pagina.py`: scritto ma mai eseguito su una pagina vera (la pagina non esiste ancora).

## Dubbi per Matteo
- (nessuno)

## Modifiche al test
- (nessuna)
