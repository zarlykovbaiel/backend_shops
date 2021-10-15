from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *


class CartProductView(ListAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer


class CartProductCreateView(CreateAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer


class CartProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer


class CartView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartCreateView(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
