# Criteri di progetto: proposta di Claude e decisione di Matteo

> Source: chat Claude desktop (Code) del 22/10/2026 sul PC di Matteo, Opus 5.5
> Collected: 2026-10-22
> Published: 2026-10-22

Data della decisione: 2026-10-22.

## La richiesta di Matteo (alla lettera)

«Chat 1, i criteri. Per ogni criterio decidi tre cose: la domanda da porsi (es. «se aggiungo una funzione, devo cancellare codice?»); come si verifica: un controllo automatico, oppure tu a mano; da quale livello di rischio diventa obbligatorio. Si parte dalla lista già pronta (ISO 25010, i quattro rischi di Cagan, i tuoi due criteri, i criteri pensati per gli agenti).»

Scopo dichiarato: «definire i criteri con cui lavoro ai progetti avviandoli da chat reasoning come questa», per far lavorare agenti come Sonnet o Opus «commettendo il minor numero di errori possibili».

## La decisione di Matteo (alla lettera)

«i miei due criteri esistono già e hanno un nome.
* «Aggiungere senza cancellare» si chiama principio aperto/chiuso: il codice si estende senza modificare quello che c'è.
* «Parallelizzabile» si chiama basso accoppiamento: pezzi che non si pestano i piedi.»

«Confermo procedi pure e fai chiusura.»

La conferma vale per la proposta qui sotto, così com'è stata presentata da Claude.

## Proposta confermata

### Livelli di rischio

- R1: lo usa solo Matteo, si annulla con git, nessun dato vero (prototipo, memory, script).
- R2: lo usa qualcun altro o tocca dati veri, ma si annulla in minuti senza perdite (nuova schermata in un'app in uso).
- R3: non si annulla del tutto (migrazioni, dati cancellati, messaggi inviati, pagamenti), oppure salute, legge o dati personali, oppure va in produzione (HACCP, prenotazioni dei clienti).
- Il livello lo decide la chat di ragionamento e sta scritto nel brief. Nel dubbio si sale.

### Chi verifica

Auto = controllo automatico; Revisore = agente in contesto pulito (anche altro modello); Matteo = Matteo.

### A. Prima di partire (in chat di ragionamento, con Matteo)

1. Valore (Cagan) — «Chi lo usa e cosa smette di fare a mano? Se non lo faccio, chi se ne accorge?» — Matteo — R1 (una riga).
2. Pre-mortem (Klein) — «È fallito fra un mese: perché?» — chat + Matteo — R3 (R2 a inizio progetto).
3. Fattibilità (Cagan) — «Qual è il pezzo che non sappiamo se funziona? Lo proviamo prima con un prototipo da buttare?» — Revisore / prototipo — R2.
4. Sostenibilità (Cagan) — «Quanto costa al mese (hosting, API, token) e che obblighi porta?» — l'agente raccoglie i fatti, decide Matteo; legge → professionista — R2.
5. Usabilità (Cagan; capacità di interazione ISO) — «Una persona del ruolo X lo usa sul suo telefono senza che tu glielo spieghi?» — Matteo con un utente vero — R2.

### B. Il brief all'agente

6. Finito verificabile — «Con quale comando o prova si vede che è finito, e cosa deve uscire?» — Auto, scritto prima del codice — R1.
7. Brief senza decisioni — «L'esecutore deve scegliere qualcosa che non è scritto?» — Revisore (la chat che lo scrive lo rilegge) — R1.
8. Fetta piccola — «Si chiude in una sessione e il diff si legge in 10 minuti?» — Auto (dimensione del diff) — R1.
9. Confini sempre/chiedi/mai — «Cosa fa da solo, cosa chiede, cosa non fa mai?» — Auto dove si può (permessi negati nelle impostazioni), altrimenti Revisore — R1 lista minima, R2 lista del progetto.
10. Parallelizzabile (criterio di Matteo; basso accoppiamento) — «Due agenti toccano gli stessi file?» — Auto (incrocio dei file dei diff) — quando lavora più di un agente.
11. Costo d'uso — «Quanti token ha consumato, ne valeva la pena?» — Auto, nella nota di fine chat — R1, da registrare.

### C. Il codice

12. Aggiungere senza cancellare (criterio di Matteo; principio aperto/chiuso) — «Per aggiungere questa funzione devo cambiare codice che già funziona?» — Auto: i test esistenti passano senza essere stati modificati — R2.
13. Leggibile in poco contesto (con interfacce esplicite e file di istruzioni corto) — «Un agente nuovo capisce questa parte leggendo pochi file? CLAUDE.md sotto 200 righe?» — Auto (lunghezze) + Revisore a freddo — R2.
14. Niente duplicati — «Esiste già qualcosa che lo fa?» — l'agente cerca prima di scrivere; Auto (rilevatore di duplicati) — R2.
15. Sicurezza (ISO) — «Chi può leggere o cambiare questi dati? Ci sono chiavi nel codice?» — Auto (scanner delle chiavi da R1, regole di accesso al database da R2) + Revisore — R1 chiavi, R2 il resto.
16. Reversibilità (con affidabilità e recuperabilità) — «Se va storto, come torno indietro e cosa perdo?» — Auto: il ritorno indietro è provato, non solo scritto — R2 scritto, R3 provato.
17. Produzione (regola di Matteo) — «Cambia qualcosa che vedono i clienti?» — collaudo a mano di Matteo; l'esecutore non ha le credenziali di produzione — R3.

A R1 i criteri obbligatori sono 7 (1, 6, 7, 8, 9, 11, 15).

### Fuori dalla lista di base

Efficienza e compatibilità (ISO) entrano solo con un requisito misurabile (esempio: «si apre in 2 secondi sul telefono del locale»). La flessibilità è coperta dal 12. La safety diventa una delle condizioni di R3.

### Tre scelte di Claude, confermate

1. «Tu a mano» resta solo dove Matteo può giudicare: 1, 2, 4, 5, 17 (valore, utenti, soldi, produzione). I criteri tecnici vanno a un controllo automatico o a un agente revisore, coerente con la decisione `0012` del 12/10/2026 (le scelte tecniche sono degli agenti).
2. Aggiunti tre controlli che la lista non aveva: brief senza decisioni (7), test esistenti non modificabili per farli passare (dentro il 12), credenziali di produzione tolte all'esecutore (17). Esempio osservato: nella sessione del 22/10/2026 era attivo un connettore `supabase-prod`.
3. Manutenzione: i criteri restano fissi; se ne aggiunge uno solo dopo un errore ripetuto; se ne toglie uno se in 3 progetti non ha mai fermato niente.
