from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, CategoryListAPIView

urlpatterns = [
    # 1. List & Search: /api/products/
    # Handles ?search=... and ?category=...
    path("", ProductListAPIView.as_view(), name="product-list"), 
    
    # 2. Navbar Categories: /api/products/categories/
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    
    # 3. Product Details: /api/products/<id>/
    path("<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
]