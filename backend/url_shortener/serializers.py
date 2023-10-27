from rest_framework import serializers

from url_shortener.models import ShortUrl


class UrlShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ('url',)

