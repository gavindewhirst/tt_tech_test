# Imports
import logging
import json
from aws_xray_sdk.core import patch_all
import os
import hashlib
import routes.lap_times as lap_times
import routes.route_interface

root = logging.getLogger()
root.setLevel(logging.INFO)
patch_all()

responseGood = {
  "statusCode": 200,
  "headers": { 
    "Content-Type": "application/json",                     
    "Access-Control-Allow-Headers": 'Content-Type',         # CORS
    "Access-Control-Allow-Origin": "*",                     # CORS
    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"      # CORS
    },     
  "isBase64Encoded": False
  }

responseErrorBadData = {
  "statusCode": 422,
  "headers": { 
    "Content-Type": "application/json",                     
    "Access-Control-Allow-Headers": 'Content-Type',         # CORS
    "Access-Control-Allow-Origin": "*",                     # CORS
    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"      # CORS
    },  
  "isBase64Encoded": False,
  }

def lambda_handler(event, context):

  root.info("Processing event :")
  root.info(event)
  path = ""
  try:
    path = event["resource"]
  except:
    return responseErrorBadData

  if path == '/lap_times':
    




    return responseGood


  return responseErrorBadData