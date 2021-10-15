from django.urls import path
from .views import *


urlpatterns = [
    path('products/list', ProductListView.as_view()),
    path('products/create', ProductCreateView.as_view())
]