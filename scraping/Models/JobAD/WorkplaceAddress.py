from django.db import models
from transliterate import slugify


class WorkplaceAddress(models.Model):
    # municipality = models.CharField(max_length=250)
    # municipality_code = models.CharField(max_length=250)
    # municipality_concept_id = models.CharField(max_length=250)
    # region = models.CharField(max_length=250)
    # region_code = models.CharField(max_length=250)
    # region_concept_id = models.CharField(max_length=250)
    # country = models.CharField(max_length=250)
    # country_code = models.CharField(max_length=250)
    # country_concept_id = models.CharField(max_length=250)
    # street_address = models.CharField(max_length=250)
    # postcode = models.CharField(max_length=250)
    city = models.ForeignKey('City',on_delete=models.CASCADE)
