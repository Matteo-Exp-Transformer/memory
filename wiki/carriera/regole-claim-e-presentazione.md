# Cosa Matteo può dire di sé (e cosa no)

> Sources: Io-Claude, 2026-07-30; Io-Claude, 2026-09-25; Io-Claude, 2026-10-12; Io-Claude, 2026-08-07; Matteo, 2026-11-13
> Raw: [02-vocabolario](../../raw/crescita-professionale/02-vocabolario.md); [01-come-mi-presento](../../raw/crescita-professionale/01-come-mi-presento.md); [12-handoff-interrogazione](../../raw/crescita-professionale/12-handoff-interrogazione.md); [04-handoff-prossimo-agente](../../raw/crescita-professionale/04-handoff-prossimo-agente.md); [08-candidature-e-profilo](../../raw/crescita-professionale/08-candidature-e-profilo.md); [competenze AI-assisted e candidature](../../raw/conversazioni/2026-11-13-competenze-ai-assisted-candidature.md)
> Updated: 2026-11-13

## Overview

Ogni parola che Matteo usa per presentarsi deve reggere il «ma cosa vuol dire?». Dal vocabolario che si è costruito (versione al 30/07/2026) emergono le parole-mina: termini che suonano bene, che lui è tentato di usare e che non può difendere alla domanda dopo. Questa pagina elenca i confini, perché sono vincoli che un agente non può dedurre dai suoi progetti.

## Candidature: competenze operative AI-assisted (13/11/2026)

Matteo vuole valutare gli annunci **mappando prima quali task tecniche può effettivamente completare con OpenAI e Claude**, combinando competenze trasversali, conoscenza del problema, dati disponibili, proprie decisioni di progetto e criteri per controllare il risultato. Considera una task completata in questo modo una sua **competenza operativa AI-assisted**, non una competenza di esecuzione manuale autonoma.

Per renderla dichiarabile nel CV, distinguere: **decisione e criteri di Matteo · esecuzione delegata al modello · verifica del risultato · limiti e dipendenze**. Testare la capacità sul tipo di task richiesto prima di attribuirla al profilo: una capacità ipotizzata non è ancora una prova. Resta valida la regola sui livelli in [Skill e livelli](skill-e-livelli.md): nessuna promozione sulla sola base di un esercizio guidato.

## I confini, parola per parola

- **Product specialist:** descrive chi porta competenza profonda di un dominio dentro le decisioni di prodotto. Non dire «product manager» finché non ha gestito una roadmap con un team reale: la roadmap con un team non l'ha fatta.
- **F&B:** se vedi facce perplesse, traduci subito in «ristorazione».
- **Definire i requisiti:** scrive il cosa e il perché, non il come (le specifiche ingegneristiche profonde).
- **AI-in-the-loop:** vale solo se c'è una decisione umana finale. Altrimenti è automazione autonoma, più rischiosa da promettere. Mai dire che «l'AI gestisce da sola» conformità o sicurezza alimentare.
- **AI-assisted development** (la più delicata): definisce requisiti e architettura e costruisce iterando con Cursor e Claude; sa leggere, capire e modificare codice, non scrive da zero codice complesso senza supporto. Non dire «full-stack developer» né «programmo in React/Node»: una domanda tecnica e cade.
- **HACCP:** la parola-mina è «garantisce la conformità». Il suo gestionale aiuta a compilare correttamente e in tempo la documentazione; la conformità dipende da come si gestisce il locale. Non è un consulente HACCP certificato.
- **Skill system:** ne ha due funzionanti, uno per gestire repository con agenti, uno in un'app di trading. La chiusura onesta, da dire prima di essere interrogato: sa costruirli e sta imparando a valutarli in modo sistematico (vedi `skill-e-livelli.md`).
- **Evals:** «ha azzeccato 8 volte su 8» non è una eval (campione minuscolo, scelto da lui, nessun criterio, nessun baseline).
- **«Capisco il business»:** il suo business è operativo e decisionale, non finanziario. Non rivendicare food cost, margini, budget: li teneva il titolare.
- **Prodotto funzionante:** non dire «production-grade» né «scalabile enterprise». La formula è «funzionante e in uso per il compito reale, non ancora indurito per grandi volumi».

## Cosa sa difendere

Sicurezza di base: le RLS (Row Level Security) chiudono le tabelle del database e, se spente, chi ha la anon key (pubblica, estraibile dal browser) legge e scrive l'intera tabella. La anon key va nel frontend; la service_role mai, perché ignora le RLS. I segreti non si versionano su git, non si espongono nel frontend e vanno reinseriti nel pannello di deploy (Vercel).

## Come si apre una presentazione

