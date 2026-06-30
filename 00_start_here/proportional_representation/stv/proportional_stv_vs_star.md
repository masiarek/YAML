# Proportional Representation: STV vs STAR-PR

**One line:** with multiple seats, a *proportional* method gives a coalition seats
in proportion to its size — not all the seats to whoever leads first-choices. **STV**
does this with ranked ballots + vote transfers; **STAR-PR** does it with scored
ballots + ballot reweighting. They're different machinery, same goal.

→ Glossary: [`STV`](../../GLOSSARY.md), [`Proportional STAR`](../../GLOSSARY.md) · Curriculum: [`301.1`](../../CURRICULUM.md) · Level: **Voting 301**
· STAR-PR methods explained: [STAR_PR](../STAR_PR/README_STAR_PR.md)

---

## The shared idea: a quota

To win one of *k* seats you need a **Droop quota** = `votes / (k+1)`, rounded up.
For **3 seats and 100 voters that's 26** (just over 25%). Any candidate over quota is
elected; surplus or last-place support is redistributed until the seats are filled.
This is why the video says "over 25% wins" for three seats.

## The demo electorate (constructed)

100 voters, 7 candidates, two clusters:

- **Progressive** — Housing, Schools, Parks, Transit — **58%** of first-choices
- **Business** — SmallBiz, BigBiz, TaxCuts — **42%**

Proportionally, 58% / 42% over 3 seats ≈ **2 progressive + 1 business**. (The
"Better elections are possible" video gives only first-choice % and STV outcomes,
not ballots — so this is an illustrative reconstruction, not a transcription.)

→ Run them: [`03a_stv_3seats.yaml`](../../../02_Multi_winner/03a_stv_3seats.yaml) (ranked, STV)
 · [`03b_star_pr_3seats.yaml`](../../../02_Multi_winner/03b_star_pr_3seats.yaml) (scored, STAR-PR)

## Results — proportional methods agree; majoritarian doesn't

| Method | Type | Seats elected |
|--------|------|---------------|
| **STV** | proportional (ranked) | Housing, Schools, **SmallBiz** |
| **STAR-PR — SSS** | proportional (score) | Housing, Schools, **SmallBiz** |
| **STAR-PR — Allocated Score** | proportional (score) | Housing, Schools, **SmallBiz** |
| **STAR-PR — RRV** | proportional (score) | Housing, Schools, **SmallBiz** |
| **Bloc STAR** | *majoritarian* (score) | Housing, Schools, **Parks** |

Two things to read off this (verified on the engine):

1. **STV and all three STAR-PR methods land on the identical slate** — 2 progressive
   + 1 business. Different mechanics (transfers vs reweighting), same proportional
   result. The business minority (42%) earns its one seat.
2. **Bloc STAR gives the third seat to Parks**, not SmallBiz — the 58% progressive
   majority sweeps **all three** seats and the business cluster gets nothing. Bloc
   STAR is majoritarian by design; it's the multi-winner method to *avoid* when you
   want proportionality.

Also note the proportional twist that matches the video: **BigBiz (17 first-choices)
wins no seat, while Schools (15) does** — breadth of support beats raw first-place
count once seats are shared.

## STV is not IRV

**STV = the proportional, multi-winner cousin of IRV.** Same ranked ballot and
transfer idea, but it fills several seats against a quota instead of one. Reserve
"IRV" for the single-winner case. (See [`TIPS_terminology.md`](../../TIPS_terminology.md).)

## Engine notes

- **STV** runs on the vendored `pyrankvote` (`single_transferable_vote`); the
  RCV-IRV wrapper now dispatches to it whenever `num_winners > 1`. No new library was
  needed — set `voting_method: STV` and `num_winners: k`.
- **STAR-PR** runs on the STAR engine: `voting_method: sss | allocated | rrv`
  (proportional) or `bloc` (majoritarian contrast), with `num_winners: k`. Each method
  is explained in [STAR_PR](../STAR_PR/README_STAR_PR.md).

Source: [Equal Vote — "Better elections are possible. Here's how." (video)](https://youtu.be/C_27pYcjsJs?t=127).
