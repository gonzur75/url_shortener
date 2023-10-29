import secrets
import string

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from url_shortener.models import ShortUrl
from url_shortener.serializers import ShortUrlSerializer, ShortUrlListSerializer


class ShortUrlViewSet(viewsets.ModelViewSet):
    queryset = ShortUrl.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ShortUrlSerializer

    def get_queryset(self):
        user = self.request.user
        return user.short_urls.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ShortUrlListSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request, *args):
        result = ShortUrlSerializer(data=request.data)
        if result.is_valid(raise_exception=True):
            characters = string.ascii_letters + string.digits
            token = ''.join(secrets.choice(characters) for i in range(8))
            url = result.data.get('url')

            ShortUrl.objects.create(author=request.user, url=url, token=token)
            absolute_url = f'{request.build_absolute_uri()}{token}'
            data = {
                'short_url': absolute_url,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, token=None, *args, **kwargs):
        obj = get_object_or_404(ShortUrl, token=token)
        return HttpResponseRedirect(redirect_to=obj.url)
