from routes.i_route import routesInterface
from data.dbAccess import dbAccess
import pandas as pd
import numpy as np

class ratings(routesInterface):

  def process_event(self, event):

    allrecords = dbAccess().readAllRecords()

    uidlist = allrecords["uid"].unique()

    # our rating will be based on : 
    ## lap time monotony - how consistent the laps have been (average/SD)
    ## fastest lap time - how fast is the fastest lap
    
    # fastest laps with great monotony values = WINNING COMBINATION (should rate highly)
    # we're going to give them a rating based on their fastest laptime - we'll directly grab the percentile
    # we'll then mark on monotony
    # Monotony
    ## < 10 = terrible   - *1
    ## < 50 = ok         - *2
    ## < 100 = not bad   - *3
    ## > 100 = excellent - *5

    ratingsList = []
    for uid in uidlist:

      useritems = allrecords[allrecords["uid"] == uid]

      fastest_lap_time = float(useritems["lt_ms"].min())
      lap_time_stddev = float(useritems["lt_ms"].std())
      avg_time = float(useritems["lt_ms"].mean())
      lap_time_monotony =  float(avg_time / lap_time_stddev)     

      rating = 0
      ratingsList.append(
        {
          "user_id": uid, 
          "fastest_lap_time": fastest_lap_time,
          "lap_time_monotony": lap_time_monotony,
          "lap_time_stddev": lap_time_stddev,
        }
      )

    ratings_df = pd.DataFrame(ratingsList)
    ratings_df['monotony_p'] = ratings_df.lap_time_monotony.rank(pct=True)
    ratings_df['fastest_p'] = ratings_df.fastest_lap_time.rank(pct=True)

    # get the rating by combining them both 
    ratings_df['rating'] = np.round(10*((1 - ratings_df["fastest_p"]) *  ratings_df['monotony_p']), 0)

    exporter = []
    for idx, item in ratings_df.iterrows():
      exporter.append({
        "user_id": item["user_id"],
        "rating": item["rating"],
      })

    return 200, exporter
