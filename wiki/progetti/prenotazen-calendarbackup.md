# PrenotaZen / CalendarBackup-v2 (in uso) e BHM (in sviluppo)

> Sources: Io-Claude, 2026-09-25; Io-Claude, 2026-10-12; Matteo, 2026-10-21
> Raw: [07-profilo-completo](../../raw/crescita-professionale/07-profilo-completo.md); [00-profilo-matteo](../../raw/crescita-professionale/00-profilo-matteo.md); [13-roadmap-complessiva](../../raw/crescita-professionale/13-roadmap-complessiva.md); [chiarimenti 21/10](../../raw/conversazioni/2026-10-21-chiarimenti-matteo.md)
> Updated: 2026-10-21

## Overview

PrenotaZen (repo `CalendarBackup-v2`) è il gestionale di calendario e prenotazioni per ristoranti che Matteo ha costruito con sviluppo AI-assisted. È l'unico suo prodotto in uso reale, oggi, in un bar-ristorante di Bologna, Al Ritrovo, dove Matteo ha lavorato e che è il committente. È deployato con autenticazione. Funzioni: calendario, turni, coperti, notifiche automatiche, interfaccia admin. Progettato da chi ha gestito una sala reale: ogni funzione risolve un problema operativo concreto.

> **Status: Outdated** (01/09/2026)
> Una sessione sul CV del 01/09/2026 aveva scritto «solo BHM è in uso reale». Matteo ha corretto il 01/09/2026: l'app in uso è questa, non il gestionale HACCP (vedi la sezione su BHM più sotto). I testi precedenti alla correzione sono da non usare.

## Prova indipendente

Il database di produzione è rimasto fermo 47 giorni con 9 migrazioni pronte, perché il collaudo manuale non era chiuso. Verificato su git nella sessione 10 dell'08/08/2026.

## Fatti dichiarati da Matteo il 25/09/2026

- In versione beta ha gestito per un anno intero il flusso delle feste di laurea di Al Ritrovo. Nei giorni di picco di marzo circa 7 prenotazioni di gruppo al giorno: valore dei giorni di sessione, non media mensile. Menu preselezionati, note su allergie, intolleranze e richieste particolari. Il locale ha pianificato il servizio sui dati raccolti dall'app. Il titolare ha riconosciuto il lavoro con un piccolo extra in busta paga.
- Volumi: feste di laurea in media 100–120 l'anno, massimo stimato ~200, concentrate in poche settimane di sessione. Crescita da circa 15 lauree nei mesi di sessione a oltre 60 in un singolo mese in circa 6 anni: è un ricordo, non documentato, e precede l'app, quindi non va attribuita a PrenotaZen.
- Canali: nessun social, mail o WhatsApp; solo presenza su Google e recensioni, passaparola e fidelizzazione di studenti abituali. La responsabile dei social è arrivata dopo la fase di crescita.
- Onboarding per ruolo: alla responsabile dei social circa 2 ore di spiegazione su menu personalizzati e link del QR code, poi domande il giorno dopo, poi autonoma; al titolare circa 1 ora su prodotti e flusso prenotazioni, ha provato da solo e su quelle funzioni non ha avuto bisogno di tornare. Tempi da ricordo, non misurati.
- Adozione: uso stagionale. Dipendenti inseriscono prenotazioni prese al telefono o di persona; il titolare consulta ogni giorno calendario e dettagli e contatta i clienti; la responsabile social crea menu e promozioni e pubblica link e QR. Poco usato l'archivio. Non usata la personalizzazione della pagina cliente: modificabile dal titolare, ma l'interfaccia richiede formazione dedicata, quindi oggi la gestisce Matteo su richiesta.
- Churn: non si vedeva, se non per sentito dire. Stima sua, non contata: al massimo ~15% della clientela fidelizzata.
- Richieste del titolare diventate funzioni: menu con QR code; gestione autonoma di prodotti e informazioni aziendali. L'app è quasi tutta modificabile dall'utente; Matteo interviene solo sui dati che creano conflitti nelle logiche. Esiste una console per le richieste particolari dei clienti.
- La pagina servizio non è ancora in produzione: nessun numero di coperti giornalieri da citare.

## La correzione del 01/09/2026 (D-01) e cosa resta da verificare

Fino a quel giorno tutto il corpus diceva l'opposto, in almeno 5 file, nel profilo completo e dentro un CV: tutti corretti il 01/09/2026. La correzione regge la verifica incrociata: il gate dei 47 giorni con 9 migrazioni pronte è documentato sul repo del calendario, non su BHM, e del `BHM v3` il verbale della sessione 10 diceva già «l'app non è completa». Il corpus era in contraddizione con sé stesso e nessuno l'aveva incrociato.

Verifica assegnata a Matteo (`VER-3`): aprire i due repo e registrare, per ciascuno, l'ultimo deploy in produzione e se esiste un utente reale diverso da lui. Chiude quando i due valori sono scritti nel verbale.

Origine, nelle parole dell'interrogazione: vede il bisogno vivendo dentro l'attività e lo traduce in funzione (il titolare che telefonava al bar per leggere l'agenda diventa il calendario sul telefono). Il Menu QR, però, l'ha chiesto Paolo, il titolare di Al Ritrovo (confermato da Matteo il 2026-10-21), e non è una sua idea. Confermato da Matteo lo stesso giorno: «hccp non è in uso. Lo è prenotazen.»

Se Andrea (Genova) risponde sulla richiesta del 01/09/2026 di valutare il SaaS già fatto, decide se PrenotaZen passa da «in sviluppo» ad artefatto dichiarabile.

## BHM (repo `BHM-Zen`): il gestionale HACCP, in sviluppo

È il gestionale con modulo HACCP personalizzabile: il progetto di maggiore complessità di Matteo. Funzioni: monitoraggio delle normative igienico-sanitarie, registrazione temperature, scadenze prodotti, controlli e alert personalizzabili per tipologia di attività, secondo le normative EU HACCP. Il cliente tipo è un'azienda della ristorazione che deve documentare i controlli per legge.

### Stato: in sviluppo, non in uso

È in sviluppo, non completo, e non è in uso presso nessun cliente. Corretto da Matteo il 01/09/2026. Non dichiararlo in uso in nessun materiale di candidatura. L'app in uso reale è PrenotaZen, descritta sopra.

### Cosa insegna

Produce output deterministici: non è un candidato a eval; serve per case study, checklist di sicurezza (Supabase, quindi RLS e anon key) e stima di fattibilità.

### Produttività e paternità

Misura retrospettiva emersa l'08/08/2026, che nessun archivio aveva: BHM v1 un anno, v2 tre mesi, v3 due giorni Opus + 4 sessioni Fable. Non è una stima, ma è la materia prima per farne una. Le decisioni di architettura di BHM v3 sono di Fable, per sua dichiarazione. Una sua competenza dichiarata come mestiere, la lista della spesa, esiste come `BHM-v.2/src/features/shopping/` (10 file) e il collegamento l'ha nominato lui per primo: è la prima riga del blocco «Al Ritrovo» che passa la prova dell'archivio.

## See Also

- [Regole di claim e presentazione](../carriera/regole-claim-e-presentazione.md)
- [Skill e livelli](../carriera/skill-e-livelli.md)
- [Candidature, ricerca e vincoli](../carriera/candidature-e-ricerca.md)
