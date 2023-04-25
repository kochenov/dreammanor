#!/bin/bash

alembic upgrade head

cd src

gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 --keyfile="/etc/letsencrypt/live/api.dreammanor.ru/privkey.pem" --certfile="/etc/letsencrypt/live/api.dreammanor.ru/cert.pem"