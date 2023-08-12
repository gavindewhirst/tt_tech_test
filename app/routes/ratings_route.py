from routes.i_route import routesInterface
from data.dbAccess import dbAccess
import pandas as pd
import numpy as np
import logging
class ratings(routesInterface):
  
  def process_event(self, event):
    root = logging.getLogger()
    root.info("starting read")
    allrecords = dbAccess().readAllRecords()

    uidlist = allrecords["uid"].unique()

    root.info("starting ratings")
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
    root.info("done ratings")
    ratings_df = pd.DataFrame(ratingsList)
    ratings_df['monotony_p'] = ratings_df.lap_time_monotony.rank(pct=True)
    ratings_df['fastest_p'] = ratings_df.fastest_lap_time.rank(pct=True)

    root.info("done rankings")
    # get the rating by combining them both 
    ratings_df['rating'] = np.round(10*((1 - ratings_df["fastest_p"]) *  ratings_df['monotony_p']), 0)

    exporter = []
    for idx, item in ratings_df.iterrows():
      exporter.append({
        "user_id": item["user_id"],
        "rating": item["rating"],
      })

    return 200, exporter
