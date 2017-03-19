import re
from rest_framework import serializers


from .models import Source, Video


class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = ('id', 'url', 'title', 'typ', 'youtube_id')
        read_only_fields = ('id', 'title', 'youtube_id', 'typ')

    def validate(self, data):
        '''
        - Apply all default validations
        - make sure provided URL is valid
        - parse the youtube_id and type
        return data or raise validation error
        '''
        data = super().validate(data)
        channel_pattern = re.compile(r'.*youtube.com/(channel|user)/(?P<id>[ A-Za-z0-9_-]*)')
        playlist_pattern = re.compile(r'.*list=(?P<id>[ A-Za-z0-9_-]*)')

        if channel_pattern.match(data['url']):
            data['youtube_id'] = channel_pattern.match(data['url']).groupdict()['id']
            data['typ'] = Source.CHANNEL
        elif playlist_pattern.match(data['url']):
            data['youtube_id'] = playlist_pattern.match(data['url']).groupdict()['id']
            data['typ'] = Source.PLAYLIST
        else:
            raise serializers.ValidationError("Source URL couldn't be validated")
        return data


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('url', 'title', 'duration', 'views_count', 'thmubnail', 'image')
