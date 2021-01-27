from django.db import models
from transliterate import slugify

from django.db import models
from transliterate import slugify


class ApplicationDetails(models.Model):
    information = models.TextField()
    reference = models.TextField()
    email = models.EmailField()
    via_af = models.BooleanField()
    url = models.URLField()
    other = models.TextField()
