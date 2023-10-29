from django.urls import path
from rest_framework.routers import SimpleRouter

from url_shortener.viewsets import ShortUrlViewSet

router = SimpleRouter()
router.register('', ShortUrlViewSet, basename='short_urls')

urlpatterns = router.urls


#
# urlpatterns = [
#     path('', ShortUrlViewSet.as_view({'post': 'create'})),
#     path('<str:token>', ShortUrlViewSet.as_view({'get': 'retrieve'})),
#     path('', ShortUrlViewSet.as_view({'get': 'list'})),
# ]