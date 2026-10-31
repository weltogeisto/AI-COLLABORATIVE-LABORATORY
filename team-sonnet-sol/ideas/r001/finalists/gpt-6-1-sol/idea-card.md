---
id: r001-sonnet-sol-gpt-6-1-sol-01
round: 1
team: sonnet-sol
status: finalist
authors: [gpt-6-1-sol]
---

# Rollback Authority

## The claim

Nobody has built an offline checker for finite, permission-changing runbooks that classifies every executable forward prefix as recoverable, authority-locked, or unrecoverable within the declared recovery catalogue by comparing authorized and authorization-waived recovery, and exports replayable traces and closed-state-set certificates supporting those classifications.

This is a **novelty hypothesis**, narrowed from longlist item 1 after research.
The claimed contribution is the runbook diagnostic and its evidence contract.
State-space search, planning with delete effects, administrative access-control
analysis, and verified compensation already exist. The search and its limitations
are in [prior-art.md](prior-art.md), accessed 2026-10-31 throughout.

## Who needs it, and why now

An operations engineer is reviewing a deployment or credential-rotation runbook
before approving it. The backup still exists, but an intermediate step can remove
the very authority needed to restore it. A final-state check can miss a temporary
gap; a list of rollback commands cannot establish that their prerequisites remain
satisfied in the order they must run.

AWS already protects one important case: a KMS policy update normally preserves
the caller's ability to update the policy again
([PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html),
accessed 2026-10-31). The proposed use is a review aid across the explicitly modeled
steps and recovery actors. Demand beyond this plausible use case is unmeasured;
no customer interviews, incident-reduction results, or production guarantees are
claimed.

## How it works

1. Read a small JSON model: current facts and actor capabilities, ordered forward actions, permitted recovery actions, and an explicit recovery goal.
2. Replay the forward sequence with all guards enforced, retaining each executable prefix's complete state.
3. From each state, search the recovery graph with world and actor-specific authorization guards enforced.
4. Search again with only authorization guards waived; keep world guards, effects, actors, and the recovery catalogue identical.
5. Classify the prefix using the two reachability answers; identify the earliest authority-locked prefix if one exists.
6. Export an action/state trace for each positive answer and a successor-closed, goal-free state set for each necessary negative answer.
7. Check the evidence with a separate verifier that reconstructs forward states and transition rules without importing the search implementation.
8. Render a prefix table explaining the missing authority on the hypothetical waived trace; never execute a real command.

### Model and meaning fixed for the proof

The model is deterministic, sequential, fully observed, and closed-world. Its
state is a valuation of at most **12 Boolean atoms in total**, counting both world
facts and explicitly declared `(principal, capability)` pairs. There are at most
24 recovery actions and 16 forward steps. Each action names one fixed actor,
conjunctive positive/negative world guards, conjunctive required capabilities of
that actor, and atomic world add/delete plus capability grant/revoke effects.
Unmentioned atoms retain their value; absent atoms are false. Conflicting effects,
contradictory guards, unknown symbols, duplicate action IDs, malformed types, and
out-of-bound models are rejected. Capability names cannot be smuggled into world
guards. Principals' grants are never pooled.

The goal is a declared conjunction of positive/negative literals over world and
capability atoms; it can specify the original baseline or another agreed safe
state. It is identical in both searches. Recovery actions may repeat, and can
regrant authority or undo other recovery actions. The catalogue is explicitly
chosen: remaining forward actions are available during recovery **only if also
listed there**. All statements about impossibility are relative to this catalogue,
its actors, goal, and the supplied initial state.

For prefix state `s`, let `A(s)` mean that the goal is reachable using authorized
recovery actions and `W(s)` mean that it is reachable with authorization guards
waived. World prerequisites and all effects remain unchanged in `W`.

| A(s) | W(s) | Report | Evidence required |
|---|---|---|---|
| true | true | `RECOVERABLE` | Authorized recovery trace, possibly empty |
| false | true | `AUTHORITY_LOCKED` | Authorized negative certificate and hypothetical waived trace |
| false | false | `NO_DECLARED_RECOVERY` | Waived negative certificate; authorized edges are a subset |

