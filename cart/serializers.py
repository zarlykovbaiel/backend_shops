from rest_framework import serializers
from .models import *


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'