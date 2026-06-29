# When the top-scoring candidate isn't the winner

This is STAR's single most important lesson — the one BetterVoting itself asks about
when it pops up *"Why is the top-scoring candidate different from the winner?"*
(Presenting with BetterVoting? [`explaining_to_voters.md`](./explaining_to_voters.md)
has a corrected, plain-language version of that popover.)

**Teaching this?** The step-by-step presenter's guide — the order to teach it in,
why it's a *good* thing, and the devil's-advocate questions with answers — is
[`teaching_runoff_reversal.md`](./teaching_runoff_reversal.md).

**The teaching set — `Runoff_01`–`Runoff_06`.** Six real BetterVoting elections, each a
**two-view lesson** (BetterVoting screenshots beside the LH report) on the *how much vs
how many* arc. Read them in order:

> **When to use two views (house principle).** Show BetterVoting beside the LH report only
> where the two **diverge** (the discrepancy is the lesson, e.g. `Runoff_07`) or where
> reading **BV's own UI** is the point (this set — the screenshots teach how a STAR result
> *looks*). When BV and LH simply agree and there's no UI to teach, LH-only is enough (see
> the [vote-splitting set](../../split_voting/README.md)).

| # | Lesson | Level | What it shows |
|---|--------|:---:|---------------|
| 01 | [confirms the leader](./Runoff_01_confirms_leader_r2pvc9.md) | 101 | control — leader leads **and** wins (baseline) |
| 02 | [the atom](./Runoff_02_atom_reversal_yx9447.md) | 101 | smallest reversal — broadly-liked runner-up loses |
| 03 | [enthusiasts vs majority](./Runoff_03_enthusiasts_vs_majority_rkgtpk.md) | 201 | intense minority leads stars, majority wins (5 cand) |
| 04 | [reversal at scale](./Runoff_04_reversal_at_scale_bfjqmg.md) | 101 | the atom blown up — 67/33, not a fluke |
| 05 | [reversal with Equal Support](./Runoff_05_reversal_with_equal_support_xgkw3w.md) | 201 | "no preference" voters → the two-denominator bridge |
| 06 | [confirms at scale](./Runoff_06_confirms_at_scale_d664xw.md) | 101 | control bookend — leader confirmed 4–1 |
| 07 ⚠️ | [flat ballot / BV bug **(WIP)**](./Runoff_07_flat_ballot_bv_bug_tf73v9.md) | 201/301 | the one case where the reports *disagree* — a flat ballot BV mis-files as an abstention ([#1407](https://github.com/Equal-Vote/bettervoting/issues/1407)) |

Concept hub for all of it: [The Automatic Runoff Round](../../00_start_here/concepts/STAR_Voting/STAR_Automatic_Runoff.md).

**The name for it:** we call this a **Runoff Reversal** — the Scoring-Round leader
*loses* the Automatic Runoff to the finalist more voters prefer. (In technical or
debate writing, the precise phrasing is "the runoff overturns the score leader," to
avoid colliding with *reversal symmetry* in social-choice theory.)

The short answer is in the name of the method. **STAR = Score Then Automatic Runoff.**
The count has just two steps:

1. **Scoring Round.** Add every candidate's stars. The two highest-scoring candidates
   become the **Finalists**.
2. **Automatic Runoff.** Now look only at those two. Each ballot's *full* vote goes to
   whichever finalist it scored higher. The finalist more voters prefer wins.

That second step is the whole point. The candidate with the biggest pile of stars is
the one who *leads the score round* — but leading the score round only makes you a
**finalist**, not the winner. The winner is whichever finalist **more voters actually
prefer**. Usually that's the same candidate. Sometimes it isn't — and *that* is the
lesson.

## The one-screen version (your real election)

This is the actual recorded race in [`03_c7_b3_ice-cream-live.yaml`](./03_c7_b3_ice-cream-live.yaml)
(BetterVoting id `c3m79f`), three voters:

```
          ChocoDrk  ChocoAlm  ChocoHzn  ...
voter 1       4         5         3
voter 2       0         3         0
voter 3       5         0         0
score total   9         8         3      ← ChocoDrk leads the score round
```

**Score round:** ChocoDrk has the most stars (9), so it tops the round. ChocoAlm is
second (8). Those two are the finalists.

**Automatic runoff — ChocoDrk vs ChocoAlm only:**

- Voter 1 scored ChocoAlm 5, ChocoDrk 4 → prefers **ChocoAlm**
- Voter 2 scored ChocoAlm 3, ChocoDrk 0 → prefers **ChocoAlm**
- Voter 3 scored ChocoDrk 5, ChocoAlm 0 → prefers **ChocoDrk**

Two of three voters prefer ChocoAlm, so **ChocoAlm wins, 2–1 (67% to 33%)** — even
though ChocoDrk had more total stars.

Why is that the *right* answer? ChocoDrk's lead came from one superfan giving it a 5.
ChocoAlm is the candidate **more people actually prefer when it comes down to the two
of them**. The runoff makes sure the winner has majority support, not just a loud
minority — and it does it without anyone having to vote dishonestly.

## The lessons in this folder

Each file is a tiny, self-contained election you can run through the engine. They're
built so the score-round leader **loses** the runoff — except the last one, which is
the control case where the leader **wins** (so you can see the runoff isn't rigged).

| File | Field | What happens |
|------|-------|--------------|
| [`01a_c3_b3_more-stars-fewer-voters`](./01a_c3_b3_more-stars-fewer-voters.yaml) | 3 cand, 3 voters | The atom: Almond leads 13 stars, **Brownie** wins the runoff 2–1 |
| [`01b_c3_b9_overturn-holds-at-scale`](./01b_c3_b9_overturn-holds-at-scale.yaml) | 3 cand, 9 voters | Same election, bigger crowd: Almond leads 39–33, **Brownie** wins 6–3 (67/33) |
| [`02_c5_b5_leader-overturned`](./02_c5_b5_leader-overturned.yaml) | 5 cand, 5 voters | Austin leads 22 stars, **Boston** (the broad compromise) wins the runoff 3–2 |
| [`03_c7_b3_ice-cream-live`](./03_c7_b3_ice-cream-live.yaml) | 7 cand, 3 voters | The real race: ChocoDrk leads 9, **ChocoAlm** wins 2–1 |
| [`04_c4_b3_runoff-confirms-leader`](./04_c4_b3_runoff-confirms-leader.yaml) | 4 cand, 3 voters | **Control:** Blue leads *and* wins — the runoff confirms the leader |
| [`05_c3_b5_low-scores-bv1265`](./05_c3_b5_low-scores-bv1265.yaml) | 3 cand, 5 voters | A *real* BetterVoting election with all-low scores: C leads (7), **A** wins the runoff 3–2 |

Two more, in the main folder, push the field even wider:

- [`../06b_c9_runoff-overturns-leader.yaml`](../06b_c9_runoff-overturns-leader.yaml) —
  nine candidates: Andre leads with 9 stars, **Carmen** wins the runoff (Carmen is also
  the candidate who beats every other one-on-one).
- [`../06a_c9_b3_large-field-equal-support.yaml`](../06a_c9_b3_large-field-equal-support.yaml) —
  another nine-candidate field where the runoff **confirms** the leader.

## Why it starts at three candidates

With only **two** candidates there's nothing to teach here: both are automatically
finalists, so the runoff is just "which of the two do more voters prefer" — plain
majority rule, and the star totals never get to matter. The interesting behavior only
appears once the score round has to *choose* two finalists out of a larger field, i.e.
**three candidates or more**. That's why the smallest lesson here is 3 candidates.

## "Is overturning the leader fair?"

It's the opposite of unfair — it's the safeguard. A high score total can come from a
small group of enthusiasts. The runoff asks a different, majority-protecting question:
*of the two finalists, which one do more voters prefer?* When the score leader really
is the most-preferred candidate, the leader wins (that's `04` and `06a`). The runoff
only changes the answer when enthusiasm and majority preference point at different
candidates — and in that case majority preference is exactly what you want to win.

A related point: because your runoff vote is decided by the scores you already gave,
you never have to lowball a candidate to "protect" your favorite. Scoring honestly is
also the smart strategy.

## Going deeper — read the full count (201)

Everything above is the *minimal* view: scores → finalists → runoff → winner, which is
all a first-time voter needs. But every example here also writes a complete **audit
report** to its `_tabulated.txt` sibling (in `runoff_overturns_leader_tabulated/`) — the
pairwise **preference matrix**, the **score distribution**, and the engine's
plain-English **Majority Preference** block stating exactly which candidate led on score
and which won the runoff. Learning to read that report is **Voting 201**: see the annotated walkthrough
[How to read a STAR report](../../00_start_here/concepts/tabulation_engines/LH_starvote/reading_a_star_report.md)
(it uses this folder's BV1265 example), plus
[CURRICULUM 201.1 — Reading the results](../../00_start_here/CURRICULUM.md) and the
step-by-step [STAR vs RCV-IRV count](../../00_start_here/concepts/tabulation_star_vs_irv.md).
Don't put the full report in front of a 101 beginner — point them here when they're ready.

## How often does it happen? (301)

Often enough to matter — but the exact rate depends entirely on your modelling
assumptions, which is a lesson in itself. A brute-force simulation
([`simulations/runoff_reversal_simulation.py`](../../simulations/runoff_reversal_simulation.py))
measures it: under a realistic *spatial* electorate of ~100 voters, a clean Runoff
Reversal happens in roughly **1 election in 11**; under white-noise *Impartial
Culture* it's higher, and at tiny electorates the figure is dominated by ties. The
takeaway for a debate: never quote a bare percentage without naming the model, the
electorate size, and how ties were counted. Full writeup:
[`simulations/README.md`](../../simulations/README.md#runoff-reversal-frequency-simulation).

## Run them yourself

From the engine directory:

```
python starvote_larry_hastings.py "01_Single_winner/runoff_overturns_leader/03_c7_b3_ice-cream-live.yaml"
```

Watch for the engine's **Majority Preference** note — it prints exactly which candidate
earned the highest score and which one won the runoff, whenever the two differ.
