
from rest_framework.routers import SimpleRouter

from url_shortener.viewsets import ShortUrlViewSet

router = SimpleRouter()
router.register('', ShortUrlViewSet, basename='short_urls')

urlpatterns = router.urls
