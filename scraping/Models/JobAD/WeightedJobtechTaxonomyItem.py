from django.db import models
from transliterate import slugify


class WeightedJobtechTaxonomyItem(models.Model):
    concept_id = models.CharField(max_length=250, unique=True)
    label = models.CharField(max_length=250)
    legacy_ams_taxonomy_id = models.CharField(max_length=250)
    weight = models.IntegerField
