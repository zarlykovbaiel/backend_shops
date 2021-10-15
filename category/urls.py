from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, CategoryDetailView

urlpatterns = [
    path('category/list', CategoryListView.as_view()),
    path('category/create', CategoryCreateView.as_view()),
    path('category/update/<int:pk>', CategoryUpdateView.as_view()),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view()),
    path('category/detail/<int:pk>', CategoryDetailView.as_view()),
]
