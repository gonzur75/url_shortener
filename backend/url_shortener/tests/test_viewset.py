import pytest
from rest_framework import status

from conftest import URL
from url_shortener.models import ShortUrl
from url_shortener.serializers import ShortUrlSerializer
from url_shortener.viewsets import ShortUrlViewSet
from rest_framework.test import force_authenticate


@pytest.mark.viewsets
def test_create_url_shortener_viewset(api_request_factory, user):
    url = "api/v1/"
    view = ShortUrlViewSet.as_view({"post": "create"})
    url_shortener_ = {
        "url": URL
    }
    request = api_request_factory.post(url, data=url_shortener_, format="multipart")
    force_authenticate(request, user=user)
    response = view(request)

    assert response.status_code == status.HTTP_201_CREATED
    short_url = ShortUrl.objects.first()
    serializer = ShortUrlSerializer(short_url)
    assert short_url.token == response.data['short_url'][-8:]


@pytest.mark.viewsets
def test_retrieve_url_shortener_viewset(api_request_factory, user, short_url):
    token = short_url.token
    url = f"api/v1/{token}/"
    view = ShortUrlViewSet.as_view({"get": "retrieve"})
    request = api_request_factory.get(url)
    force_authenticate(request, user=user)

    response = view(request, token=short_url.token)

    assert response.status_code == status.HTTP_302_FOUND
    assert short_url.url == response.url


@pytest.mark.viewsets
def test_list_url_shortener_viewset(api_request_factory, user, short_url):
    url = f"api/v1/urls/"
    view = ShortUrlViewSet.as_view({"get": "list"})
    request = api_request_factory.get(url)
    force_authenticate(request, user=user)
    obj = ShortUrl.objects.filter(author=user)[0]
    serializer = ShortUrlSerializer(obj)
    response = view(request)

    assert response.status_code == status.HTTP_200_OK
    assert obj.url in response.data[0].get('url')
