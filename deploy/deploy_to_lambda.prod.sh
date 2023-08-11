#!/usr/bin/env bash
aws ecr get-login-password --region=us-east-1 | docker login --username AWS --password-stdin 680118005139.dkr.ecr.us-east-1.amazonaws.com
docker build --no-cache -t shelfradar-gateway-notify:latest -f Dockerfile .
docker tag shelfradar-gateway-notify:latest 680118005139.dkr.ecr.us-east-1.amazonaws.com/shelfradar-gateway-notify:latest
docker push 680118005139.dkr.ecr.us-east-1.amazonaws.com/shelfradar-gateway-notify:latest
aws lambda update-function-code --function-name shelfradar-gateway-notify --image-uri "680118005139.dkr.ecr.us-east-1.amazonaws.com/shelfradar-gateway-notify:latest"