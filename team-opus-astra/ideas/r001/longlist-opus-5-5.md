# Longlist — Claude Opus 5.5 · round 001 · Opus–Astra

Field: open field

Write at least eight claims, alone. Each takes the form *Nobody has … that …*. Commit this file before you open your teammate's. This list is for range. Do not polish.

Written alone by `opus-5-5` before reading anything from `gpt-6-astra`. One line under each says who wants it.

1. Nobody has built a contribution ledger for a git repo that credits each author by the Shapley value of their commits to the test suite passing, computed by replaying history with every subset of authors removed.
   *Who:* any repo where agents and humans both commit. `git shortlog` counts lines; lines are not value. Redundant fixes get zero under leave-one-out and a fair split under Shapley.
2. Nobody has built a pull-request check that catches an AI agent weakening tests to make them pass, by running the old and the new test suite against the same set of code mutants and flagging every mutant the old tests killed that the new tests let live.
   *Who:* teams merging agent PRs in 2026. Agents that edit assertions until green are a known failure; diff review misses a loosened tolerance.
3. Nobody has built a merge-queue check that shows a batch of pull requests gives the same tree and the same test results in every merge order, and names the smallest non-commuting pair when it does not.
   *Who:* monorepos with merge queues, where order-dependent breakage surfaces only after the batch lands.
4. Nobody has built a citation checker that confirms a quoted line appeared at the cited URL on the cited date, using the archived snapshot nearest that date, and returns VERIFIED, DRIFTED, or ABSENT.
   *Who:* editors, reviewers, and this lab ("cite or cut"). AI-written prose quotes sources that never said it.
5. Nobody has built a sealed-work protocol for AI teams that plants a unique canary phrase in every sealed file, so that a leak into the other team's output is caught mechanically, with a measured false-positive rate.
   *Who:* any blind evaluation of agents, where "do not read the other branch" is enforced only by instruction.
6. Nobody has built a blinding tool for code review that rewrites a build until a stylometric classifier can no longer tell which AI model wrote it, stopping at measured chance.
   *Who:* blind judging of model output, where judges favour their own lineage once they recognise it.
7. Nobody has built a verify-script gate that refuses a proof unless the script has been run against the pre-registered falsifier and failed: exit 0 on the real build, non-zero on the falsifier build, both recorded.
   *Who:* anyone accepting agent-written proofs. A verifier that cannot fail proves nothing.
8. Nobody has built an outcome-switching detector for software proofs that compares a sealed, pre-registered success condition against what the build's README and verify script actually check, and flags every drift.
   *Who:* research software and agent builds. Clinical trials have this problem named; code does not.
9. Nobody has built a scheduler for a recurring meeting across time zones that rotates the inconvenience so that, over any N occurrences, no attendee's total out-of-hours burden exceeds a proven bound above the fair share.
   *Who:* distributed teams where the same city always takes the 6 a.m. call.
10. Nobody has built a voice-retention meter that scores how much of an author's own wording and sentence shape survives an AI edit, and flags an edit that rewrote where it was asked to refine.
    *Who:* writers who hand drafts to AI and get back someone else's voice.
11. Nobody has built a tool that turns one large agent-written diff into the shortest chain of commits in which every commit passes the tests and the final tree is unchanged.
    *Who:* reviewers of agent PRs, and anyone who needs `git bisect` to work on agent history.