The fourth Boolean combination is impossible under these semantics and is an
implementation error. An authority-locked result isolates the contribution of
authorization guards **within the model**; it is neither a unique real-world root
cause nor advice to bypass permissions. A waived trace is visibly hypothetical.
If a forward action cannot execute, report its index and failed guards, analyze
only the valid prefixes, and mark the overall runbook `INVALID_FORWARD`.

A negative certificate contains a finite set `C` of complete valuations with the
prefix state in `C`, no goal state in `C`, and every enabled recovery successor of
every member also in `C`, under the named search mode. These three checks prove
unreachability by induction. The verifier enumerates every enabled action at each
member; a list of blocked first actions alone is insufficient. Evidence binds to
the canonical model hash, semantics version, mode, and prefix index. This binds
artifacts to their inputs; it does not authenticate an operator or a real system.

## Nearest neighbours

The deltas below are readings of the cited sources, not proofs of absence.
All were accessed on **2026-10-31**; detailed source locations are in prior-art.md.

| What exists | Link | What it does | Delta |
|---|---|---|---|
| Joltrin `verify` | [Pinned source](https://github.com/SharedCode/joltrin/blob/a139ad7d1af5babf2c1d2105ba4312802264f315/verify/reachability.go) | Checks runbook rollback reachability using a graph of individual facts; its source documents the conjunctive-state limitation. | Complete mutable states, actor-specific revocation, and paired authorized/waived certificates. |
| VAC | [Author's tool documentation](https://www.southampton.ac.uk/~gp1y10/VAC.html) | Analyzes administrative RBAC role reachability, including counterexamples. | A strong reusable foundation; no inspected interface supplies this prefix-by-prefix recovery diagnosis and evidence bundle. |
| Action reversibility planning | [Morak et al., KR 2020](https://proceedings.kr.org/2020/65/kr2020-0065-morak-et-al.pdf) | Defines reverse plans and studies action reversibility in STRIPS. | No claim to invent reverse planning; the proposed contribution is its differential authorization diagnostic for runbooks. |
| AWS KMS lockout check | [API documentation](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html) | Normally retains the caller's ability to submit another key-policy update. | A single-operation guard, rather than this supplied multi-step recovery model. |
| Compensation correctness | [Vaz and Ferreira, 2012](https://repositorio.ipl.pt/server/api/core/bitstreams/c27d9d25-be37-4d30-a429-a2be7d91ce07/content) | Formal compensation correctness and automated checking with ProB. | The inspected calculus checks compensation behavior; it does not present this differential actor-authority report. |

## Proof plan (pre-registered)

Fixed in the Claim turn on **2026-10-31**, before any implementation or experiment.
This submission contains design and research only. The following are promised
checks for a later Proof turn, not results already obtained.

- **Smallest build that shows the claim:** Python 3.11+ standard-library CLI, strict JSON loader, exact finite-state search, separate evidence verifier, named fixtures, and a plain HTML or terminal prefix report. All future code belongs under `team-sonnet-sol/builds/r001/`. No cloud integration, natural-language parser, or live credentials.
- **Time-box:** at most six Proof sessions, matching round.toml: one for frozen fixtures/reference semantics, three for checker and evidence, one for the demonstration, one for adversarial verification. No extension is assumed.
- **Reproduction command:** from a clean clone, `bash team-sonnet-sol/builds/r001/verify.sh`; no network or secrets. Exit 0 only after every required check below passes; a model labeled unsafe is a correct test outcome when expected.
- **It works if:** every valid prefix in the named fixtures receives exactly the registered classification; all positive traces replay and all negative certificates pass independent closure checking; all 256 generated models agree with an independently implemented exhaustive oracle; forged evidence is rejected; the report exposes the earliest authority-only lockout even when the final prefix is recoverable.
- **It is falsified if:** one valid supported model has an accepted authorized trace with a missing guard, an accepted negative certificate with a reachable goal, a false `RECOVERABLE`/`AUTHORITY_LOCKED`/`NO_DECLARED_RECOVERY` classification, an incorrect earliest lockout index, or an oracle disagreement. Any one is a failure, not an averageable error rate. A complete prior-art match independently falsifies novelty even if the software works.

### Fixed adversarial fixtures

All nine cases are required. Names identify the scenarios to be materialized in
the first Proof commit before the main search implementation is written.

| Fixture | Required observation |
|---|---|
| `revoke_restore` | Prefix 0 already meets the goal; deployment is recoverable; revoking the operator's restore capability makes the next prefix `AUTHORITY_LOCKED` while the backup remains. |
| `break_glass_regrant` | Add an explicitly authorized second actor who can regrant the operator's restore permission: the same post-revocation state is `RECOVERABLE` through regrant then restore, despite the direct restore being blocked. |
| `split_actor_capabilities` | Two capabilities needed by one recovery action are split between two principals, with no transfer action: `AUTHORITY_LOCKED`; combining their grants would be a false positive. |
| `deleted_backup` | Destroy the only backup after deployment, with no recreation action: `NO_DECLARED_RECOVERY` even though restore authority remains. |
| `conjunctive_world_guard` | A restore needs both backup and key; the key is absent and has no producer: `NO_DECLARED_RECOVERY`, despite an individual-fact edge from backup to restored. |
| `self_revoking_undo` | The only world-feasible recovery sequence revokes a capability that a later recovery action requires: `AUTHORITY_LOCKED`; initial permission preflight must not call it recoverable. |
| `temporary_gap` | A valid forward sequence has recoverable, authority-locked, then recoverable prefixes. A later scheduled forward grant is excluded from the approved recovery catalogue; the report must state that exclusion and still show the earlier gap. |
| `recovery_cycle` | Recovery actions can cycle without reaching the goal even with authorization waived: finite termination and `NO_DECLARED_RECOVERY`, with a genuine closed-set certificate. |
| `blocked_forward` | The next forward action lacks authority: valid earlier prefixes are reported, the blocked step is `INVALID_FORWARD`, and no later state is invented. |

The `temporary_gap` exclusion is a modeling assumption, not a claim that no human
could continue forward. A companion variant explicitly adds that grant to the
recovery catalogue and must become recoverable. The goal remains fixed across
these variants.

### Oracle, evidence attacks, and delivery checks

The first Proof commit freezes 256 generated models using seeds 0 through 255,
with two to five total atoms, at most eight recovery actions, two named actors,
and zero to four executable forward steps. Generation must not filter cases
using the implementation's classifications. A separate reference implementation
uses sets/tuples, enumerates all valuations, constructs both complete adjacency
matrices, and computes transitive closure to compare reachability at every prefix.
The main search uses state bitsets and graph traversal. The reference and verifier
must not import the main transition or search routines. Same-author independent
implementations are error checks, not independent scientific replication.

For every emitted evidence bundle, the verifier recomputes its forward prefix.
Required attacks: alter the bound model or prefix; remove a necessary closure
member; insert a goal into a negative set; forge a successor; use another actor's
capability on a trace; and submit a waived trace as authorized. Each invalid
bundle must be rejected. Unknown symbols, conflicting effects and models above
the 12-atom bound must produce explicit input errors, never a safe verdict.

A five-minute walkthrough must show `revoke_restore`, `deleted_backup`, and the
break-glass repair side by side, including their assumptions and certificates.
No latency, scale, usability-study, or incident-reduction threshold is claimed.

## Risks and kill criteria

- **Nearest-neighbour risk:** a planner, policy-analysis tool, paper, product, or patent that already supplies the full stated differential runbook diagnosis and evidence is a kill. Generic expressibility alone establishes that the underlying algorithm is known; it substantially limits novelty depth.
- **Model fidelity:** omitted recovery actors, undeclared policy conditions, or inaccurate effects can manufacture a lockout. Every report must expose the catalogue, goal, actors, and model bound. The prototype does not parse AWS IAM or certify actual infrastructure.
- **Limited failure model:** only interruption between atomic, successful modeled actions is covered. Partial API effects, concurrent administrators, eventual consistency, time, stochastic failure, and corrupted backups are outside this proof unless encoded as explicit finite states/actions; no general support is promised.
- **State explosion:** the bound is part of the contract. If exact checking and independently verifiable evidence cannot be delivered within it and the six sessions, stop with an incomplete result; do not substitute a heuristic or treat search exhaustion as unreachability.
- **Value risk:** if the examples require contrived catalogue omissions and the ordinary revocation/regrant cases add no useful information beyond existing tools, shelving is preferable to claiming a new general theory.
