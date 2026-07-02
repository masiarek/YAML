# Ranked Robin (aka Consensus Voting) — RCV-RR

*A ranked method that compares every candidate head-to-head and elects whoever beats the most rivals. Same ranked ballot as IRV, but a completely different — and far more transparent — way of counting it.*

→ **Run it / tabulated example:** [`summability_demo/`](../../method_comparisons/summability_demo)
shows the **pairwise matrix** (the Ranked Robin tally) computed and *added across precincts*;
the [`pref_voting` engine](../../pref_voting_tabulation_engine/README_pref_voting_tabulation_engine.md) reports the
**Copeland = Ranked Robin** winner on any election (`python pref_voting_tabulation.py example_tennessee.yaml`).
· Topic hub: [Summability](../topics/summability/README_summability.md).

---

**Ranked Robin** (also marketed as **Consensus Voting**, and abbreviated **RCV-RR**) is a **Condorcet** method: it's a round-robin tournament among the candidates. You rank the candidates — and crucially, **you may rank candidates equally** — then the count compares **every pair** of candidates head-to-head and elects the one who **wins the most matchups** (ties broken by the sum of win margins).

Because it's computed entirely from the **pairwise matrix** (for each pair, how many voters preferred A to B), it has the properties IRV lacks while using essentially the same ballot voters already know.

> **Sibling branding — "Consensus Choice."** The same core Condorcet idea is promoted by *Better Choices for Democracy* as **Consensus Choice** (often paired with a "Top 4" open primary front end). It allows equal ranks, compares every pair head-to-head, and is precinct-summable. It differs from Equal Vote's Ranked Robin mainly in packaging and in its **cycle-resolution rule** ("Most Wins, Smallest Loss" vs. RR's sum-of-margins). Treat "Ranked Robin," "Consensus Voting," and "Consensus Choice" as close cousins in the Condorcet family, not identical algorithms.

## How it differs from RCV-IRV (Hare)

| | **RCV-IRV (Hare)** | **Ranked Robin (RCV-RR)** |
|---|---|---|
| Ballot | Rank, **no equal ranks** | Rank, **equal ranks allowed** |
| How it counts | Eliminate fewest-first-choice, transfer, repeat | Compare **every pair**; most head-to-head wins |
| Uses your lower ranks? | Only after higher ones are eliminated | **Always** — every ranking counts against every opponent |
| Pairwise (head-to-head)? | ❌ No | ✅ **Yes** |
| Elects the Condorcet winner? | Not always (can center-squeeze) | ✅ Yes, when one exists |
| Monotonic? | ❌ No | ✅ Yes |
| Precinct-summable? | ❌ No | ✅ Yes (add pairwise matrices) |
| Exhausted ballots? | Possible | No — all rankings are read |

The headline: the two things people *assume* "RCV" does — let you mark ties and compare candidates head-to-head — are exactly what **RCV-RR (Ranked Robin)** does and what **RCV-IRV (Instant-Runoff Voting)** does not. (See [strict_vs_weak_ranks.md](../scores_and_ranks/strict_vs_weak_ranks.md) and [RCV_IRV_and_plurality.md](../RCV_IRV/RCV_IRV_and_plurality.md).)

## Why it matters

Because it reads every ranking against every opponent, Ranked Robin elects the candidate **most voters prefer in head-to-head comparison** — the "consensus" / Condorcet winner — which is precisely the broadly-liked moderate that IRV can [center-squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md) out. It's also **monotonic** and **summable** by adding precinct pairwise matrices, so it avoids two of IRV's biggest mechanical problems while keeping a familiar ranked ballot.

## A worked example — the consensus center wins the round-robin

