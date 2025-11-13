from celery import shared_task

@shared_task
def task_hello(user):
    print(f"Hello, {user}!")

@shared_task
def add(x, y):
    return x + y