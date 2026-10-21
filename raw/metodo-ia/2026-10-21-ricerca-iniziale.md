# 2026-10-21 ricerca-iniziale

> Source: Io-Claude/Metodo-IA/ricerche/2026-10-21_ricerca-iniziale.md (PC di Matteo)
> Collected: 2026-10-21
> Published: Unknown
> Ultima modifica originale: 2026-10-21

# Ricerca iniziale — metodo di lavoro con IA (21/10/2026)

> Materiale grezzo per la futura wiki. Tre ricercatori (Sonnet) + sintesi della chat principale.
> Affidabilità: A = fonte ufficiale/primaria · M = README, blog esperti · B = casi singoli.
> Nulla di questo è stato provato sul campo: sono letture.

## Contesto misurato (dai file di Matteo)
- MSS: 8 blocchi «Direzione nuova» in HANDOFF §0 tra 12/10 e 21/10; due decisioni diverse numerate `0027`.
- `misure/costi-lotti.md`, lotto 14/10: 43 punti di quota della finestra 5h per ~1M token di sotto-agenti; una finestra ≈ 1,8M token di sotto-agente.
- Documenti md: MSS 358 file / 660k parole (senza worktree); CalendarBackup ~2.300 file / 3,8M parole (840 report di sessione, 972 in Archives); Io-Claude 30 file / 76k parole. Totale ~4,6M parole ≈ 11× la scala della wiki di Karpathy.

