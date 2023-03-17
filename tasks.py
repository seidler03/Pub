from celery import Celery
from redis import Redis
from json import dumps

redis = Redis(host='localhost', port=6379)
celery_app = Celery('teste', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')


@celery_app.task
def publish_item_to_pubsub(item):
    try:
        redis = Redis(host='localhost', port=6379)
        message = dumps(dict(item))
        message = str(message)
        data = redis.publish('my_pubsub_channel', message)
        return data
    except Exception as Error:
        print(Error)


