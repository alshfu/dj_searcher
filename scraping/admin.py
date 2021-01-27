from django.contrib import admin

from scraping.Models.JobAD.JobAd import JobAd
from scraping.Models.JobAD.JobTechTaxonomyItem import JobTechTaxonomyItem
from scraping.Models.JobAD.Employer import Employer
from scraping.Models.location.City import City

admin.site.register(City)
admin.site.register(JobAd)
admin.site.register(Employer)
admin.site.register(JobTechTaxonomyItem)