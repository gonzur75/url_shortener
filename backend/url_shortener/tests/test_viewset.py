from rest_framework import status

from conftest import URL
from url_shortener.models import ShortUrl
from url_shortener.serializers import UrlShortenerSerializer
from url_shortener.viewsets import UrlShortenerViewSet
from rest_framework.test import force_authenticate


def test_create_url_shortener_viewset(api_request_factory, user):
    url = "api/v1/urls/"
    view = UrlShortenerViewSet.as_view({"post": "create"})
    url_shortener_ = {
        "url": URL
    }
    request = api_request_factory.post(url, data=url_shortener_, format="multipart")
    force_authenticate(request, user=user)
    response = view(request)

    assert response.status_code == status.HTTP_201_CREATED
    short_url = ShortUrl.objects.first()
    serializer = UrlShortenerSerializer(short_url)
    assert short_url.token == response.data['short_url'][-8:]


def test_retrieve_url_shortener_viewset(api_request_factory, user, short_url):
    token = short_url.token
    url = f"api/v1/{token}/"
    view = UrlShortenerViewSet.as_view({"get": "retrieve"})
    request = api_request_factory.get(url)
    force_authenticate(request, user=user)

    response = view(request, token=short_url.token)

    assert response.status_code == status.HTTP_302_FOUND
    assert short_url.url == response.url
