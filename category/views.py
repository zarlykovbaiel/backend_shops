from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializers
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class CategoryCreateView(CreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = (TokenAuthentication, SessionAuthentication)


class CategoryUpdateView(RetrieveUpdateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = (TokenAuthentication, SessionAuthentication)


class CategoryDeleteView(RetrieveDestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = (TokenAuthentication, SessionAuthentication)


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    authentication_classes = (TokenAuthentication, SessionAuthentication)
