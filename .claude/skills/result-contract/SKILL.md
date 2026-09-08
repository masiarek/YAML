---
name: result-contract
description: The `--json` result contract of the STAR tabulation engine — what star_result.schema.json guarantees, the never-re-derive-a-count rule, the five shared tallies, and the tiebreaks[] history. Load before touching result_json.py, star_result.schema.json, classify_method, any *_tally function, or anything that emits or consumes the JSON result.
---

# The `--json` result contract

*Migrated out of `CLAUDE.md` on 2026-09-08 so it loads on demand instead of in every session. The rules below are unchanged.*

**The machine-readable result contract (`--json`) — never re-derive a count into it**
(added 2026-08-10). `starvote_larry_hastings.py <case.yaml> --json` emits one versioned
JSON object per election — winners, the rounds that produced them, the pairwise matrix,
and which tie-break rung fired — built by
[`result_json.py`](STARVote_LH_tabulation_engine/result_json.py) against the published
[`star_result.schema.json`](STARVote_LH_tabulation_engine/star_result.schema.json).
The implementer-facing door is
[`result_schema.md`](07_Concepts/tabulation_engines/result_schema.md); it is Track A's
A-1/A-2 and the built half of D3 in
[`star_reference_package.md`](07_Concepts/tabulation_engines/star_reference_package.md).
**The one rule:** every number in it comes from the same function the printed report
calls. Five tallies were split out of their printers for exactly this —
`classify_method` (the method-alias table, one place, read by the CLI dispatch *and* the
contract), `ranked_robin_tally`, `approval_tally`, `plurality_single_tally` /
`plurality_multi_tally`, and `rcv_irv_tabulation.tabulate` — so adding a family means
extending the shared tally, **never** writing a second count inside `result_json.py`.
Two things the build proved, worth not re-learning: **multi-winner Choose-One counts
every MARK while single-winner Choose-One SPOILS an overvote**, so neither can be
derived from the other (it elected the wrong slate on five block-voting cases); and
`tiebreaks: []` is a **positive claim** that no rung fired — which is how a
right-winner-wrong-path result gets caught, and what 567 winner-only answer keys never
could. A claim that strong has to be *earned*, and for a year it was not: the builder
could see one kind of tie (the finalists ladder `resolve_finalists()` replays for
single-winner STAR), so every seat the **lot** bought — a Bloc/PR seat, and a
single-winner Automatic Runoff too — emitted `tiebreaks: []`, on **23 cases**, most of
them cases whose whole subject is the lot. Fixed 2026-08-21 (schema **1.1.0**, +
`tiebreaks[].round`) the only way that respects the never-re-derive rule:
`LotNumberTiebreaker` now logs its own calls in `self.events`, and `_lot_ties()` reads
that log — the count is not replayed, it is *read off the object that broke the tie*.
The invariant to keep is a mirror one, and it is tested over the whole score corpus:
**one `rung: "lot"` entry per `[Tiebreaker: Lot Number Priority]` banner the report
prints** — no fewer, and no more (the finalists replay must not double-count the banner
it shares). **The mirror gap closed the same day (schema 1.2.0):** 1.1.0 taught the
builder to see the *lot*, but a runoff tie broken by a **deterministic** rung fires no lot
event and belongs to neither replay, so **16 more cases** emitted `tiebreaks: []` on an
election whose report says in full *"Automatic Runoff Round: First tiebreaker"* — including
`bv830_vb3xv2_no_condorcet_tie_score` and `tie_break_04_runoff_five_star_breaks`, files
named for the rung the JSON did not mention (12 `score`, 4 `five-star`). `resolve_runoff()`
is the mirror of `resolve_finalists()` — same replay discipline, starvote's own round
functions — and the mirror invariant is tested too: `rounds.runoff.tied` and a
`stage: "winner"` entry must agree in **both** directions, so a swallowed tie and an
invented one both fail. It was found by pointing
[`tie_taxonomy_sweep.py`](STARVote_LH_tabulation_engine/tools_adam/tie_taxonomy_sweep.py)
at the contract — a quarter-million coarse-scale elections, every tie classified against the
published taxonomy — which is the general lesson: a claim this strong needs something
adversarial aimed at it, not more cases that happen to agree. Still invisible, and said so
in print: the rungs *below* the lot inside a Bloc/PR round, which run in starvote's own
counting functions and report nothing back. Locked by
[`tests/test_result_json.py`](STARVote_LH_tabulation_engine/tests/test_result_json.py)
(every case validates against the schema and meets its answer key through the JSON path;
`--json` must stay pure — JSON on stdout, no report, no `_tabulated` mirror). A method
the engine does not count (Range 0–9, CAV, 3-2-1) raises `UnsupportedMethod` rather than
being answered: "out of scope" must stay distinguishable from "wrong".
