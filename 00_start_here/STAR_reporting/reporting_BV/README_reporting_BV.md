# How BetterVoting reports a STAR result

**One line:** BetterVoting (bettervoting.com) shows a **live, visual** result —
interactive bar/pie charts plus "Race Details" tables — for the same STAR election the
LH engine prints as text. Same method, same winner; a friendlier, less exhaustive view.

→ Hub: [STAR Reporting](../README_STAR_reporting.md) · the mapping in full: [BetterVoting and the LH engine](../../tabulation_engines/bettervoting_and_the_engine.md) · the percentages: [Runoff percentages](../../STAR_Voting/runoff_percentages.md).

---

## What BetterVoting shows

- **Scoring Round** — a bar chart of total stars; the top two bars are the finalists.
- **Automatic Runoff** — a chart with a **toggle**:
  - **bar view** uses the *all-voters* numbers (e.g. 42 / 38 / 20) with a dashed
    **majority-threshold** line labelled "½ of voters **with preference**";
  - **pie view** drops Equal Support and shows just the two finalists (52 / 48),
    footnoting the no-preference share.
- **Race Details tables** — a **Scores Table** (the score totals) and a **Runoff
  Table** with **two percent columns**:
  - **% Runoff Votes** — out of *all* ballots (includes the Equal Support share);
  - **% Between Finalists** — out of only the voters *with a preference*. This is the
    column that decides the race. (Same idea, named: [Runoff percentages](../../STAR_Voting/runoff_percentages.md).)
- **Abstentions / tally** — the result data carries `nAbstentions` and `nTallyVotes`.

## The screenshots (the pet race)

**Scoring Round + Automatic Runoff bars** — totals on the left; on the right each
ballot's full vote goes to the higher-scored finalist, with the dashed
*majority-threshold* line (½ of voters **with a preference**) that only the winner's
bar crosses:

![BetterVoting result for the pets race: the Scoring Round bar chart (Dog 1798, Cat 1741, Bird 969, Rabbit 954, Fish 854, Rat 580, Python 440) beside the Automatic Runoff bar chart (Dog 190, Cat 173, Equal Support 92) with a dashed majority-threshold line that only Dog's bar crosses](../../STAR_Voting/img/pets_rounds_bars.png)

**Race Details tables** — the Scores Table and the Runoff Table, where the same 190
votes appear as **two percentages**: `% Runoff Votes` (out of all 455) and
`% Between Finalists` (out of the 363 with a preference):

![BetterVoting Race Details: a Scores Table (Dog 1798 … Python 440) and a Runoff Table showing Dog 190 / 42% / 52%, Cat 173 / 38% / 48%, Equal Support 92 / 20%, Total 455 / 100% / 100%](../../STAR_Voting/img/pets_race_details_tables.png)

**Pie view** — the runoff toggled to drop Equal Support and show just the two
finalists (52 / 48), footnoting the no-preference share:

![BetterVoting pie view of the runoff: Dog 52% vs Cat 48%, with the footnote "20.2% of voters expressed no preference between the two finalists"](../../STAR_Voting/img/pets_rounds_pie.png)

(The same screenshots, walked through against the two denominators, are in
[Runoff percentages](../../STAR_Voting/runoff_percentages.md).)

## One thing to watch: what BetterVoting calls an "abstention"

BetterVoting counts a ballot as an **abstention** when it is **flat** — every
candidate scored the same — and excludes it from the tally. That includes an
all-zeros ballot **and** an engaged ballot like all-5s or `3,3,3`. The LH engine
instead counts every cast ballot and treats only a **blank** ballot as an abstention,
filing flat ballots under **Equal Support**. Same winner, different tally and score
totals — see [Where the two reports differ](../reporting_diff_BV_LH.md).

Try it: [bettervoting.com](https://bettervoting.com) · a real frozen result:
[pet race snapshot](../../../01_Single_winner/pet_real_bv_election/BV_result_snapshot.md).