Si apre con l'asset, non col titolo: non annunciare «sono un product specialist», la trappola che lo smaschera. L'asset da dire per primo è un gestionale calendario/prenotazioni in uso reale, oggi, in un locale; il gestionale HACCP non è completo e non si nomina come in uso (correzione del 01/09/2026, vedi `progetti/prenotazen-calendarbackup.md`). Apertura che chiude il posizionamento in tre righe, sua: «Per anni al bancone intuivo cosa voleva un cliente prima che lo dicesse.» Il resto del pitch del 13/07/2026: «undici anni tra sala e bancone», un locale gestito in autonomia, banqueting a Londra, poi il software che da gestore avrebbe voluto. Nei materiali pubblicati oggi si dice «oltre 10 anni» (vedi `persona/chi-e-matteo.md`).

Le cinque regole, dal campo:

1. Il fatto batte l'astratto: «ho un gestionale in uso in un bar» vale più di «porto conoscenze di dominio».
2. Non annunciare il titolo: si fa riconoscere dai fatti.
3. Ogni frase astratta si copre con un fatto pronto (RLS attive, service_role mai nel frontend, guardrail su input e output).
4. Pianta la bandiera dove è fortissimo, poi accenna all'estensibilità, mai il contrario: altrimenti si annacqua.
5. Mai nominare uno standard, strumento o numero che non saprebbe spiegare alla domanda dopo. È così che si è dato la zappa con le ISO.

Risposte pronte alle domande scomode: sul codice, «Programmo con l'utilizzo di tool AI» e dove serve giudizio ingegneristico profondo si appoggia a uno sviluppatore; sulla roadmap, «La roadmap con un team la voglio imparare — non la rivendico ancora.» Sul perché lui e non un dev junior: un junior scrive il codice, lui sa cosa vale la pena costruire nel food (l'overbooking del sabato perché una quota non si presenta). La risposta al dev junior è ancora una bozza.

## Il cliente difficile e le recensioni (25/09/2026)

- La formula col cliente è «non rispondo mai con un muro: rispondo con una o due alternative». Non «non dico mai di no»: in un ruolo di Customer Success il sì a tutto è un difetto, a volte va detto che una cosa non si può fare.
- Esempio STAR principale: festa di laurea al locale, pacchetto di 13 € a persona con sette portate, madre del laureato con richieste continue. Lui è andato dal titolare prima di promettere, è tornato con tre sì e un no motivato (il servizio in ceramica, che si concorda in prenotazione) e ha promesso un follow-up di persona. Il ponte da dire: il problema nasce quando si fissano le aspettative, in un software durante l'onboarding.
- Recensioni, campione di 5 verificato da lui e non contato. Si può dire: «le recensioni citano spesso la cordialità dello staff, e una su TripAdvisor (aprile 2025) mi nomina per nome». Non si dice che una recensione è della cliente dello STAR (ricordo incerto) né «tutte» né «sempre».

- Nell'episodio dello STAR Matteo non aveva nominato la sua mossa più forte, l'escalation al titolare prima di promettere: è il divario tra ciò che fa e ciò che sa nominare (vedi `persona/rubrica-e-valutazioni.md`). Nominagliela tu, in lingua Customer Success.
- Il «di più» (i prodotti) si racconta dentro il ruolo Customer Experience: voce del cliente, requisito, prodotto usato. Mai «in realtà sono un PM»: in un colloquio di Customer Success suona come rischio di fuga.

## Domande a freddo pronte

Per la simulazione con un'azienda vera (non con gli amici): «Perché dovrei prendere te e non un dev junior che costa uguale?», «Raccontami una volta in cui hai sbagliato a valutare la fattibilità di qualcosa.» E nella versione commerciale e CS: «Come qualifichi un lead?», «Un merchant non usa una funzione da tre mesi: cosa fai?», «Come misuri se l'onboarding è andato bene?»

## Le cinque metriche di Customer Success

La tabella ha una colonna «prova che ho» che contiene solo ciò che un recruiter può verificare, oppure «nessuna». Frasi di colloquio sicure: sul churn, «Non lo misuravamo: lo sapevamo solo per sentito dire. È il primo dato che metterei in un software.» Sull'adozione, «Una funzione l'ho costruita personalizzabile, ma non l'ho resa semplice: il titolare non la usa e chiede a me.» Raccontare un proprio limite con la lettura di Customer Success accanto è credibile proprio perché non è un successo. Divieti: non citare la stima del 15% (invita a «come l'avete misurato?»), non attribuire a PrenotaZen una crescita che la precede, non dire «non mi ha mai fatto domande» ma «non ha avuto bisogno di tornarci». La quinta metrica (rinnovo nel software) non ha ancora contenuto.

## See Also

- [Chi è Matteo](../persona/chi-e-matteo.md)
- [Profilo LinkedIn](../carriera/profilo-linkedin.md)
- [PrenotaZen e BHM](../progetti/prenotazen-calendarbackup.md)
