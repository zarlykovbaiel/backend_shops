from django.db import models
from category.models import Category


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product/images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    salesPrice = models.DecimalField(max_digits=10, decimal_places=2)
    is_publish = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products_category')

    def __str__(self):
        return self.title