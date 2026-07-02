# IRV Non-Monotonicity — When *More* Support Makes You Lose

**One line:** under **RCV-IRV**, giving the eventual winner **more** first-choice
support can cause them to **lose** — and moving a loser **down** can make them
**win**. This isn't a glitch; it's baked into eliminate-and-transfer.

> **Applies to:** [Hare](RCV-IRV-Hare.md) **and the other sequential-elimination
> variants** — [BTR](RCV-IRV-BTR.md), [Coombs](RCV-IRV-Coombs.md), and
> [Baldwin/Nanson](RCV-IRV-Baldwin-Nanson.md) are non-monotonic too, because
> *eliminate-and-transfer* is the cause. (So this is **not** Hare-specific the way
> [center squeeze](RCV_IRV_center_squeeze.md) is.) The non-eliminating Condorcet
> methods like [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) are **monotonic**.
> See [Which RCV-IRV?](RCV_IRV_variants.md).

> Why this page matters: most people are never told this. "Rank your honest
> favorite first, it can't backfire" is the core promise of IRV — and
> non-monotonicity is the case where that promise breaks. It's the single most
> underappreciated structural problem with the method.

→ STAR doesn't have this failure — see [`STAR is monotone`](../STAR_Voting/STAR_monotonicity.md).
Glossary: [`monotonicity`](../GLOSSARY.md).

---

## What "monotone" means

A voting method is **monotone** if **ranking a candidate higher can never cause
them to lose**, and ranking them lower can never cause them to win. It's the most
basic sanity check you'd expect from any election: support should help, not hurt.

**RCV-IRV fails it.** STAR (and any additive, summable method) passes it.

## Why IRV fails it

IRV doesn't add support up — it **eliminates** the candidate with the fewest
first-choices, round by round, and transfers their ballots. The winner depends
entirely on **who gets eliminated, and in what order.**

That's the trap: changing how many first-choices a candidate has changes *who is
eliminated first* — which changes *who their ballots transfer to* — which can flip
the final result **backwards**. Adding support to your favorite can knock out the
opponent who would have lost to them, leaving behind the opponent who beats them.

## Worked example — run it yourself

The classic 3-candidate case, as two elections that differ by **one change**: 4
voters raise X from second to first.

→ [`monotonicity_irv_before.yaml`](../../method_comparisons/monotonicity/monotonicity_irv_before.yaml)
 · [`monotonicity_irv_after.yaml`](../../method_comparisons/monotonicity/monotonicity_irv_after.yaml)

```
BEFORE                              AFTER  (4 voters raise X: Y>Z → X>Y)
  12: X>Y                             16: X>Y
  12: Y>Z                              8: Y>Z
  10: Z>X                             10: Z>X
R1: X12  Y12  Z10  → Z eliminated    R1: X16  Y8  Z10  → Y eliminated
    Z>X transfers → X 22             Y>Z transfers → Z 18
    ✅ X WINS                          ❌ X LOSES — Z wins
```

X went from **12 first-choices and a win** to **16 first-choices and a loss** —
and *nothing else changed*. The four extra first-place votes for X eliminated Y
instead of Z; Y's ballots flowed to Z; Z then beat X. (Verified on the RCV-IRV
engine: X elected with 22 before, Z elected with 18 after.)

## How often does this happen? Not rare

- A spatial-model study (**Ornstein & Norman, *Public Choice* 2014**) estimates a
  **lower bound of ~15%** monotonicity failure in *competitive* three-candidate IRV
  races — and the rate climbs as the race gets closer. This is a structural hazard
  of elimination, not a freak coincidence.

## Two real-world flavors (both have happened)

Per a study of US RCV-IRV elections 2004–2022 (Graham-Squire & McCune, arXiv 2301.12075):

- **Upward paradox — Alaska 2022 (US House special).** Had ~6,000 Palin-only voters
  instead ranked the *winner* Peltola first, Peltola would have **lost** — those
  extra first-place votes eliminate Palin first, and Begich then beats Peltola.
  Raising the winner defeats the winner.
- **Downward paradox — San Francisco 2020 (D7 Supervisor).** Shifting the *loser*
  Engardio **down** on ~800 ballots would have made him **win**. Less support, more
  victory.

## A textbook real election

**Burlington, VT 2009 (mayor).** Kiss won, but the result was **non-monotonic** —
and it was also a [center squeeze](RCV_IRV_center_squeeze.md): the Condorcet winner
Montroll (who beat every rival head-to-head) was eliminated early. Voters who ranked
Kiss *lower* could have made him win. Burlington **repealed IRV in 2010** over this
race.

## Don't confuse it with Later-No-Harm

A frequent mix-up: **monotonicity** asks "can *raising* a candidate ever hurt them?"
**Later-No-Harm** asks "can adding a *lower* preference ever hurt your *top* choice?"
They're different criteria. IRV **passes** Later-No-Harm but **fails** monotonicity;
STAR is the opposite shape. (Worked out in
[`favorite_betrayal_voting_301.md`](../../interviews_conversations/favorite_betrayal_voting_301.md).)

→ More source notes: **RCV-IRV monotonicity** group in
[`LINKS.md`](../../interviews_conversations/LINKS.md).

Sources: [Ornstein & Norman 2014 (Public Choice)](https://link.springer.com/article/10.1007/s11127-013-0118-2),
[Graham-Squire & McCune, RCV in the US 2004–2022 (arXiv)](https://arxiv.org/pdf/2301.12075.pdf),
[Burlington 2009 (Wikipedia)](https://en.wikipedia.org/wiki/2009_Burlington_mayoral_election),
[monotonicity criterion (Wikipedia)](https://en.wikipedia.org/wiki/Monotonicity_criterion).
