import os

from celery import Celery

# Установите модуль настроек Django по умолчанию для программы 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загрузите модули задач из всех зарегистрированных приложений Django..
app.autodiscover_tasks()
