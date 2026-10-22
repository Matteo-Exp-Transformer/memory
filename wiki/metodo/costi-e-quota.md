# Costi e quota: come si misura il lavoro degli agenti

> Sources: Io-Claude, 2026-10-12; Io-Claude, 2026-10-10; Io-Claude, 2026-10-21; Io-Claude, 2026-10-09
> Raw: [2026-10-21-avvio-memoria](../../raw/sessioni/2026-10-21-avvio-memoria.md); [2026-10-22-stato-chiudi-controlli](../../raw/sessioni/2026-10-22-stato-chiudi-controlli.md); [2026-10-22-skill-progetta](../../raw/sessioni/2026-10-22-skill-progetta.md); [2026-10-22-criteri-di-progetto](../../raw/sessioni/2026-10-22-criteri-di-progetto.md); [12-10-2026-nuovo-ritmo-lotti](../../raw/mss/12-10-2026-nuovo-ritmo-lotti.md); [12-10-2026-audit-motore-lotto14](../../raw/mss/12-10-2026-audit-motore-lotto14.md); [mappa-esplorazioni](../../raw/esplorazione/mappa-esplorazioni.md); [2026-10-21-ricerca-iniziale](../../raw/metodo-ia/2026-10-21-ricerca-iniziale.md); [09-10-2026-controllo-sistema](../../raw/mss/09-10-2026-controllo-sistema.md)
> Updated: 2026-10-22

## Overview

Matteo lavora con abbonamenti personali (20 euro al mese per Claude e per GPT) e con una quota che si azzera ogni 5 ore. Il 12/10/2026 ha deciso che i lavori degli agenti si raggruppano in lotti e che il costo di ogni lotto si stima e si misura, per fissare il tetto sul dato e non sull'intuizione. La regola che ne esce: prima il dato, poi la regola.

## La regola di Matteo

- Un lotto va completato per intero, senza il vecchio limite di tre lavori. Il tetto: al massimo metà dei token disponibili in 5 ore per lavorare sul lotto, l'altra metà per la revisione e i fix, così che un lotto consumi al massimo tutti i token di 5 ore.
- Non serve che il primo lotto rispetti già il tetto: si può partire da una percentuale più bassa; l'importante è cominciare a raccogliere dati sul costo e a fare previsioni.
- Le chat di ragionamento hanno la precedenza sui lotti: «meno quota sono più importanti chat di reasoning al momento».
- Un ricercatore programmato deve indagare come i professionisti stimano e gestiscono il costo dei task assegnati ai modelli (ricerca del 13/10/2026; l'esito non è nel corpus).

## Le prime misure (12/10/2026)

La quota di Matteo partiva dal 62% quando sono partiti gli esecutori del secondo lotto, ed era all'87% alla fine del secondo esecutore: circa 450.000 token di agenti più la chat, cioè circa 18.000 token per punto di quota. Il secondo lotto aveva 9 lavori stimati 1,9 milioni di token. Matteo ha commentato «Consideriamola già un po' abbondante», e l'agente l'ha letto come «lotto troppo grande» abbassando il tetto. Era una lettura sbagliata: per «abbondante» intendeva il valore del costo, perché include in piccola parte anche il ragionamento dell'agente, e il lotto andava bene come impostato. Il tetto è tornato a circa 2 milioni stimati, 0,5–1 milione reali, così resta quota per le chat di ragionamento (vedi anche `persona/lettura-non-verbale.md`, sulle parole che per lui hanno un senso proprio).

Lotto del 14/10/2026: 9 lavori, 1,97 milioni stimati; gli esecutori hanno consumato circa 0,8 milioni contro 1,4 stimati; la sua quota è passata dal 6% al lancio al 49% con la chat, al 75% in serata.

## Strumenti per misurare

L'audit del motore ha trovato che la misura dei costi del sistema conta le verifiche, non i token; si adotta `ccusage` per i costi. Per i lotti si usa un metodo di stima con taglie S, M e L e un registro dei costi, documentato nella repo MSS.

## Quando finisce la quota

Nessun agente riparte da solo dopo la quota: nella stessa chat basta «continua», in una nuova chat si usa `ripartiamo:`; le attività programmate ripartono al loro orario come giro nuovo. Matteo ha anche programmato una sessione alle 22:40, dopo il reset delle 22:30, che riprende il lavoro se manca qualcosa, esegue i fix di revisione o fa il merge in base a come trova il lavoro.

## Cosa dice la documentazione ufficiale (letture del 21/10/2026)

- Su Claude Pro c'è una finestra di 5 ore più un limite settimanale; la chat e Claude Code attingono allo stesso serbatoio e non esiste un numero pubblico. Opus «usa molta più quota» e costa «diverse volte» Sonnet per turno. Il modello predefinito di Claude Code su Pro è Opus; i sotto-agenti ereditano il modello e Explore gira su Opus.
- Il lotto del 14/10/2026 ha usato 43 punti di quota della finestra di 5 ore per circa 1M token di sotto-agenti: una finestra vale circa 1,8M token di sotto-agente.
- Risparmio: Sonnet di base, `opusplan`, un modello dedicato ai sotto-agenti, `/clear` tra i compiti, `/compact` nelle pause, MCP inutili spenti, `/usage` settimanale. I team di agenti costano circa 7 volte i token; le attività ricorrenti rimandano tutto il contesto ogni volta.
- Controlli a zero token: «CLAUDE.md è consultivo, gli hook sono deterministici: se una regola viene ignorata, trasformala in hook o test». Gli hook coprono il blocco dei comandi prima dell'uso, la formattazione dopo, e i test verdi prima di chiudere; a questi si affiancano pre-commit e le GitHub Actions (2.000 minuti al mese sui repo privati del piano Free).
- Fonti da seguire: Anthropic Engineering, la documentazione di Claude Code, quella di OpenAI Codex, Simon Willison, Armin Ronacher, Hamel Husain, Pragmatic Engineer, Latent Space. Da evitare: numeri senza link ufficiale, gli elenchi di «N trucchi», i siti che vendono un prodotto.

## Costi misurati delle sessioni di memory (21-22/10/2026)

Solo i sotto-agenti sono contati; la chat principale non è mai stata letta, quindi sono costi parziali.

| Sessione | Costo letto |
|---|---|
| Avvio della memoria (21/10) | sotto-agenti Sonnet 131.237 + 169.660 + 156.602 + 152.151 token |
| Criteri di progetto (22/10) | non letto, nessun sotto-agente |
| STATO.md, «chiudi» e controlli (22/10) | sotto-agente Sonnet 88.838 token |
| Skill `progetta` (22/10) | sotto-agente Sonnet 107.472 token; Codex 18.105 token |

Per decisione di Matteo, per ora «Quasi tutto» l'abbonamento va a ricerca e definizione. Aperto: quanto le attività pianificate dell'MSS pesino sulla quota non è misurato.

## See Also

- [MSS](../progetti/mss-metaskillsystem.md)
- [Definire un progetto e tenere la memoria](../metodo/definizione-progetto-e-memoria.md)
- [Lavorare con gli agenti](../metodo/lavorare-con-agenti.md)
