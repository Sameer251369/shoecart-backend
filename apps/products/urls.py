from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, CategoryListAPIView

urlpatterns = [
    # This matches: /api/products/
    path("", ProductListAPIView.as_view(), name="product-list"), 
    
    # This matches: /api/products/categories/
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    
    # This matches: /api/products/1/
    path("<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
]