from pytube import YouTube

from rest_framework import viewsets, response
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.decorators import detail_route

from .models import Source, Video
from .serializers import SourceSerializer, VideoSerializer


class ContentSourceViewset(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class VideosGroupViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    @detail_route(methods=['get'])
    def download(self, request, pk, *args, **kwargs):
        video = YouTube(self.get_object().url)
        medium_quality = video.filter('mp4', resolution='360p')[0]
        return response.Response({'url': medium_quality.url})
