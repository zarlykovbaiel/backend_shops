from django.db import models
from authentication.models import User
from cart.models import Cart


class Delivery(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return f'delivery{self.name}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders_user')
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    # order_id = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL, null=True, related_name='orders_delivery')
    created = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'orders{self.id}'
