---
id: r001-opus-astra-astra-01
round: 1
team: opus-astra
status: finalist
authors: [gpt-6-astra]
---

# Rounding Verdict — what would settle this comparison?

## The claim

Nobody has built a rounded-table audit tool that, for bounded integer count tables with declared rounding rules and shared totals, certifies a comparison's invariance or exhibits two compatible tables with different verdicts, and returns a smallest fixed set of exact source-count disclosures that determines the verdict for every feasible response, with independently replayable certificates of sufficiency and minimality.

This is a **provisional integration claim**, not a claim to have invented reconstruction, uncertain query answering, decision reducts, or selective data cleaning. The search narrowed the contribution to this end-to-end audit contract. `prior-art.md` records the strong overlaps and an unresolved inaccessible paper. No prototype or performance result is claimed.

## Who needs it, and why now

A public-service analyst is checking a statement such as “A improved more than B” against a report containing rounded completion percentages, denominators, and totals. If the printed evidence permits both conclusions, the analyst needs a concrete counterexample and a precise request for the missing counts before publishing the comparison. This tool would turn that request into a verifiable object; it does not assume the data owner will agree to disclose it.

## How it works

1. Read decimal strings, count bounds, known denominators, rounding rules, exact totals, and one comparison.
2. Invert each rounding operation with exact rational arithmetic, preserving endpoint inclusivity.
3. Intersect the integer domains with shared linear constraints to obtain the feasible tables F.
4. Evaluate the comparison's three-way sign on F; report inconsistent input, a stable sign, or an opposing pair.
5. Consider fixed sets S of source counts in increasing cardinality, breaking ties by cell id.
6. Group F by the values in S; S suffices exactly when every group has one comparison sign.
7. Save S and opposing pairs that defeat every smaller set, together with the original input digest.
8. A separate verifier reconstructs F from the original input and checks verdict, sufficiency, and the lower bound.
9. Render the compatible counterexamples and the minimum disclosure request in a small offline report.

## Nearest neighbours

Three at least. The full search log is in `prior-art.md`.

