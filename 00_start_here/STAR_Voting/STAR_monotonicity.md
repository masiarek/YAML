# STAR Is Monotone — More Support Never Backfires

**One line:** under **STAR**, raising a candidate's score can **never** cause them
to lose, and lowering it can never cause them to win. Honest support always helps
the candidate it's given to. STAR satisfies the **monotonicity** criterion.

→ The method that *fails* this is RCV-IRV — see
[`IRV non-monotonicity`](../RCV_IRV/RCV_IRV_non_monotonicity.md) (where more first-place
votes can defeat the winner). Glossary: [`monotonicity`](../GLOSSARY.md).

---

## Why STAR can't fail it

STAR's winner comes entirely from **sums**: add up each candidate's scores to find
the two finalists, then take the pairwise majority between those two. There is **no
elimination order** to perturb.

- Raising a candidate's score can only **increase** their total, so it can never
  push them *out* of the top two.
- In the runoff, scoring a finalist higher can only move your vote **toward** them,
  never away.

Because every step is additive and there's nothing to "transfer," the backwards
paradox that hits IRV simply has no mechanism to occur.

## Worked example — the same profile that breaks IRV

Take the exact ballots that make RCV-IRV fail (see the IRV page), translated to
0–5 scores (1st → 5, 2nd → 3, unranked → 0), and run STAR before and after **4
voters raise X**:

→ [`monotonicity_star_before.yaml`](../../01_Single_winner/monotonicity_star_before.yaml)
 · [`monotonicity_star_after.yaml`](../../01_Single_winner/monotonicity_star_after.yaml)

```
            BEFORE                         AFTER (4 voters raise X)
  12: 5,3,0  (X>Y)               16: 5,3,0  (X>Y)
  12: 0,5,3  (Y>Z)                8: 0,5,3  (Y>Z)
  10: 3,0,5  (Z>X)               10: 3,0,5  (Z>X)
  STAR winner: X                  STAR winner: X
```

STAR elects **X both before and after** — raising the winner can't hurt them. The
*after* file's `[Divergence from STAR]` block makes the contrast self-documenting on
the very same ballots:

```
STAR    = X
RCV-IRV = Z   (differs from STAR)
```

Same voters, same change: RCV-IRV flips X → Z; STAR doesn't budge. (Verified on the
engine: STAR elects X in both files.)

## Why this matters

Monotonicity is what lets you tell a voter, truthfully, *"score your favorite at the
top — it can only help them."* Under IRV that advice can backfire; under STAR it
always holds. It's a quieter virtue than the spoiler story, but it's the one that
keeps honest voting safe.

Sources: [monotonicity criterion (Wikipedia)](https://en.wikipedia.org/wiki/Monotonicity_criterion).
