import secrets
import string

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import conftest
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from url_shortener.models import ShortUrl
from url_shortener.serializers import UrlShortenerSerializer


class UrlshortenerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ShortUrl.objects.all()
    serializer_class = UrlShortenerSerializer

    def create(self, request, *args, **kwargs):
        result = UrlShortenerSerializer(data=request.data, context={'user': conftest.user})
        if result.is_valid():
            characters = string.ascii_letters + string.digits
            token = ''.join(secrets.choice(characters) for i in range(8))
            url = result.data.get('url')
            ShortUrl.objects.create(url=url, token=token)
            absolute_url = f'{request.build_absolute_uri()}{token}'
            data = {
                'short_url': absolute_url,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
