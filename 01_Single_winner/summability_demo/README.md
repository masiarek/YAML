# Summability demo — one example, three methods

Runnable elections behind the **[Summability topic hub](../../00_start_here/topics/summability/README.md)**.
The point: *summability is a property of the **count**, not the ballot.* The same two
districts are summable under STAR and Ranked Robin, and **not** under RCV-IRV.

## Files

| File(s) | Method | Summable? | Shows |
|---------|--------|:---:|-------|
| `irv_district_A.yaml`, `irv_district_B.yaml`, `irv_combined.yaml` | **RCV-IRV** | ❌ | B wins **both** districts but is *eliminated* when merged — no precinct subtotal predicts it |
| `star_district_A.yaml`, `star_district_B.yaml`, `star_combined.yaml` | **STAR** | ✅ | precinct **score totals + pairwise matrix add** to the combined winner |
| *(reuses the `irv_*` ballots)* | **Ranked Robin / RCV-RR** | ✅ | the **same ranked ballots** IRV couldn't combine — the **pairwise matrix adds** cell by cell and recovers B |

> **Why there are no `rr_*` files.** Ranked Robin runs on the *same ranked ballots* as IRV
> (`irv_*`); only the *count* differs. So the RR demo **is** the `irv_*` files, tabulated as
> a pairwise matrix instead of by elimination. Prefixing the folder `RCV_RR_` would wrongly
> imply it's RR-only — it's a cross-method (IRV/STAR/RR) summability demo.

## Run them

```bash
# STAR (summable) — score totals + matrix
cd STARVote_LH_tabulation_engine
python starvote_larry_hastings.py ../01_Single_winner/summability_demo/star_combined.yaml

# RCV-IRV (not summable) — B eliminated when districts merge
python starvote_larry_hastings.py ../01_Single_winner/summability_demo/irv_combined.yaml

# Ranked Robin / Copeland on the SAME irv_* ballots (pairwise matrix winner)
cd ../pref_voting_tabulation_engine
python pref_voting_tabulation.py ../01_Single_winner/summability_demo/irv_combined.yaml
```

## The three write-ups

- [STAR is summable](../../00_start_here/STAR_Voting/STAR_summability.md)
- [Ranked Robin is summable](../../00_start_here/RCV_Ranked_Robin/RCV_RR_summability.md)
- [IRV is *not* summable](../../00_start_here/RCV_IRV/RCV_IRV_lack_of_summability.md)

The STAR files carry `expected_winners` and are guarded by the positive test harness; all
six are run through the [`pref_voting` cross-check](../../00_start_here/tabulation_engines/cross_checking_with_pref_voting.md).
