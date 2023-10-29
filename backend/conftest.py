import pytest
from django.contrib.auth import get_user_model

from url_shortener.models import ShortUrl

URL = 'https://data.stackexchange.com/stackoverflow/query/58883/test-long-url'
TOKEN = '1234'


@pytest.fixture
def short_url(db):
    short_url = ShortUrl.objects.create(url=URL, token=TOKEN)
    return short_url


@pytest.fixture
def api_request_factory():
    from rest_framework.test import APIRequestFactory

    return APIRequestFactory()


@pytest.fixture
def user(db):
    User = get_user_model()
    user = User.objects.create_user(email="test_email@com.pl", username="testUser", password="testPass")
    return user
