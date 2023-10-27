import pytest
from django.db import DataError

from conftest import TOKEN, URL
from url_shortener.models import ShortUrl


def test_url_gui_representation(short_url):
    assert str(short_url) == short_url.url


def test_short_url_in_database(short_url):
    assert short_url.url == URL
    assert short_url.token == TOKEN

def test_short_url_token_max_length(db, short_url):

    with pytest.raises(DataError) as excinfo:
        ShortUrl.objects.create()

        assert "value too long for type character varying(8)" in str(excinfo.value)
