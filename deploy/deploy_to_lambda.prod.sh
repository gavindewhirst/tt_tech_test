#!/usr/bin/env bash
aws ecr get-login-password --region=us-east-1 | docker login --username AWS --password-stdin 680118005139.dkr.ecr.eu-west-1.amazonaws.com
docker build --no-cache -t gavintechtest-gateway:latest -f Dockerfile .
docker tag gavintechtest-gateway:latest 680118005139.dkr.ecr.eu-west-1.amazonaws.com/gavintechtest-gateway:latest
docker push 680118005139.dkr.ecr.eu-west-1.amazonaws.com/gavintechtest-gateway:latest
aws lambda update-function-code --function-name gavintechtest-gateway --image-uri "680118005139.dkr.ecr.eu-west-1.amazonaws.com/gavintechtest-gateway:latest"