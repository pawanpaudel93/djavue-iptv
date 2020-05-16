from django.db import models


class TvInfo(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField(max_length=2083, blank=True, null=True)
    url = models.URLField(max_length=2083)
    category = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=60, blank=True)
    country = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return self.name
