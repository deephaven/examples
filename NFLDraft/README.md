# NFL Draft Data

Sample data for the [NFL Draft Analytics](https://deephaven.io/blog/2026-04-20-nfl-draft-analytics/) blog post. Covers 2000–2023 NFL Draft picks with career outcomes and combine measurables.

## Files

| File | Rows | Source |
|------|------|--------|
| `csv/nfl_draft_picks.csv` | ~12,670 | [nflverse](https://github.com/nflverse/nflverse-data) |
| `csv/nfl_combine.csv` | ~7,999 | [nflverse](https://github.com/nflverse/nflverse-data) |

## Schema

**`nfl_draft_picks.csv`**

| Column | Type | Description |
|--------|------|-------------|
| `year` | int | Draft year |
| `round` | int | Round (1–7) |
| `pick` | int | Overall pick number |
| `team` | string | Drafting team abbreviation |
| `player` | string | Player name |
| `position` | string | Position |
| `college` | string | College |
| `games_played` | int | Career games played |
| `pro_bowls` | int | Pro Bowl selections |
| `all_pro` | int | All-Pro selections |
| `approximate_value` | float | Career approximate value (PFR metric) |

**`nfl_combine.csv`**

| Column | Type | Description |
|--------|------|-------------|
| `player` | string | Player name |
| `year` | int | Combine year |
| `forty_yard` | float | 40-yard dash (seconds) |
| `bench_press` | int | Bench press reps (225 lbs) |
| `vertical` | float | Vertical jump (inches) |
| `broad_jump` | int | Broad jump (inches) |
| `cone_drill` | float | 3-cone drill (seconds) |
| `shuttle` | float | 20-yard shuttle (seconds) |

## Usage

```python
from deephaven import read_csv

draft = read_csv("https://media.githubusercontent.com/media/deephaven/examples/main/NFLDraft/csv/nfl_draft_picks.csv")
combine = read_csv("https://media.githubusercontent.com/media/deephaven/examples/main/NFLDraft/csv/nfl_combine.csv")
```

# Source and Licence

Data sourced from [nflverse](https://github.com/nflverse/nflverse-data), which aggregates NFL data under open licenses.

Deephaven makes no claim of its authenticity or its accuracy. It has been placed here for demonstrative purposes.
