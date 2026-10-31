# Prior-art search — r001 · sonnet-sol · gpt-6-1-sol

Claim under test: Nobody has built an offline checker for finite, permission-changing runbooks that classifies every executable forward prefix as recoverable, authority-locked, or unrecoverable within the declared recovery catalogue by comparing authorized and authorization-waived recovery, and exports replayable traces and closed-state-set certificates supporting those classifications.

Research date: **2026-10-31 (UTC)**. This is the independent Claim turn; no
teammate or opposing-team idea files were opened.

## Search method and query log

All keyword queries issued for this finalist are logged below, including failed,
empty, off-target and follow-up searches. A query's text links to a reproducible
search URL; the next column links to a primary hit when one was inspected.
GitHub searches used the connected repository/code search. Other searches used
the web-search tool, including site-restricted Google Patents searches. The
first direct Google fetch failed to return usable search results.

Several web calls batched four queries and returned a combined result list.
For those rows, “best hit” means the closest reviewed lead from the batch,
not a claim about that query's isolated rank. “None relevant assessed” means
no usable primary match was established from that result set, not that the
database contains no match. Unassessed leads are retained for audit and have
no weight in the feature comparisons. Primary-source readings follow the log.

| Date | Channel | Query (search URL) | Best hit (URL) | Covers the claim? |
|---|---|---|---|---|
| 2026-10-31 | code | [Q01: runbook rollback permissions](https://github.com/search?q=runbook%20rollback%20permissions&type=repositories) | none | GitHub repository search returned no repositories; not proof of absence. |
| 2026-10-31 | code | [Q02: workflow compensation verification](https://github.com/search?q=workflow%20compensation%20verification&type=repositories) | [S18: ChangeGuard](https://github.com/anil7000/changeguard/blob/main/README.md) | Partly: recovery, authorization and compensation; no inspected differential reachability checker. |
| 2026-10-31 | papers | [Q03: runbook rollback permissions formal verification](https://www.google.com/search?q=runbook+rollback+permissions+formal+verification) | none usable | Direct Google HTTP fetch returned a JavaScript interstitial; repeated using the web-search tool below. |
| 2026-10-31 | papers | [Q04: "workflow" "compensation" "access control" verification](https://www.google.com/search?q=%22workflow%22%20%22compensation%22%20%22access%20control%22%20verification) | none relevant assessed | Mixed payroll/access-control results; no primary source from this query used for novelty. |
| 2026-10-31 | papers | [Q05: "administrative" "RBAC" "recovery" safety rollback](https://www.google.com/search?q=%22administrative%22%20%22RBAC%22%20%22recovery%22%20safety%20rollback) | [Security Enhanced ARBAC poster](https://profsandhu.com/confrnc/misconf/ccs16-rajkumar.pdf) (unassessed lead) | Unassessed discovery lead; no coverage conclusion drawn. |
| 2026-10-31 | products | [Q06: runbook rollback permission lockout verification checker](https://www.google.com/search?q=runbook%20rollback%20permission%20lockout%20verification%20checker) | [Ansible authentication runbook](https://runbook.academy/courses/ansible/runbooks/ansible-runbook-troubleshoot-authentication-failure/) (unassessed lead) | Operational guide lead; no claim about its full features inferred from the snippet. |
| 2026-10-31 | patents | [Q07: site:patents.google.com "rollback" "permissions" workflow](https://www.google.com/search?q=site%3Apatents.google.com%20%22rollback%22%20%22permissions%22%20workflow) | [S13: US20260212138A1](https://patents.google.com/patent/US20260212138A1/en) | Partly: rollback plans and validation; no inspected prefix-wise authorized/waived certificate diagnosis. |
| 2026-10-31 | papers | [Q08: formal verification compensating transactions workflow recovery reachability planning](https://www.google.com/search?q=formal%20verification%20compensating%20transactions%20workflow%20recovery%20reachability%20planning) | [S5: Vaz and Ferreira 2012](https://repositorio.ipl.pt/server/api/core/bitstreams/c27d9d25-be37-4d30-a429-a2be7d91ce07/content) | Partly: compensation correctness is already formally analyzed and checked. |
| 2026-10-31 | papers | [Q09: administrative RBAC safety analysis model checking can revoke role reachability](https://www.google.com/search?q=administrative%20RBAC%20safety%20analysis%20model%20checking%20can%20revoke%20role%20reachability) | [S3: Sasturkar et al. 2006](https://www3.cs.stonybrook.edu/~stoller/papers/csfw-2006.pdf); [S2: VAC](https://www.southampton.ac.uk/~gp1y10/VAC.html) | Partly: dynamic access-policy reachability is established; broad algorithmic novelty is excluded. |
| 2026-10-31 | products | [Q10: AWS KMS BypassPolicyLockoutSafetyCheck put key policy permissions](https://www.google.com/search?q=AWS%20KMS%20BypassPolicyLockoutSafetyCheck%20put%20key%20policy%20permissions) | [S7: AWS KMS PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html) | Partly: a concrete existing policy lockout check; one-step lockout prevention is not new. |
| 2026-10-31 | products | [Q11: AWS Systems Manager Automation rollback permissions onFailure steps](https://www.google.com/search?q=AWS%20Systems%20Manager%20Automation%20rollback%20permissions%20onFailure%20steps) | [S8: AWS SSM Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-actions.html) | Partly: permissions and failure routing; no inspected preflight recovery classification. |
| 2026-10-31 | papers | [Q12: "runbook" "rollback" "verification"](https://www.google.com/search?q=%22runbook%22%20%22rollback%22%20%22verification%22) | none scholarly assessed | Operational runbook guides were returned; no scholarly source from this query supports the novelty verdict. |
| 2026-10-31 | papers | [Q13: "compensation correctness" "access"](https://www.google.com/search?q=%22compensation%20correctness%22%20%22access%22) | [S5: Vaz and Ferreira 2012](https://repositorio.ipl.pt/server/api/core/bitstreams/c27d9d25-be37-4d30-a429-a2be7d91ce07/content) | Partly: primary PDF found through the repository after the publisher blocked access. |
| 2026-10-31 | code | [Q14: "rollback" "static analysis" runbook](https://www.google.com/search?q=%22rollback%22%20%22static%20analysis%22%20runbook) | [S22: runbook package snapshot](https://pkg.go.dev/github.com/runbookdev/runbook); [S23: Agent Undo Plan Validator](https://www.altftool.com/tools/all/agent-undo-plan-validator) | Partly: rollback execution and text-based undo review; neither inspected interface is the claimed state analysis. |
| 2026-10-31 | patents | [Q15: site:patents.google.com workflow rollback "authorization" verification](https://www.google.com/search?q=site%3Apatents.google.com%20workflow%20rollback%20%22authorization%22%20verification) | [S12: WO2021069621A1](https://patents.google.com/patent/WO2021069621A1/en) | Partly: per-step execution conditions, rollback actions and workflow validation are disclosed. |
| 2026-10-31 | code | [Q16: ARBAC VAC](https://github.com/search?q=ARBAC%20VAC&type=repositories) | none | GitHub repository search returned no repositories; VAC's separate author site was read. |
| 2026-10-31 | code | [Q17: rollback verification](https://github.com/search?q=rollback%20verification&type=repositories) | [S21: Hazmat](https://github.com/dredozubov/hazmat/blob/master/README.md) | No complete hit: the inspected project is agent containment and snapshot recovery. |
| 2026-10-31 | papers | [Q18: workflow verification "permission" "compensation"](https://www.google.com/search?q=workflow%20verification%20%22permission%22%20%22compensation%22) | none relevant assessed | Payroll compensation results predominated; no research conclusion drawn. |
| 2026-10-31 | papers | [Q19: "runbook" "model checking"](https://www.google.com/search?q=%22runbook%22%20%22model%20checking%22) | [S1: Joltrin verify](https://github.com/SharedCode/joltrin/blob/a139ad7d1af5babf2c1d2105ba4312802264f315/verify/reachability.go) | Partly and very close: runbook rollback reachability exists; inspected source explicitly limits its state treatment. |
| 2026-10-31 | patents | [Q20: site:patents.google.com "lockout" "rollback"](https://www.google.com/search?q=site%3Apatents.google.com%20%22lockout%22%20%22rollback%22) | none relevant assessed | No query-specific primary hit established in the combined returned batch; not an exhaustive negative. |
| 2026-10-31 | code | [Q21: "runbook" "recoverability"](https://www.google.com/search?q=%22runbook%22%20%22recoverability%22) | [S20: Microsoft Entra recoverability](https://learn.microsoft.com/en-us/entra/architecture/recoverability-tenant) | Product guidance surfaced; no complete code implementation identified by this query. |
| 2026-10-31 | papers | [Q22: "workflow" "resiliency" "revocation"](https://www.google.com/search?q=%22workflow%22%20%22resiliency%22%20%22revocation%22) | [SwissSign revocation issue](https://bugzilla.mozilla.org/show_bug.cgi?id=2034359) (unassessed lead) | Off-target operational lead, not used as research evidence. |
| 2026-10-31 | papers | [Q23: "rollback" "access control" "model checking"](https://www.google.com/search?q=%22rollback%22%20%22access%20control%22%20%22model%20checking%22) | [Conference-volume mirror](https://www.scribd.com/document/1059044994/978-3-642-30904-5) (unassessed lead) | Secondary search lead only; not used to infer a paper's method or scope. |
| 2026-10-31 | papers | [Q24: "runbook" "permissions" "reachability"](https://www.google.com/search?q=%22runbook%22%20%22permissions%22%20%22reachability%22) | [AWS CloudWatch troubleshooting runbook](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshootcloudwatchagent.html) (unassessed lead) | Product documentation lead; no scholarly match established. |
| 2026-10-31 | products | [Q25: "rollback" "permission" "static" "checker"](https://www.google.com/search?q=%22rollback%22%20%22permission%22%20%22static%22%20%22checker%22) | [S17: policy-diff-guard](https://github.com/chenhz01/policy-diff-guard/blob/main/README.md) | Partly: static permission diffs and rollback suggestions; not recovery-action reachability. |
| 2026-10-31 | papers | [Q26: "compensation" "authorization" "verification" workflow security](https://www.google.com/search?q=%22compensation%22%20%22authorization%22%20%22verification%22%20workflow%20security) | none relevant assessed | Mixed compensation/HR results; no primary scholarly hit relied upon. |
| 2026-10-31 | papers | [Q27: "recoverability" "permissions" "planning"](https://www.google.com/search?q=%22recoverability%22%20%22permissions%22%20%22planning%22) | [S20: Microsoft Entra recoverability](https://learn.microsoft.com/en-us/entra/architecture/recoverability-tenant) | Partly as motivation: identity recovery guidance; no inspected offline checker with this contract. |
| 2026-10-31 | code | [Q28: "rollback" "reachability" "permissions" checker](https://www.google.com/search?q=%22rollback%22%20%22reachability%22%20%22permissions%22%20checker) | [S17: policy-diff-guard](https://github.com/chenhz01/policy-diff-guard/blob/main/README.md) | Partly: permission-surface review is already a product/code function. |
| 2026-10-31 | patents | [Q29: site:patents.google.com "rollback" "reachability"](https://www.google.com/search?q=site%3Apatents.google.com%20%22rollback%22%20%22reachability%22) | [S15: CN121601097A](https://patents.google.com/patent/CN121601097A/en); [S14: US20250337645A1](https://patents.google.com/patent/US20250337645A1/en) | Partly: recovery-path reachability and configuration auto-rollback already appear in patents. |
| 2026-10-31 | code | [Q30: rollback permission reachability](https://github.com/search?q=rollback%20permission%20reachability&type=code) | none relevant among six returned excerpt hits | Global connector code search returned off-target repositories; no completeness inference. |
| 2026-10-31 | papers | [Q31: workflow authorization-aware rollback recovery verification](https://www.google.com/search?q=workflow%20authorization-aware%20rollback%20recovery%20verification) | [S9: Permission to Retry](https://arxiv.org/html/2610.31916); [S10: Runtime Authorization Consistency](https://arxiv.org/html/2609.23498) | Partly: recovery under changing authority and workflow authorization are existing research topics. |
| 2026-10-31 | papers | [Q32: "recoverability" "authorization" model checker](https://www.google.com/search?q=%22recoverability%22%20%22authorization%22%20model%20checker) | [S11: Recoverability as a System Primitive](https://arxiv.org/html/2609.13672) | Partly: source/route authority and independent recovery evidence; primary source located in Q38. |
| 2026-10-31 | patents | [Q33: site:patents.google.com "rollback" "lockout" "permission"](https://www.google.com/search?q=site%3Apatents.google.com%20%22rollback%22%20%22lockout%22%20%22permission%22) | [S16: US12676749B1](https://patents.google.com/patent/US12676749B1/en) | Partly: lockout, policy rollback detection and offline authorization evidence; different inspected diagnostic. |
| 2026-10-31 | products | [Q34: runbook checker mutable permissions rollback lockout](https://www.google.com/search?q=runbook%20checker%20mutable%20permissions%20rollback%20lockout) | [S19: Octopus Config as Code Runbooks](https://octopus.com/docs/runbooks/config-as-code-runbooks); [S22: runbook package snapshot](https://pkg.go.dev/github.com/runbookdev/runbook) | Partly: runbook execution permissions and rollback tooling; no inspected full state/certificate comparison. |
| 2026-10-31 | papers | [Q35: action reversibility planning inverses verification STRIPS](https://www.google.com/search?q=action%20reversibility%20planning%20inverses%20verification%20STRIPS) | [S4: Morak et al. 2020](https://proceedings.kr.org/2020/65/kr2020-0065-morak-et-al.pdf) | Partly: action reversibility and reverse plans predate this proposal. |
| 2026-10-31 | papers | [Q36: workflow resiliency access control security planning recovery](https://www.google.com/search?q=workflow%20resiliency%20access%20control%20security%20planning%20recovery) | [S6: Wang and Li 2007](https://www.cs.purdue.edu/homes/ninghui/papers/workflow_esorics07.pdf) | Partly: workflow completion under changing user availability is established. |
| 2026-10-31 | patents | [Q37: site:patents.google.com "rollback" "authorization" "model checking"](https://www.google.com/search?q=site%3Apatents.google.com%20%22rollback%22%20%22authorization%22%20%22model%20checking%22) | none relevant assessed | No query-specific complete patent match established in the combined results; adjacent patents are analyzed below. |
| 2026-10-31 | papers | [Q38: "recoverability as a system primitive for long-horizon AI agents"](https://www.google.com/search?q=%22recoverability%20as%20a%20system%20primitive%20for%20long-horizon%20AI%20agents%22) | [S11: Recoverability as a System Primitive](https://arxiv.org/html/2609.13672) | Partly: primary manuscript read; narrows away any general claim to policy-aware recovery. |

## Claim revision after attempted disproof

The longlist was committed as
`2e4c3ecb07bd8037a202e7020c60d97fd652ba8d` before research. Its item 1 proposed
a permission-aware rollback checker without the present diagnostic contract.

That broad space is occupied: Joltrin already checks runbook rollback
reachability (S1); VAC and ARBAC research analyze changing authority (S2–S3);
reverse planning is established (S4); and verified compensation is established
(S5). AWS already implements a practical lockout check (S7). Consequently the
finalist does **not** claim the first rollback checker, the first model of
revocation, or a new reachability algorithm.

The revised hypothesis requires the conjunction of:

1. Complete finite states containing both world facts and actor-specific mutable grants.
2. Analysis at every executable prefix of a supplied forward runbook.
3. Two recovery graphs with the same state, goal, catalogue and effects, differing only in enforcement of authorization guards.
4. The resulting three-way diagnosis, with the earliest authority-only gap identified.
5. Exported replay traces and successor-closed goal-free sets that a separate verifier can check.

This conjunction is an interface and application contribution made from known
methods. A generic planner/model checker can express the underlying two
queries. Encoding a runbook twice is therefore a serious simplicity objection,
not evidence that the mathematics is new. The proof plan was committed as
`25a10a5e0cfce522ed0aab6163222b055f73f2c9`; no implementation preceded it.

## Primary-source readings

Every source in this section was accessed on **2026-10-31**. “Delta” states what
the inspected source did not establish; it is a bounded reading, not a universal
assertion about all versions, unpublished work or possible encodings.

### S1 · Joltrin: the closest code neighbour

[S1: Joltrin verify](https://github.com/SharedCode/joltrin/blob/a139ad7d1af5babf2c1d2105ba4312802264f315/verify/reachability.go); companion
[`verify.go`](https://github.com/SharedCode/joltrin/blob/a139ad7d1af5babf2c1d2105ba4312802264f315/verify/verify.go).
Snapshot: `a139ad7d1af5babf2c1d2105ba4312802264f315`.
Read the complete transition/trace definitions and reachability implementation,
plus the property and workflow tests.

The reachability source says it “checks reachability per individual State, not over the full powerset”.
It constructs edges from individual required facts to established facts.
The trace implementation accumulates facts without a delete effect.
**Delta:** this supports dropping broad rollback-checker novelty, while leaving
the proposed mutable-state, typed-authorization differential and exported
negative-certificate interface unestablished in the inspected implementation.
An encoding that expands configurations into graph nodes is possible; it does
not make that underlying capability a new algorithm.

### S2 · VAC: existing administrative-policy analysis

[S2: VAC](https://www.southampton.ac.uk/~gp1y10/VAC.html). Read the author's architecture, feature list, input grammar and
counterexample description. Its input includes can-assign and can-revoke rules;
role reachability has complete analysis backends and counterexample support.
**Delta:** it is a powerful existing analysis foundation. The inspected interface
does not present the paired recovery report/certificate contract of this card.
The linked CAV paper landing page at
[Southampton eprints](https://eprints.soton.ac.uk/365363/) returned HTTP 403,
so no finding here relies on an unread paper.

### S3 · ARBAC policy analysis

[S3: Sasturkar et al. 2006](https://www3.cs.stonybrook.edu/~stoller/papers/csfw-2006.pdf). Read the author's PDF, especially pp. 1–3 on analysis problems,
positive/negative preconditions, administrative operations and the connection
to planning. Reachability and availability under administrative changes are
existing questions, and the paper also treats bounded reachability.
**Delta:** dynamic permissions and planning-based safety analysis are not novel.
The inspected sections do not supply the stated runbook-specific differential
diagnostic and evidence export.

### S4 · Action reversibility

[S4: Morak et al. 2020](https://proceedings.kr.org/2020/65/kr2020-0065-morak-et-al.pdf). Read pp. 652–654: introduction, STRIPS state/action semantics and
definitions of state-relative and uniform reversibility. Reverse plans, add/delete
effects and dead-end detection all predate this proposal.
**Delta:** the proposal specializes known planning to a diagnostic interface;
its novelty cannot rest on finding an undo sequence or allowing delete effects.

### S5 · Compensation correctness

[S5: Vaz and Ferreira 2012](https://repositorio.ipl.pt/server/api/core/bitstreams/c27d9d25-be37-4d30-a429-a2be7d91ce07/content). Read pp. 585–586 on scope, pp. 593–594 on correctness mappings, and
pp. 598–604 on the ProB approach and examples. The paper defines compensation
correctness and implements automated checking. Its correctness map is
programmer supplied; its communication model is explicitly stateless.
**Delta:** verified compensation is not new. The inspected approach does not
present the paired actor-authorization graph comparison in the claim.
The [publisher page](https://www.sciencedirect.com/science/article/pii/S1567832612000409)
returned HTTP 403; the linked institutional full text was readable.

### S6 · Workflow satisfiability and resiliency

[S6: Wang and Li 2007](https://www.cs.purdue.edu/homes/ninghui/papers/workflow_esorics07.pdf). Read pp. 1–3 and section 5, particularly definitions 6–8.
Authorized assignment of users to steps and completion despite changing user
availability are established research problems.
**Delta:** retaining a path through changing authority is not a new research
theme. This source studies workflow completion/resiliency rather than the
declared forward-prefix rollback classification and certificates.

### S7–S8 · Existing AWS product behaviour

[S7: AWS KMS PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html). Read the Policy and BypassPolicyLockoutSafetyCheck request parameters.
The normal KMS policy update checks that the caller retains a subsequent
policy-update permission. **Delta:** concrete prevention of authority loss already
exists; the inspected API is a single-operation guard.

[S8: AWS SSM Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-actions.html). Read the service-role requirements and shared onFailure/onCancel
properties. SSM documents required invocation permissions and explicit
failure/cancellation routing. **Delta:** routing to recovery is established, but
the inspected reference does not prove future recovery feasibility for all
intermediate modeled states.

### S9–S11 · Recent authorization and recovery research

[S9: Permission to Retry](https://arxiv.org/html/2610.31916). Read sections 1–4, 7 and the availability section. Its bounded
conformance study distinguishes current write authority, recovery evidence and
uncertain external effects across persistent execution hosts.
**Delta:** authority-sensitive recovery is existing work; the paper's inspected
contract evaluates histories, rather than exporting this pair of reachability
certificates for a runbook's prefixes.

[S10: Runtime Authorization Consistency](https://arxiv.org/html/2609.23498). Read introduction, security objective and formal consistency
predicate. RAC checks whether pending tool calls stay within authority inherited
through accepted history.
**Delta:** workflow authorization monitoring exists; the inspected objective is
admission consistency rather than rollback-goal reachability.

[S11: Recoverability as a System Primitive](https://arxiv.org/html/2609.13672). Read sections 3.3–3.5 and 4.4–5.3 on source/route permission, recovery
decisions and implemented runtime boundaries.
**Delta:** policy-aware continuation and separate verification evidence already
exist. The inspected design does not establish the card's offline authorized
versus authorization-waived recovery graph/certificate interface. It is a close
conceptual neighbour, not an unrelated paper to dismiss.

### S12–S16 · Patents and disclosures

[S12: WO2021069621A1](https://patents.google.com/patent/WO2021069621A1/en). Read the description's workflow execution conditions and validation
passages, including the paragraph beginning with rollback information, and the
claims. Per-step permissions, stored rollback actions and validation already
coexist in this disclosure. **Delta:** the inspected text does not specify the
claim's paired reachability diagnosis or closed-state-set evidence.

[S13: US20260212138A1](https://patents.google.com/patent/US20260212138A1/en). Read independent claims 1–3 and rollback-location/behaviour claims
9–13. It discloses validation and rollback plans for executable directives,
including target-specific mechanisms.
**Delta:** rollback plans and predeployment validation are not novel; the
inspected claims do not present the stated differential runbook analysis.

[S14: US20250337645A1](https://patents.google.com/patent/US20250337645A1/en). Read the description's operational checks and claims 1–8.
Configuration changes can trigger automated restoration when programmable
operational checks fail, including for access-control configurations.
**Delta:** this is a substantial existing recovery mechanism, but the inspected
method tests runtime conditions rather than exporting the proposed finite-state
three-way preflight diagnosis.

[S15: CN121601097A](https://patents.google.com/patent/CN121601097A/en). Read the S7 description, especially S701, and the associated claims.
It explicitly discusses a return path after forward material-proportion
adjustments under operating constraints.
**Delta:** even prefix-related rollback reachability is not a new idea in
general. The inspected domain has no actor-authorization erasure comparison;
renaming return-path checking alone would not justify this finalist.

[S16: US12676749B1](https://patents.google.com/patent/US12676749B1/en). Read claim 1 and the offline-verifier appendix AB.
It discloses execution gates, persistent lockouts, policy rollback detection
and offline authorization evidence.
**Delta:** offline evidence and lockouts are already disclosed concepts. The
inspected predicates check authorization artifacts, rather than successor-closed
absence of a recovery path in two modeled graphs.

### Other primary readings and their limited relevance

| Source, accessed 2026-10-31 | Reading and conclusion |
|---|---|
| [S17: policy-diff-guard](https://github.com/chenhz01/policy-diff-guard/blob/main/README.md) | Complete README: permission-surface diff, risk annotations and removal suggestions; no inspected recovery-action state search. |
| [S18: ChangeGuard](https://github.com/anil7000/changeguard/blob/main/README.md) | Complete README: authorized corrective workflows, compensation and outcome verification; no inspected offline paired-graph checker. Runtime recovery is already built. |
| [S19: Octopus Config as Code Runbooks](https://octopus.com/docs/runbooks/config-as-code-runbooks) | Permissions-by-branch and required-resource sections: control of runbook editing/execution; not evidence of future recovery reachability. |
| [S20: Microsoft Entra recoverability](https://learn.microsoft.com/en-us/entra/architecture/recoverability-tenant) | Definitions and operational guidance: recovery needs capabilities and runbooks; motivation, not evidence of the claimed checker. |
| [S21: Hazmat](https://github.com/dredozubov/hazmat/blob/master/README.md) | README's containment and snapshot/restore sections: different problem; not a close novelty match. |
| [S22: runbook package snapshot](https://pkg.go.dev/github.com/runbookdev/runbook) | Package's published documentation snapshot: executable blocks, rollback handlers, dry run and static-analysis claims. Current GitHub README fetch returned 404; no current-source feature conclusion. |
| [S23: Agent Undo Plan Validator](https://www.altftool.com/tools/all/agent-undo-plan-validator) | Product's method and limitations sections: it explicitly describes local keyword classification of plan text. No state/authorization reachability claim inferred. |
| [S24: Google Research disclosure record](https://research.google/pubs/stakes-adaptive-verification-and-origin-traced-rollback-in-autonomous-agent-workflows/) | Primary publication record/abstract only: intent checks and origin-traced checkpoint rollback. Full disclosure not read; not used to establish a feature absence. |

## Reproducibility and search limits

Searches were performed with `search_service.web_run(system2_search_query=[{"q": QUERY}])`
and GitHub connector `search_repositories(query=QUERY)` /
`search(query=QUERY, topn=6)`. Primary pages were opened by URL; source files were
read with GitHub `fetch_file`. The literal queries and replay URLs are above.
These are research commands, not claimed experimental results.

For the closest code source, repeat these read-only commands:

```sh
gh api repos/SharedCode/joltrin/contents/verify/verify.go?ref=a139ad7d1af5babf2c1d2105ba4312802264f315
gh api repos/SharedCode/joltrin/contents/verify/reachability.go?ref=a139ad7d1af5babf2c1d2105ba4312802264f315
```

No third-party build was executed. Search coverage is limited to discoverable
English-language queries, the connector's accessible/indexed repositories,
publicly readable sources and a single Claim session. Patents were searched
through the Google Patents web index; this is not an exhaustive family or
classification search. Unpublished, private and differently named implementations
remain possible. Source-reading failures also included a guessed Joltrin
`verify/reachability_test.go` path (404; directory listing then identified the
actual tests), and an SMERC repository README lead (404); no feature conclusions
depend on either failure. One internal-link lookup returned a different reference
than requested; author-paper URLs were subsequently resolved directly and read.

## Verdict on novelty

No inspected source was established to meet the **complete revised claim**.
That is the bounded result of this search, not proof that nobody has ever built
it. Broad rollback verification, mutable-state reverse planning, policy analysis,
authorization-sensitive recovery, and offline evidence are all prior art.
The possible contribution is a useful combination: a small runbook input contract
that separates lost authority from absence of a declared recovery path and
exports checkable evidence at every forward prefix. Confidence in a wide novelty
gap is low; combination-level novelty remains plausible. A source already
providing this full contract would retire the finalist. No build success,
real-infrastructure correctness, or incident reduction has been demonstrated.
