from database.connection import celery_app

from celery import Celery

app = Celery('tasks', broker='redis://localhost')

@celery_app.task
def add(x, y):
    return x + y



