from django.db import models
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'price', 'categories')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


