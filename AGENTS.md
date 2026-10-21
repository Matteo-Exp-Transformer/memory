# memory — regole per ogni agente (Claude, Codex, altri)

Questa repo è la **memoria di contesto** di Matteo Cavallaro: chi è, come lavora, i suoi progetti,
il suo metodo con l'IA, cosa è già fallito. Lingua: italiano, dando del tu a Matteo.

## Cosa è e cosa non è
- **Sa cose.** Non decide e non organizza lavori: qui niente task, lotti, code, decisioni numerate,
  attività pianificate. Il lavoro vive nelle repo dei progetti; qui arriva solo ciò che se ne impara.
- **Solo ciò che un agente non può dedurre da solo:** chi è Matteo, cosa vuole, come comunicare con lui,
  perché ha scelto una cosa, cosa ha provato e com'è andata, vincoli (budget, strumenti, tempo).
  Niente riassunti di codice o di repo: un agente li ricava leggendo la repo.

## Come si legge
1. Apri `wiki/index.md` e leggi **solo** le pagine utili al compito che hai.
2. Se serve una prova, segui il campo `Raw` della pagina fino al file originale in `raw/`.
3. Non caricare tutta la wiki: costa token e peggiora il lavoro.

## Come si scrive
- Usa la skill `karpathy-llm-wiki` (`.claude/skills/` per Claude, `.agents/skills/` per Codex).
  Le sue tre operazioni: **aggiungi** (ingest), **interroga** (query), **controlla** (lint).
- `raw/` è **immutabile**: mai modificare né cancellare; si aggiungono solo file nuovi.
- Ogni pagina di `wiki/` ha `Raw` (da dove viene) e `Updated` (data). Numeri, date e citazioni
  devono comparire **alla lettera** nel file raw collegato.
- Un'informazione superata non si cancella: si marca `Status: Outdated` con la data.
- Le pagine restano brevi (indicativamente sotto le 150 righe); se crescono, si dividono.

## Controlli
- Prima di proporre modifiche: `python3 .claude/skills/karpathy-llm-wiki/scripts/check_evidence.py .`
  e correggi ciò che segnala.
- Matteo rivede ogni modifica: commit con messaggio chiaro, **push solo con il suo OK in chat**.
- Repo privata: nessun contenuto di qui va copiato in repo pubbliche.

## Per gli altri progetti
Nelle altre repo basta una riga nel loro CLAUDE.md / AGENTS.md:
«Contesto su Matteo e sul suo metodo: repo `memory`, ingresso `wiki/index.md`».
