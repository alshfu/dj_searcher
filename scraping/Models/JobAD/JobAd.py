from django.db import models
from transliterate import slugify


class JobAd(models.Model):
    # logo_url = models.URLField()
    # af_id = models.IntegerField(unique=True)
    # webpage_url = models.URLField(unique=True)
    # employer = models.ForeignKey('Employer', on_delete=models.CASCADE)
    # headline = models.CharField(max_length=500,verbose_name='Title')
    # description = models.ForeignKey('JobAdDescription', on_delete=models.CASCADE)
    # duration = models.ForeignKey('JobTechTaxonomyItem', on_delete=models.CASCADE)
    # working_hours_type = models.ForeignKey('JobTechTaxonomyItem', on_delete=models.CASCADE)
    # application_details= models.ForeignKey('ApplicationDetails', on_delete=models.CASCADE)
    # experience_required = models.BooleanField()
    # access_to_own_car = models.BooleanField()
    # driving_license_required = models.BooleanField()
    # workplace_address = models.ForeignKey('WorkplaceAddress', on_delete=models.CASCADE)
    # must_have = models.ForeignKey('Requirements', on_delete=models.CASCADE)
    # nice_to_have = models.ForeignKey('Requirements', on_delete=models.CASCADE)
    # publication_date = models.DateField()
    # last_publication_date = models.DateField()
    # removed = models.BooleanField()
    # removed_date = models.DateField()
    # source_type = models.CharField(max_length=250)
    # application_deadline = models.DateField()
    # number_of_vacancies = models.IntegerField()
    # duration = models.CharField(max_length=250, verbose_name='Anställningsform')
    # timestamp = models.DateField(auto_now_add=True)
    # employment_type = models.ForeignKey('JobTechTaxonomyItem')
    headline = models.CharField(max_length=250, verbose_name='Title', unique=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Ort')
    url = models.URLField(unique=True)
    logo_url = models.URLField(unique=True)
    company = models.ForeignKey('Employer', on_delete=models.CASCADE, verbose_name='Företag')
    description = models.TextField(verbose_name='Beskrivning')
    timestamp = models.DateField(auto_now_add=True)
    occupation = models.ForeignKey('JobTechTaxonomyItem', on_delete=models.CASCADE, verbose_name='Branch')
    af_id = models.IntegerField(unique=True)

    class Meta:
        verbose_name = 'Tjänst'
        verbose_name_plural = 'Tjänster'

    def __str__(self):
        return self.headline
