from django.db import models
from transliterate import slugify

class Employer(models.Model):
    phone_number = models.CharField(max_length=50, verbose_name='Telefon nr:')
    email = models.EmailField(verbose_name='E-post')
    url= models.URLField(verbose_name='Url')
    organization_number = models.CharField(max_length=50, verbose_name='Org.nr')
    name = models.CharField(max_length=350, verbose_name='Nanm')
    slug = models.CharField(max_length=350)
    workplace = models.TextField(verbose_name='Adress')


    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.name))
        super().save(*args, **kwargs)

