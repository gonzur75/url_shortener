import secrets
import string

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response


from rest_framework.permissions import IsAuthenticatedOrReadOnly

from url_shortener.models import ShortUrl
from url_shortener.serializers import UrlShortenerSerializer


class UrlShortenerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ShortUrl.objects.all()
    serializer_class = UrlShortenerSerializer

    def create(self, request, *args):
        result = UrlShortenerSerializer(data=request.data, context={'user': request.user})
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

    def retrieve(self, request, token, *args, **kwargs):
        obj = get_object_or_404(ShortUrl, token=token)
        return HttpResponseRedirect(redirect_to=obj.url)


