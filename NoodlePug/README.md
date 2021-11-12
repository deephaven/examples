# Bones / No Bones data

This folder contains one CSV file with the [bones/no-bones status of Noodle the Pug](https://www.tiktok.com/@jongraz/video/7022251358833118469?refer=embed&is_copy_url=1&is_from_webapp=v1) from [@jongraz](https://www.tiktok.com/@jongraz?refer=embed).
Here we want to find out, does Noodle normally have a [case of the Mondays](https://www.youtube.com/watch?v=2AB9zPfXqQQ)?

## Table of contents

- `noodle_pug.csv`: A standard format CSV file with a header: `Date`, `noodles_status`, `Day`

## Fields in each file

- `Date`: The day the TikTok video was posted.
- `noodles_status`: The Bones/No Bones status of Noodle; if not stated, status is inferred.
- `Day`: The day of the week the observation occurred.


# How to use the data

[Launch Deephaven](https://deephaven.io/core/docs/tutorials/quickstart/) with examples.


For Python:

```bash
# Choose your compose file selected above.
compose_file=https://raw.githubusercontent.com/deephaven/deephaven-core/main/containers/python-examples/docker-compose.yml
curl  -O "${compose_file}"
docker-compose pull
docker-compose up -d
```

For Groovy:

```bash
# Choose your compose file selected above.
compose_file=https://raw.githubusercontent.com/deephaven/deephaven-core/main/containers/groovy-examples/docker-compose.yml
curl  -O "${compose_file}"
docker-compose pull
docker-compose up -d
```


Navigate to [http://localhost:10000/ide/](http://localhost:10000/ide/), then use the script below to open some tables in the Deephaven IDE.

```python
from deephaven.TableTools import readCsv

noodle_pug = readCsv("https://media.githubusercontent.com/media/deephaven/examples/4f15c29972ae216b5bd8077b5e3dc57351eccb27/NoodlePug/noodle_pug.csv")

number_bones = noodle_pug.dropColumns("Date", "Day_of_Week", "Weather_NYC").sumBy()

number_per_day = noodle_pug.dropColumns("Date","Weather_NYC").sumBy("Day_of_Week")

number_per_weather = noodle_pug.dropColumns("Date", "Day_of_Week").sumBy("Weather_NYC")
```


```groovy
noodle_pug = readCsv("https://media.githubusercontent.com/media/deephaven/examples/4f15c29972ae216b5bd8077b5e3dc57351eccb27/NoodlePug/noodle_pug.csv")

number_bones = noodle_pug.dropColumns("Date", "Day_of_Week", "Weather_NYC").sumBy()

number_per_day = noodle_pug.dropColumns("Date","Weather_NYC").sumBy("Day_of_Week")

number_per_weather = noodle_pug.dropColumns("Date", "Day_of_Week").sumBy("Weather_NYC")
```


Three Deephaven tables populate the IDE. Does Noodle have more "No Bone" days on Monday?


# Planet data

As an interesting use case, we wanted to see if the separation of Mercury and Jupiter is what causes Noodles to have No Bones days.

Here, we have a function that does a calculation to find the separation of the two planets and then we see how this correlates with Bones and No Bones days.  We see that for Bone days, we are accurate 66% of the time - not bad! But for No Bones days, we are accurate with this model 80% of the time! 

We look at the week ahead and give our predictions. Now the question is, what really causes No Bones days? We think it is a complex mixture of all these models.

```python
os.system("pip install ephem")

import ephem

def sep(date):
    m = ephem.Mercury()
    j = ephem.Jupiter()
    m.compute(date)
    j.compute(date)
    return (int)(10*ephem.separation(m, j))

planet = noodle_pug.update("Mercury_Jupiter_sep = (int)sep(Date)","Prediction = (Mercury_Jupiter_sep <= 13) ? `no Bones` : `Bones`")

planet_no_bones = planet.where("Prediction.startsWith(`no`)").dropColumns("Date", "Day_of_Week", "Weather_NYC","Mercury_Jupiter_sep", "Prediction").sumBy()

planet_bones = planet.where("Prediction.startsWith(`Bone`)").dropColumns("Date", "Day_of_Week", "Weather_NYC","Mercury_Jupiter_sep", "Prediction").sumBy()

from deephaven.TableTools import newTable, stringCol

future = newTable(
    stringCol("Date", "11/1/2021", "11/2/2021", "11/3/2021", "11/4/2021", "11/5/2021"))\
    .update("Prediction = ((int)sep(Date)<=13) ? `no Bones` : `Bones`")
```

# Source and License

This data was built from viewing TikToks created by [@jongraz](https://www.tiktok.com/@jongraz?refer=embed).  It is provided here for demonstrative use without any warranty as to the accuracy, reliability, or completeness of the data.
