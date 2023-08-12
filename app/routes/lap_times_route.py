from os import access
from routes.i_route import routesInterface
from data.dbAccess import dbAccess

class LapTimes(routesInterface):

  def sorter(self, df, sortType):

    return df

  def process_event(self, event={}):
    accessor = dbAccess()
    
    sessionid, userid, sort = None
    try:
      sessionid = event["querystringparamers"]["sid"]
    except KeyError:
      pass

    try:
      userid = event["querystringparamers"]["uid"]
    except KeyError:
      pass

    try:
      sort = event["querystringparamers"]["sort"]
    except KeyError:
      pass

    records = None
    if sessionid == None and userid == None:
      records = accessor.readAllRecords()  
    elif sessionid == None and userid != None:
      records = accessor.readOneUser(userid)
    elif sessionid != None and userid != None:
      records = accessor.readOneUserOneSession(userid, sessionid)
    
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



    