# Paradoxes & whoopses — when methods disagree 🎭

A small gallery of **low-stakes elections with surprising results** — the kind where the
*same ballots* hand the win to a *different candidate depending on the method.* They're
fun ("ha! three winners from one set of ballots!"), they're great teaching moments, and —
read with care — they keep us **honest**.

> **The even-handedness pledge.** These examples are *not* a stick for beating one method.
> Every voting method fails *some* fairness criterion (that's Arrow & Gibbard — no method
> escapes), so this folder makes a point of letting **each camp take a turn as the
> punchline**. If you catch yourself only collecting IRV's faults, that's the bias to
> resist — add the matching STAR, Approval, and Condorcet whoopses too. Read
> **[`reading_these_fairly.md`](./reading_these_fairly.md)** before adding any case.

## The cases

| # | Lesson | The whoops | Who takes the hit |
|---|--------|-----------|-------------------|
| 01 | [Tennessee — 3 methods, 3 winners](./Whoops_01_tennessee_three_winners.md) | one ballot set → Plurality=Memphis, IRV=Knoxville, Condorcet/STAR=Nashville | **Plurality & IRV** |
| 02 | [STAR misses the Condorcet winner](./Whoops_02_star_misses_condorcet.md) | the head-to-head winner is too low-scored to reach the runoff | **STAR** |
| 03 | [a Condorcet cycle (rock-paper-scissors)](./Whoops_03_condorcet_cycle_rps.md) | majority rule is intransitive — *no* Condorcet winner exists | **Condorcet / Ranked Robin** |
| 04 | [IRV buries the centrist (Ossipoff)](./Whoops_04_ossipoff_centrist_irv.md) | the plurality *and* Condorcet winner is eliminated; IRV elects D | **IRV** |
| 05 | [many IRV pathologies in one (Brams)](./Whoops_05_brams_many_pathologies_irv.md) | Condorcet failure + no-show + truncation + non-monotonicity | **IRV** |

Cases 01–03 are STAR/score files (engine-verified, in the test library); 04–05 are
**ranked-ballot** RCV-IRV cases (IRV rounds engine-verified, Condorcet winners checked by
pairwise tally). Each carries a **fairness box**.

## Balance ledger

The even-handedness pledge isn't a vibe — it's a count. Keep this honest, and when it
tilts, the **next** case should hit the over-represented direction's *opposite*.

| Method | Times it's the punchline | Cases |
|--------|:---:|-------|
| Plurality | 1 | 01 |
| **RCV-IRV** | **3** | 01, 04, 05 |
| STAR / score | 1 | 02 |
| Condorcet / Ranked Robin | 1 | 03 |
| Approval | 0 | — |

**Balance owed (as of cases 01–05): the folder leans IRV (3).** The next additions should
embarrass the *score family* — **Approval** (0 so far) and **STAR** — not IRV. Candidate
follow-ups: an Approval "bland-winner" / chicken-dilemma case, or a STAR
non-monotonicity construction. *Don't add another IRV whoops until this evens out.*

## How to read these (the short version)

A "whoops" is only worth teaching if it's an **honest** one. The full test is in
[`reading_these_fairly.md`](./reading_these_fairly.md), but the gist:

- **Structural, not contrived** — happens across a region of realistic electorates, not at
  one knife-edge with absurd weights.
- **Sincere, not strategic** — failures under honest voting are fair game; "but you can
  game it" applies to *every* method (Gibbard), so it's the weakest, muddiest angle.
- **Realistic electorate** — spatial / natural distributions, not alien voter behavior.
- **Bonus: it really happened** — Burlington 2009, Alaska 2022 aren't constructions.

All three cases here pass that test (Tennessee is canonical; the STAR miss and the
Condorcet cycle are foundational, sincere-vote results) — which is itself the lesson:
these aren't cheap gotchas.

## These are LH-only (house principle)

The contrast here is **method vs method**, not **BV vs LH** — BetterVoting and the engine
agree on these. So no BV screenshots; see the
[two-view principle](../Flat_scores_ties/README.md) for when those are warranted.

## Run them yourself

```
cd STARVote_LH_tabulation_engine
python starvote_larry_hastings.py "../01_Single_winner/paradoxes_and_whoops/Whoops_01_tennessee_three_winners.yaml"
```

Each writes a full audit copy to `paradoxes_and_whoops_tabulated/`. All three also live as
flat-schema positive test cases in `YAML_library/1_positive/` (each verifies the **STAR**
winner — the gallery is about *disagreement*, so the test pins STAR's answer, and the
lesson narrates the others).

## Books on voting paradoxes

Voting theory is rife with mathematical anomalies, and several books catalogue them:

- **Hannu Nurmi — *Voting Paradoxes and How to Deal with Them* (1999).** The reference
  manual: systematically catalogues the no-show paradox, monotonicity failures, Condorcet
  cycles, etc., and rates how vulnerable each method is to each.
- **Donald G. Saari — *Disposing Dictators, Demystifying Voting Paradoxes* (2008).** A
  geometric take on social choice — argues Arrow's theorem and the paradoxes reflect
  positional systems *discarding information*, not democracy being broken.
- **William Poundstone — *Gaming the Vote: Why Elections Aren't Fair* (2008).** The
  general-audience pick: history of paradoxes and strategic voting, arguing independent-
  score methods (Approval, Score) sidestep paradoxes inherent to strict ranking like IRV.
- **Michel Balinski & Rida Laraki — *Majority Judgment* (2011).** Argues that turning
  individual rankings into a collective ranking makes Arrow/Condorcet paradoxes
  inevitable, and proposes grading candidates on a common scale instead.

## More whoopses to mine (sources)

- **rangevoting.org** (Warren Smith, the Center for Range Voting) — a deep trove of
  method-failure constructions and paradoxes.
- Burlington 2009, Alaska 2022 (real center-squeeze elections — see
  [`RCV_IRV_center_squeeze.md`](../../00_start_here/concepts/RCV_IRV/RCV_IRV_center_squeeze.md)).
- Classic social-choice paradoxes (Condorcet, Arrow, no-show, monotonicity).

> Adding one? Run it through the engine, write the fairness box, and make sure the camp it
> embarrasses isn't always the same one.
