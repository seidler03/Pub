from fastapi import FastAPI
from tasks import publish_item_to_pubsub
from models.item import Item
from celery import Celery
from redis import Redis
from json import dumps

app = FastAPI()

redis = Redis(host='localhost', port=6379)
celery_app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@app.post("/item")
async def create_item(item: Item):
    try:
        item = item.dict()
        publish_item_to_pubsub.delay('item')
    except Exception as Error:
        print(Error)
    return item

