# March Madness Analytics

Historical NCAA Tournament data for bracket analysis and prediction.

## Data Files

| File                      | Description                                                                 |
| ------------------------- | --------------------------------------------------------------------------- |
| `538 Ratings.csv`         | FiveThirtyEight team ratings and predictions                                |
| `KenPom Barttorvik.csv`   | Team efficiency metrics (adjusted offensive/defensive ratings, tempo, etc.) |
| `Public Picks.csv`        | Public bracket pick percentages                                             |
| `Seed Results.csv`        | Historical win rates by seed matchup                                        |
| `Team Results.csv`        | Team performance and tournament results                                     |
| `Tournament Matchups.csv` | Game-by-game tournament results                                             |
| `Upset Count.csv`         | Historical upset statistics by round                                        |

## Usage

```python
from deephaven import read_csv

seed_results = read_csv("/data/examples/MarchMadness/csv/Seed Results.csv")
matchups = read_csv("/data/examples/MarchMadness/csv/Tournament Matchups.csv")
kenpom = read_csv("/data/examples/MarchMadness/csv/KenPom Barttorvik.csv")
```

# Source and Licence

This dataset is publicly available on [Kaggle](https://www.kaggle.com/) at [this url](https://www.kaggle.com/datasets/nishaanamin/march-madness-data).

The data is licensed under the Creative Commons public domain CC BY-NC-SA 4.0. Deephaven makes no claim of its authenticity or its accuracy. It has been placed here for demonstrative purposes.
