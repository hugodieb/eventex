from django.db import models

class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    website = models.URLField('website')
    photo = models.URLField('foto')
    description = models.TextField('descrição')

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'