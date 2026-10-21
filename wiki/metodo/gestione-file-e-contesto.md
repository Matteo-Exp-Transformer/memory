# File, cartelle e contesto: come è organizzata la memoria di lavoro

> Sources: Io-Claude, 2026-08-07; Io-Claude, 2026-09-25; Io-Claude, 2026-10-10
> Raw: [04-handoff-prossimo-agente](../../raw/crescita-professionale/04-handoff-prossimo-agente.md); [contesto-progetto](../../raw/crescita-professionale/contesto-progetto.md); [io-claude-claude](../../raw/istruzioni-agenti/io-claude-claude.md)
> Updated: 2026-10-21

## Overview

Il binario crescita professionale vive in una cartella locale (`Documents\Io-Claude\Crescita professionale`), versionata con git, su cui l'agente ha lettura e scrittura. Il 29/07/2026 la knowledge di Claude Desktop è stata riorganizzata: i 9 documenti sono stati rimossi e sostituiti da un solo file-mappa, `CONTESTO_Progetto.md`, affiancato al CV. Motivo: le copie nella knowledge erano già divergenti dal disco (l'handoff era un terzo della versione reale) e la knowledge è di sola lettura per l'agente, quindi il divario poteva solo allargarsi. Regola risultante: disco come fonte di verità, knowledge come un solo file che è una mappa e non una copia.

## Ruolo dei file

- **00 Profilo:** valutazioni e log evolutivo; file-traccia, a ogni sessione si appende una riga. Racconta come lavora e a che punto è.
- **07 Profilo completo:** fatti grezzi (anagrafica, esperienze, descrizione dei prodotti), materia prima per CV e candidature; statico. Non confondere 00 e 07.
- **01 Come mi presento, 02 Vocabolario, 03 Skill e studio, 05 Metodo, 06 Piano corsi e LinkedIn, 08 Candidature e profilo:** i documenti di lavoro tematici; il 05 è il motore, e ogni sessione si conduce su quello.
- **10 Eval pipeline:** artefatto congelato (vedi `progetti/hubspot-pipeline-eval.md`).
- **11 Valutazioni didattiche:** rubrica per sessione (vedi `persona/rubrica-e-valutazioni.md`), da compilare a fine di ogni sessione e prima di un commit che contenga nuovi dati su come ha lavorato.
- Regola file: aggiornare solo il file pertinente e appendere sempre una riga al log del 00.

## Binari paralleli

La cartella aveva due handoff: uno attivo e uno congelato. Il binario HubSpot è stato sospeso il 07/08/2026 su sua decisione, con la frase «viene prima di tutto ora chiudere interrogazione… HubSpot lascio in sospeso per completare questo lavoro fino in fondo prima»; quel file resta valido, e alla ripresa si riparte da dov'era. La numerazione «sessione 7» è anteriore: la sessione 7 reale è quella dell'interrogazione, e le sessioni HubSpot si rinumerano alla ripresa. Il metro (i 7 criteri) resta uno solo su entrambi i binari.

## Quando non c'è la cartella

Se l'agente ha accesso alla cartella, i file su disco sono l'unica fonte di verità e ci si scrive direttamente. Se non ce l'ha (chat normale, mobile, altro PC), usa il riassunto e lo dice apertamente: «sto lavorando sul riassunto, non sui file aggiornati». Non inventa il contenuto dei file; per un lavoro serio chiede una sessione con la cartella collegata. Il file-mappa è l'unico che va tenuto allineato a mano, su disco e nel progetto; tutto il resto si aggiorna solo su disco. Per i task di interrogazione, profilo, valutazione e roadmap si carica prima la bussola della valutazione, senza navigare a tappeto.

## Le tre aree di lavoro e le regole operative (mappa del 28/09/2026)

Sul PC di Matteo (Windows) gli agenti lavorano in tre aree: `Io-Claude` (documentazione personale: profilo, crescita professionale, handoff tra agenti), `GitHub` (tutti i repo di codice) e `Downloads` (zona di passaggio: file scaricati, allegati, input grezzi). Se una cartella non è collegata alla sessione, si chiede l'accesso con i percorsi esatti; altre aree del PC solo se Matteo le autorizza di volta in volta. Ogni repo con un proprio `CLAUDE.md` ha la precedenza su quello generale per il proprio contenuto. Il file d'ingresso è stato creato per avere lo stesso contesto ovunque (desktop, mobile, Cowork, Claude Code).

Regole: leggere è libero in tutte e tre le aree; scrivere nella cartella dove sta il file, modificando un file esistente solo se Matteo lo chiede (le versioni trasformate vanno in un file nuovo accanto all'originale); cancellare mai senza conferma esplicita e, nel dubbio, spostare in `_to_delete\`; non toccare `.git\`, commit e push solo su richiesta; Download è un'area di input, gli output finali vanno nel progetto giusto o in `Io-Claude`; a fine lavoro si aggiorna l'handoff del binario annotando già le decisioni che l'agente può prendere; italiano, del tu. Il progetto «Esplorazione e lettura di Matteo» (fissato il 10/10/2026) va letto prima di ogni chat di ragionamento: la sezione «In 30 secondi» del file di lettura (vedi `persona/lettura-non-verbale.md`), con una riga nel suo registro a fine chat.

## See Also

- [Lavorare con gli agenti](../metodo/lavorare-con-agenti.md)
- [Definire un progetto e tenere la memoria](../metodo/definizione-progetto-e-memoria.md)
- [Modo esplorazione](../metodo/modo-esplorazione.md)
