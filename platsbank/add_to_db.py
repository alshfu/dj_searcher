import csv
import os, sys
from slugify import slugify, Slugify, UniqueSlugify

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'dj_searcher.settings'

import django

django.setup()

from scraping.Models.JobAD import JobAd
from scraping.Models.location.City import City
from scraping.Models.JobAD.JobTechTaxonomyItem import JobTechTaxonomyItem
# name = models.CharField(max_length=50, verbose_name='Ort', unique=True)
# slug = models.CharField(max_length=50, blank=True, unique=True)
# with open('jobb_tag_list.csv', newline='', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     data = list(reader)
#
# for ort in data:
#     custom_slugify = Slugify(to_lower=True)
#     name = ort[0]
#     slug = custom_slugify(ort[0])
#     city = JobTechTaxonomyItem(concept_id=slug,label=name,legacy_ams_taxonomy_id=slug)
#     city.save()
#     print(city)