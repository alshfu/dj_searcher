from django.db import models
from transliterate import slugify

class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ort', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Ort'
        verbose_name_plural = 'Ort'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.name))
        super().save(*args, **kwargs)