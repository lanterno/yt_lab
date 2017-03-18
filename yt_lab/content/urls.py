from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import ContentSourceViewset, VideosGroupViewSet

router = ExtendedSimpleRouter()
sources = router.register(r'sources', ContentSourceViewset)

sources.register(
    r'videos',
    VideosGroupViewSet,
    base_name='source-videos',
    parents_query_lookups=['source']
)

urlpatterns = router.urls
