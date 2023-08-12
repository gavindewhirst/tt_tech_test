resource "aws_ecr_repository" "gavintechtest-gateway" {
  name                 = "gavintechtest-gateway"
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = false
  }
}

resource "aws_lambda_function" "gavintechtest-gateway" {
  image_uri     = "${aws_ecr_repository.gavintechtest-gateway.repository_url}:latest"
  package_type  = "Image"
  timeout = 10
  memory_size = 1769 # let it have a single CPU
  function_name = "gavintechtest-gateway"
  role          = "arn:aws:iam::680118005139:role/service-role/spine-builder-role-w9pu06bh" # SORT THIS
  image_config {
    command = ["app.lambda_handler"]
  }
  environment {
    variables = {
      CLASSIC_ROCK = "Creedence"
    }
  }
}

### API gateway (REST) ######################
resource "aws_api_gateway_rest_api" "gavintechtest-gateway" {
  name = "gavintechtest-gateway"
}
####################################

### DEPLOYMENT ################################### 
resource "aws_api_gateway_deployment" "gavintechtest_gw_deployment" {
  rest_api_id = aws_api_gateway_rest_api.gavintechtest-gateway.id
  depends_on = [aws_api_gateway_integration.ratings_GET_integration, aws_api_gateway_method.ratings_GET, aws_api_gateway_method.lap_times_GET ]
  triggers = {
    redeployment = sha1(jsonencode(aws_api_gateway_rest_api.gavintechtest-gateway.body))
  }
  lifecycle { create_before_destroy = true }
}

resource "aws_api_gateway_stage" "stage_prod" {
  deployment_id = aws_api_gateway_deployment.gavintechtest_gw_deployment.id
  rest_api_id = aws_api_gateway_rest_api.gavintechtest-gateway.id
  stage_name = "stage_prod"
  cache_cluster_size = "0.5"
  variables = {
      lambda_tag = "latest"
    }
}

resource "aws_lambda_permission" "allow-api-gavintechtest" {
  statement_id = "AllowAPIGatewayInvokationGavinTechTest"
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.gavintechtest-gateway.function_name
  principal = "apigateway.amazonaws.com"
}


### ratings [GET] ->  function.shelfradar-gateway ######################
resource "aws_api_gateway_resource" "ratings" {
  rest_api_id = aws_api_gateway_rest_api.gavintechtest-gateway.id
  parent_id = aws_api_gateway_rest_api.gavintechtest-gateway.root_resource_id
  path_part = "ratings"
}
resource "aws_api_gateway_method" "ratings_GET" {
  rest_api_id = aws_api_gateway_rest_api.gavintechtest-gateway.id
  resource_id = aws_api_gateway_resource.ratings.id
  http_method = "GET"
  authorization = "NONE"
  api_key_required = false
}
resource "aws_api_gateway_integration" "ratings_GET_integration" {
  rest_api_id = aws_api_gateway_rest_api.gavintechtest-gateway.id
  resource_id = aws_api_gateway_resource.ratings.id
  http_method = "GET"
  integration_http_method = "POST"
  type = "AWS_PROXY"
  uri = aws_lambda_function.gavintechtest-gateway.invoke_arn
}
###################################


### lap_times [GET] ->  function.shelfradar-gateway ######################
resource "aws_api_gateway_resource" "lap_times" {
  rest_api_id = aws_api_gateway_rest_api.gavintechtest-gateway.id
  parent_id = aws_api_gateway_rest_api.gavintechtest-gateway.root_resource_id
  path_part = "lap_times"
}
resource "aws_api_gateway_method" "lap_times_GET" {
  rest_api_id = aws_api_gateway_rest_api.gavintechtest-gateway.id
  resource_id = aws_api_gateway_resource.lap_times.id
  http_method = "GET"
  authorization = "NONE"
  api_key_required = false
}
resource "aws_api_gateway_integration" "lap_times_GET_integration" {
  rest_api_id = aws_api_gateway_rest_api.gavintechtest-gateway.id
  resource_id = aws_api_gateway_resource.lap_times.id
  http_method = "GET"
  integration_http_method = "POST"
  type = "AWS_PROXY"
  uri = aws_lambda_function.gavintechtest-gateway.invoke_arn
}
###################################