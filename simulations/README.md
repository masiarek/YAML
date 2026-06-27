# Simulations — measure it, don't guess it

This folder holds brute-force simulations that **measure** a claim instead of citing a
number we can't defend. Two rules — each a 301-level lesson in its own right: **always
report the model and parameters with any number**, and **never let an arbitrary
tiebreaker silently inflate a result**.

- **Favorite-Betrayal (FBC)** — `fbc_simulation.py` (below).
- **Runoff Reversal frequency** — `runoff_reversal_simulation.py`
  ([jump to section](#runoff-reversal-frequency-simulation)).

## Favorite-Betrayal (FBC) simulation

`fbc_simulation.py` measures, by brute force over many random elections, how often
**STAR** and **RCV-IRV** actually satisfy the **Favorite Betrayal Criterion (FBC)** —
and how often a favorite-betrayal vote pays off vs backfires.

## Why this exists

The debate doc once claimed STAR is *"~98% favorite-betrayal-proof."* That number had
**no defensible source**: Equal Vote's criteria chart is binary pass/fail (STAR gets a ❌),
and the ~91–98% figure that floats around is **Voter Satisfaction Efficiency** — an
*accuracy* metric, a different thing entirely. Rather than cite a number we can't defend,
this script **measures** one — and reports the modelling assumptions, because the result
swings hugely with them.

## What it measures

1. **FBC-compliance frequency.** For each random election, compute the sincere STAR (or
   IRV) winner `W`. Then for every voter ask: holding everyone else sincere, is there *any*
   ballot in which they do **not** keep their true favorite (co-)top — a real betrayal —
   that elects someone they sincerely prefer to `W`? If even one voter has such a ballot,
   the election **fails** FBC. The betrayal search is **exhaustive** (every 0–5 ballot for
   STAR, every ranking for IRV), so this is a true best-response test, not a heuristic.

2. **Works : backfires ratio.** Over every `(voter, betrayal ballot)` pair, count how many
   strictly **help** the voter vs strictly **hurt** them (by sincere utilities). Reported
   per method. This is the brute-force cousin of Equal Vote's "honesty" stat — note it
   counts *all possible* betrayals, so it is a superset of the realistic strategies a real
   faction would attempt (read it as "if you betray blindly, how often does it pay?").

### Electorate models (both run by default)
- **spatial** — voters & candidates are points in issue space; utility = −distance. The
  realistic model (what VSE uses).
- **impartial** — each utility is uniform[0,1], independent. An adversarial stress test
  that manufactures far more paradoxes; treat its FBC rate as a rough lower bound.

Sincere ballots are derived deterministically: STAR scores = per-voter min-max scaling of
utilities onto 0–5; IRV ranks candidates by utility. Tie-breaks are fixed and documented in
the script header. Everything is seeded (`--seed`).

## Running it

```bash
python3 fbc_simulation.py                 # default sweep, both models
python3 fbc_simulation.py --selftest      # known-answer checks only
python3 fbc_simulation.py --elections 3000 --voters 41 --candidates 3 --seed 7
```

`--selftest` confirms the tabulators are correct on known cases (clear STAR winner; a
center-squeeze where IRV eliminates the center and STAR elects it).

## Representative results

3 candidates, 2-D spatial / impartial, seeded. (FBC % = elections with **no** profitable
favorite betrayal; ratio = help : hurt over all betrayal ballots.)

| model | voters | STAR FBC % | RCV-IRV FBC % | STAR works:backfires | IRV works:backfires |
|-------|:---:|:---:|:---:|:---:|:---:|
| spatial   | 15 | 91.9% | 95.5% | 0.02 : 1 | 0.07 : 1 |
| spatial   | 41 | 96.2% | 97.2% | 0.02 : 1 | 0.13 : 1 |
| impartial | 15 | 79.4% | 89.6% | 0.04 : 1 | 0.08 : 1 |
| impartial | 41 | 80.8% | 90.8% | 0.04 : 1 | 0.09 : 1 |

## What this means for the "98%" claim

1. **"98%" is not reproducible as a distinctive STAR FBC property.** Under the realistic
   spatial model STAR lands in the low-to-mid 90s%; under impartial culture, ~80%. It is
   never a clean "98%."

2. **Both methods fail FBC at broadly similar low rates** by this existence test — and, on
   raw existence, STAR is *slightly worse* than IRV, not better. The reason is mechanical:
   FBC is an *existence* criterion, and STAR's score ballot offers ~36× more betrayal
   ballots (216 vs a handful of rankings) — more lottery tickets to find one that helps,
   even though almost none do. So **"STAR fails FBC less often than IRV" is not supported**;
   the honest statement is "neither is favorite-betrayal-proof."

3. **The real, robust difference is that betrayal reliably backfires in STAR.** Across every
   run, a STAR favorite-betrayal is far more likely to hurt the voter than an IRV one
   (STAR ~0.02–0.04 : 1 vs IRV ~0.07–0.13 : 1 help : hurt). That is the measurable version
   of "honest voting is your safest bet in STAR" — and it's the claim to make, instead of a
   bare percentage.

   (Magnitudes here are **not** directly comparable to Equal Vote's published ~1:1 STAR vs
   ~3:1 IRV, which uses a realistic strategic-faction model, not an exhaustive ballot
   search. Only the *direction* — STAR less rewardingly manipulable — is shared.)

## Caveats (read before quoting)

- Small candidate field (default 3) — where center squeeze / favorite betrayal lives, but
  not the whole story.
- FBC tested for an **individual** pivotal voter, not a coordinated bloc; center squeeze in
  real polarized races is partly a bloc phenomenon.
- The works:backfires denominator includes every possible betrayal, so it understates how
  often a *well-chosen* strategy pays (and is not Quinn's VSE pipeline).
- Results are model-dependent. **Always report the model and parameters with the number.**

---

## Runoff Reversal frequency simulation

`runoff_reversal_simulation.py` measures how often a **Runoff Reversal** happens — the
Scoring-Round leader losing the Automatic Runoff (the phenomenon taught in
[`runoff_overturns_leader/`](../01_Single_winner/runoff_overturns_leader/README.md)).

### Why this exists

A simulation once reported *"16.9% divergence"* under Impartial Culture with 5
candidates and **10 ballots**. That number is reproducible — and, on its own,
misleading. This script makes three hidden assumptions visible:

1. **The model is white noise.** Impartial Culture makes every score independent and
   uniform, so `5,5,5,5,5` is as likely as a realistic ballot. Real electorates are
   *correlated*, and correlation makes the score leader and the majority winner agree
   far more often — so the realistic reversal rate is much lower.
2. **10 ballots is mostly ties.** At that size ~24% of elections have a tie for the
   top-two-by-score and ~14% have a tied runoff — nearly **40% are tie-ambiguous**.
3. **An arbitrary tiebreaker inflated the count.** The original picked the "score
   winner" by alphabetical order but broke STAR ties by *reverse* alphabetical order;
   when those two arbitrary rules disagreed it was logged as a "divergence." The
   genuine clean-reversal rate at that size is ~9–10%, not 17%.

### What it measures

Each election lands in exactly one of four buckets, so ties are **counted, not
hidden**: `reversal` (clean), `runoff_tie`, `finalist_score_tie`, `no_reversal`. Two
electorate models run by default — **impartial** (white-noise stress test) and
**spatial** (realistic, correlated). Everything is seeded; `--selftest` checks the
classifier on hand-built reversal / no-reversal / tie cases.

### Running it

```bash
python3 runoff_reversal_simulation.py --selftest
python3 runoff_reversal_simulation.py --elections 300000 --voters 21 --candidates 5
```

### Representative results (5 candidates, seed 42)

| model | voters | clean reversal | runoff tie | finalist score tie | no reversal |
|-------|:---:|:---:|:---:|:---:|:---:|
| impartial | 10  | 9.5%  | 14.3% | 23.6% | 52.6% |
| spatial   | 10  | 6.2%  | 12.2% | 14.0% | 67.6% |
| impartial | 21  | 13.2% | 11.0% | 16.8% | 59.0% |
| spatial   | 21  | 8.7%  | 6.2%  | 7.2%  | 77.9% |
| impartial | 101 | 18.6% | 5.7%  | 8.1%  | 67.5% |
| spatial   | 101 | 9.0%  | 1.8%  | 1.6%  | 87.7% |

### What this means

1. **There is no single "reversal rate."** It depends on the model (impartial ≈ 2×
   spatial) and on electorate size (it *rises* as ties vanish with more voters).
2. **Report the model.** Under the realistic spatial model with a real electorate
   (101 voters), clean Runoff Reversals are ~9% — not the ~17% the 10-ballot toy
   setup implied.
3. **It's still common enough to matter.** Even on the conservative spatial model it's
   ~1 election in 11 — which is exactly *why* Runoff Reversal is worth teaching. The
   runoff isn't catching a rare freak case; it's a regular, deliberate correction.

### Caveats (read before quoting)

- Sincere ballots only — no strategy.
- Spatial model is 2-D uniform; real issue spaces are lumpier (clusters, polarization).
- "Reversal" here is score-leader-vs-runoff only; it says nothing about the Condorcet
  winner (see [Three notions of "winner"](../00_start_here/concepts/STAR_Voting/STAR_three_winner_notions.md)).
- **Always report the model, the size, and the tie split with the number.**
