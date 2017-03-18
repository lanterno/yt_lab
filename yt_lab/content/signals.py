from django.db.models.signals import post_save
from django.dispatch import receiver

from yt_lab.taskapp.celery import update_source
from .models import Source


@receiver(post_save, sender=Source)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        update_source.delay(
            source_id=instance.pk
        )
