#!/bin/bash

cd src

if [[ "${1}" == "celery" ]]; then
  celery --app=pars.tasks:celery_app worker -l INFO
elif [[ "${1}" == "flower" ]]; then
  celery --app=pars.tasks:celery_app flower
 fi