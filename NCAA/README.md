# NCAA

The `tweets.csv` file contains raw tweets with the search terms:

```python
elite_8_mens =['razorbackmbb', 'dukembb', 'uhcougarmbk', 'kuhoops', 'caneshoops', 'peacocksmbb', 'unc_basketball', 'novambb']
elite_8_womens =['stanfordwbb', 'texaswbb', 'gamecockwbb', 'creightonwbb', 'uconnwbb', 'packwomensbball', 'uoflwbb', 'umichwbball']
```


The `teams_grouped.csv` file contains aggregated data from `tweets.csv`.


## Fields in  `tweets.csv`

- **Text:** Contents of Tweet
- **Compound:** Percent positive or negative sentiment of `Text`
- **Negative:** Percent negative sentiment of `Text`
- **Neutral:** Percent neutral sentiment of `Text`
- **Positive:** Percent positive sentiment of `Text`
- **ID:** The unique twitter id
- **DateTime:** Time of tweet
- **Retweet_count:** Number of retweets for that original tweet
- **Reply_count:** Number of replies for that original tweet
- **Like_count:** Number of likes for that original tweet
- **Quote_count:** Number of quotes for that original tweet
- **team:** First team mentioned in `Text`

## Fields in  `teams_grouped.csv`

- **team:** Groupped team 
- **Avg_Pos:** Average percent positive sentiment of all `Text` values for that `team`
- **Avg_Neg:** Average percent negative sentiment of `Text`values for that `team`
- **Avg_Compound:** Average percent positive or negative sentiment of `Text`values for that `team`
- **Avg_retweet:** Average retweets for each tweet for that `team`
- **Number_tweets:** Total tweets for for that `team`

# Source and License

This data was contributed to the public domain by the the TwitterV2 API. It is provided here for demonstrative purposes without any warranty for fitness of purpose or usability.
