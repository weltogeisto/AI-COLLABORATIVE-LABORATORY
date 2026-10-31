# Prior-art search — r001 · sonnet-sol · sonnet-5-5

Claim under test: Nobody has built a verifier for negative claims: it takes an agent's "I found nothing," replays the searches behind it, and rejects the report when the scope is inflated, a near-miss is ignored, queries are cherry-picked, or the evidence has gone stale.

Every query run for this claim is logged, with its best hits. "Covers the claim?" is my reading of the abstract or snippet, not of the full text. Where I could read only a snippet, the row says so.

| Date | Channel | Query | Best hit (URL) | Covers the claim? |
|---|---|---|---|---|
| 2026-10-31 | papers | LLM research agents "no prior work" negative claims absence verification search completeness faithfulness paper | https://arxiv.org/pdf/2604.22080 | partly: argues falsifying experiments go unrun and proposes a falsification-first standard. No artifact, no verifier |
| 2026-10-31 | papers | same query, second hit | https://arxiv.org/pdf/2511.05524 | partly: EviBound gates positive claims on machine-checkable evidence IDs. Says nothing about absence |
| 2026-10-31 | papers | "certificate of absence" OR "proof of absence" OR "evidence of absence" LLM agent literature search receipt coverage saturation capture-recapture completeness | https://arxiv.org/abs/2608.04591 | partly, and closest on concept: CROWN-QA is a benchmark of LLM negative reasoning; "Certified-Negative" needs full query-scope coverage. Abstract page only. No artifact, replay or omission check |
| 2026-10-31 | papers | fetched abstract page for OpenNovelty | https://arxiv.org/abs/2601.01576 | partly: LLM novelty reports grounded in retrieved papers. No query log, graded absence, omission check or re-run. Abstract page only |
| 2026-10-31 | papers | PRISMA-S searchRxiv search strategy reproducibility LLM automated systematic review search log replay | https://www.medrxiv.org/content/10.1101/2023.05.11.23289873.full.pdf | partly: the human standard. Finds 4.9% of database searches fully reproducible. Nothing machine-checked |
| 2026-10-31 | papers | capture-recapture estimate number of missed studies literature search completeness systematic review | https://core.ac.uk/works/100848577 | no: adjacent method. Estimates missed studies from the overlap of searches, run by humans |
| 2026-10-31 | papers | patent system AI agent search query log signed attestation "no results" claim verification report omitted results tamper-evident | https://arxiv.org/abs/2609.12582 | no: NovaFabric records replayable agent runs. Abstract page says nothing on absence, omission or coverage |
| 2026-10-31 | papers | DRAT proof checker certificate of unsatisfiability verified SAT solver proof of absence of solution | https://ar5iv.arxiv.org/html/1610.06229 | no: a formal certificate of absence for SAT. The lineage, not prior art for open-world search |
| 2026-10-31 | code | agents misreport tool use fabricated verification claims audit final report against tool call trajectory | https://moshe-ship.github.io/toolproof/ | partly: ToolProof scores each call VERIFIED, UNVERIFIED or TAMPERED. Its page does not mention results, omissions or negative claims |
| 2026-10-31 | code | github agent claims verifier hash-chained ledger search queries replay diff "new hits" since absence claim expires | https://pypi.org/project/claimstamp/0.1.0/ | partly: hash-chained ledger of commands. Scans reports for stamps. PyPI snippet only. No hits, scope or expiry |
| 2026-10-31 | code | same query, second hit | https://bernstein.readthedocs.io/en/latest/operations/replay/ | partly: replay and diff of hash-chained journals. Snippet only. Nothing on absence |
| 2026-10-31 | code | answerproof github signed receipts retrieval Merkle inclusion proof RAG | https://github.com/royalpinto007/answerproof | partly: signed receipts and Merkle inclusion proofs over a retrieval set. Proves presence, not absence |
| 2026-10-31 | code | github novelty checker agent prior art search log replay reproducible search receipt | https://github.com/niansia/NoveltyAudit/releases | unknown: the README was unreachable (the repo URL returned 404). Release notes only. Unread |
| 2026-10-31 | code | TLSNotary zkTLS prove API response empty search result attestation AI agent web search proof | https://fosdem.org/schedule/event/QZ8NAZ-tlsnotary | no: cryptographic proof of an HTTPS response. Attesting an empty result is not addressed |
| 2026-10-31 | products | AI patent prior art search novelty checker documents search strategy audit trail report product 2026 | https://eureka.patsnap.com/novelty-search | partly: traceable novelty reports for expert review. No replayable absence record documented |
| 2026-10-31 | products | same query, second hit | https://xlscout.ai/what-are-the-best-tools-for-quick-prior-art-searches/ | no: ranked references and key-feature analysis. Search-strategy logging not documented |
| 2026-10-31 | products | Undermind AI literature search estimate completeness how many relevant papers found discovery curve saturation | https://www.undermind.ai/whitepaper.pdf | partly: a vendor-estimated completeness curve. A 2025 library review (https://journals.library.ualberta.ca/jchla/index.php/jchla/article/download/29854/22212?inline=1) notes no reproducible search strategy. Graded, not auditable |
| 2026-10-31 | products | verifiable search receipt AI agent replayable proof negative search "nothing found" attestation hash-chained tool call log | https://arkforge.tech/en/blog/mcp-client-verification-receipts/ | no: transport-layer receipts for agent actions. States that receipts do not prove correctness |
| 2026-10-31 | patents | patent system AI agent search query log signed attestation "no results" claim verification report omitted results tamper-evident | https://patents.google.com/patent/US8230228 | no: tamper detection for a log of records. A building block |
| 2026-10-31 | patents | patent method system verifying completeness of a search "search log" tamper-evident audit prior art search negative result certificate | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10621381 | no: event-log tamper detection. A building block |
| 2026-10-31 | patents | same query, second hit | https://www.epo.org/en/about-us/transparency-portal/general/annual-review-2023/goal-3 | no: the EPO's 2021 human audit of search-report completeness. The institutional version of the same worry |
| 2026-10-31 | patents | same query, combination of a search ledger, report-versus-hit checking and replay expiry | none | no hit found. Searched through a general web index, not Espacenet or Google Patents full text |

**Channels.** `papers`: arXiv, Scholar, journals. `code`: GitHub, package registries. `products`: launches, docs, apps. `patents`: Espacenet, Google Patents.

## Verdict on novelty

The parts exist, and the field around them is crowded. Tamper-evident logs, signed retrieval receipts, replayable run capsules, claim-versus-trace auditors and vendor completeness estimates are all out there. None of what I found checks a prose report's "nothing" against the hits the agent actually saw, ties the claim to a declared scope, or re-runs the search to date the absence. The closest on concept is CROWN-QA, which states the principle and tests models on it. The closest on mechanism are ToolProof and claimstamp, which check that actions happened and stop short of what came back.

So the honest reading: a new composition aimed at a case nobody has aimed at, not a new field. Novelty depth, by this lab's rubric, is a 3 with a chance of a 4.

**Not checked.** The full text of CROWN-QA and OpenNovelty. The READMEs of claimstamp, NoveltyAudit and truth-layer. Espacenet and Google Patents full text, which need an interactive search. A Challenger with better access should start there.
