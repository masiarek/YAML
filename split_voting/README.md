# Vote-Splitting / Spoiler Examples

Dramatic single-winner elections where **Choose-One Plurality elects the wrong
winner** because a majority bloc splits its vote across similar candidates — and
**STAR elects the candidate the majority actually preferred.**

Each file declares a `blocs:` group, so the engine's `[Vote-splitting check]`
confirms the spoiler automatically. Run any of them through the STAR engine:

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py \
       split_voting/01_political_left_split.yaml
```

| File | Story | Choose-One winner | STAR winner |
|------|-------|-------------------|-------------|
| `01_political_left_split.yaml` | A 66% progressive coalition splits 3 ways | **Conservative (34%)** — the spoiler | **Labour** — the coalition's consensus |
| `02_icecream_chocolate_split.yaml` | Chocolate lovers (66%) split across 3 chocolates | **Vanilla (34%)** | **MilkChoco** |
| `03_lunch_veggie_vs_meat.yaml` | A 70% veggie majority splits across 3 dishes | **BeefBurger (30%)** | **VeggieCurry** |

In every case the bloc is an outright majority, yet Choose-One hands the win to
the lone outsider. STAR lets each voter score every candidate, so the bloc isn't
split — and the automatic runoff elects the majority's compromise pick.

> Teaching tip: show the **Choose-One first choices** line first (the wrong
> winner) and let it sting, then reveal the STAR result. The `[Vote-splitting
> check]` block states the verdict in numbers.
