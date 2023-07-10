import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bulletin_board.settings')

app = Celery('bulletin_board')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
