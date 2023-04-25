# pars/tasks.py
import asyncio

from celery import Celery

from pars.pars import run

#  celery -A tasks.tasks:celery_app worker --loglevel=INFO --pool=solo
celery_app = Celery('tasks', broker='redis://redis:6379')


@celery_app.task
def start_parser():
    asyncio.run(run())
