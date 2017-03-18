from rest_framework import serializers

from .models import Source, Video


class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = ('id', 'url', 'title', 'typ')


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('url', 'title', 'duration', 'views_count', 'thmubnail', 'image')
