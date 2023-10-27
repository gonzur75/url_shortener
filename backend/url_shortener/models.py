from django.db import models


# Create your models here.
class ShortUrl(models.Model):
    url = models.URLField()
    token = models.CharField(max_length=8)

    def __str__(self):
        return self.url
