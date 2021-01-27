from django.db import models
from transliterate import slugify

class Requirements(models.Model):
    skills = models.ForeignKey('JobTechTaxonomyItem',on_delete=models.CASCADE)
    languages = models.ForeignKey('JobTechTaxonomyItem', on_delete=models.CASCADE)
    work_experiences = models.ForeignKey('JobTechTaxonomyItem',on_delete=models.CASCADE)