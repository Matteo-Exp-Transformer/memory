# Criteri di progetto

> Sources: chat Claude desktop, 2026-10-22
> Raw: [2026-10-22-criteri-di-progetto](../../raw/conversazioni/2026-10-22-criteri-di-progetto.md); [2026-10-22-criteri-di-progetto (nota di fine chat)](../../raw/sessioni/2026-10-22-criteri-di-progetto.md)
> Updated: 2026-10-22

## Overview

I criteri con cui Matteo avvia un progetto da una chat di ragionamento e lo affida ad agenti (Sonnet, Opus). Ogni criterio ha una domanda, chi lo verifica e il livello di rischio da cui è obbligatorio. Decisi da Matteo il 22/10/2026 («Confermo procedi pure»), partendo da ISO 25010, i quattro rischi di Cagan, i suoi due criteri e i criteri pensati per gli agenti (vedi [Definire un progetto](definizione-progetto-e-memoria.md)). Non ancora provati su un progetto.

## Livelli di rischio

- **R1:** lo usa solo Matteo, si annulla con git, nessun dato vero (prototipo, memory, script).
- **R2:** lo usa qualcun altro o tocca dati veri, ma si annulla in minuti senza perdite.
- **R3:** non si annulla del tutto (migrazioni, dati cancellati, messaggi inviati, pagamenti), oppure salute, legge o dati personali, oppure va in produzione.

Il livello lo decide la chat di ragionamento e sta scritto nel brief. Nel dubbio si sale.

## Chi verifica

**Auto** = controllo automatico; **Revisore** = agente in contesto pulito, anche di altro modello; **Matteo** solo dove può giudicare lui: valore, utenti, soldi, produzione (criteri 1, 2, 4, 5, 17). I criteri tecnici non vanno a Matteo, coerente con la decisione `0012` (le scelte tecniche sono degli agenti, vedi [Lavorare con gli agenti](lavorare-con-agenti.md)).

## A. Prima di partire (chat di ragionamento, con Matteo)

| # | Criterio | Domanda | Verifica | Da |
|---|---|---|---|---|
| 1 | Valore (Cagan) | Chi lo usa e cosa smette di fare a mano? Se non lo faccio, chi se ne accorge? | Matteo | R1, una riga |
| 2 | Pre-mortem (Klein) | È fallito fra un mese: perché? | chat + Matteo | R3; R2 a inizio progetto |
| 3 | Fattibilità (Cagan) | Qual è il pezzo che non sappiamo se funziona? Prima un prototipo da buttare? | Revisore, prototipo | R2 |
| 4 | Sostenibilità (Cagan) | Quanto costa al mese e che obblighi porta? | l'agente raccoglie i fatti, decide Matteo; legge → professionista | R2 |
| 5 | Usabilità (Cagan; capacità di interazione ISO) | Una persona del ruolo lo usa sul suo telefono senza spiegazioni? | Matteo con un utente vero | R2 |

## B. Il brief all'agente

| # | Criterio | Domanda | Verifica | Da |
|---|---|---|---|---|
| 6 | Finito verificabile | Con quale comando o prova si vede che è finito, e cosa deve uscire? | Auto, scritto prima del codice | R1 |
| 7 | Brief senza decisioni | L'esecutore deve scegliere qualcosa che non è scritto? | Revisore (chi scrive il brief lo rilegge) | R1 |
| 8 | Fetta piccola | Si chiude in una sessione e il diff si legge in 10 minuti? | Auto (dimensione del diff) | R1 |
| 9 | Confini sempre/chiedi/mai | Cosa fa da solo, cosa chiede, cosa non fa mai? | Auto (permessi negati), altrimenti Revisore | R1 minimi, R2 del progetto |
| 10 | Parallelizzabile (basso accoppiamento) | Due agenti toccano gli stessi file? | Auto (incrocio dei file dei diff) | quando lavora più di un agente |
| 11 | Costo d'uso | Quanti token ha consumato, ne valeva la pena? | Auto, nella nota di fine chat | R1, da registrare |

## C. Il codice

| # | Criterio | Domanda | Verifica | Da |
|---|---|---|---|---|
| 12 | Aggiungere senza cancellare (principio aperto/chiuso) | Per aggiungere questa funzione devo cambiare codice che già funziona? | Auto: i test esistenti passano senza essere stati modificati | R2 |
| 13 | Leggibile in poco contesto | Un agente nuovo capisce questa parte leggendo pochi file? CLAUDE.md sotto 200 righe? | Auto (lunghezze) + Revisore a freddo | R2 |
| 14 | Niente duplicati | Esiste già qualcosa che lo fa? | l'agente cerca prima; Auto (rilevatore di duplicati) | R2 |
| 15 | Sicurezza (ISO) | Chi può leggere o cambiare questi dati? Chiavi nel codice? | Auto (scanner chiavi; regole di accesso al DB) + Revisore | R1 chiavi, R2 il resto |
| 16 | Reversibilità | Se va storto, come torno indietro e cosa perdo? | Auto: ritorno indietro provato | R2 scritto, R3 provato |
| 17 | Produzione (regola di Matteo) | Cambia qualcosa che vedono i clienti? | collaudo a mano di Matteo; l'esecutore non ha credenziali di produzione | R3 |

A R1 i criteri obbligatori sono 7 (1, 6, 7, 8, 9, 11, 15): un lavoro piccolo resta leggero, contro l'errore dell'MSS (troppa struttura prima dell'uso).

## Fuori dalla lista di base

Efficienza e compatibilità (ISO) entrano solo con un requisito misurabile. La flessibilità è coperta dal 12. La safety è una delle condizioni di R3.

## Come sono nati (nota di fine chat del 22/10/2026)

Obiettivo di Matteo: «definire i criteri con cui lavoro ai progetti avviandoli da chat reasoning come questa», per far lavorare Sonnet e Opus «commettendo il minor numero di errori possibili». Sua definizione: ««Parallelizzabile» si chiama basso accoppiamento: pezzi che non si pestano i piedi».

- I tre livelli di rischio non erano definiti da nessuna parte: la ricerca diceva solo «è una costruzione di Matteo». Li ha proposti Claude e Matteo li ha confermati; sono quindi una proposta confermata, non una fonte esterna.
- La prima bozza metteva «Tu a mano» sui criteri tecnici, in contraddizione con la decisione `0012`; è stato spostato su controllo automatico o agente revisore.
- Ha funzionato: leggere solo indice, due pagine di metodo e il raw della ricerca è bastato per proporre tutto in un turno.
- Aperto: i criteri non sono ancora provati su un progetto vero. Dopo questa chat sono diventati la skill `progetta` (vedi [Il ciclo progetta, brief, chiudi](ciclo-progetta-brief-chiudi.md)).

## Manutenzione

I criteri restano fissi. Se ne aggiunge uno solo dopo un errore ripetuto; se ne toglie uno se in 3 progetti non ha mai fermato niente.

## See Also

- [Definire un progetto e tenere la memoria](definizione-progetto-e-memoria.md)
- [Lavorare con gli agenti](lavorare-con-agenti.md)
- [Costi e quota](costi-e-quota.md)
- [Il ciclo progetta, brief, chiudi](ciclo-progetta-brief-chiudi.md)
