# Palestra — stato
Aggiornato: 2026-10-25 (sera: menù «Lezioni archiviate»)

## Dove siamo
- Pagina costruita e pubblicata: `palestra/pagina/palestra.html`, url https://claude.ai/artifact/WRiA3GcF23P1FgeZwAdyZs (privata: la apri solo tu finché non la condividi).
- Test `python palestra/test/prova_pagina.py` → TUTTO OK (17 controlli), 2026-10-25, anche dopo i ritocchi grafici.
- Screenshot a 390×844, chiaro e scuro, guardati: Home, duello, cronometro in corsa, Fascicolo, Sensore.
- Nuovo: menù «Lezioni archiviate» (da completare / completate, riprendi e rileggi). Test `python palestra/test/prova_lezioni.py` → LEZIONI OK; `prova_pagina.py` ancora TUTTO OK (17).
- Nuovo: durante una seduta, «Rivedi i passi già fatti» mostra in sola lettura le risposte dei passi precedenti, senza perdere il passo in corso.
- Database della pagina: 3 cartucce caricate e verificate con `list` (u1-ripasso-collo-di-bottiglia, missione-cronometro-bar, campo-code-ovunque); `sedute` vuota (normale).

## Cosa funziona
- Tutti i tipi di blocco, fiducia, rivelazione, correzioni, fine seduta, «Copia risultati».
- Cronometro con previsione collegata, wake lock e bozza; Scale, Sensore, Fascicolo, Quaderno, modalità ripresa.
- Archivio a tre livelli (db di claude.ai, locale, memoria) e importazione con le stesse regole del validatore Python.

## Decisioni prese dall'esecutore (non sono domande)
- La previsione collegata al cronometro si confronta sempre in secondi, come nell'esempio della specifica.
- Nessun font esterno: solo caratteri di sistema (nessun rischio di blocco senza rete).
- «Importa» accetta anche il JSON dentro un blocco di codice (```json), utile con ChatGPT.
- «Da rivedere» e «Togli riga» non cancellano dati salvati: la prima è un segno, la seconda toglie una riga del modello in costruzione.

## Dubbi per Matteo
- Aperto (dipende da un fatto non disponibile): la pagina è provata solo con un finto database; il primo uso vero sul telefono dirà se il db di claude.ai risponde come previsto.

## Modifiche al test
- Nessuna modifica ai controlli esistenti. Aggiunto il file nuovo `test/prova_lezioni.py`.
