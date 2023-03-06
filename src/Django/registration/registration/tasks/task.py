from time import sleep
from ..celery import app


@app.task()
def sleep_task():
    sleep(30)
    print("woke up")
