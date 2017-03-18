from rest_framework import viewsets, mixins
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Source, Video
from .serializers import SourceSerializer, VideoSerializer


class ContentSourceViewset(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class GoupVideosViewSet(NestedViewSetMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
