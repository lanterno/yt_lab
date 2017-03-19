from django.db.models.signals import post_save
from django.dispatch import receiver

from yt_lab.taskapp.celery import update_source
from .models import Source


@receiver(post_save, sender=Source)
def auto_sync_source(sender, instance=None, created=False, **kwargs):
    '''
    This signals add an update_source celery call to the queue
    which in tern should update the created object will needed details and videos
    '''
    if created:
        update_source.delay(
            source_id=instance.pk
        )
