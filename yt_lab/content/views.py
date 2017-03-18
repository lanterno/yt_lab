from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Source, Video
from .serializers import SourceSerializer, VideoSerializer


class ContentSourceViewset(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class VideosGroupViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
