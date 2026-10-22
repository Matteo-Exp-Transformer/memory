# Scheda — esporta le prenotazioni in CSV
Progetto: esempio-app
Data: 2026-10-22
Inizio progetto: no
Agenti in parallelo: 1

## Mancanze e incognite
- [non blocca] il nome del file esportato — si parte con `prenotazioni-AAAA-MM-GG.csv`, rinominarlo costa una riga
- [non blocca] prenotazioni cancellate — restano fuori dall'export, si aggiungono dopo se servono
- [aperta] separatore che il commercialista apre senza errori in Excel italiano → prova con il file vero del commercialista

## Ricerche
- Excel italiano apre un CSV con la virgola? — agente leggero (Haiku) — no, usa il punto e virgola; serve la codifica UTF-8 con BOM per gli accenti — fonti: documentazione Microsoft sul formato CSV (A)
- Libreria standard Python basta per scrivere il CSV? — agente leggero (Haiku) — sì, il modulo csv gestisce virgolette e a capo — fonti: documentazione Python del modulo csv (A)
- Come lo fanno altri gestionali di prenotazioni — agente leggero (Haiku) — quasi tutti esportano con punto e virgola in Italia — fonti: due post di forum (B)

## Soluzione
Una funzione `esporta_csv` in un file nuovo `esporta.py` che legge le prenotazioni dal database e scrive il CSV con punto e virgola e UTF-8 con BOM. Un comando da riga di comando la lancia. Nessun file esistente cambia, salvo la riga che registra il comando.
Scartata: esportare da un foglio Google — richiede credenziali e rete.
Scartata: aggiungere un pulsante nell'interfaccia — fetta troppo grande per ora.
Stima: media
Perché: il formato è confermato da fonti primarie (A); il separatore giusto per Excel del commercialista non è ancora provato su un suo file.
Cambia se: il file del commercialista non si apre bene con il punto e virgola.

## 1 Valore
Il titolare oggi copia a mano le prenotazioni del mese in un foglio per il commercialista, circa 20 minuti. Se non lo faccio se ne accorge il commercialista, che riceve il foglio in ritardo.

## 3 Fattibilità
Il pezzo incerto è solo il separatore in Excel italiano; si prova con un file di esempio prima di consegnare.

## 4 Sostenibilità
Costo al mese zero: gira in locale con la libreria standard. Nessun obbligo nuovo, i dati restano sul computer del titolare.

## 5 Usabilità
Il titolare lancia un solo comando con il mese e apre il file con doppio clic; la prova la fa lui sul suo computer con un mese vero.

## 6 Finito verificabile
`python esporta.py --mese 2026-09 --prova` → deve uscire: un file `prenotazioni-2026-09.csv` con la riga di intestazione e una riga per ogni prenotazione del mese di prova, e il messaggio «esportate N prenotazioni».

## 7 Brief senza decisioni
L'esecutore potrebbe scegliere il separatore, la codifica e il nome del file: sono già scelti (punto e virgola, UTF-8 con BOM, `prenotazioni-AAAA-MM.csv`).

## 8 Fetta piccola
Si chiude in una sessione: un file nuovo di circa 60 righe e un test; il diff si legge in 10 minuti.

## 9 Confini
Sempre: scrivere solo `esporta.py` e il suo test · Chiedi: se serve cambiare lo schema del database · Mai: toccare i dati reali o la cartella dei backup

## 11 Costo d'uso
Budget di una sessione con Sonnet, circa 150.000 token letti; il consumo si registra nella nota di fine chat.

## 12 Aggiungere senza cancellare
Il codice nuovo sta in un file nuovo; i test già presenti devono passare senza essere modificati.

## 13 Leggibile in poco contesto
Un agente nuovo capisce l'export leggendo `esporta.py` e il suo test, due file; il CLAUDE.md del progetto resta sotto 200 righe.

## 14 Niente duplicati
Prima di scrivere, l'esecutore cerca nel progetto funzioni che già scrivono file CSV o esportano prenotazioni; se ne trova una la riusa.

## 15 Sicurezza
Nessuna chiave nel codice. Il file esportato contiene nomi e telefoni dei clienti: resta nella cartella locale del titolare e non viene caricato in rete.

## 16 Reversibilità
Se va storto basta cancellare `esporta.py` e il suo test: nessun dato esistente viene modificato, l'export legge soltanto.
