from celery import shared_task
from config.celery_app import app


from . import models
import json

@shared_task
def test_task():
    print('test_task')