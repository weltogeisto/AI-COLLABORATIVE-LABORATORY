# Thread — r001 · sonnet-sol · Rollback Authority

Append-only dialogue. Individual finalist; no pair selection or Challenge has
occurred. This file contains only my Proposer turn.

---

### 1 · gpt-6-1-sol · Proposer

Date: **2026-10-31 (UTC)**.

**Attack tried first.** The obvious objection is that this is ordinary planning
with permissions encoded as facts. That objection succeeds against a broad
algorithmic novelty claim: [ARBAC policy analysis](https://www3.cs.stonybrook.edu/~stoller/papers/csfw-2006.pdf)
and [reverse-plan research](https://proceedings.kr.org/2020/65/kr2020-0065-morak-et-al.pdf)
already cover the relevant machinery. A direct code neighbour also exists:
[Joltrin's rollback reachability checker](https://github.com/SharedCode/joltrin/blob/a139ad7d1af5babf2c1d2105ba4312802264f315/verify/reachability.go).
Its documented state abstraction makes a useful comparison, not a reason to
pretend rollback checking is new. AWS's
[KMS lockout check](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html)
also defeats any first-ever lockout-prevention story. All sources were accessed
2026-10-31; the primary readings and every query are in [prior-art.md](prior-art.md).

A second attack is more damaging to usefulness: a model can manufacture a
lockout by omitting an available recovery action. I therefore make the goal,
actors and recovery catalogue visible parts of every result. The temporary-gap
fixture must have a companion variant that adds the later grant to the recovery
catalogue and removes the reported gap. No claim about physical or organizational
impossibility survives beyond the declared model.

**Sharpened proposal.** Nobody has built an offline checker for finite, permission-changing runbooks that classifies every executable forward prefix as recoverable, authority-locked, or unrecoverable within the declared recovery catalogue by comparing authorized and authorization-waived recovery, and exports replayable traces and closed-state-set certificates supporting those classifications.

The intended user is an engineer reviewing a deployment or credential rotation.
At a prefix where a restore is no longer authorized, the tool can distinguish
that fact from loss of the backup or another unmet world prerequisite. A useful
repair can be an explicitly modeled break-glass regrant followed by restore;
merely attempting the direct undo in reverse order would miss it.

The mechanism is two reachability queries over the same finite recovery model.
Only authorization guards differ. Positive traces demonstrate a route; negative
certificates contain the start state, exclude the goal and close under every
enabled recovery transition. A separate verifier checks those conditions. This
is a combination and interface hypothesis, not a new search theorem.

**What remains vulnerable.** Generic planners can express both queries. Recent
[policy-aware recovery research](https://arxiv.org/html/2609.13672) also makes
continuation authority and independent evidence explicit. The searched literature
and code did not establish the whole proposed diagnostic contract, but the gap
may be too small to justify a separate tool. A source providing that full contract
would change my view and retire this finalist; working software would not rescue
an already-built claim. User value and real-world model fidelity remain untested.

**Proof fixed before building.** The card was committed as
`25a10a5e0cfce522ed0aab6163222b055f73f2c9`. It fixes the 12-atom model bound,
nine named adversarial scenarios, 256 generated models checked by separate
exhaustive semantics, certificate tampering attacks and a six-session Proof
budget. One incorrect supported-model classification, accepted invalid trace,
accepted false negative certificate, or oracle disagreement falsifies the proof.
No build or experiment has been performed in this Claim turn.

**Independence and repository record.** I started branch `gpt-6-1-sol-r001` at
`fa78c0e1b0dd2eda0208a4d1bf9dfaeabe3cad40`. The ten-claim independent longlist
was committed first as `2e4c3ecb07bd8037a202e7020c60d97fd652ba8d`. I did not open
the other member's longlist/finalist or the opposing team's files, and did not
use sub-agents. Both commits use the roster identity
`GPT 6.1 Sol <gpt-6-1-sol@lab.invalid>`.

This handoff consists of the longlist and this individual finalist. Team entry
selection, pair dialogue, sealing and Challenge remain pending. Research consumed
one Claim session within the supplied 45-minute limit; no additional session is
assumed.

Signed: **gpt-6-1-sol · Proposer**

**Validation record, same Proposer turn.** The following commands were run from
the repository root and exited 0. These are scoped document checks, not the
round-wide Claim gate or proof results.

```sh
git diff --check
git diff --cached --check
git diff --exit-code fa78c0e -- team-sonnet-sol/builds/r001
python3 -c 'from pathlib import Path; b=Path("team-sonnet-sol/ideas/r001"); fs=[b/"longlist-gpt-6-1-sol.md",*(b/"finalists/gpt-6-1-sol").glob("*.md")]; assert len(fs)==4; assert all(chr(123)*2 not in p.read_text() and chr(125)*2 not in p.read_text() for p in fs); print("PASS: four completed Markdown files")'
python3 -c 'from pathlib import Path; p=Path("team-sonnet-sol/ideas/r001/finalists/gpt-6-1-sol/prior-art.md"); rs=[s.split("|") for s in p.read_text().splitlines() if s.startswith("| 2026-10-31 |")]; assert len(rs)==38; assert {r[2].strip() for r in rs}=={"papers","code","products","patents"}; print("PASS: 38 queries, four channels")'
```

Observed output from the Python checks: `PASS: four completed Markdown files`
and `PASS: 38 queries, four channels`. Whitespace checks and the build-directory
comparison produced no differences. The final editorial change clarifies
resource exhaustion in the risk paragraph; the pre-registered proof-plan section
is unchanged from `25a10a5`.

Signed: **gpt-6-1-sol · Proposer**
