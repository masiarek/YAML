# A real BetterVoting election, end to end — "What Makes the Best Pet?"

This is a **real STAR election run on BetterVoting** (BV id `pet`): 7 candidates, **461
ballots**, single winner. It's the worked example behind the screenshots in the
[runoff percentages lesson](../../00_start_here/concepts/STAR_Voting/runoff_percentages.md)
and the [BetterVoting ↔ LH engine](../../00_start_here/concepts/tabulation_engines/bettervoting_and_the_engine.md)
page — here you get the **whole thing**: the election file and the full engine report,
side by side, so you can read a real result from raw ballots to winner.

- **The election file:** [`best_pet_c7_b461.yaml`](./best_pet_c7_b461.yaml) — the actual
  BetterVoting JSON export, converted to YAML (461 score ballots, 0–5, with blanks).
- **The full engine report:** [`best_pet_c7_b461_tabulated.txt`](../pet_real_bv_election_tabulated/best_pet_c7_b461_tabulated.txt)
  — matrix, Condorcet check, score distribution, both rounds, winner.
- **The live BetterVoting result:** [bettervoting.com/pet/results](https://bettervoting.com/pet/results).

This is **Voting 201** — reading a real, full audit report. (A 101 viewer needs only the
last three lines: Scoring Round → Automatic Runoff → winner.) For the section-by-section
method, see [How to read a STAR report](../../00_start_here/concepts/tabulation_engines/LH_starvote/reading_a_star_report.md).

## 1. The scoring round — add every star

The engine sums each candidate's stars across all 461 ballots. The two highest advance:

```
   Dog           -- 1807 -- First place
   Cat           -- 1750 -- Second place
   Bird          --  978
   Rabbit        --  963
   Fish          --  863
   Rat           --  589
   Python        --  449
 Dog and Cat advance.
```

**Dog** and **Cat** are the Finalists. The other five are out — but their stars still
counted (they're what *made* Dog and Cat the top two).

## 2. The automatic runoff — majority of those with a preference

Now only the two finalists matter. Each ballot's full vote goes to whichever of Dog/Cat
it scored higher:

```
   Dog           -- 190 -- First place
   Cat           -- 173
   Equal Support --  98
 Dog wins.
   Voters with a preference: 363 of 461 (98 Equal Support).
   Dog 190 (52%) vs Cat 173 (48%); majority = 182.
```

**Dog wins.** The line self-reconciles: of **461** cast ballots, **363 had a preference**
between the finalists and **98 are Equal Support** (`461 − 98 = 363`). The same 190 reads
two ways — 190 of all 461 isn't the point; 190 of the **363 with a preference** is **52%**,
clearing the 182-vote majority. The 98 Equal Support voters scored Dog and Cat the same, so
they sit out *this* head-to-head (but counted fully in the scoring round). That
two-denominator idea is the whole
[runoff percentages lesson](../../00_start_here/concepts/STAR_Voting/runoff_percentages.md);
the engine prints the decisive line because the file sets `show_runoff_percent: true`. (The
saved `_tabulated` copy expands it into a "Runoff math" funnel.)

## 3. Did STAR pick the "right" pet? (the Condorcet check)

The full report's pairwise matrix shows **Dog beats every other candidate head-to-head**
— so Dog is also the **Condorcet winner**, and STAR's runoff result matches it:

```
[Condorcet Winner]
  Condorcet Winner: Dog — matches the STAR winner
```

When the score leader, the runoff winner, and the Condorcet winner are the *same*
candidate (as here), the result is about as uncontroversial as it gets. (For the case
where they *differ*, see [three notions of "winner"](../../00_start_here/concepts/STAR_Voting/STAR_three_winner_notions.md)
and the [Runoff Reversal](../runoff_overturns_leader/README.md) walkthrough.)

## 4. Real-ballot details: abstention vs. explicit zero

Real exports are messy. This one has blanks (`-`) and all-zero ballots, and the report
is careful to separate them:

```
 Tabulating 461 ballots. Note: 1 of 461 ballots is marked as an abstention.
```

Exactly **one** ballot is a true abstention — a fully blank ballot (`-,-,-,-,-,-,-`),
no score for anyone. That is **not** the same as the handful of all-zeros ballots
(`0,0,0,0,0,0,0`), which are *cast* ballots that simply support no one. Both tabulate as
0 stars, but a blank is "I didn't weigh in" while an explicit 0 is "I rate you zero" —
the engine counts only the blank ballot as an abstention. (The score distribution's
**Abs** column tracks per-candidate blanks the same way.)

### Where BetterVoting and the engine disagree (and why it doesn't change the winner)

BetterVoting reports this race as **6 abstentions, 455 ballots tallied**; the engine counts
all **461** and calls only the 1 blank an abstention. BetterVoting's 6 are all *flat*
ballots (every candidate scored equally) — and two of them are real votes: one voter scored
**all seven candidates 5**, another **all 4**. Those are **Equal Support**, not
abstentions; treating them as abstentions is what makes BetterVoting's score totals run 9
lower per candidate (`5 + 4 = 9`) and its Equal Support 92 instead of 98 (`92 + 6 = 98`).
The winner, finalists, and runoff margin are identical. This is documented as a
reconciliation/correctness issue:

- **Canonical small case (a lesson in itself): [`small_case_abstention_lesson.md`](./small_case_abstention_lesson.md)** — real BV election `dq2dmm`, 3 candidates / 8 ballots, where BV files 3 flat ballots (incl. an engaged `3,3,3`) under "abstention"
- Frozen BetterVoting result + raw export (this 461-ballot race): [`BV_result_snapshot.md`](./BV_result_snapshot.md)
- Write-up & GitHub issue → [Equal-Vote/bettervoting#1407](https://github.com/Equal-Vote/bettervoting/issues/1407): [`LH_BV_reconciliation_issue.md`](./LH_BV_reconciliation_issue.md)
- Even-simpler 2-candidate lesson + synthetic illustration: [`small_abstention_c2_b5_lesson.md`](./small_abstention_c2_b5_lesson.md) · [`abstention_reconciliation_min_c2_b6.yaml`](./abstention_reconciliation_min_c2_b6.yaml)
- Reproduce it on BetterVoting yourself: [`SMALL_CASE_reproduce_on_BV.md`](./SMALL_CASE_reproduce_on_BV.md)
- Concept: [BetterVoting and the LH engine — when the reports differ](../../00_start_here/concepts/tabulation_engines/bettervoting_and_the_engine.md#when-the-two-reports-differ--abstentions-vs-equal-support)

## Run it yourself

From the engine directory:

```
python starvote_larry_hastings.py "01_Single_winner/pet_real_bv_election/best_pet_c7_b461.yaml"
```

Re-running rewrites the `_tabulated` sibling. Because this is a converted BetterVoting
export, it uses the nested `election: → races:` schema (options live under
`election.options`) — exactly the format the
[convert → validate → tabulate pipeline](../../00_start_here/concepts/tabulation_engines/bettervoting_and_the_engine.md)
produces and cross-checks against BetterVoting's own result.
