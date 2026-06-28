<!--
  GitHub issue text. Filed as Equal-Vote/bettervoting#1407:
  https://github.com/Equal-Vote/bettervoting/issues/1407
  Framing: a reconciliation + correctness issue — the WINNER is identical, but
  BetterVoting labels "Equal Support" (no-preference) ballots as ABSTENTIONS and
  drops their stars, which is confusing and arguably wrong.
-->

> **Filed as [Equal-Vote/bettervoting#1407](https://github.com/Equal-Vote/bettervoting/issues/1407).**

# Equal Support ballots (incl. an all-5s vote) are being counted as "abstentions" and dropped from the score totals

## One-line summary

In a real STAR race, BetterVoting reports **6 abstentions**, but those 6 ballots
are not abstentions — they are **Equal Support** ballots (every candidate scored
the same), and **two of them carry non-zero scores**: one voter gave *all seven*
candidates **5 stars**, another gave all seven **4 stars**. Treating an all-5s
ballot as an "abstention" is confusing, and dropping its stars changes the score
totals. The winner is unaffected, but the labeling and the score-round bookkeeping
are wrong.

## The election

A real BetterVoting STAR race, id `pet` ("What Makes the Best Pet?"), 7 candidates,
461 ballots. Public ballots + both reports:

- Repo (ballots, converted YAML, full engine report): <https://github.com/masiarek/YAML/tree/master/01_Single_winner/pet_real_bv_election>
- Live result (**may change** if recounted): <https://bettervoting.com/pet/results>
- **Frozen snapshot** of the result + raw export this issue is based on (so the
  numbers below stay reproducible even if the live page changes):
  [`BV_result_snapshot.md`](https://github.com/masiarek/YAML/blob/master/01_Single_winner/pet_real_bv_election/BV_result_snapshot.md)
  · [`best_pet_c7_b461_bv_export.json`](https://github.com/masiarek/YAML/blob/master/01_Single_winner/pet_real_bv_election/best_pet_c7_b461_bv_export.json)

## Evidence

From this election's own export, `summaryData` reports:

```json
{ "nAbstentions": 6, "nTallyVotes": 455 }
```

Pulling those ballots out of the 461, **all six are "flat" — every candidate gets
the same score** — and they are:

```
[0,0,0,0,0,0,0]   ×3    all-zero (cast: "I rate everyone zero")
[ blank      ]    ×1    truly blank — no score recorded (a real abstention)
[5,5,5,5,5,5,5]   ×1    all FIVES — a maximally engaged voter
[4,4,4,4,4,4,4]   ×1    all FOURS
```

So of BetterVoting's "6 abstentions," **only the 1 blank ballot is actually an
abstention.** The other five are *cast* ballots, and two of them are about as
engaged as a ballot can be.

This single classification explains every difference between BetterVoting and an
independent STAR tabulator on the same ballots:

| | BetterVoting | Full count (all 461) |
|---|---:|---:|
| Ballots tallied | 455 | 461 |
| "Abstentions" | 6 | 1 (the blank only) |
| Equal Support in runoff | 92 | 98 |
| Per-candidate score totals | 9 lower (e.g. Dog **1798**) | (e.g. Dog **1807**) |
| Runoff: Dog vs Cat | 190 / 173 | 190 / 173 |
| **Winner** | **Dog** | **Dog** |

Note the arithmetic closes exactly: `92 + 6 = 98`, and the all-5s + all-4s ballots
contribute `5 + 4 = 9` stars to **every** candidate — precisely the uniform
9-point gap in the score totals. The flat ballots' stars are being removed from
the **scoring round**, not just set aside in the runoff.

## Why this is wrong (and confusing)

A ballot that scores every candidate the same is **Equal Support / no preference**,
which is a real, deliberate vote — not an abstention:

1. **An all-5s voter clearly participated.** Calling that an "abstention" tells the
   voter (and any auditor) that the ballot was blank. It wasn't.
2. **Those stars should count in the score round.** In STAR, the score round is
   "add every star." An all-5s ballot adds 5 to every candidate; dropping it
   silently lowers every total. (It doesn't change *who* finishes top-two here, but
   it makes BetterVoting's published totals fail to match a hand count of the
   ballots.)
3. **It only *looks* harmless because the example is symmetric.** Equal Support is
   correctly *neutral in the runoff* (a flat ballot has no preference between the
   two finalists, so it's rightly excluded from the runoff **denominator**). That
   is the legitimate idea — but it belongs in an **Equal Support** bucket, counted
   in the score round and excluded only from the runoff percentage. Folding it into
   "abstention" and dropping it from the tally conflates two different things.

The correct STAR treatment (and what the other tabulator does): a flat ballot is
**counted in the score round** and lands in **Equal Support** in the runoff; only a
**blank** ballot (no scores at all) is an abstention.

## Minimal reproduction

Two candidates, and a single `5,5` ballot shows it
([file](https://github.com/masiarek/YAML/blob/master/01_Single_winner/pet_real_bv_election/abstention_reconciliation_min_c2_b6.yaml)):

```
A,B
5,0    # prefers A
4,0    # prefers A
0,5    # prefers B
5,5    # EQUAL SUPPORT — loves both equally (NOT an abstention)
0,0    # all-zero — cast, supports neither
-,-    # blank — the only true abstention
```

Expected, correct STAR reading: **6 ballots cast, 1 abstention** (the blank). The
`5,5` and `0,0` are counted in the score round and sit in Equal Support in the
runoff:

```
Automatic Runoff:  A 2,  B 1,  Equal Support 3
Voters with a preference: 3 of 6 (3 Equal Support). A 2 (67%) vs B 1 (33%).
```

**Confirmed on two controlled BetterVoting elections.** Both pick the same winner as
an independent STAR tabulator; both show BetterVoting filing flat ballots as abstentions.

**(a) Two candidates** — the tightest statement (id `3w6v4b`, 5 ballots: `0,5` `4,0`
`5,5` `5,0`, blank). BetterVoting reported `nAbstentions: 2, nTallyVotes: 3` — it
counted the **`5,5`** *and* the blank as abstentions. With two candidates a `5,5` *is*
flat, so it gets flagged directly.

**(b) Three candidates** — shows it's a systematic *flat-ballot* rule, not just a
`5,5` quirk (id `dq2dmm`, 8 ballots incl. `0,0,0`, `3,3,3`, `5,5,0`, blank).
BetterVoting reported `nAbstentions: 3, nTallyVotes: 5` — it counted the blank,
`0,0,0`, **and an engaged `3,3,3`** (a voter who scored *every* candidate 3) as
abstentions, but correctly kept `5,5,0` (tied on the two finalists but not flat). So
the rule drops a fully-marked ballot while a real "no preference between the finalists"
ballot is counted — the two ideas are different, and only the flat one is mislabeled.

Frozen exports + both reports, side by side:
[`small_case_abstention_lesson.md`](https://github.com/masiarek/YAML/blob/master/01_Single_winner/pet_real_bv_election/small_case_abstention_lesson.md)
(3-candidate) ·
[`small_abstention_c2_b5.yaml`](https://github.com/masiarek/YAML/blob/master/01_Single_winner/pet_real_bv_election/small_abstention_c2_b5.yaml)
(2-candidate).

## The ask

1. **Don't label Equal Support as "abstention."** A flat / no-preference ballot is
   a cast vote; reserve "abstention" for ballots with no score recorded.
2. **Count flat ballots' stars in the score round**, so published totals reconcile
   with the raw ballots. Exclude no-preference ballots only from the runoff
   **percentage** denominator (as "Equal Support"), where exclusion is correct.
3. If the current behavior is intentional, **document it** on the result card and
   in the docs, with the exact definition, so the numbers can be reconciled.

Happy to share the full JSON export, the other tabulator's complete report, or run
any case you'd like. The runoff result matched perfectly — this is about labeling
and the score-round count, not the outcome. Thanks for BetterVoting.

---

*Cross-reference (our learning docs):*
frozen evidence `BV_result_snapshot.md` ·
synthetic minimal case `abstention_reconciliation_min_c2_b6.yaml` ·
small real-BV reproduction recipe `SMALL_CASE_reproduce_on_BV.md` ·
full race `best_pet_c7_b461.yaml` + `README.md` ·
concept lessons `00_start_here/concepts/tabulation_engines/bettervoting_and_the_engine.md`
and `00_start_here/concepts/STAR_Voting/runoff_percentages.md`.
*This issue:* [Equal-Vote/bettervoting#1407](https://github.com/Equal-Vote/bettervoting/issues/1407).
