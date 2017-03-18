from django.apps import AppConfig


class ContentConfig(AppConfig):
    name = 'yt_lab.content'

    def ready(self):
        from . import signals
