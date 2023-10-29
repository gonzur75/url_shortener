from django.urls import path

from url_shortener.viewsets import UrlShortenerViewSet

urlpatterns = [
    path('', UrlShortenerViewSet.as_view({'post': 'create'})),
    path('<str:token>', UrlShortenerViewSet.as_view({'get': 'retrieve'}))
]