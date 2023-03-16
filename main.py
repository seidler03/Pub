from fastapi import FastAPI, APIRouter
from celery import Celery
from redis import Redis

app = FastAPI()


redis = Redis(host='localhost', port=6379)

celery_app = Celery('tasks', broker='redis://localhost:6379/0')
