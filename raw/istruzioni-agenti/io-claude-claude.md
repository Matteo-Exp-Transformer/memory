# CLAUDE

> Source: Io-Claude/CLAUDE.md (PC di Matteo)
> Collected: 2026-10-21
> Published: Unknown
> Ultima modifica originale: 2026-10-10

# CLAUDE.md — Mappa di lavoro di Matteo (leggi per primo)

> File d'ingresso per qualunque agente Claude (desktop, mobile, Cowork, Claude Code).
> Scopo: avere lo **stesso contesto** ovunque. Creato il 28/09/2026.

## Le 3 aree di lavoro (sul PC "mio", Windows)

| Area | Percorso Windows | Cosa contiene |
|---|---|---|
| **Io-Claude** | `C:\Users\matte.MIO\Documents\Io-Claude` | Documentazione personale di Matteo (profilo, crescita professionale, handoff tra agenti) |
| **GitHub** | `C:\Users\matte.MIO\Documents\GitHub` | Tutti i progetti/repo di codice |
| **Download** | `C:\Users\matte.MIO\Downloads` | Zona di passaggio: file scaricati, allegati, input grezzi |

In `device_bash` le trovi sotto `$HOME/mnt/<cartella-collegata>/...`.
Se una di queste cartelle **non** è collegata alla sessione, chiedila con
`device_request_folder_access` usando esattamente i percorsi sopra.
Altre aree del PC: solo se Matteo le autorizza di volta in volta.

## Punti d'ingresso (non navigare a tappeto)

- ⭐ **MSS (MetaSkillSystem) — focus dal 28/09/2026**, dal 07/10 sul **sistema di agenti** (Claude + Codex) → `GitHub\MSS\CLAUDE.md` → `HANDOFF.md` §0
- 🌱 **Esplorazione e lettura di Matteo (fissato il 10/10/2026)** — Matteo usa l'IA per esplorare sé stesso, l'IA e il mondo professionale. **Prima di ogni chat di ragionamento** leggi `Io-Claude\Esplorazione\LETTURA_MATTEO.md` § «In 30 secondi» (come leggerlo e quali manovre usare; a fine chat una riga nel suo registro). Poi, se serve: `MODO_ESPLORAZIONE.md` (storia → fondamenta → gioco → mossa), `MAPPA_ESPLORAZIONI.md` (temi esplorati), `DIREZIONE.md` (figure professionali a confronto)
- **Crescita professionale / candidature / CV** (⏸️ candidature in pausa dal 28/09) → `Io-Claude\Crescita professionale\CLAUDE.md`
- **App HACCP / gestionale (CalendarBackup-v2)** → `GitHub\CalendarBackup-v2\docs\APP_CONTEXT_SKILL.md` §0
- **Trading** → `GitHub\Trading-Platform-main\CLAUDE.md`, `GitHub\Trade-Analyst-Agent`
- **Libri per bambini (KDP)** → `GitHub\Libri Bambini\CLAUDE.md`
- **BHM** → `GitHub\BHM-Zen\CLAUDE.md`
- **Prenotazioni ristoranti** → `GitHub\PrenotaZen`
- Ogni repo con un proprio `CLAUDE.md` ha la precedenza su questo file per il suo contenuto.

## Regole operative

1. **Leggere**: libero in tutte e 3 le aree.
2. **Scrivere/modificare**: sì, nella cartella dove sta il file. Modifica un file esistente
   solo se Matteo lo chiede; versioni trasformate → file nuovo accanto all'originale.
3. **Cancellare**: mai senza conferma esplicita. Nel dubbio sposta in `_to_delete\`.
4. **Git**: non toccare `.git\`; commit/push solo su richiesta.
5. **Download**: è un'area di input. Gli output finali non restano lì: vanno nel progetto
   giusto (GitHub\…) o in Io-Claude, salvo richiesta diversa.
6. **Handoff**: a fine lavoro aggiorna il file di handoff del binario, annotando già le
   decisioni che puoi prendere tu; lascia aperto solo ciò che dipende da fatti non disponibili.
7. Lingua: italiano, dando del tu.
