# Reading the Runoff Percentages — Two Denominators, One Winner

**One line:** in the Automatic Runoff, the *same* vote count is shown as **two
different percentages** — out of **all** voters, and out of only the voters who
**expressed a preference** between the two finalists. The winner needs a majority of
the second group, not the first. The gap between the two numbers is the **Equal
Support** voters, who scored both finalists the same.

→ Part of [The Automatic Runoff Round](STAR_Automatic_Runoff.md) (the round this
percentage summarizes). The no-preference bucket is [`Equal Support`](../GLOSSARY.md);
why those ballots still count is [Are equal-score votes discounted?](../../interviews_conversations/are_equal_score_votes_discounted.md).
Reading the whole report: [How to read a STAR report](../tabulation_engines/LH_starvote/reading_a_star_report.md).

---

## The example (the Dog/Cat race, 455 voters)

Seven candidates, Dog wins. The Scoring Round adds every star and takes the top two —
**Dog (1798)** and **Cat (1741)** — as Finalists. The Automatic Runoff then compares
*only those two*, giving each ballot's full vote to whichever of Dog/Cat it scored
higher. (Live, interactive version of the screenshots below:
[bettervoting.com/pet/results](https://bettervoting.com/pet/results).)

![BetterVoting result for the pets race: the Scoring Round bar chart (Dog 1798, Cat 1741, Bird 969, Rabbit 954, Fish 854, Rat 580, Python 440) beside the Automatic Runoff bar chart (Dog 190, Cat 173, Equal Support 92) with a dashed majority-threshold line that only Dog's bar crosses](img/pets_rounds_bars.png)

The runoff result is the same numbers no matter how you slice it:

| In the runoff | Votes | of **all 455** | of the **363 with a preference** |
|---------------|------:|---------------:|---------------------------------:|
| **Dog** (winner) | 190 | 42% | **52%** |
| Cat | 173 | 38% | 48% |
| **Equal Support** | 92 | 20% | — |
| Total | 455 | 100% | 100% |

That table is exactly BetterVoting's **Race Details** — the two percent columns are
"% Runoff Votes" (out of all 455) and "% Between Finalists" (out of the 363 with a
preference):

![BetterVoting Race Details: a Scores Table (Dog 1798 … Python 440) and a Runoff Table showing Dog 190 / 42% / 52%, Cat 173 / 38% / 48%, Equal Support 92 / 20%, Total 455 / 100% / 100%](img/pets_race_details_tables.png)

And the result card has two **chart views** (the toggle in its corner) — same runoff,
two ways of slicing it. The **bar view** above uses the all-voters numbers
(42 / 38 / 20) with the dashed *majority threshold*; the **pie view** drops Equal
Support and shows just the two finalists (52 / 48), footnoting the no-preference share:

![BetterVoting pie view of the runoff: Dog 52% vs Cat 48%, with the footnote "20.2% of voters expressed no preference between the two finalists"](img/pets_rounds_pie.png)

## The two denominators

This is the whole lesson. **190 votes for Dog is both 42% and 52%** — nothing changed
but what you divide by.

- **% of all voters** = `190 / 455 = 42%`. Useful for one thing: it shows how big the
  no-preference group is. Here **20%** of voters rated Dog and Cat equally, so they had
  no say in *this* head-to-head. The three numbers add to 100%.
- **% between finalists** = `190 / 363 = 52%`. This is the number that **decides the
  race**. The Equal Support voters are set aside (they declined to pick between these
  two), leaving `455 − 92 = 363` voters with a preference. Of those, more chose Dog.
  Dog and Cat's two numbers add to 100%; Equal Support has no entry here — it's the
  group that was removed to form the denominator.

## Why the winner isn't "majority of everyone"

Notice Dog wins with **42% of all ballots** — *less* than half of everyone. That is
not a flaw, and it's why the bar chart's threshold line is labelled **"½ of voters
with preference,"** not ½ of all voters.

A runoff asks one question: *of the two finalists, which do more voters prefer?* A
voter who scored Dog and Cat the same has answered "neither — they're equal to me," so
counting them against either finalist would be putting words in their mouth. The
majority bar is therefore half of the **363** who actually expressed a preference:
`363 / 2 = 181.5`. Dog's **190 clears it**; Cat's 173 doesn't. Dog is the true majority
choice *of the voters who had a preference* — a real majority, honestly earned.

## Equal Support is not "discarded"

The 92 Equal Support voters counted **fully in the Scoring Round** — their stars are
*inside* Dog's 1798 and Cat's 1741, and helped make both of them finalists. They simply
didn't break the Dog-vs-Cat tie, **because their own ballots said the two were tied**.
They're excluded from the runoff *percentage* only, and only because they asked to be.
Nothing was thrown away; the voters chose to sit out one specific comparison. (Contrast
this with an IRV *exhausted* ballot, which stops counting because the method ran out of
ranks — a method-caused loss, not a voter's choice. See
[exhausted ballots](../RCV_IRV/RCV_IRV_exhausted_ballots.md).)

## The same number in the LH engine

The `starvote` engine prints this decisive percentage on two lines — with the
denominator **named**, so there's no second column to misread. Turn it on with
`options: { show_runoff_percent: true }` (it's off by default, but the always-full
`_tabulated` copy carries it automatically):

```
Automatic Runoff Round
   Dog           -- 190 -- First place
   Cat           -- 173
   Equal Support -- 98
 Dog wins.
   Voters with a preference: 363 of 461 (98 Equal Support).
   Dog 190 (52%) vs Cat 173 (48%); majority = 182.
```

Those two lines are the **% Between Finalists** column, spelled out — and they now
*self-reconcile*: **363 of 461** voters had a preference, the other **98 are Equal
Support**, Dog's 190 is 52% of the 363, and a strict majority needs 182, which Dog clears.
(In the saved `_tabulated` copy this expands into a "Runoff math" funnel that shows
`461 − 98 = 363` explicitly.)

**Why 98 here but 92 in the BetterVoting table above (and 461 vs 455)?** Same ballots,
one classification difference: BetterVoting files 6 *flat* "no-preference" ballots —
including a voter who scored every candidate **5** — under *abstention* and tallies 455;
the LH engine counts all 461 cast ballots, so those 6 stay in Equal Support (`92 + 6 = 98`)
and only the 1 truly-blank ballot is an abstention. The **363 decided voters and the
winner are identical** either way. Full reconciliation:
[BetterVoting and the LH engine](../tabulation_engines/bettervoting_and_the_engine.md#when-the-two-reports-differ--abstentions-vs-equal-support)
and the frozen evidence in
[`BV_result_snapshot.md`](../../01_Single_winner/pet_real_bv_election/BV_result_snapshot.md). (See [reading a STAR report](../tabulation_engines/LH_starvote/reading_a_star_report.md) for the
rest of the engine output, and `CLAUDE.md` for the option's house default.)

The BetterVoting screenshots above and this engine line are **two reports of the same
election** — why there are two, and how every piece maps between them, is
[BetterVoting and the LH engine](../tabulation_engines/bettervoting_and_the_engine.md).
The full election file and complete report for this pets race are in the worked lesson
[A real BetterVoting election, end to end](../../01_Single_winner/pet_real_bv_election/README.md).

## The one-sentence version

> The runoff winner needs a majority of the voters **who expressed a preference**
> between the two finalists — Dog's 190 is 52% of those 363, so Dog wins; the other
> 20% rated the two finalists equally and counted in the score round but not in this
> head-to-head.
