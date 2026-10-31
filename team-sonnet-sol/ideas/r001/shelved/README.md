# Shelved — sonnet-5-5, round 001

What the longlist's other claims did under a first search. One query each, unless stated. All run 2026-10-31. "Killed" means the claim as worded is already built. "Runner-up" means the gap held and the idea lost on proof or reach.

| # | Claim (short) | Fate | Why | Evidence |
|---|---|---|---|---|
| 1 | Search receipts | **Developed.** See `../finalists/sonnet-5-5/` | Gap held after a full four-channel search | |
| 2 | Instruction coverage for AGENTS.md | Runner-up | No dedicated tool found. Ablation studies and a practitioner protocol exist. The proof would need live agent runs, which `verify.sh` cannot do offline | https://arxiv.org/html/2601.20404 · https://eth-sri.github.io/publications/gloaguen2026agentsmd · https://developertoolkit.ai/en/shared-workflows/context-management/pruning-context-files/ |
| 3 | Crux maps from model disagreement | Killed, mostly | An open-source project already outputs a map of disagreement with cruxes. A plan for a crux graph with "what would change my mind" fields exists. A preprint defines cruxes over model rollouts (identified in results, not matched to a URL) | https://github.com/yilgara/agora · https://www.longtermwiki.com/internal/cairn-vision |
| 4 | Expiring decisions | Runner-up | No tool found that monitors ADR revisit triggers. Practitioners write "revisit if" clauses and check by hand. The idea is incremental, and the importance is modest | https://dev.to/alexandreamadocastro/stop-architecture-drift-operationalizing-adrs-with-automated-fitness-functions-22oi · https://eprints.ost.ch/id/eprint/1381/1/MSE-Master-Thesis_ADE_Raphael-Schellander.pdf |
| 5 | Cross-vendor usage-window scheduler | Killed | Community tools already read Claude and Codex quota windows and route work between them | https://pypi.org/project/ccswap/ · https://pypi.org/project/windowping/ · https://skillselion.com/skills/PocketConservatory/plugins/subtask |
| 6 | Timelocked sealed phases | Killed | The pattern exists: drand timelock with commit-reveal for agents (Tacet), validators (Bittensor), and a sealed-message service (qub) | https://hackquest.io/projects/Tacet · https://www.bittensor.com/docs/guides/timelock |
| 7 | Idea-collision matrix | Not probed | Likely adjacent to research on homogeneity across models. A by-product of this round's four longlists, worth computing in the retro | |
| 8 | Review-surface metric | Not probed | Semantic-diff and refactoring-aware review tools exist. High risk of prior art | |
| 9 | Claim diff | Not probed | | |
| 10 | Non-goal enforcement | Not probed | Architecture fitness functions are close | |
