from celery import Celery
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

broker_url = os.getenv('REDIS_URL')

app = Celery('task', broker=broker_url, backend=broker_url)

@app.task
def some_task():
    print('started some work')
    sleep(20)
    return 'task completed'