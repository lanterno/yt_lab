from django.db import models


class Source(models.Model):
    '''
    This is a source of videos. It can be anything with a url that links to a webpage that has videos.
    Currently the system can handle only two types on Content sources; Playlists and Channels
    '''
    SOURCE_TYPES = (
        (0, 'Playlist'),
        (1, 'Channel'),
    )
    url = models.URLField()
    title = models.CharField(max_length=400, null=True, blank=True)
    typ = models.PositiveSmallIntegerField(choices=SOURCE_TYPES, null=True, blank=True)

    class Meta:
        verbose_name = 'Content Source'


class Video(models.Model):

    source = models.ForeignKey(Source, related_name='videos')

    url = models.URLField()
    title = models.CharField(max_length=400)
    duration = models.DurationField()
    views_count = models.PositiveIntegerField()
    thmubnail = models.ImageField()
    image = models.ImageField()
