from routes.i_route import routesInterface
from data.dbAccess import dbAccess

class LapTimes(routesInterface):

  def process_event(self, event={}):
    accessor = dbAccess()
    
    sessionid, userid, sort = None, None, None
    try:
      sessionid = event["queryStringParameters"]["sessionId"]
    except KeyError:
      pass

    try:
      userid = event["queryStringParameters"]["userId"]
    except KeyError:
      pass

    try:
      sort = event["queryStringParameters"]["sort"]
    except KeyError:
      pass

    # fetch the data
    records = None
    if sessionid == None and userid == None:
      records = accessor.readAllRecords()  
    elif sessionid == None and userid != None:
      records = accessor.readOneUser(userid)
    elif sessionid != None and userid != None:
      records = accessor.readOneUserOneSession(userid, sessionid)

    # sortable
    if sort == "userId":
      records.sort_values(by=['uid'], inplace=True, ascending=False)
    elif sort == "lapTime":
      records.sort_values(by=['lt_ms'], inplace=True, ascending=False)
    elif sort == "lapTime, userId":
      records.sort_values(by=['lt_ms', 'uid'], inplace=True, ascending=[False, False])
    elif sort == "userId, lapTime":
      records.sort_values(by=['uid', 'lt_ms'], inplace=True, ascending=[False, False])
    
    # export to nice reading json
    exporter = []
    for idx, r in records.iterrows():
      exporter.append(
        {
          "user_id": r["uid"],
          "session_id": r["sid"],
          "laptime_milliseconds": r["lt_ms"],
          "date_recorded": r["ts_epoch"],
        }
      )
    return 200, exporter



    