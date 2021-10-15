from django.urls import path
from .views import OrderListCreateView, OrderDetailView

urlpatterns = [
    path('order/list_create/', OrderListCreateView.as_view()),
    path('order/detail/<int:pk>', OrderDetailView.as_view())
]
