from django.contrib import admin

from url_shortener.models import ShortUrl

admin.site.register(ShortUrl)
