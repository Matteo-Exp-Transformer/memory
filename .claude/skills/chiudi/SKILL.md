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
4. Leggi il costo: dalla cartella in cui gira la chat lancia
   `python C:\Users\matte.MIO\Documents\GitHub\memory\strumenti\costo_sessione.py` (in Codex aggiungi `codex`);
   per i sotto-agenti prendi il «subagent_tokens» del loro avviso di fine. Ripassa i file che hai letto
   nella chat e segna per ciascuno se è servito (ha cambiato una decisione o il risultato) o no.
   Poi scrivi la nota NUOVA in `C:\Users\matte.MIO\Documents\GitHub\memory\raw\sessioni\AAAA-MM-GG-<argomento>.md`
   (crea la cartella se manca). `raw/` è immutabile: mai modificare una nota esistente; se il nome
   esiste già aggiungi `-2`, `-3`. Il formato (massimo 20 righe) è quello della sezione
   «Note di fine chat» di `AGENTS.md`, con l'esempio `raw/sessioni/2026-10-21-avvio-memoria.md`:
   non copiarlo qui. Le parole e le decisioni di Matteo vanno alla lettera tra «», perché la wiki
   potrà citare solo ciò che è scritto nella nota. Niente riassunti di codice: si ricavano dalla repo.
5. Lancia il controllo: `python C:\Users\matte.MIO\Documents\GitHub\memory\strumenti\controlla.py <radice repo progetto>`
   e `python strumenti/controlla.py .` nella memoria; correggi gli errori.
   Nel cloud Linux, o dove `python` manca: `sh <memory>/strumenti/controlli.sh <radice repo progetto>`.
6. Commit e push, senza chiedere l'OK a Matteo (Matteo, 27/10: «non mi chiedono autorizzazione ma agiscano autonomamente»):
   - memoria: commit della sola nota con `git commit -- <nota>` (mai lo staging di altre sessioni),
     messaggio `sessione: AAAA-MM-GG <argomento>`, poi `git push`; se il push è rifiutato, `git pull --rebase` e riprova;
   - progetto: commit di `STATO.md` sul branch della chat e push secondo i criteri di push della repo
     (in CalendarBackup-v2: `team/costruttore.md`, sezione Push). Un progetto senza criteri scritti: chiedi l'OK come prima.
   Niente push, e lo dici nel riepilogo, se: hook o controlli falliscono (mai `--no-verify`), il branch è main
   o di un altro agente, servirebbe un force push, o il diff contiene credenziali o dati personali.
7. Riferisci a Matteo in 3 righe cosa hai scritto, dove, e cosa è stato pushato o perché no.
   Se c'è un agente senior o manager da far ripartire, il prompt di avvio va per intero in chat, in un blocco
   da copiare; il file in repo è solo la copia (Matteo, 29/10: «deve darmi prompt in chat da copiare e incollare no file linkato»).

«chiudi» non aggiorna la wiki: portare la nota nella wiki è l'operazione «aggiungi» della skill
`karpathy-llm-wiki`, da fare a parte.
