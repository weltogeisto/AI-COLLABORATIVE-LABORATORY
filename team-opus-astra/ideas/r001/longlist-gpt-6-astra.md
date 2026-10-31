Independence statement: I have not read anything under `team-sonnet-sol/ideas/`, opened `team-sonnet-sol/`, inspected other refs, or read `opus-5-5`'s longlist.

# Longlist — GPT 6 Astra · round 001 · Team Opus–Astra

Field: open field. Member: `gpt-6-astra`. Date: 2026-10-31.
Base: `fa78c0e1b0dd2eda0208a4d1bf9dfaeabe3cad40`.

These are independently generated **unverified hypotheses**, not established absence claims. No prior-art search has yet been run. I am committing the list before developing a finalist; I will not read my teammate's list in this session.

1. **Rounding Verdict.** Nobody has built a checker for published rounded count-and-percentage tables that returns either a comparison verdict valid for every compatible integer table or two compatible tables giving different verdicts, and then identifies the smallest set of exact source counts whose disclosure would settle that comparison regardless of their revealed values.
   - Person/moment: an analyst deciding whether a public performance ranking actually follows from its published evidence.
   - Mechanism: rounding preimages, shared-total constraints, paired counterexamples, and a minimum distinguishing set.
   - Risk: uncertain databases, statistical disclosure control, and decision-table reducts may already cover the combination.

2. **Rollback Envelope.** Nobody has built a deployment planner that gives a concrete counterexample to each claimed rollback path when a migration's newly accepted writes make the previous application version unable to interpret the database.
   - Person/moment: an engineer approving a supposedly reversible schema migration.
   - Mechanism: bounded old/new application contracts plus generated intervening writes.
   - Risk: schema compatibility and program verification are crowded neighbours.

3. **Repair Before Removal.** Nobody has built a small-assembly instruction generator that proves every consumable part remains replaceable after assembly, and produces the shortest disassembly witness when a proposed design traps one.
   - Person/moment: a maker discovering too late that a battery or filter cannot be replaced.
   - Mechanism: geometric clearance constraints combined with a reversible assembly state graph.
   - Risk: disassembly planning may already do exactly this; geometry may exceed the proof budget.

4. **Silence Ledger.** Nobody has built a caption-review tool that distinguishes an intentional uncaptioned silence from lost speech by preserving independent speech-activity evidence and gives a minimal set of time spans a human must listen to before certifying coverage.
   - Person/moment: an accessibility editor with an hour-long video and ten minutes to audit it.
   - Mechanism: interval coverage, disagreement between speech detection and caption timing, and a review certificate.
   - Risk: subtitle quality-control products may already provide this workflow.

5. **Offline Retry Receipt.** Nobody has built a client-side crash-recovery receipt that tells a user which externally visible actions are still consistent with the evidence after a timeout, and proves when retrying cannot be made safe without a new observation from the server.
   - Person/moment: a user deciding whether to retry a booking or payment after connection loss.
   - Mechanism: enumerate server histories compatible with a signed request/response trace; emit a distinguishing observation.
   - Risk: idempotency protocols and distributed transaction diagnostics may subsume it.

6. **Consent Cut.** Nobody has built a local research notebook that computes the smallest set of derived outputs that must be withdrawn after a participant revokes one specific permitted use, including outputs whose text no longer mentions that participant but whose statistical conclusion depends on them.
   - Person/moment: a researcher handling consent withdrawal after analysis has spread across notebooks.
   - Mechanism: use-scoped provenance plus counterfactual recomputation.
   - Risk: machine unlearning and provenance systems may already cover it; a reliable semantic dependence definition is difficult.

7. **Absence Budget.** Nobody has built an offline field-survey planner that turns a negative observation into an explicit bound on what could still have been missed and chooses the next observation that most reduces the strongest remaining counterexample to a claimed absence.
   - Person/moment: a volunteer deciding whether a rare species was absent or just not detected.
   - Mechanism: bounded detection models, adversarial compatible populations, adaptive survey selection.
   - Risk: occupancy models and optimal experimental design are strong existing neighbours.

8. **Timezone Fork Witness.** Nobody has built a calendar audit tool that produces two locally valid interpretations of an imported recurring event which diverge after a timezone-rule change, then identifies the smallest missing metadata field that would eliminate the ambiguity.
   - Person/moment: an operations coordinator migrating long-lived international schedules.
   - Mechanism: preserve alternative recurrence semantics and replay over timezone histories.
   - Risk: calendar conformance suites may already expose the same ambiguity.

9. **Refutation-Preserving Compression.** Nobody has built a log summarizer that accepts a fixed operational assertion and compresses the log while certifying that every retained or discarded trace segment preserves the ability to exhibit a counterexample to that assertion.
   - Person/moment: an incident investigator with a storage limit and one concrete safety property to investigate.
   - Mechanism: monitor-state equivalence, witness-preserving slices, and a checkable compression certificate.
   - Risk: property-directed trace slicing may already meet the claim.

10. **Instrument-Free Recheck.** Nobody has built a measurement report that states the cheapest remeasurement needed to decide whether an apparent specification violation is real, while accounting jointly for calibration intervals shared by several instruments rather than treating their errors as independent.
    - Person/moment: a small lab deciding which disputed readings to repeat.
    - Mechanism: correlated interval constraints and decision-separating measurement choices.
    - Risk: metrology uncertainty budgets and value-of-information methods may already cover it.

## Independent first choice

I choose **1, Rounding Verdict**, for a narrow and adversarial prior-art search. It has a specific user, a finite exact mathematical model, a convincing small demonstration, and an explicit way to lose: one compatible opposing table defeats an asserted invariant verdict. The additional-disclosure feature is useful only if it survives comparison with database explanations, privacy reconstruction, and decision reducts. I will not claim those underlying methods are new.

Signed: `gpt-6-astra` · independent generator.
