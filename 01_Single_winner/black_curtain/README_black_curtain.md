# The Black Curtain — one electorate, four "identical" landslides

*A worked case study from the video
["The Black Curtain"](https://www.youtube.com/watch?v=5_ZMruwOZgw)
by Common Sense for Uniting America (Ted Getschman / [MaxVoting.org](https://maxvoting.org)).
BetterVoting template: <https://bettervoting.com/p9gwc3/vote>.
Adam's notes doc: [The Black Curtain (Google Doc)](https://docs.google.com/document/d/1ntOS5PQ_kkPnaZpDeqLShGv2pz_k6Zom9LnTEdjjd4o).
This folder on GitHub:
<https://github.com/masiarek/YAML/tree/master/01_Single_winner/black_curtain>.
This folder re-creates all four elections as runnable YAML cases for this repo's engine.*

---

## The thought experiment

Five voters score candidates on a 0–9 ballot ("least" → "most"). You are shown
four different elections, one at a time, and asked the same question each time:
**"Which candidate should win? Write down your answer."**

Then the curtain drops. If all you count is each voter's *first choice* —
which is all Choose-One (plurality) uses, and all RCV-IRV needs here (C has 3
of 5 first choices, an instant >50% majority, so the count stops immediately) —
the four elections are **indistinguishable**: four identical landslide
victories for candidate C, 3 votes to 2. Everything that made them different
is hidden behind the black curtain.

The score ballots reveal four very different electorates:

| # | What the scores actually show |
|---|---|
| 1 | **A hidden consensus.** Every voter scored B an 8 — but B is nobody's first choice. |
| 2 | **Two near-clones.** Everyone loves both A and C (8s and 9s); B is universally hated. |
| 3 | **A polarizing "winner."** C is loved by 3, zeroed by 2; A is loved by *all five*. |
| 4 | **Four candidates, same curtain.** A compromise candidate (B) leads on average score by a hair. |

## The four elections (original 0–9 video ballots)

**Election 1** — first choices: C 3, A 2

| voter | A | B | C |
|---|---|---|---|
| 1–3 | 0 | 8 | 9 |
| 4–5 | 9 | 8 | 0 |

Choose-One → **C** · RCV-IRV → **C** (instant >50%) · STAR → **C** (runoff 3–2 over B) ·
Approval (approve = 5+) → **B** (5 vs 3 vs 2) · Score 0–9 → **B** (avg 8.0 vs C 5.4, A 3.6)

**Election 2** — first choices: C 3, A 2

| voter | A | B | C |
|---|---|---|---|
| 1–3 | 8 | 0 | 9 |
| 4–5 | 9 | 0 | 8 |

Choose-One / RCV-IRV / STAR / Score 0–9 → **C** (avg 8.6 vs A 8.4) ·
Approval → **coin toss A/C** (5 approvals each)

**Election 3** — first choices: C 3, A 2

| voter | A | B | C |
|---|---|---|---|
| 1–3 | 8 | 0 | 9 |
| 4–5 | 9 | 1 | 0 |

Choose-One / RCV-IRV / STAR → **C** · Approval → **A** (5 vs 3) ·
Score 0–9 → **A** (avg 8.4 vs C 5.4, B 0.4)

**Election 4** — first choices: C 3, A 2

| voter | A | B | C | D |
|---|---|---|---|---|
| 1–3 | 0 | 4 | 9 | 5 |
| 4–5 | 9 | 8 | 0 | 1 |

Choose-One / RCV-IRV / STAR → **C** · Approval → **coin toss C/D** (3 each) ·
Score 0–9 → **B** (avg 5.6 vs C 5.4, A 3.6, D 3.4)

## Results at a glance

| Election | Choose-One | RCV-IRV | STAR | Approval (5+) | Score 0–9 |
|---|---|---|---|---|---|
| 1 | C | C | **C** | **B** | **B** |
| 2 | C | C | **C** | tie A/C | C |
| 3 | C | C | **C** | **A** | **A** |
| 4 | C | C | **C** | tie C/D | **B** |

## Lessons learned

1. **There is no "right" answer — but the method decides.** The video's own
   framing: *"There was no right answer, only your answer. However, your answer
   will impact how united or divided this society is."* Identical voters,
   different counting rules, different winners. Choosing a voting method is
   choosing **which question you ask**: *who is the majority's favorite?*
   (Choose-One, RCV-IRV, STAR) or *who has the broadest support?* (Approval,
   Score).

2. **The ballot decides what you can even know.** A choose-one ballot records
   only the top of each voter's mind. A ranked ballot records order but not
   intensity — 9-vs-8 and 9-vs-0 both flatten to "1st > 2nd" (see
   [`../../00_start_here/scores_and_ranks/scores_vs_ranks.md`](../../00_start_here/scores_and_ranks/scores_vs_ranks.md)).
   Only the score ballot distinguishes these four electorates. And because C
   has an outright first-choice majority, RCV-IRV's count ends in round one —
   the published result is *identical* in all four elections. Election 1's
   universally-liked B and Election 3's universally-liked A are invisible: the
   black curtain.

3. **STAR reads score ballots but answers the majoritarian question.** In all
   four elections STAR sees the full score data, puts the consensus candidate
   in the runoff where relevant, and still elects C — because the automatic
   runoff hands the decision to the 3-voter majority. That is by design: the
   runoff is exactly what separates STAR from pure Score (compare
   [`../runoff_overturns_leader/`](../runoff_overturns_leader/), especially
   `Runoff_03_enthusiasts_vs_majority`). Whether that's a feature or a bug *is
   the values question this video is about.*

4. **Approval is Score at 1-bit resolution.** The approve/don't-approve
   threshold (here: video score 5+) collapses the near-clones of Election 2
   into a coin toss and manufactures a C/D tie in Election 4. More resolution,
   more information, finer distinctions — the fidelity ladder
   ([`../../00_start_here/scores_and_ranks/fidelity_ladder.md`](../../00_start_here/scores_and_ranks/fidelity_ladder.md)).

5. **Scale granularity matters (the 0–9 → 0–5 problem).** The video uses six
   distinct scores — 0, 1, 4, 5, 8, 9 — which map one-to-one onto this repo's
   0–5 scale (0→0, 1→1, 4→2, 5→3, 8→4, 9→5). Order inside every ballot is
   preserved, so **every Choose-One, RCV-IRV, STAR, Approval, and Condorcet
   result above reproduces exactly**. The single casualty: Election 4's pure-
   Score winner, decided by a 0.2-average margin (B 5.6 vs C 5.4), can't be
   expressed at 0–5 resolution (integer totals become C 15, B 14). No
   monotone integer mapping into 0–5 can save it — six distinct values are
   forced onto exactly 0,1,2,3,4,5. A near-tie that flips under rescaling is
   itself a teaching point: the finer the scale, the more of the electorate's
   mind survives the count.

6. **Verify, don't trust — even friendly sources.** Two on-screen averages in
   the video don't reproduce from its own ballots: Election 1 shows A's
   average as 1.6 (the ballots as shown compute to **3.6**), and Election 3
   shows C's as 5.6 (computes to **5.4**). Neither changes any winner — but
   catching them is exactly why this repo embeds `expected_winners:` in every
   file and re-runs everything through the engine.

## Files in this folder

| File | Method | Winner | Shows |
|---|---|---|---|
| `Black_Curtain_01_c3_b5_hidden-consensus.yaml` | STAR | Cal | Majority favorite beats the everyone's-second consensus |
| `Black_Curtain_01a_c3_b5_approval.yaml` | Approval | **Bob** | Same 5 voters, different method, different winner |
| `Black_Curtain_02_c3_b5_near-clones.yaml` | STAR | Cal | Two loved near-clones; approval can't tell them apart |
| `Black_Curtain_03_c3_b5_polarized-on-cal.yaml` | STAR | Cal | The "landslide" winner is zeroed by 40% of voters |
| `Black_Curtain_04_c4_b5_four-candidates.yaml` | STAR | Cal | Four candidates, same curtain; score near-tie lost at 0–5 |

Candidate names follow the BetterVoting template cast: Ann, Bob, Cal (+ Dee).
Run any file:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_Single_winner/black_curtain/Black_Curtain_01_c3_b5_hidden-consensus.yaml
```

## Related

- [`../../00_start_here/scores_and_ranks/`](../../00_start_here/scores_and_ranks/) — scores vs ranks, the fidelity ladder
- [`../../00_start_here/rcv_irv_vs_star.md`](../../00_start_here/rcv_irv_vs_star.md) — method comparison
- [`../runoff_overturns_leader/`](../runoff_overturns_leader/) — when STAR's runoff agrees/disagrees with the score leader
- Source video: [The Black Curtain](https://www.youtube.com/watch?v=5_ZMruwOZgw) · playlist: [Common Sense for Uniting America](https://www.youtube.com/watch?v=5_ZMruwOZgw&list=PLQod5if9cV9hiWml-4ZyQQNWvys8vlYHM)


# file: README_black_curtain.md
