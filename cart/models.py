from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from authentication.models import User


class CartProduct(models.Model):
    user = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Итог', default=0)

    def save(self, *args, **kwargs):
        self.final_price = self.quantity * self.product.salesPrice
        super().save(*args, **kwargs)

    def str(self):
        return self.user


class Cart(models.Model):
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
