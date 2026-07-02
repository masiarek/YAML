# Reporting true ties

**One line:** a **true tie** is when two candidates are genuinely equal at a step —
same score, or an equal split in the runoff. This page is about how a tie **shows up
in the reports**; the mechanics of *breaking* one (the full ladder, lot order,
imported `tieBreakType`) are the canonical
[STAR Tie-Breaking](../STAR_Voting/Tie_Breaking_STAR/tie_breaking.md) deep-dive.

→ Hub: [STAR Reporting](README_STAR_reporting.md) · [How the LH engine reports](reporting_LH/README_reporting_LH.md) · [How BetterVoting reports](reporting_BV/README_reporting_BV.md) · imported tie data: [tie-break JSON](../STAR_Voting/Tie_Breaking_STAR/tie_breaking_JSON.md).

---

## How a tie reads in the LH report

The engine marks the tied rows and says so in words, then resolves them by the
tie-break ladder. A runoff that splits evenly:

```
[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Choco         -- 1 -- Tied for first place
   Vanilla       -- 1 -- Tied for first place
 There's a two-way tie for first.
```

— here broken by the **Scoring Round** (Vanilla had the higher total), exactly the
ladder's first rung. (Worked end-to-end, with ties in *both* rounds:
[Tie-Breaking — the Ice Cream example](../STAR_Voting/Tie_Breaking_STAR/tie_breaking.md#worked-example--ice-cream-6-flavors-ties-in-both-rounds).)

**Reporting detail:** on an **exact runoff tie** the one-line runoff-percentage
summary (`Voters with a preference: …`) is **suppressed** — a 50/50 split has no
"winner vs other" to state, so the **tie-break chain explains the result instead**.
The percentage line returns only for a decided runoff.

<!-- Screenshot slot — LH engine tie report.
     Source: run election `02b_c3_b2_three-candidates` (in 01_Single_winner/) and
     screenshot the colored terminal output. Save as: img/REPLACE_02b_c3_b2_lh_tie.png
![LH engine report of a runoff tie, resolved by the score round](img/REPLACE_02b_c3_b2_lh_tie.png) -->

## How a tie reads in BetterVoting

BetterVoting records how a tie was settled in its result data as **`tieBreakType`**,
and shows the resolved order on the result card. (For how an imported BetterVoting
tie-break maps into a YAML election's lot order, see
[tie-break JSON](../STAR_Voting/Tie_Breaking_STAR/tie_breaking_JSON.md).)

<!-- Screenshot slot — BetterVoting tie result.
     No BV tie election captured yet. To make one: create a tiny STAR election on
     BetterVoting whose runoff splits evenly (e.g. 2 voters, ballots `5,3,0` and
     `0,5,3` over Choco/Vanilla/Berry → a 1-1 runoff broken by the score round).
     Save the result screenshot as img/<BV_ID>_bv_tie.png and note the BV id here.
![BetterVoting result card showing a tie and how it was broken](img/REPLACE_bv_tie.png) -->

## Why ties feel common in tiny examples

Teaching elections use the **fewest ballots** that make a point, and small electorates
tie easily (a 1–1 runoff needs just two voters). That's a feature for *showing* the
tie-break ladder — and a reason real public elections, with thousands of ballots,
almost never reach the lot-drawing floor. (→ [Tie-Breaking — quick rules](../STAR_Voting/Tie_Breaking_STAR/tie_breaking.md#quick-rules).)
