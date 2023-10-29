from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ShortUrl(models.Model):
    author = models.ForeignKey(User, related_name='short_urls', on_delete=models.CASCADE)
    url = models.URLField()
    token = models.CharField(max_length=8)

    def __str__(self):
        return self.url
