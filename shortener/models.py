from django.db import models

# Create your models here.

class UrlShortner(models.Model):
    long_url = models.URLField(primary_key=True)
    short_code = models.CharField(unique=True,max_length=30)

