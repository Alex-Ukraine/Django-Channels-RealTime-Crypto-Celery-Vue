from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ccymc.settings')

app = Celery('ccymc')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get-data-every-35-seconds': {
        'task': 'get_the_data',
        'schedule': 35.0
    }
}

app.autodiscover_tasks()