Thirteen voters, four candidates on a left→right line (Ada, Ben, Cara, Dan). Run it:
[`ranked_robin_consensus_center.yaml`](../../05_Ranked_Robin/_main/ranked_robin_consensus_center.yaml)
(or paste the `count:A>B>C` block into [LeGrand's calculator](https://www.cs.angelo.edu/~rlegrand/rbvote/calc.html)).

```
4 : Ada > Ben > Cara > Dan
4 : Dan > Cara > Ben > Ada
3 : Ben > Cara > Ada > Dan
2 : Cara > Ben > Dan > Ada
```

**Step 1 — every head-to-head.** Compare each pair across all 13 ballots:

| Matchup | Winner | | Matchup | Winner |
|---|---|---|---|---|
| Ben vs Ada | **Ben** 9–4 | | Cara vs Dan | **Cara** 9–4 |
| Ben vs Cara | **Ben** 7–6 | | Ada vs Dan | **Ada** 7–6 |
| Ben vs Dan | **Ben** 9–4 | | Cara vs Ada | **Cara** 9–4 |

**Step 2 — the win–loss record (Copeland score).** Count each candidate's wins minus losses:

| Candidate | Wins | Losses | Score |
|---|:--:|:--:|:--:|
| **Ben** | 3 | 0 | **+3** ← winner |
| Cara | 2 | 1 | +1 |
| Ada | 1 | 2 | −1 |
| Dan | 0 | 3 | −3 |

**Ben wins Ranked Robin** by beating everyone head-to-head (he's the Condorcet winner).
The kicker: **Ada and Dan each had *more* first-choice votes (4 apiece) than Ben (3)** — under
Plurality or a first-past-the-post lens, Ben looks like an also-ran. Ranked Robin reads the
*whole* ballot, so the candidate the majority prefers in every matchup wins, not the one
with the biggest first-choice pile. (Verified on the engine; the
[`pref_voting` cross-check](../tabulation_engines/cross_checking_with_pref_voting.md)
confirms Copeland = Ben, and IRV happens to agree here too.)

## For balance — its limits

Ranked Robin isn't a cure-all. Like all ranked methods it captures **order only, not strength** — it can't tell a near-tie from a landslide ([scores_vs_ranks.md](../scores_and_ranks/scores_vs_ranks.md)) — so it carries less information than a scored method like STAR. When there's a **Condorcet cycle** (A beats B, B beats C, C beats A, with no candidate beating all others), there is no Condorcet winner and the method falls back on a tiebreak rule (sum of margins), which reasonable people can debate. And no method escapes Gibbard–Satterthwaite. Its real-world **adoption is limited** so far compared with IRV.

## Now you can tabulate it — the `pref_voting` engine

The repo's new [`pref_voting_tabulation_engine/`](../../pref_voting_tabulation_engine/README_pref_voting_tabulation_engine.md)
computes this method on any example election, under its **academic name, Copeland**.

> **The LH engine now tabulates Ranked Robin first-class.** Set
> `voting_method: RankedRobin` (aliases `RCV_RR` / `Copeland` / `Consensus`) and the
> engine prints the **round-robin report** — ballots, the full pairwise table, and each
> candidate's win-loss record — instead of the RCV-IRV elimination rounds:
> ```
> python starvote_larry_hastings.py 01_Single_winner/ranked_robin_consensus_center.yaml
> ```
> It flags a **cycle** (when the top candidates tie on wins) and points to
> [cycle resolution](cycle_resolution.md). For an *independent* Copeland cross-check,
> [`ranked_robin_report.py`](../../pref_voting_tabulation_engine/ranked_robin_report.py)
> (in the `pref_voting` engine) computes the same result a second way.

### Options for an RCV-RR YAML file — and what shows where

The Ranked Robin path follows the same **minimal echo / always-full `_tabulated`**
discipline as STAR ([reading a STAR report](../tabulation_engines/LH_starvote/reading_a_star_report.md)).
It honors **three** `options:` (the rest of the STAR option block is silently ignored —
it doesn't error, it just does nothing for RR):

| Option | Default | Effect on RCV-RR |
|--------|:-------:|------------------|
| `show_matrix` | `false` | When `true`, the **on-screen echo** also prints the full N×N pairwise matrix. The `_tabulated` mirror **always** includes it regardless. |
| `collapse_ballots` | `true` | `true` → identical ballots shown as `N × ballot`; `false` → one row per voter. |
| `count_separator` | `×` | The glyph between the count and the ballot (`×`, `:`, or `x`/`X`). |

Everything else — `matrix_finalists_only`, `show_condorcet`, `show_score_counts`,
`show_runoff_percent`, `brief`, `show_description` — is **STAR-specific** and has no
effect here (RR has no finalists, no score round, and no automatic runoff).

**What you'll see.** Take this 7-ballot, 3-candidate file:

```yaml
voting_method: RankedRobin
num_winners: 1
ballots: |-
  3:Ada>Ben>Cara
  2:Ben>Cara>Ada
  2:Cara>Ben>Ada
```

The **on-screen echo** (compact — no `show_matrix`) shows the ballots, the aligned
head-to-head list, the win-loss record table, and the winner. The record table reports
the **Copeland score** (`wins + ½·ties`, the academic standard) alongside the win-loss
count and total margin:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 7 ballots (ranked ballots).

Ballots:
     3 × Ada > Ben > Cara
     2 × Ben > Cara > Ada
     2 × Cara > Ben > Ada

Round-Robin — every pair, head-to-head (For – Against):
   Ben   beats Ada    4 – 3
   Cara  beats Ada    4 – 3
   Ben   beats Cara   5 – 2

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ben        2–0–0         2      +4  Cara, Ada
    2  Cara       1–1–0         1      -2  Ada
    3  Ada        0–2–0         0      -2  —

Winner — Ranked Robin (RCV-RR): Ben
   beats every opponent head-to-head — the Condorcet winner.
```

The **`_tabulated` mirror** is identical *plus* the full N×N pairwise matrix — the
Ranked Robin tally itself — inserted before the win-loss record (each cell reads
`For - Equal Support - Against`, row vs column; the middle column is `0` here because
these are strict ranks with no equal support):

```text
--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |
--------------------------------------------
   Ada > |    ---    |3 - 0 - 4 |3 - 0 - 4 |
   Ben > | 4 - 0 - 3 |   ---    |5 - 0 - 2 |
  Cara > | 4 - 0 - 3 |2 - 0 - 5 |   ---    |
```

Add `options: { show_matrix: true }` to pull that matrix onto the screen too — which
is what [`ranked_robin_consensus_center.yaml`](../../05_Ranked_Robin/_main/ranked_robin_consensus_center.yaml)
does, since the matrix is the point of that worked example.

> **Why this format.** The two conventions every source agrees on are the **preference
> (pairwise) matrix** and the **win-loss record** — Equal Vote leads with the record and
> calls the matrix the tool "for making sense of the ballot data," and the academic
> [Copeland](https://en.wikipedia.org/wiki/Copeland%27s_method) literature treats the
> outranking matrix as the standard presentation (row = "runner," column = "opponent,"
> diagonal blank). We follow both, and add the academic **Copeland score** (`wins + ½·ties`)
> as an explicit column, since there's no finalized public-facing spec to defer to. Our
> tie-break is **total margin, then lot order** — a deliberate, fully-reported choice
> (the record table shows the margin that settles it); it differs from Equal Vote's
> published hierarchy (Favorite / Copeland / Smith-Minimax), which we treat as one option
> among several until a standard settles. See [cycle resolution](cycle_resolution.md).

**Copeland = Ranked Robin = Consensus Voting = RCV-RR** — *the same core method wearing
different brand names from different proponent groups:*

| Name | Who calls it that |
|------|-------------------|
| **[Copeland's method](https://en.wikipedia.org/wiki/Copeland%27s_method)** | academic social-choice literature (order candidates by pairwise **wins − losses**) |
| **Ranked Robin** | the **Equal Vote Coalition** |
| **Consensus Voting / Consensus Choice** | **Better Choices for Democracy** |
| **RCV-RR** | this repo's house compound (ranked ballot + Ranked-Robin count) |

They're the **same idea**: elect whoever wins the most head-to-head matchups (the
Condorcet/Copeland winner). They agree on the winner whenever a Condorcet winner exists —
i.e. almost always — and differ *only* in the **cycle/tie-break rule** (Ranked Robin: sum
of margins; Consensus Choice: "Most Wins, Smallest Loss"; textbook Copeland: by score). So
treat them as one method with several brands, not byte-identical algorithms.

> **House naming (which word when).** Say **Ranked Robin (RR)** to people — it's the
> friendliest adopted name. Use **RCV-RR** in method comparisons and engine output, exactly
> parallel to **RCV-IRV** (ranked ballot + which count). Use **Copeland** when talking to
> the *engine* or academics (it's what `pref_voting` calls it). Mention **Consensus
> Voting / Consensus Choice** once as the advocacy brand, then move on. (Same
> meet-them-where-they-are rule as [`TIPS_terminology.md`](../TIPS_terminology.md).)

```bash
# run Copeland (= Ranked Robin) on any election, beside the other methods:
cd pref_voting_tabulation_engine
python pref_voting_tabulation.py example_tennessee.yaml
#   Copeland   pref_voting=Nashville   (= the Ranked Robin / Consensus winner)
```

Since BetterVoting ships a Ranked Robin tabulator too, this gives you an **independent
Python reference** to reconcile BV's RCV-RR results against — the same cross-checking we do
for STAR and RCV-IRV. Details:
[`cross_checking_with_pref_voting.md`](../tabulation_engines/cross_checking_with_pref_voting.md).

---

## Related concept pages

- [Ranked Robin is summable](RCV_RR_summability.md) — the pairwise matrix adds across precincts (and the topic hub: [Summability](../topics/summability/README_summability.md))
- [Cycle resolution](cycle_resolution.md) — why Copeland is tie-prone, and why Minimax / Ranked Pairs / Schulze exist (they differ only on cycles)
- [Strict vs. weak ranks](../scores_and_ranks/strict_vs_weak_ranks.md) — Ranked Robin allows equal ranks; IRV doesn't
- [Center squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md) — the failure RR avoids and IRV doesn't
- [Is IRV "just plurality"?](../RCV_IRV/RCV_IRV_and_plurality.md) — why IRV isn't pairwise
- [Scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md) — RR is still order-only, unlike STAR
- [RCV-IRV vs. STAR (side-by-side)](../rcv_irv_vs_star.md)
- [RCV vs. IRV vs. RCV-IRV — terminology](../RCV_IRV/RCV-IRV-confusing-name.md)

## Learn more — external

- [Equal Vote Coalition — Ranked Robin](https://www.equal.vote/ranked_robin) *(pro-Ranked-Robin advocacy)*
- [Better Choices for Democracy — Consensus Choice FAQs](https://www.betterchoices.vote/faqs) *(advocacy; the same Condorcet idea, "Top 4" + Consensus Choice branding)*
- [Rob LeGrand — Ranked-ballot voting calculator](https://www.cs.angelo.edu/~rlegrand/rbvote/calc.html) *(paste `count:A>B>C` ballots; computes Condorcet methods, Borda, Hare/IRV, Coombs, Bucklin — a quick independent hand-check)*
- [Copeland's method (Wikipedia)](https://en.wikipedia.org/wiki/Copeland%27s_method) *(the academic name for Ranked Robin's win-loss-record count)*
- [Copeland's method (electowiki)](https://electowiki.org/wiki/Copeland%27s_method) *(the election-methods community wiki — more depth on the count and its tie-break variants)*
