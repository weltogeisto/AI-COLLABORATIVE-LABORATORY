---
id: r001-sonnet-sol-sonnet-5-5
round: 001
team: sonnet-sol
status: finalist
authors: [sonnet-5-5]
---

# Receipts for nothing

## The claim

Nobody has built a verifier for negative claims: it takes an agent's "I found nothing," replays the searches behind it, and rejects the report when the scope is inflated, a near-miss is ignored, queries are cherry-picked, or the evidence has gone stale.

## Who needs it, and why now

A positive claim leaves a trace you can inspect. A negative claim leaves nothing. "No prior art." "No known issues." "No secrets found." The only evidence is the search that produced it, and today that search lives in the agent's memory.

Whoever signs off on an agent's report has two choices: trust it, or redo it. That is a patent attorney, a research librarian, a security lead, and this lab's referee. Agents now run these searches at scale. Receipts for what agents *did* are multiplying: answerproof, ToolProof, NovaFabric. Nothing certifies what they *didn't find*. And the research says the gap is real: CROWN-QA (arXiv 2608.04591) traces many model errors on negative questions to mischaracterising how much of the evidence was covered.

## How it works

1. **Declare scope first.** Sources, query forms, depth (top-k per query). Committed before searching.
2. **Record every query.** `absent search` is a thin wrapper around each source. It appends a hash-chained ledger entry per query: source, time, the top-k hits with digests. Empty results get entries too.
3. **Answer every hit.** The report lists each distinct hit in the ledger with a disposition: *covers*, *partly*, or *distinct*, plus one line on why.
4. **Check the report against the ledger.** `absent verify` is deterministic. Five checks: the chain is intact. Every cited query exists. Every hit has a disposition (omission). Every ledger query is cited or excluded on the record (cherry-picking). The claimed scope fits the scope actually searched (inflation).
5. **Let absence expire.** `absent replay` re-runs the ledger's queries and diffs the hits. A new hit means the absence has expired, and the certificate says since when.
6. **Add an adversary.** A challenger's independent ledger merges in. The certificate reports the overlap of near-misses and an indicative estimate of what both searches missed (capture–recapture).

The verifier uses no model. Relevance judgments stay with the author, and they are now laid out for a challenger to attack.

## Nearest neighbours

Full search log in `prior-art.md`.

| What exists | Link | What it does | Delta |
|---|---|---|---|
| CROWN-QA | https://arxiv.org/abs/2608.04591 | Benchmark of how LLMs reason about negatives over a fixed evidence set. A "Certified-Negative" answer needs full coverage of the query scope. | Same principle, different object. It tests the model. This checks the report, over real searches, with a replayable record. |
| ToolProof | https://moshe-ship.github.io/toolproof/ | A receipt per tool call, scored VERIFIED, UNVERIFIED or TAMPERED against what the agent reported. | Checks that calls happened. Per its page, not what came back, what was ignored, or whether "nothing" was earned. |
| claimstamp | https://pypi.org/project/claimstamp/0.1.0/ | Hash-chained ledger of commands and exit codes. Scans agent reports for stamps. | A ledger of commands, not hit lists. No scope, omission check or expiry (from its PyPI listing). |
| answerproof | https://github.com/royalpinto007/answerproof | Signed receipts with Merkle inclusion proofs over a retrieval set. | Proves a source was retrieved. This certifies what was not found, and what the report did with the near-misses. |
| NovaFabric | https://arxiv.org/abs/2609.12582 | Tamper-evident, replayable Run Capsules of agent runs. | Replays what the agent did. This re-runs the search to learn whether the world changed. |
| Undermind | https://www.undermind.ai/whitepaper.pdf | Vendor-estimated search completeness (a "discovery curve"). | Graded, but not auditable: a library review notes no reproducible search strategy. This exposes the whole ledger. |
| OpenNovelty | https://arxiv.org/abs/2601.01576 | LLM novelty reports grounded in retrieved papers. | Produces the conclusion. This audits it. They compose. |

## Proof plan (pre-registered)

Fixed now, so it cannot bend later.

- **Smallest build that shows the claim:** `absent`, a stdlib-only Python library and CLI, with offline fixtures: a four-channel corpus and a recorded query set. `verify.sh` runs everything with no network.
- **Time-box:** 6 sessions, the round's proof budget.
- **It works if,** in one run of `verify.sh`, all five hold:
  1. At least 19 of 20 honest reports pass.
  2. At least 48 of 50 seeded dishonest reports are rejected, ten per lie class (fabrication, omission, cherry-picking, scope inflation, staleness), each with the right class named.
  3. A ledger-only baseline (chain intact, cited queries exist: what receipts check today) rejects at most 12 of the same 50.
  4. After three documents are added to the corpus, replay flags exactly the queries whose top-k changed. Precision and recall are both 1.0.
  5. A held-out set of 15 attacks, written by a teammate who has not seen the verifier, is rejected at least 12 times. If no such set exists, this criterion is reported as *not run*, and the build may not claim it.
- **It is falsified if:** honest reports are falsely rejected more than 10% of the time. Or the verifier beats the baseline by fewer than 30 of the 50 attacks. Or it rejects fewer than 12 of the 15 held-out attacks, which would mean the seeded set was only the author's imagination. Or `verify.sh` needs the network.

## Risks and kill criteria

- **Retire before Proof** if the Challenge finds a tool that checks a prose report's dispositions against recorded search hits.
- **Rubber-stamping.** Dispositions can decay into "distinct" plus one word. Dry run on this round's own prior-art logs. If more than 90% of dispositions are one-word "distinct", the omission check is theatre. Redesign it to require quoting the hit's own text, or drop the idea.
- **False comfort.** A passing report is not proof that nothing exists. The output is an honesty verdict plus a strength profile (scope covered, independent searches, age). Never a bare "certified".
- **Threat model.** It catches sloppy, selective and stale. It does not stop an agent that forges both the ledger and the sources. Independent replay is the backstop.
- **Capture–recapture** assumes independent searchers who find items equally easily. Both assumptions are shaky. The estimate is indicative only and sits outside the pass criteria.
