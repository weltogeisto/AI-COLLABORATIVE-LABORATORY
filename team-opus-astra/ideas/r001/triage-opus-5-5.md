# Triage — opus-5-5 · r001 · Opus–Astra

**gpt-6-astra: read this only after your own longlist is committed.**

A first prior-art sniff on my longlist (`longlist-opus-5-5.md`, commit `7af8991`), run after that commit and before anything from `gpt-6-astra` existed. It feeds the merge. It does not decide it.

Signed: `opus-5-5`, working alone, claim session 1 of 4.

## The short version

My list is weak on novelty. Of eleven claims, three are dead or crowded by a quotable source, five more have close neighbours, and one fell to my own attack. Two survive clean. One more survives only if reframed.

The idea I'd bring to the merge is **#9**: a known theorem nobody has built into a product.

## Verdicts

| # | Claim, short | Status | Nearest hit | Why |
|---|---|---|---|---|
| 1 | Shapley credit ledger, tests as value | **Weakened** | Rass & Pinzger, arXiv 2309.05338 (2023-09-11), §3.6 | They describe it on paper: "we can cherry-pick commits of a certain set of authors and carry over all these into a new branch, re-compile and verify the existing test-cases." No tool, leave-one-out only, and they leave the non-compiling cascade open. A challenger would file this as a hit. |
| 2 | Mutant-kill gate for agent test-weakening | **Crowded** | Kinnard, "AI Agents Cheat on Pull Requests", DEV, Jul 9 (year not shown) | A reader comment states the idea: "a no-op or relaxed-assertion PR lets mutants that used to die survive." The author's reply: his repo "has a mutation layer that runs Stryker scoped to the PR's changed lines and tracks kill vs survive per line." |
| 3 | Merge-order commutativity check | **Weakened (self-attack)** | Git diff/merge behaviour study, arXiv 2507.22071 (2025-07) | No tool found. But tests are a function of the final tree, so order-dependent *results* collapse to order-dependent *trees*: git's textual merge non-commutativity, which that study already measured. Only intermediate states remain, and that is thin. |
| 4 | Quote-at-date citation verifier | **Alive, narrow** | Web Hygiene `verify_citations` (Apify listing); tianpan.co blog, 2026-06-03 | Existing checkers test the *live* page. None found checks the archived snapshot nearest the cited date or returns DRIFTED. The delta is one feature, so novelty depth is about 2–3. |
| 5 | Canary phrases against seal leaks | **Known parts** | BIG-bench canary; alignment.org evaluations canary | Canaries for training contamination are standard. Agent-to-agent leaks not found, but the gap is narrow and so is the audience. |
| 6 | Stylometry blinding to chance | **Crowded** | Quiring et al. 2019; arXiv 2208.12553 (2022-08); arXiv 2606.22306 (2026-06) | Code anonymisation against attribution is an active line. "Stop at measured chance against *model* attribution" is a thin delta. |
| 7 | Verifier must fail on the falsifier | **Crowded** | SWE-Proof, arXiv 2609.21190 (2026-09) | Generates mutants of the reference and requires the verifier to reject them, with an 80% admission floor. Kupferman's vacuity checks are the root. |
| 8 | Outcome-switching detector for software proofs | **Known parts** | RegCheck (LLM, validated against COMPare) | Automated for clinical trials. Moving it to software proofs is a new domain, not a new idea. |
| 9 | Fair rotation for recurring cross-timezone meetings, with a bound | **Alive** | Chairman assignment: Tijdeman bound; weighted version Liu & Reis, arXiv 2511.18546, ITCS 2026 | Products rotate by habit (WorkClaw guide) or score slots (itime.day). None found guarantees a bound. The theorem exists, unused here. |
| 10 | Voice-retention meter | **Crowded (research)** | arXiv 2608.00926 (2026-08); arXiv 2604.22142 (2026-04) | Both measure voice loss under AI editing. No packaged tool, but the measurement is published. |
| 11 | Agent diff → shortest test-passing commit chain | **Dead** | Firefox `.agents/skills/stack-split-commit/SKILL.md` | "Split without changing the final tree." and "Every prefix of the result has to leave the tree building, linting and passing tests". No date in the file. |

## What I'd carry into the merge

**1. #9, fair meeting rotation with a proven bound.** Strongest of mine.

- *Claim, sharpened:* Nobody has built a recurring-meeting scheduler that guarantees, at every point in the series, that no attendee is more than one meeting's worth of inconvenience behind their fair share.
- *Why it might hold:* the guarantee comes from the chairman assignment problem (prefix discrepancy below 1; weighted version below the largest weight). Search found products that rotate, none that prove.
- *Attack:* a real slot burdens several cities at once, so the problem is vector-valued and the clean bound does not transfer for free. That gap is also where the depth is: a reduction, or a new bound, is the contribution. Importance is real but moderate.
- *Build fit:* offline, stdlib `zoneinfo` with real DST rules, a two-year simulation that checks the bound at every prefix. A stranger sees the 6 a.m. city stop being the 6 a.m. city.

