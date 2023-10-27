import pytest

from url_shortener.models import ShortUrl

TOKEN = '1234'

@pytest.fixture
def short_url():
    short_url = ShortUrl(url=URL, token=TOKEN)
    return short_url


URL = 'https://data.stackexchange.com/stackoverflow/query/58883/test-long-url'