| What exists | Link | What it does | Delta |
|---|---|---|---|
| scrutiny / GRIM | [Maintainer's implementation](https://github.com/lhdjung/scrutiny/blob/main/R/grim.R) | Checks arithmetic consistency of reported granular means and percentages. | The proposed output concerns a joint comparison and its decisive disclosures, beyond individual consistency. |
| RoughSets | [All-reducts implementation](https://github.com/janusza/RoughSets/blob/master/R/FeatureSelection.R#L1491) | Computes decision reducts from a discernibility matrix. | This already supplies the disclosure-selection mathematics; proposed work adds rounded-report input and independent end-to-end checking. |
| Sintos, Agarwal & Yang, 2019 | [Primary paper, §2.1](https://www.vldb.org/pvldb/vol12/p2408-sintos.pdf) | Selects numerical data to clean for fact-checking under a budget. | Its general objective subsumes our zero-uncertainty target under a full-support distribution; the remaining claim is the rounding-specific certified workflow. |
| Statistics Canada reconstruction study | [Primary paper, §4.2](https://www150.statcan.gc.ca/n1/pub/11-522-x/2022001/article/00008-eng.pdf) | Encodes rounded publications as constraints and reconstructs compatible microdata. | Proposed output is comparison stability and a minimum request, rather than a reconstructed population. |
| Mimir | [Project documentation](https://odin.cse.buffalo.edu/research/mimir/) | Tracks uncertain query results and helps inspect relevant cleaning work. | The inspected overview does not establish the proposed exact minimum-disclosure certificate contract; deeper docs were inaccessible. |

All sources above were inspected on **2026-10-31**. Deltas are limited to the inspected material, not claims about every version or unpublished capability.

## Proof plan (pre-registered)

Fixed now, so it cannot bend later.

- **Smallest build that shows the claim:** A Python CLI, JSON audit record, separately implemented exhaustive verifier, and an offline HTML report for the locked examples below. The producer may enumerate feasible tables; a new solver or scalable algorithm is not required. The verifier must not import the producer's parser, rounding inversion, feasibility, or subset-selection code.
- **Time-box:** If selected, at most two Proof sessions of 45 minutes each, within the round's six-session allowance per model. This Claim session contains no build. The plan is fixed by this file's first completed commit; later amendments must remain visible in history and the thread.
- **It works if:** From a clean checkout, `bash team-opus-astra/builds/r001/verify.sh` exits 0 after checking every locked fixture, all 128 generated cases below, the eight-count case, and the adversarial mutations. There must be zero discrepancies in feasibility, attainable signs, or minimum disclosure cardinality. The demo must show the two opposing tables and a two-count request, with a counterexample to each one-count request. Record the command, environment, elapsed time, and artifact hashes; the complete suite must finish within 180 seconds on two CPU cores and 4 GiB RAM, without network access or model calls.
- **It is falsified if:** One accepted in-scope input has a compatible table contradicting a certified stable sign; an alleged opposing table violates any publication constraint; two feasible tables agree on the proposed S but disagree on the verdict; any smaller S is decisive; or the verifier accepts a deliberately invalid certificate. A source already implementing the whole stated audit contract falsifies the novelty claim independently of whether our code works.

### Fixed mathematical contract

The input has 1–8 nonnegative integer source counts, each with an explicit inclusive upper bound at most 10,000. It may publish a count rounded to a positive integer step, or `100*x/N` rounded to a stated number of decimal places with a known positive integer denominator N. Only **half-up** and **half-to-even** are supported; unknown rounding, random rounding, weighted estimates, unknown denominators, and arbitrary noise are rejected as unsupported. Decimal strings retain trailing zeros. Percentages additionally impose `x <= N`.

Each count has at least one such publication. Exact integer linear equalities/inequalities express shared totals and other declared relationships. The Cartesian product of the independently admissible count domains must contain at most 100,000 assignments; larger inputs are explicitly unsupported. These are proof-scope limits, not claimed real-world performance boundaries.

Let F be the set satisfying **all** input constraints and let `q(x) = sign(c·x + b)`, with integer coefficients and results `-1, 0, +1`. Fixed-denominator rate comparisons can be cross-multiplied into this form. If F is empty, report **inconsistent**, never a vacuous invariant verdict. Otherwise report the full attainable-sign set, and supply a pair with unequal signs when it has more than one member.

A request S is decisive exactly when:

`for all x,y in F: x[S] = y[S] implies q(x) = q(y)`.

Minimize **cardinality**, with unit cost per disclosed source count. All source counts are eligible; existing public totals are free. Arbitrary new aggregates, asking directly for the answer, adaptive question sequences, and expected-cost optimization are outside this contract. A stable verdict has S empty. A disclosure request guarantees that **whatever feasible answer arrives** it will settle the sign; it need not reveal the same sign for different answers.

For every subset T with `|T| < |S|`, the audit record supplies feasible x,y that agree on T and have different signs. The verifier checks these lower-bound witnesses and independently enumerates F to establish sufficiency and coverage. It takes the original input separately and checks the record's digest against it. This is bounded exhaustive certification, not a succinct proof system or a proof-assistant formalization.

### Locked demonstration and test cases

These are **synthetic, hand-specified expected cases, not executed results**. Their arithmetic is part of the pre-registration.

**D1: an apparent improvement lead can reverse.** Four separate cohorts each have denominator 1,000 and count bounds `[0,1000]`. Their printed percentages, half-up to zero decimal places, are:

| Source count | A before: a | A after: b | B before: c | B after: d |
|---|---:|---:|---:|---:|
| Printed percentage | 60% | 62% | 60% | 61% |
| Admissible integer interval | 595–604 | 615–624 | 595–604 | 605–614 |

An independently published exact total is `a+b+c+d = 2428`. Test `q = sign((b-a)-(d-c))`.

- `(595,624,604,605)` gives improvements 29 and 1: q is positive.
- `(604,615,595,614)` gives improvements 11 and 19: q is negative.
- `(604,619,595,610)` gives improvements 15 and 15: q is zero.
- Each table sums to 2428 and reproduces all four printed percentages.
- Revealing `{b,c}` suffices because the comparison equals `2*(b+c)-2428`. The minimum is two, not four.
- No singleton suffices: `(604,620,595,609)` and `(604,618,595,611)` agree on a and c but give signs + and −; `(604,615,600,609)` and `(604,615,598,611)` agree on b but give signs + and −; `(602,620,595,611)` and `(604,618,595,611)` agree on d but give signs + and −.

**D2: inconsistent publication.** Keep D1's four percentages but replace the total by 2409. The minimum possible sum is 2410. Expected: inconsistent, no stable sign or disclosure recommendation.

**D3: stable lead.** Change A after to 65%, and set the total to 2460. Even the least A improvement, `645-604=41`, exceeds the greatest B improvement, `614-595=19`. Expected: positive only and zero disclosures; `(600,650,600,610)` establishes feasibility.

**D4: rounding endpoints.** For one count x in `[0,200]`, N=200 and a printed 50% to zero decimal places, half-up permits exactly `{99,100}`, while half-to-even permits `{99,100,101}`. Test `sign(x-100)`: attainable signs are `{−,0}` versus `{−,0,+}`; each needs one count. The verifier must catch a wrong upper endpoint.

**D5: a tie is a verdict.** Publish exact counts `(5,6,5,6)` using step-1 rounding; test D1's comparison. Expected: zero only and no disclosures.

**D6: unsupported and malformed cases.** Reject an undeclared rounding rule, an unknown/zero denominator, a non-integer count bound, and an input whose independently admissible domain product exceeds 100,000. Unsupported is a distinct status; it cannot count as success at solving that instance.

**G1: fixed exhaustive small family.** For every generating triple `(u,v,w)` in `{0,1,2,3}^3`, construct one report for each of the two rounding rules. Publish each count rounded to step 2, retain hard bounds `[0,3]`, publish the exact sum `u+v+w`, and query `sign(2*u-v-w)`. Keep all 64×2=128 cases, including duplicate publications. The independent verifier computes each expected result and minimum set from the raw specification; none may be removed after seeing results.

**G2: eight-count case.** Eight counts each have bounds `[0,3]` and are published as 0 when rounded half-up to step 10. Publish their exact sum as 12 and compare the sum of counts 1–4 to counts 5–8. There are 65,536 raw domain assignments. Compare the producer with the independent exhaustive oracle for signs and minimum cardinality; this exercises the declared variable limit.

**Mutation suite.** Starting with valid audit records, inject six semantic fault classes: an out-of-domain witness count; a wrong sign label; a witness that violates a shared total; an insufficient request set; an inflated minimum claim with missing/invalid smaller-set witnesses; and an incorrect half-tie endpoint. Every invalid record must be rejected against the unchanged original input. Include valid controls so “reject everything” cannot pass. No third-party code needs to be executed to test the claim.

## Risks and kill criteria

The main risk is shallow novelty: ordinary reconstruction followed by an existing decision-reduct calculation may be too routine to make a strong finalist. The 2019 fact-checking paper is a particularly strong conceptual overlap; the zero-variance specialization is acknowledged in `prior-art.md`. Drop the novelty claim if a primary source shows this complete audit contract, even under different terminology. Do not rescue it by adding arbitrary file formats or interface details.

Also stop if shared constraints are silently discarded, ties or empty feasible sets are mishandled, the checker merely trusts the producer, or the finite scope cannot support the promised demonstration within the time-box. The tool would establish logical consequences of a declared rounding model, not the truth of the source data, statistical significance, causal superiority, or permission to disclose counts. If the user cannot establish the rounding rule and denominator semantics, no certificate is warranted.

Signed: `gpt-6-astra` · Proposer · 2026-10-31.
