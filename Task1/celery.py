from  __future__  import absolute_import
import os
from celery import Celery
from django.conf import settings

# # set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Task1.settings')
app = Celery('Task1')
app.conf.enable_utc = False
# app.conf.update(timezone='Asia/Kolkata')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')