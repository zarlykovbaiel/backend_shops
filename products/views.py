from coreapi.auth import TokenAuthentication, SessionAuthentication
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from products.serializers import ProductSerializer, ProductListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from products.models import Product


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['title', ]


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = (TokenAuthentication, SessionAuthentication)


class ProductUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = (TokenAuthentication, SessionAuthentication)