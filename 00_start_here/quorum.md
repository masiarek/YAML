# Quorum — did enough of the electorate show up?

**One line:** **quorum** is a *turnout* threshold, separate from who wins: enough of
the **eligible electorate** must participate for the election to count. It's
**opt-in** (set `eligible_voters` and/or `quorum`), and a **cast abstention counts
toward it** — showing up and turning in a blank ballot is still participation.

→ What an abstention is: [`GLOSSARY`](GLOSSARY.md) · the abstention vs Equal Support
distinction: [the abstention lesson](../01_STAR/pet_real_bv_election/small_case_abstention_lesson.md) · how results are reported: [STAR Reporting](STAR_reporting/README_STAR_reporting.md).

---

## How it works in the engine

Quorum is only checked when a file opts in. Two inputs:

- **`eligible_voters`** — the size of the electorate (aliases: `electorate`,
  `registered_voters`). This is an **external** number; it is *not* in the ballots.
- **`quorum`** — the threshold (alias: `minimum_quorum`):
  - **omitted** → default: a **majority (>50%) of eligible voters**;
  - **a percentage** (`"50%"`, or `0.5`) → that fraction **of eligible voters**;
  - **an integer ≥ 1** → an **absolute** minimum number of ballots.

**Participation = total ballots cast, abstentions included.** If quorum is **not met**,
the engine declares **no winner** (turnout failed), rather than crowning one on too
few votes. A percentage/majority quorum needs `eligible_voters`; without it the engine
says *"quorum not assessed"* rather than inventing a denominator.

## Worked example — the abstention that carries quorum

A 10-member board; six submit a ballot, one of them **blank**. No explicit quorum, so
the default is a majority of 10 — **at least 6**
([`quorum_demo_c3_b6.yaml`](../01_STAR/_main/quorum_demo_c3_b6.yaml)):

```
 Quorum: 6 of 10 eligible voters participated (60% turnout); requires more than 50% (>= 6). MET.
 Tabulating 6 ballots. Note: 1 of 6 ballots is marked as an abstention.
 ...
 Anna wins.
   Voters with a preference: 5 of 6 (1 Equal Support).
   Anna 3 (60%) vs Ben 2 (40%); majority = 3.
```

The blank ballot is the **sixth participant**. Because a cast abstention counts toward
quorum, turnout reaches 6 and the election is valid — **drop that abstention and
quorum would fail** (5 of 10). The abstainer changed no candidate's score, but their
presence made the result count. Full report:
[`quorum_demo_c3_b6_tabulated.txt`](../01_STAR/_main/_main_tabulated/quorum_demo_c3_b6_tabulated.txt).

## Won the count, but not elected (quorum fails)

Take the **exact same six ballots** — Anna wins the tabulation — and change only the
assumed electorate. For teaching, invent one: *"the electorate is the turnout plus
another 100%,"* so `eligible_voters: 12` ([`quorum_fail_demo_c3_b6.yaml`](../01_STAR/_main/quorum_fail_demo_c3_b6.yaml)).
(That "cast + X%" rule is a **demo device only** — real elections use the actual
registered roll, never a formula off the ballots.)

```
--- STAR Voting Method (single winner) ---
 Quorum: 6 of 12 eligible voters participated (50% turnout); requires more than 50% (>= 7). NOT MET.
 No winner declared — quorum not reached.
```

Exactly half turned out, and a quorum is a *strict* majority, so 50% fails by one. Anna
won the vote, but **winning the vote and being elected are different things** when
turnout falls short — the engine stops before declaring a winner. (Note it bails *before*
tabulating, so it doesn't reprint who would have won; that's the
[quorum-met run](../01_STAR/_main/quorum_demo_c3_b6.yaml) above, on the same ballots.)

## Why `eligible_voters` isn't auto-filled from the ballots

It's tempting to default `eligible_voters` to the number of ballots cast — but that
makes participation always equal eligibility, so **turnout would always read 100% and
quorum would always pass**, defeating the entire check. A turnout quorum is meaningful
only against the *real* electorate, which has to be supplied from outside the ballot
data. So the engine keeps `eligible_voters` an explicit, optional input and stays
silent when it's unknown. (For the same reason there's **no "eligible = cast + X%"
engine option** — it would bake a fiction into the tool when you can already type a
literal number for a demo, as the files above do.)

## Quorum vs the runoff denominator — three different "how many"

Don't confuse these (they answer different questions):

| Count | Question it answers |
|---|---|
| **Eligible voters** | how many *could* vote (the electorate) — the quorum denominator |
| **Ballots cast** (incl. abstentions) | how many *did* participate — the quorum numerator |
| **Voters with a preference** | of those, how many picked between the two finalists — the [runoff percentage](STAR_Voting/runoff_percentages.md) denominator |

An **abstention** drops out of the *runoff* denominator (no preference) but stays in
the *quorum* numerator (still participated). That's the whole reason the two counts can
differ — see [Equal Support vs abstention](STAR_Voting/runoff_percentages.md).
