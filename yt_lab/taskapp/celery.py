import os
from celery import Celery
from django.apps import apps, AppConfig
from django.conf import settings

from celery.decorators import periodic_task
from celery.task.schedules import crontab


if not settings.configured:
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')  # pragma: no cover


app = Celery('yt_lab')


class CeleryConfig(AppConfig):
    name = 'yt_lab.taskapp'
    verbose_name = 'Celery Config'

    def ready(self):
        # Using a string here means the worker will not have to
        # pickle the object when using Windows.
        app.config_from_object('django.conf:settings')
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)


@app.task
def update_source(source_id):
    from yt_lab.content.utils import update_source_info, update_source_videos
    from yt_lab.content.models import Source

    source = Source.objects.get(id=source_id)
    update_source_info(source)
    update_source_videos(source)


@periodic_task(
    # this makes the task happen every day at midnight
    # to change: http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
    run_every=(crontab(minute=0, hour='*/3',)),
    name="periodic_videos_update",
    ignore_result=True
)
def periodic_videos_update():
    from yt_lab.content.utils import update_source_videos
    from yt_lab.content.models import Source

    for source in Source.objects.all():
        update_source_videos(source)
