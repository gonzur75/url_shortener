from rest_framework import serializers

from url_shortener.models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ('url', 'token')
        read_only_fields = ('token',)


class ShortUrlListSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        request = self.context['request']
        return {
            'url': instance.url,
            'short_url': f'{request.build_absolute_uri()}{instance.token}'
        }
