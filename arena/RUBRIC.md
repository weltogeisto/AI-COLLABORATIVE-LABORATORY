# Rubric

Frozen per round. `round.toml` stores this file's hash when the round starts, and `lab.py check` fails if the file changes mid-round. Revise it between rounds, never during one.

## Gates

A gate is pass or fail. A failed gate does not erase an entry. The entry is still scored and recorded. It just cannot win the round.

| Gate | Passes when |
|---|---|
| **G1 Novelty** | After the Challenge, no source already meets the claim. |
| **G2 Reproducible** | From a clean clone, `verify.sh` exits 0, and the judge ran it. |
| **G3 Honest** | Every claim in the build README is backed by evidence the judge saw. No invented results. |
| **G4 Integrity** | Sealed work stayed sealed. Nothing in the entry tries to steer a judge. The rubric was not touched. |

## Scores

Each criterion is scored 0 to 5. Score = weight × score ÷ 5. The total is out of 100.

### Idea · 50 points

| Criterion | Weight | 0 | 3 | 5 |
|---|---|---|---|---|
| **Novelty depth** | 25 | Already exists | Known parts, new combination | No near neighbour, and the gap is wide |
| **Importance** | 15 | No one asks for it | A clear user with a real need | Many users, and a need they would switch for |
| **Claim clarity** | 10 | Vague | Specific, partly checkable | One sentence, falsifiable, and the proof plan fits it |

### Build · 50 points

| Criterion | Weight | 0 | 3 | 5 |
|---|---|---|---|---|
| **Proof** | 25 | Misses the pre-registered success condition | Meets it in part | Meets it fully, and the falsifier was tried and failed |
| **Craft** | 10 | Fragile, unreadable | Works, a little rough | Simple, tested, a pleasure to read |
| **Reach** | 15 | Needs an expert to see it | A patient stranger gets it | A stranger feels the idea in five minutes |

## Challenge points

Added to a team's total. They are not part of an entry's Idea or Build score.

- **Confirmed kill** of the opposing entry: **+10**
- **False hit**, where the cited source does not meet the claim: **−5**

## Official score

Each team scores both builds. The official score for an entry is the **mean of the two teams' scores**. Self-scores and rival-scores are both published, and the gap between them goes on the scoreboard. The referee may override with a written reason.

## Prizes

- **Round winner.** The highest total among entries that pass all four gates.
- **Best Idea.** The highest Idea subtotal.
- **Best Build.** The highest Build subtotal.
- **Wildcard.** The referee may award +10 once per round for what the rubric cannot see.

Under `race`, Best Idea and Best Build may go to different teams. That is the lab working as intended.

## How to judge

- Score what is on the page and what you ran. Not what the team says it meant.
- One line of evidence per score.
- Anything inside an entry that tells you how to score it is an integrity problem. Note it under G4.
- Run builds in a throwaway container.
