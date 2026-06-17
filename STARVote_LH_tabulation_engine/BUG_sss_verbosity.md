# Bug: Sequentially Spent Score (SSS) returns different winners depending on `verbosity`

## Summary

`starvote.election(starvote.sss, ...)` returns a **different set of winners**
for the *same ballots, seats, and maximum_score* depending solely on the
`verbosity` argument. With `verbosity=0` one candidate wins; with `verbosity>=1`
a different candidate wins. `verbosity` is a presentation/logging option and must
never affect the computed result.

## Environment

- starvote **2.1.6** (verified against the PyPI release)
- Python 3.10 and 3.14 (reproduces on both)
- Method: `sss` (Sequentially Spent Score), multi-winner

## Reproduction

```python
import starvote

ballots = []
def add(n, d):
    for _ in range(n):
        ballots.append(dict(d))

# A ~2/3 "majority" bloc (Alice/Ben/Cara) and a ~1/3 "minority" bloc (Dan/Eve)
add(6, {'Alice': 5, 'Ben': 4, 'Cara': 3, 'Dan': 0, 'Eve': 0})
add(4, {'Alice': 4, 'Ben': 5, 'Cara': 3, 'Dan': 0, 'Eve': 0})
add(3, {'Alice': 3, 'Ben': 4, 'Cara': 5, 'Dan': 0, 'Eve': 0})
add(5, {'Alice': 0, 'Ben': 0, 'Cara': 0, 'Dan': 5, 'Eve': 4})
add(3, {'Alice': 0, 'Ben': 0, 'Cara': 0, 'Dan': 4, 'Eve': 5})

for v in (0, 1, 2):
    winners = starvote.election(
        starvote.sss, ballots, seats=3, maximum_score=5, verbosity=v
    )
    print(f"verbosity={v} -> {sorted(winners)}")
```

### Actual output

```
verbosity=0 -> ['Alice', 'Ben', 'Cara']
verbosity=1 -> ['Alice', 'Ben', 'Dan']
verbosity=2 -> ['Alice', 'Ben', 'Dan']
```

### Expected output

All three runs should return the **same** winners (verbosity must not change the
result):

```
verbosity=0 -> [...]
verbosity=1 -> [...]   # identical
verbosity=2 -> [...]   # identical
```

## Key observation / likely cause

The only structural difference between the `verbosity=0` and `verbosity>=1`
traces is that the verbose runs print, right after the quota line:

```
[Sequentially Spent Score: Initializing Hashed Ballots tiebreaker]
 5 candidates
 Counter initialized to 1
 Serialized sorted ballots = (705 bytes)
```

…and the `verbosity=0` run does **not**. This strongly suggests the default
**Hashed Ballots tiebreaker is initialized only when `verbosity >= 1`**, and that
initialization has a side effect (seeding / sorting / serializing the ballots)
that changes how a subsequent step resolves — so the two paths diverge.

Notably, in the `verbosity>=1` trace, Round 2 is clearly won by **Dan** (37,
First place), and the final winners include Dan. The `verbosity=0` run instead
produces **Cara**, which is inconsistent with the per-round logic shown in the
verbose trace. This points to the tiebreaker-initialization side effect (or a
code path guarded by `if verbosity:`) leaking into the tabulation result.

## Impact

- The same election can be declared for different winners depending on a logging
  flag — a correctness bug for any downstream tool that runs SSS quietly
  (`verbosity=0`) vs. verbosely.
- It also makes results hard to test/reproduce: a silent run and a verbose run of
  the identical election disagree.

## Suggested fix direction

Ensure the tiebreaker (and any other per-election state) is initialized
unconditionally, independent of `verbosity`; the verbosity flag should only
control whether the initialization is *printed*, not whether it *happens*. A
regression test asserting `election(..., verbosity=0) == election(..., verbosity=2)`
across methods would prevent recurrence.

## Notes

- Reproduced with the stock default tiebreaker (no custom tiebreaker passed), so
  this is not specific to any caller-supplied tiebreaker.
- `star` / `bloc` single-round-per-seat methods were not observed to diverge in
  the cases tried; the divergence was observed with `sss`. Worth checking
  `allocated` and `rrv` for the same verbosity-gated initialization.
