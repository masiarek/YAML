# The Fidelity Ladder — converting between scores and ranks

*Every time you turn a **score** ballot into a **ranked** one (or vice versa), the
conversion either **drops** information or **invents** it. This page ranks the common
conversions by **how much they fabricate** — which turns out to explain why Ranked Robin is
clean, why RCV-IRV is fragile, and why Borda is a leap.*

→ Companions: [scores vs. ranks](scores_vs_ranks.md) · [strict vs. weak ranks](strict_vs_weak_ranks.md) ·
[Borda](../other_ranked_methods/borda.md) · Glossary: [`scores vs ranks`](../GLOSSARY.md)

---

## The one idea: scores contain ranks; ranks don't contain scores

A score ballot says *how much* you like each candidate — and that **automatically** contains
the order. A ranked ballot says only the **order** — it never contained the intensities. So
the two directions are not symmetric, and a conversion is only as honest as the amount it has
to make up.

## The ladder

| # | Conversion | Used by | Drops | **Invents** |
|:-:|------------|---------|-------|-------------|
| 1 | **score → weak rank** | **Ranked Robin** | intensity | **nothing** — ties stay ties (`A=B`) |
| 2 | **score → strict rank** | **RCV-IRV (Hare)** | intensity | a **tie-break order** (`A=B` forced to `A>B`) |
| 3 | **rank → score** | **Borda** | — | the **entire intensity** (the spacing) |

Read it top to bottom and the fabrication grows:

- **Rung 1 — score → weak rank (Ranked Robin).** A score ballot `A5 B3 C3 D0` becomes
  `A > B=C > D`. You lose the intensity, but the **ties survive** (B and C stay tied, because
  weak ranks allow it). Nothing is invented — RR's pairwise count reads exactly the equal-
  preference structure the voter gave. **This is the honest reduction.**
- **Rung 2 — score → strict rank (RCV-IRV).** IRV needs a *strict* order and **cannot
  represent a tie**, so it must turn `B=C` into either `B > C` or `C > B` using an arbitrary
  rule (candidate priority / lot). That invented order is real input to the count — and it's
  exactly why an IRV result can be **fragile**: flip the tiebreak and the manufactured order
  flips, which can change who's eliminated.
- **Rung 3 — rank → score (Borda).** Starting from a bare ranking `A > B > C`, there are *no*
  intensities to recover, so [Borda](../other_ranked_methods/borda.md) **invents all of them**
  by assuming a spacing (even gaps: 2, 1, 0). It's a defensible convention, but it's pure
  fabrication of a dimension the ballot never had.

## One ballot, all three conversions

Voter #1 from the random-sweep record 0, a score ballot `A3 B3 C0 D2 E4 F3`:

```
scores:                A3 B3 C0 D2 E4 F3

rung 1  (RR, weak):    E > A=B=F > D > C          ← ties kept; nothing invented
rung 2  (IRV, strict): E > A > B > F > D          ← A=B=F forced to A>B>F; C dropped (0=unranked)
rung 3  (Borda, if you ONLY had a ranking): assign 5,4,3,2,1,0 by position — invents the gaps
```

Same ballot; the more strictness or intensity the method demands, the more it has to make up.

## Why this matters in practice

- **You can hand STAR scores to Ranked Robin or RCV-IRV** (derive ranks) — but **you cannot
  run STAR on ranked ballots**, because there are no scores to add. The richer object only
  flows downhill.
- **RCV-IRV's fragility is rung 2 in action** — the tie-break it's forced to invent. See
  [center squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md) and the
  [RR-vs-Condorcet side-by-side](../RCV_Ranked_Robin/ranked_robin_vs_condorcet.md), which
  shows rung 1 and rung 2 on the same ballot.
- **STAR's ballot sits above the whole ladder** — it carries the intensity natively, so it
  never has to drop or invent anything to *be* itself; it only converts *downward* when
  compared against ranked methods.

## Related

- [Scores vs. ranks](scores_vs_ranks.md) — why scores are the richer ballot
- [Strict vs. weak ranks](strict_vs_weak_ranks.md) — the rung-1-vs-rung-2 distinction in depth
- [Borda](../other_ranked_methods/borda.md) — rung 3, manufacturing scores from ranks
- [Ranked Robin vs. Condorcet](../RCV_Ranked_Robin/ranked_robin_vs_condorcet.md) — rungs 1 & 2 live on one election
