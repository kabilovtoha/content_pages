from celery import shared_task
from config.celery_app import app


from . import models
import json

@shared_task
def test_task():
    print('test_task')

@shared_task
def increase_post_content_counters(post_id):
    contents = models.Content.objects.filter(post_id=post_id)
    for cont in contents:
        cont.counter += 1
        cont.save()
    return True