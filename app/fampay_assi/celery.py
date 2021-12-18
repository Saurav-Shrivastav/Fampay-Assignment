import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fampay_assi.settings")

app = Celery("fampay_assi")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()