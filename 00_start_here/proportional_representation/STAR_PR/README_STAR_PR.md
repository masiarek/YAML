# STAR-PR — proportional STAR, and its methods

**One line:** STAR-PR fills **several seats proportionally** using ordinary STAR
**score ballots** (0–5). After each seat is awarded, the ballots that helped win it
are **reweighted** (their remaining influence is reduced), so the next seat reflects
the voters who haven't been represented yet. Same scored ballot as single-winner
STAR — different counting, run as many times as there are seats.

→ STV (the ranked-ballot proportional method) side by side with STAR-PR:
[STV vs STAR-PR](../stv/proportional_stv_vs_star.md) ·
Glossary: [`Proportional STAR`](../../GLOSSARY.md) ·
Curriculum: [`301.1`](../../CURRICULUM.md) · Level: **Voting 301**

---

## The core idea: quota + reweighting

A proportional method shares the seats among coalitions in proportion to their
support, instead of letting the largest group take everything. Two ingredients:

1. **A quota** — the share of support that earns one seat. With *k* seats, the
   **Droop quota** is `votes / (k + 1)`, rounded up (for 3 seats, just over 25%).
2. **Reweighting** — once a candidate is seated, the ballots that scored them highly
   have "spent" some of their weight, so they count for less when the next seat is
   decided. That is what stops a 58% majority from sweeping all the seats.

This is the whole difference from **Bloc STAR**, which just elects the top *N*
score-leaders with no reweighting — and is therefore *majoritarian*, not
proportional (see the contrast below).

## The three STAR-PR methods

All three are proportional and use the same score ballots; they differ only in *how*
a ballot's weight is spent after each seat. The LH engine runs each via
`voting_method:` plus `num_winners: k`.

| Method | `voting_method` | How it reweights, in a line |
|---|---|---|
| **Allocated Score** | `allocated` | Seat the top scorer, then fully **spend a quota's worth** of the ballots that supported them most (those ballots are "used up"); repeat. This is the Equal Vote Coalition's recommended "STAR-PR." |
| **Sequentially Spent Score** (SSS) | `sss` | Like Allocated Score, but each supporting ballot **spends score proportionally** toward the quota rather than being fully exhausted — a smoother allocation. |
| **Reweighted Range Voting** (RRV) | `rrv` | Don't spend ballots; instead **divide each ballot's weight** by a growing factor based on how much score it has already given to winners (a D'Hondt/Jefferson-style divisor). |

In practice, on a clean two-coalition electorate they tend to **agree on the slate**
(see the worked example below); they can diverge on closer or more fragmented races.

## The majoritarian contrast: Bloc STAR

`voting_method: bloc` runs STAR's score-then-runoff *N* times with **no reweighting**,
so the largest bloc can win **every** seat. It's useful when you *want* an at-large
majority result, and it's the method to **avoid when you want proportionality**.
Keep it in the comparison precisely to show what reweighting buys you.

## Run them

```
voting_method: allocated   # or: sss | rrv   (proportional)
num_winners: 3
```

Worked examples in [`02_Multi_winner/`](../../../02_Multi_winner/):

- [`02a_c5_b63_proportional-allocated-score.yaml`](../../../02_Multi_winner/02a_c5_b63_proportional-allocated-score.yaml) — Allocated Score
- [`02b_c5_b63_proportional-sss.yaml`](../../../02_Multi_winner/02b_c5_b63_proportional-sss.yaml) — SSS
- [`02c_c5_b63_proportional-rrv.yaml`](../../../02_Multi_winner/02c_c5_b63_proportional-rrv.yaml) — RRV
- [`03b_star_pr_3seats.yaml`](../../../02_Multi_winner/03b_star_pr_3seats.yaml) — STAR-PR vs the STV file in the same race
- [`01_c4_b2_bloc-star-2-seats.yaml`](../../../02_Multi_winner/01_c4_b2_bloc-star-2-seats.yaml) — Bloc STAR (majoritarian contrast)

The head-to-head with STV, on one shared electorate, is in
[STV vs STAR-PR](../stv/proportional_stv_vs_star.md): STV and all three STAR-PR
methods land on the same proportional slate; Bloc STAR doesn't.
