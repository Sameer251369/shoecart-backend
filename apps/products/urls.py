# apps/products/urls.py
from django.urls import path
# Use the full path from the project root
from apps.products.views import (
    ProductListAPIView, 
    ProductDetailAPIView, 
    CategoryListAPIView
)

urlpatterns = [
    path("", ProductListAPIView.as_view(), name="product-list"),
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
]