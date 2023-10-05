from app.config import settings
from celery import Celery

celery = Celery(
    'app.worker',
    broker=f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}',
    include=['app.worker.tasks']
)

celery.config_from_object('app.worker.celery_config')
