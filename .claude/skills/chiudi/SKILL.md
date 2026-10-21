---
name: chiudi
description: Usa questa skill quando Matteo scrive «chiudi» a fine chat: riscrive da capo lo STATO.md del progetto e scrive la nota di sessione in memory/raw/sessioni/.
---

# chiudi — chiusura di fine chat

A fine chat servono due cose: lo **stato del lavoro** (vive nella repo del progetto, in `STATO.md`)
e **ciò che si è imparato** (vive qui, come nota in `raw/sessioni/`). La memoria non organizza lavori:
per questo `STATO.md` non sta mai nella repo `memory`.

## Formato di STATO.md

Massimo 40 righe, riscritto **da capo** ogni volta (la storia sta in git e nelle note di sessione).

```
# STATO — <nome progetto>
Aggiornato: AAAA-MM-GG · Nota: memory/raw/sessioni/AAAA-MM-GG-<argomento>.md

## Dove siamo
(max 5 righe: lo stato reale, verificato aprendo i file, non copiato dal vecchio STATO)

## Fatto in questa chat
(max 5 righe, ognuna con la prova: file, commit o comando)

## Prossimo passo
(uno solo, con la condizione di chiusura: "finito quando …")

## Decisioni prese
(decisione — criterio; non si riaprono senza un fatto nuovo)

## Aperto
(solo ciò che aspetta un fatto mancante: fatto che manca → chi o cosa lo sblocca)

## Da leggere per ripartire
(in ordine, solo questi file)

## Come verificare lo stato reale
(1–3 comandi)
```

Regole:
- Massimo 40 righe in tutto.
- La riga `Aggiornato:` è la riga 2 e ha la data di oggi.
- Niente copie di contenuto che sta altrove: metti il link.
- Sezione vuota: scrivi «niente».

## Procedura di «chiudi»

1. Guarda lo stato reale: `git status`, `git log` della chat, i file toccati. Non fidarti del vecchio `STATO.md`.
2. Se la repo è `memory` stessa: niente `STATO.md` (memory non organizza lavori), solo la nota (passo 4).
3. Riscrivi da capo `STATO.md` nella radice della repo del progetto, nel formato sopra.
4. Scrivi la nota NUOVA in `C:\Users\matte.MIO\Documents\GitHub\memory\raw\sessioni\AAAA-MM-GG-<argomento>.md`
   (crea la cartella se manca). `raw/` è immutabile: mai modificare una nota esistente; se il nome
   esiste già aggiungi `-2`, `-3`. Formato della nota (max ~80 righe):
   - righe d'intestazione: `Data:`, `Progetto:`, `Repo:`, `Agente:` (il modello);
   - `## Cosa si è fatto` (breve);
   - `## Cosa si è imparato` (su Matteo, sul metodo, cosa ha funzionato e cosa no);
   - `## Decisioni e criterio`;
   - `## Parole di Matteo` (citazioni alla lettera tra «», perché la wiki potrà citare solo ciò che è scritto qui alla lettera);
   - `## Numeri` (numeri e date esatti).
   Niente riassunti di codice: si ricavano dalla repo.
5. Lancia il controllo: `python C:\Users\matte.MIO\Documents\GitHub\memory\strumenti\controlla.py <radice repo progetto>`
   e `python strumenti/controlla.py .` nella memoria; correggi gli errori.
6. Commit locale: nella memoria solo la nota (messaggio `sessione: AAAA-MM-GG <argomento>`);
   nella repo del progetto solo `STATO.md`, salvo regole proprie di quella repo.
   Push mai senza l'OK di Matteo in chat.
7. Riferisci a Matteo in 3 righe cosa hai scritto e dove, e chiedi l'OK per il push.

«chiudi» non aggiorna la wiki: portare la nota nella wiki è l'operazione «aggiungi» della skill
`karpathy-llm-wiki`, da fare a parte.
