from rest_framework import serializers
from .models import Order, Delivery


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id', 'user', 'first_name', 'last_name', 'email',
            'created', 'total',
        )
        read_only_fields = (
            'total', 'created',
        )


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('name',)