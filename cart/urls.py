from django.urls import path
from .views import *

urlpatterns=[
    path('cart/product/list/', CartProductView.as_view()),
    path('cart/product/create/', CartProductCreateView.as_view()),
    path('cart/product/detail/<int:pk>', CartProductDetailView.as_view()),
    path('cart/list/', CartView.as_view()),
    path('cart/create/', CartCreateView.as_view()),
    path('cart/detail/<int:pk>', CartDetailView.as_view())
]