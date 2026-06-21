# Summability (precinct-summable)

**One line:** a method is *summable* if you can tally it by **adding up independent
precinct totals**. STAR is summable; **RCV-IRV is not** — it needs every ballot in
one place to know the elimination order.

→ Glossary: [`summability`](../GLOSSARY.md)

---

## Why STAR is summable

STAR's whole count reduces to **sums**:
- The **scoring round** is just each candidate's total stars — add precinct totals.
- The **runoff** uses the **pairwise (For / Equal / Against) matrix**: for each pair
  of candidates, how many ballots scored A over B, equal, or B over A. Those counts
  also just **add** across precincts.

So each precinct can publish a small table, and the statewide result is their sum.
That makes STAR **precinct-auditable** and gives meaningful early/partial results.

## Test case (run it)

→ [`01_Single_winner/04b_c4_b3_display-options-all.yaml`](../../01_Single_winner/04b_c4_b3_display-options-all.yaml)
with `show_matrix: true`.

The printed **Runoff (Preference) Matrix** *is* the summable artifact — the
head-to-head table that any precinct can produce and that sum to the whole.

## Why RCV-IRV is not summable

IRV is a sequence of eliminations, and **which candidate is eliminated in round 2
depends on every ballot's round-1 result**. You can't add precinct winners; you need
the full ballot set centrally to run the rounds. Consequences:
- **Central tabulation** — a single point of failure and a heavier audit.
- No meaningful precinct-level subtotals; partial counts can mislead.

(This is one row on the method scorecard: *Summable / local tally? — STAR: yes,
RCV-IRV: no.* See the flagship Segment 6 in
[`whats_so_good_about_STAR_Voting.md`](../../interviews_conversations/whats_so_good_about_STAR_Voting.md).)

## The nuance

Summability is about the **tabulation**, not the ballot. A *ranked* ballot counted
by a **Condorcet** method (Ranked Robin) is also summable via the same pairwise
matrix — so "ranked = not summable" is wrong; it's **IRV's elimination count**
specifically that isn't. (See [`TIPS_terminology.md`](../TIPS_terminology.md).)
