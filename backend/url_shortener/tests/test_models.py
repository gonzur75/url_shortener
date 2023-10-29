import pytest
from django.db import DataError

from conftest import TOKEN, URL
from url_shortener.models import ShortUrl


@pytest.mark.models
def test_url_gui_representation(short_url):
    assert str(short_url) == short_url.url


@pytest.mark.models
def test_short_url_in_database(short_url):
    assert isinstance(short_url, ShortUrl)
    assert short_url.url == URL
    assert short_url.token == TOKEN
