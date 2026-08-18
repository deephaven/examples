# Fantasy Football Data

Sample data for the [AI at Your Draft Table](/blog/2026/08/25/fantasy-football-draft-ai) blog post. Contains 2026 preseason fantasy football projections and average draft position (ADP) data for PPR scoring.

## Files

| File | Rows | Description |
|------|------|-------------|
| `projections.csv` | 120 | Consensus fantasy point projections |
| `adp.csv` | 120 | Average draft position from major platforms |

## Schema

**`projections.csv`**

| Column | Type | Description |
|--------|------|-------------|
| `player` | string | Player name |
| `team` | string | NFL team abbreviation |
| `position` | string | Position (QB, RB, WR, TE) |
| `projected_points` | float | Projected fantasy points (PPR scoring) |
| `injury_status` | string | Injury designation if applicable |

**`adp.csv`**

| Column | Type | Description |
|--------|------|-------------|
| `player` | string | Player name |
| `adp` | float | Average draft position |
| `adp_rank` | int | Overall ADP rank |

## Usage

```python
from deephaven import read_csv

projections = read_csv(
    "https://media.githubusercontent.com/media/deephaven/examples/main/FantasyFootball/projections.csv"
)

adp = read_csv(
    "https://media.githubusercontent.com/media/deephaven/examples/main/FantasyFootball/adp.csv"
)

# Join and calculate value
draft_board = projections.natural_join(
    adp, on=["player"], joins=["adp", "adp_rank"]
).update_view([
    "value_score = projected_points / adp_rank"
]).sort_descending("value_score")
```

## Notes

- Projections are illustrative samples based on 2026 preseason consensus.
- For live data, use [FantasyPros API](https://www.fantasypros.com/api-data/), [Sleeper](https://docs.sleeper.com/), or ESPN projections.

## Source and license

This dataset was created for demonstrative purposes. Deephaven makes no claim of its authenticity or its accuracy.
