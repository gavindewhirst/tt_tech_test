# Imports
import json
import logging
import responses.responses as responses
from routes.ratings_route import ratings
from routes.lap_times_route import LapTimes

root = logging.getLogger()
root.setLevel(logging.INFO)

def lambda_handler(event, context):

  root.info("Processing event :")
  root.info(event)
  path = ""
  try:
    path = event["resource"]
  except:
    return responses.responseErrorBadData
  
  eventResponse = None
  status = None
  handler = None

  if path == '/lap_times':
    handler = LapTimes()
  if path == '/ratings':
    handler = ratings()
    
  status, eventResponse = handler.process_event(event=event)
  
  # send the response
  if status is not None and eventResponse is not None:
    responseBody = responses.responseBasic
    responseBody["status"] = status
    responseBody["body"] = json.dumps(eventResponse)
    return responseBody
  else:
    return responses.responseErrorBadData


if __name__ == "__main__":

  nEve = {
    "resource": "/ratings", 
    "queryStringParameters" : 
      {
        "sessionId": "631abfeb-2cf3-4381-b966-3db9c5c7b67f",
        "userId": "d3351574-af98-426d-a00c-48d1fd27899d", 
        "sort": "userId"
      }
  }


  lambda_handler(nEve, None)