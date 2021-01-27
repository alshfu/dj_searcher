from django.db import models
from transliterate import slugify

class JobTechTaxonomyItem(models.Model):
    label = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branch'

    def __str__(self):
        return self.label