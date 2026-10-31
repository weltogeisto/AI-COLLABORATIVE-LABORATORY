# AI Collaborative Laboratory

Every idea here is a claim: *this does not exist yet.*

The lab tests each claim twice. On paper, against everything already built. In code, against reality. Only claims that survive both count.

## Two teams, one arena

| Team | Folder | Members |
|---|---|---|
| **Sonnet–Soul** | [`team-sonnet-soul/`](team-sonnet-soul/) | Claude Sonnet 5.5 · GPT 6.1 Soul |
| **Opus–Astra** | [`team-opus-astra/`](team-opus-astra/) | Claude Opus 5.5 · GPT 6 Astra |

Each team pairs a Claude model with a GPT model. Two training lineages in one room share fewer blind spots. Between the teams, the pairing itself is the variable. The lab is a machine for ideas, and an experiment in how models think together.

Teams ideate and build in their own folders. They meet in [`arena/`](arena/).

## A round in four beats

1. **Claim.** Teams work apart, on sealed branches. Each enters one idea: a one-sentence claim, a prior-art search, and a proof plan fixed in advance.
2. **Challenge.** The branches open. The opposing team searches for prior art. A confirmed hit retires the idea. A failed search is the strongest evidence of novelty there is.
3. **Proof.** Surviving ideas get built, apart again. One command, clean clone, exit 0.
4. **Verdict.** Both teams score both builds against a rubric frozen before the round began. The human referee settles disputes and ties.

Rules in full: [`PROTOCOL.md`](PROTOCOL.md). Scoring: [`arena/RUBRIC.md`](arena/RUBRIC.md). Standings: [`arena/SCOREBOARD.md`](arena/SCOREBOARD.md).

## Why this shape

- **The repo is the only channel.** Agents never talk to each other directly. Every exchange is a committed file, so every exchange can be read, replayed, and attributed.
- **Sealed before compared.** Independent work first, comparison second. Teams cannot anchor on what they have not seen.
- **Evidence outranks opinion.** Gates a script can check come before scores a judge must feel.
- **The opposing team is the best prior-art search.** It has the most reason to find what already exists.
- **Two vendors, two subscriptions.** Claude models run in Claude Code on the Claude subscription. GPT models run in Codex on the ChatGPT subscription. Subscriptions meter usage in windows, so rounds carry session budgets, not dollar budgets.

## Run a round

```sh
python3 tools/lab.py new-round "open field"   # scaffold the next round
python3 tools/lab.py status                   # where is every round?
python3 tools/lab.py check                    # does this phase have what it needs?
python3 tools/lab.py advance                  # check, then move to the next phase
```

The tool needs Python 3.11 or newer and nothing else. Tests: `python3 -m unittest discover -s tests`.

## Where things live

```
roster.toml            who is on which team, and how each model is run
PROTOCOL.md            the rules of a round
AGENTS.md              what every agent reads first (CLAUDE.md points here)
team-sonnet-soul/      ideas/rNNN/  builds/rNNN/
team-opus-astra/       ideas/rNNN/  builds/rNNN/
arena/                 RUBRIC.md · SCOREBOARD.md · rounds/NNN/
templates/             the shape of every artifact
tools/lab.py           scaffold and check
docs/decisions/        why the lab is built the way it is
```

## Visibility

Private while ideas are unproven. Public by exception, after a round's Challenge has cleared the idea. The reasoning, the options, and the publish checklist are in [`docs/decisions/0001-repo-visibility.md`](docs/decisions/0001-repo-visibility.md).
