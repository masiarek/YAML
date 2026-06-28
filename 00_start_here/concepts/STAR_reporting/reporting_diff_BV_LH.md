# Where the two reports differ — abstentions vs Equal Support

**One line:** BetterVoting and the LH engine **agree on the winner and the runoff
margin** on every election. They can differ in one bookkeeping detail — **how a
"no preference" ballot is classified** — which shifts the abstention count, the tally
total, and the score totals, but never the result.

→ Hub: [STAR Reporting](./README.md) · canonical write-up: [BetterVoting and the LH engine — when the reports differ](../tabulation_engines/bettervoting_and_the_engine.md#when-the-two-reports-differ--abstentions-vs-equal-support).

---

## The difference, at a glance (the 461-ballot pet race)

| | BetterVoting | LH engine (all 461) |
|---|---:|---:|
| Ballots tallied | 455 | 461 |
| "Abstentions" | 6 (every **flat** ballot) | 1 (the **blank** only) |
| Equal Support in runoff | 92 | 98 |
| Per-candidate score totals | 9 lower (Dog 1798) | Dog 1807 |
| Runoff Dog / Cat | 190 / 173 | 190 / 173 |
| **Winner** | **Dog** | **Dog** |

The whole gap is one rule: **BetterVoting files a flat ballot (every candidate scored
the same) as an *abstention* and drops it; the LH engine counts it as a cast ballot
and, in the runoff, as Equal Support.** `92 + 6 = 98`; the dropped flat ballots
included an all-5s and an all-4s vote, whose `5 + 4 = 9` stars are exactly the
per-candidate score-total gap.

## Why "no preference" ≠ "abstention"

A ballot that scores everyone the same is a **cast vote** with no preference between
the finalists — that's **Equal Support**, which is correctly *neutral in the runoff
denominator* but still **counts in the score round**. An **abstention** is a ballot
with no score recorded at all (a blank). Folding the first into the second mislabels
engaged voters and makes published score totals miss a hand count. (Terms:
[`GLOSSARY`](../../GLOSSARY.md) · the denominator: [Runoff percentages](../STAR_Voting/runoff_percentages.md).)

## Two views of the same election

The cleanest proof is the 3-candidate case shown both ways:

- **BetterVoting view** — election ID **`dq2dmm`** (reports `nAbstentions: 3`).
- **LH view** — the same BV JSON tabulated by LH: [`flat_scores_abstention_c3_b8_tabulated.txt`](../../../01_Single_winner/pet_real_bv_election_tabulated/flat_scores_abstention_c3_b8_tabulated.txt) (1 abstention; the flat `3,3,3` counted as Equal Support).

<!-- Screenshot slot — BetterVoting result for BV id `dq2dmm` (shows 3 abstentions / 5 tallied).
     Save as: img/dq2dmm_bv_abstentions.png
![BetterVoting result for dq2dmm: 3 abstentions / 5 tallied, Banana wins](./img/dq2dmm_bv_abstentions.png) -->

## Same numbers, different words

The two reports never disagree on the runoff numbers — they just **name and format**
them differently, because one is a visual table and the other is a text audit report.

| BetterVoting (Race Details column) | LH engine (the runoff line) | What it is |
|---|---|---|
| **Runoff Votes** | the finalist counts — `Boston 2`, `Austin 1` (also the Automatic Runoff block) | each finalist's head-to-head vote total |
| **% Between Finalists** | the `(67%)` / `(33%)` in the line | share of the **decided** voters (Equal Support excluded) — the number that decides the race |
| **% Runoff Votes** | not a separate line; the `_tabulated` "Runoff math" funnel carries the all-ballots total | share of **all** ballots (Equal Support left in the denominator) |
| *(denominator: a column header)* | **`Voters with a preference: N of TOTAL (E Equal Support)`** | LH states the denominator **inline** instead of in a header |

**Why the words differ.** BetterVoting is a **visual, voter-facing** display: it can
afford several columns and let you read whichever percentage you want, with the
denominator implied by the header. The LH engine is a **text audit report**: it can't
assume you've read a column header, so it folds the decisive count and percentage into
one **self-reconciling line** and *names* the denominator (`Voters with a preference`)
— the one thing BetterVoting's two percent columns leave you to infer.

**Why there are two percentages at all.** When some voters rate the two finalists
equally (**Equal Support**), "what fraction did the winner get?" has two honest answers
— out of *everyone*, or out of only the voters who *picked* between the two finalists.
BetterVoting prints both; the LH line prints the **decisive** one (decided voters) and
names it, then expands the full funnel in `_tabulated`. With no Equal Support the two
percentages are identical; with Equal Support they diverge (e.g. the flat-scores
`4 of 8` case). So: `LH "Boston 2 (67%)"` = `BV Runoff Votes (2)` + `BV % Between
Finalists (67%)`, in one line that says what it's dividing by.

## Evidence & the filed issue

- Frozen BetterVoting result + raw export: [`BV_result_snapshot.md`](../../../01_Single_winner/pet_real_bv_election/BV_result_snapshot.md)
- Minimal cases: [3-candidate](../../../01_Single_winner/pet_real_bv_election/small_case_abstention_lesson.md) (a flat `3,3,3` dropped) · [2-candidate](../../../01_Single_winner/pet_real_bv_election/small_abstention_c2_b5_lesson.md) (a `5,5` dropped)
- Write-up filed with BetterVoting: [`LH_BV_reconciliation_issue.md`](../../../01_Single_winner/pet_real_bv_election/LH_BV_reconciliation_issue.md) → [Equal-Vote/bettervoting#1407](https://github.com/Equal-Vote/bettervoting/issues/1407)
