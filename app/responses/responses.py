responseBasic = {
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