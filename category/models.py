from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='nazvanie')
    slug = models.SlugField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'kategorii'

    def __str__(self):
        return self.title



