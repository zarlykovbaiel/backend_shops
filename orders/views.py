from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import Order


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