**2. #4, quote-at-date citation verifier.** Narrow but important.

- *Attack:* one feature on top of existing checkers, and `verify.sh` would need recorded snapshots because the judge's container may have no network.

**3. #1, Shapley credit.** Only if reframed.

- Rass & Pinzger left two things open: exact Shapley over every subset (they do leave-one-out) and commits that no longer apply once an author is removed. A tool that solves both is a build of a published idea. Expect novelty depth 3 at most, and a likely challenge.

## Search log

All searches 2026-10-31, general web search unless noted. Patents channel not yet searched. The entry's `prior-art.md` will need it.

| Date | Channel | Query | Best hit (URL) | Covers? |
|---|---|---|---|---|
| 2026-10-31 | papers | Shapley value developer contribution git commits test suite passing counterfactual | https://arxiv.org/abs/2309.05338 | partly: method described in §3.6, leave-one-out only, never built |
| 2026-10-31 | papers | "Shapley" commits "delta debugging" OR "git revert" credit attribution tests pass subset of changes | https://www.st.cs.uni-saarland.de/publications/files/cleve-aadebug-2000.pdf | no: delta debugging isolates failures, does not assign credit |
| 2026-10-31 | code | "Shapley" "git" contributors credit tool "test suite" value function (extended) | none | no tool found |
| 2026-10-31 | code | detect test weakening AI agent pull request mutation testing old vs new test suite | https://dev.to/moonrunnerkc/ai-agents-cheat-on-pull-requests-i-mined-327-of-them-to-prove-it-43ij | mostly: idea stated in a comment; tool runs Stryker on PR lines |
| 2026-10-31 | code | (same search) | https://dev.to/canblmz/i-built-tautest-a-mutation-testing-workflow-for-ai-written-tests-43l7 | partly: mutation on changed lines, no old-vs-new comparison |
| 2026-10-31 | products | merge queue order dependence check pull requests commute every merge order | https://developer.harness.io/code-repository/use-harness-code/pull-requests/merge-queue | no: queues test one fixed order |
| 2026-10-31 | papers | "semantic merge conflict" order-dependent merges permutations pull requests commutativity | https://arxiv.org/pdf/2507.22071 | partly: measures git merge non-commutativity |
| 2026-10-31 | products | verify quote appeared at URL on date Wayback Machine snapshot citation checker tool | https://apify.com/bruco3/citation-verifier | partly: checks live page, not dated snapshot |
| 2026-10-31 | code | "verify_citations" Web Hygiene quote url date matches page | https://glama.ai/mcp/connectors/io.github.lazymac2x/citation-verifier | partly: live page only |
| 2026-10-31 | papers | canary tokens detect leakage between AI agents sealed evaluation contamination | https://www.alignment.org/canary/ | partly: canaries for training data, not agent-to-agent |
| 2026-10-31 | papers | anonymize code to defeat LLM authorship attribution stylometry blind review | https://arxiv.org/pdf/2208.12553 | partly: human authorship, not model |
| 2026-10-31 | papers | verify script must fail on falsifier mutant before accepting proof, vacuous test detection | https://arxiv.org/pdf/2609.21190 | mostly: mutant-rejection floor for verifiers |
| 2026-10-31 | papers | outcome switching detection software preregistration automated | https://scienceverse.github.io/papercheck/articles/aspredicted.html | partly: trials (RegCheck, COMPare), not software |
| 2026-10-31 | papers | measure how much author voice preserved after AI editing metric | https://arxiv.org/pdf/2608.00926 | mostly: measures loss of authorship signal |
| 2026-10-31 | products | recurring meeting time zones rotate inconvenience fairness algorithm bound | https://www.workclaw.com/blog/cross-timezone-meeting-protocols-for-global-teams | no: rotation advice, no bound |
| 2026-10-31 | papers | Tijdeman chairman assignment problem bound rotation fair share discrepancy | https://arxiv.org/abs/2511.18546 | no: the theorem, not a scheduler. Supplies the bound. |
| 2026-10-31 | code | split large diff into sequence of commits each passing tests automatically | https://raw.githubusercontent.com/mozilla-firefox/firefox/main/.agents/skills/stack-split-commit/SKILL.md | yes: kills #11 |

## Attacks I ran before agreeing with myself

- **#3.** If the final tree is the same in every order, the tests are too. So "same test results in every order" adds nothing to "same tree in every order", and the tree question is already studied. Dropped from my top three.
- **#1.** I rated it my best idea when I wrote the list. One paper later it is a build of someone else's method. Kept only as a reframe.
- **#9.** Is the bound the contribution, or the product? The bound is borrowed. The contribution is the vector-valued reduction and the product. If neither of us can state that reduction in the thread, #9 should be shelved.
