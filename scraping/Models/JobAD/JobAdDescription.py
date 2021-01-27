from django.db import models
from transliterate import slugify


class 	JobAdDescription(models.Model):
    text = models.TextField()
    text_formatted = models.TextField()
    company_information = models.TextField()
    needs = models.TextField()
    requirements = models.TextField()
    conditions = models.TextField()

