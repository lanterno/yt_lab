import re
from rest_framework import serializers


from .models import Source, Video


class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = ('id', 'url', 'title', 'typ')
        read_only_fields = ('id', 'title', 'typ')

    def validate_id(self, id):
        if Source.objects.filter(id=id):
            raise serializers.ValidationError({'error': 'This list/channel has already been added'})

        return id

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
            data['id'] = channel_pattern.match(data['url']).groupdict()['id']
            data['typ'] = Source.CHANNEL
        elif playlist_pattern.match(data['url']):
            data['id'] = playlist_pattern.match(data['url']).groupdict()['id']
            data['typ'] = Source.PLAYLIST
        else:
            raise serializers.ValidationError("Source URL couldn't be validated")

        data['id'] = self.validate_id(data['id'])
        return data


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('id', 'url', 'title', 'duration', 'views_count', 'thumbnail', 'image')