## 1. Metodo per definire un progetto
- Strumenti «spec-driven» (Spec Kit, Kiro, BMAD, OpenSpec, Agent OS, Tessl): tutti producono molta documentazione; BMAD = 12-16 h di piano prima del codice. Böckeler/Fowler: Kiro trasforma un bug piccolo in 4 user story e 16 criteri. Thoughtworks Radar: «Assess». → Rischio di rifare l'errore MSS. [A] https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html · https://www.thoughtworks.com/en-au/radar/techniques/spec-driven-development
- Nativo e gratuito: Claude Code plan mode + «intervista» che scrive SPEC.md, poi sessione nuova; Codex plan mode + PLANS.md. [A] https://code.claude.com/docs/en/best-practices · https://learn.chatgpt.com/guides/best-practices
- Criteri pronti: ISO/IEC 25010:2023 (9 caratteristiche: adeguatezza funzionale, efficienza, compatibilità, capacità di interazione, affidabilità, sicurezza, manutenibilità, flessibilità, safety) [M, riassunto arc42] https://quality.arc42.org/standards/iso-25010 ; costi/valore: quattro rischi di Cagan (valore, usabilità, fattibilità, sostenibilità) [A] https://svpg.com/four-big-risks/
- Criteri di Matteo → nomi tecnici: «parallelizzabile» = modularità / basso accoppiamento (Carlini, Anthropic: test indipendenti si parallelizzano, un compito gigante no) [A] https://anthropic.com/engineering/building-c-compiler ; «aggiungere senza cancellare» = principio aperto/chiuso [A] https://blog.cleancoder.com/uncle-bob/2014/05/12/TheOpenClosedPrinciple.html
- Altri criteri utili con agenti: verificabilità (controllo eseguibile), leggibilità in poco contesto, interfacce esplicite (Pocock https://www.aihero.dev/how-to-make-codebases-ai-agents-love), fetta piccola, niente duplicati, recuperabilità, confini sempre/chiedi/mai (Osmani https://addyosmani.com/blog/good-spec/), file di istruzioni corto, costo d'uso, reversibilità.
- Pre-mortem di Klein (20-30 min: «è fallito, perché?») [A] https://www.psychologytoday.com/ie/blog/seeing-what-others-dont/202101/the-pre-mortem-method
- Overplanning: «spec-first è waterfall con battitura migliore; non puoi specificare un ignoto» (Butler) [M] https://world.hey.com/johnnybutler/spec-first-ai-is-just-waterfall-with-better-typing-35a91a66 ; Scrum.org: checklist esaustive diventano waterfall [M] https://www.scrum.org/node/14779
- Prototipo: «il prototipo è il tuo documento dei requisiti, non la prima versione» (McGuinness) [M]. Si tiene ciò che ha validato (regole, casi limite, flusso), il codice si butta.
- Nessun modello pronto per «a tre livelli di rischio»: è una costruzione di Matteo.

## 2. Memoria e contesto (LLM wiki)
- Gist di Karpathy (apr 2026): raw/ immutabile, wiki/ scritta dall'LLM, file di regole; operazioni ingest/query/lint; index.md + log.md; regge ~100 fonti. [A] https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Implementazioni: Astro-Han/karpathy-llm-wiki (skill, MIT, 1,6k stelle, Claude Code + Codex, nessun server) [M] https://github.com/Astro-Han/karpathy-llm-wiki ; lucasastorian/llmwiki (server MCP) ; akitaonrails/ai-memory (hook automatici, Windows solo WSL2, rischio note vecchie) ; Basic Memory (MCP, AGPL, cloud 15 $/mese).
- Anthropic, context engineering: «il più piccolo insieme di token ad alto segnale»; riferimenti leggeri + caricamento a richiesta; sotto-agenti restituiscono 1-2k token. [A] https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Claude Code: CLAUDE.md < 200 righe; gli @import NON riducono il costo; usare CLAUDE.md nelle sottocartelle e skill. [A] https://code.claude.com/docs/en/memory
- Codex: AGENTS.md concatenati, tetto 32 KiB; «corto e preciso batte lungo e vago»; aggiungere regole solo dopo errori ripetuti. [A] https://developers.openai.com/codex/learn/best-practices.md
- Studio ETH (arXiv 2602.11988): i file di contesto spesso non aumentano il successo e alzano i costi >20%; quelli generati dall'LLM peggio; servono solo informazioni non deducibili. [A] https://arxiv.org/abs/2602.11988
- Rischio deriva: i riassunti perdono dettagli e vengono riletti come fonti. Contromisure: raw immutabile, ogni pagina con data e fonte, ricostruire dagli originali quando conta. [M] https://foundanand.medium.com/the-hidden-flaw-in-karpathys-llm-wiki-e3a86a94b459
- Architettura proposta: repo privato «memoria» (raw/ + wiki/), un solo AGENTS.md (CLAUDE.md = @AGENTS.md), puntatore cortissimo da ogni repo, skill in .claude/skills/ e .agents/skills/, partire da 20-30 documenti, Matteo rivede il diff.

## 3. Costi e controlli
- Claude Pro: finestra 5h + limite settimanale, chat e Claude Code stesso serbatoio; nessun numero pubblico. Opus «usa molta più quota», costa «diverse volte» Sonnet per turno. [A] https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code
- Su Pro il modello predefinito di Claude Code è Opus; i sotto-agenti ereditano il modello; Explore gira su Opus. [A] https://code.claude.com/docs/en/model-config · https://code.claude.com/docs/en/sub-agents
- Risparmio: Sonnet di base, `opusplan`, CLAUDE_CODE_SUBAGENT_MODEL (+ _FORCE=1), /clear tra compiti, /compact nelle pause, MCP inutili spenti, /usage settimanale; agent teams ≈ 7× token; attività ricorrenti rimandano tutto il contesto ogni volta. [A] https://code.claude.com/docs/en/costs
- Codex Plus: limite 5h tornato il 25/8/2026 (stampa); stime messaggi in https://learn.chatgpt.com/docs/pricing
- Controlli a zero token: «CLAUDE.md è consultivo, gli hook sono deterministici: se una regola viene ignorata, trasformala in hook o test». Hook PreToolUse (blocca comandi), PostToolUse (formatta), Stop (test verdi prima di chiudere). [A] https://code.claude.com/docs/en/hooks ; pre-commit https://pre-commit.com/ ; GitHub Actions (2.000 min/mese privati, piano Free).
- Fonti da seguire: Anthropic Engineering, doc Claude Code, OpenAI Codex docs, Simon Willison, Armin Ronacher, Hamel Husain, Pragmatic Engineer, Latent Space; awesome-claude-code solo come elenco da verificare. Da evitare: numeri senza link ufficiale, «N trucchi», siti che vendono un prodotto (es. ClaudeLog contraddice la doc ufficiale).

## Non verificato
Moltiplicatori Opus/Sonnet su Pro; se le attività pianificate pesano sulla stessa quota (probabile); hook bash su Windows; Codex da telefono che legge la repo; licenze di Kiro/Tessl/Agent OS; nessuno strumento è stato provato.
