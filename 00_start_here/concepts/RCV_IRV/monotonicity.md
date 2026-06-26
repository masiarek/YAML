# Monotonicity

**One line:** a method is *monotone* if **ranking/scoring a candidate higher can
never cause them to lose** (and lower can never cause them to win). **RCV-IRV
violates this**; STAR (and any additive, summable method) does not.

→ Glossary: [`monotonicity`](../../GLOSSARY.md) · related: [`center_squeeze.md`](./center_squeeze.md)

---

## Why IRV can fail it

IRV decides *who is eliminated* round by round, so **changing the elimination order
can flip the result backwards.** Adding first-place support to the eventual winner
can knock out a *different* candidate first, changing who survives — and the winner
can end up **losing**. Extra support hurt them.

## Worked example — run it

The classic 3-candidate case, as two elections that differ by **one change**:

→ [`monotonicity_irv_before.yaml`](../../../01_Single_winner/monotonicity_irv_before.yaml)
 · [`monotonicity_irv_after.yaml`](../../../01_Single_winner/monotonicity_irv_after.yaml)

```
BEFORE                          AFTER  (4 voters raise X: Y>Z → X>Y)
  12: X>Y                         16: X>Y
  12: Y>Z                          8: Y>Z
  10: Z>X                         10: Z>X
R1: X12 Y12 Z10 → Z out          R1: X16 Y8 Z10 → Y out
Z>X transfers → X 22  ✅ X WINS   Y>Z transfers → Z 18  ❌ X LOSES (Z wins)
```

X went from **12 first-choices and a win** to **16 first-choices and a loss** —
nothing else changed. (Verified on the RCV-IRV engine.)

## STAR stays monotone — same profile

Translate those ballots to 0–5 scores (1st → 5, 2nd → 3, unranked → 0) and run STAR:

→ [`monotonicity_star_before.yaml`](../../../01_Single_winner/monotonicity_star_before.yaml)
 · [`monotonicity_star_after.yaml`](../../../01_Single_winner/monotonicity_star_after.yaml)

STAR elects **X before *and* after** the 4 voters raise X — raising the winner can't
hurt them. The _after file's `[Divergence from STAR]` block makes the contrast
self-documenting, on the very same ballots:

```
STAR    = X
RCV-IRV = Z   (differs from STAR)
```

Same voters, same change: RCV-IRV flips X → Z; STAR doesn't budge. (Verified on the engine.)

## How often? Not rare

A spatial-model study (**Ornstein & Norman, *Public Choice* 2014**) estimates a
**lower bound of ~15%** monotonicity failure in *competitive* three-candidate IRV
races — and the rate rises with closeness. This is a structural hazard of
eliminate-and-transfer, not a freak event.

## Two flavors (both real)

Per a study of US RCV elections 2004–2022 (Graham-Squire & McCune, arXiv 2301.12075):
- **Upward paradox — Alaska 2022.** Had ~6,000 Palin-only ballots instead ranked the
  *winner* Peltola first, Peltola would have **lost** (the extra first-place votes
  eliminate Palin first, and Begich then beats Peltola).
- **Downward paradox — San Francisco 2020 (D7 Supervisor).** Shifting the *loser*
  Engardio **down** on ~800 ballots would have made him **win**.

## Not the same as Later-No-Harm

A common mix-up: monotonicity (does *raising* a candidate ever hurt them?) is a
different criterion from Later-No-Harm (does adding a *lower* preference ever hurt
your *top* choice?). IRV passes LNH but **fails** monotonicity; STAR is the reverse
shape. (LNH vs FBC is worked out in
[`favorite_betrayal_voting_301.md`](../../../interviews_conversations/favorite_betrayal_voting_301.md).)

## Real election

**Burlington, VT 2009 (mayor)** is the textbook real-world failure — Kiss won, and
the result was non-monotonic (and a [center squeeze](./center_squeeze.md): Condorcet
winner Montroll was eliminated early). IRV was repealed there in 2010.

## How STAR avoids it

STAR's winner comes from **sums** (total scores, then a pairwise majority between the
top two). Adding support can only **raise** a candidate's total and head-to-head
standing — there's no elimination order to perturb, so the backwards paradox can't
arise.

→ More source notes: **RCV-IRV monotonicity** group in
[`LINKS.md`](../../../interviews_conversations/LINKS.md).

Sources: [Ornstein & Norman 2014 (Public Choice)](https://link.springer.com/article/10.1007/s11127-013-0118-2),
[Graham-Squire & McCune, RCV in the US 2004–2022 (arXiv)](https://arxiv.org/pdf/2301.12075.pdf),
[Burlington 2009 (Wikipedia)](https://en.wikipedia.org/wiki/2009_Burlington_mayoral_election),
[monotonicity criterion (Wikipedia)](https://en.wikipedia.org/wiki/Monotonicity_criterion).
