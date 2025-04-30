#!/bin/bash

# Змінна з назвою проєкту
PROJECT_ID="autoreportbot"
SERVICE_NAME="auto-report"
REGION="europe-central2"
IMAGE="gcr.io/${PROJECT_ID}/${SERVICE_NAME}"

# 🚀 Збірка Docker-образу
gcloud builds submit --tag $IMAGE

# 🌍 Деплой до Cloud Run
gcloud run deploy $SERVICE_NAME \
  --image $IMAGE \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated
