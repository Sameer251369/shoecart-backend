from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from django.db.models import Q # For search logic

from .models import Product, Category # Make sure you have a Category model
from .serializers import ProductSerializer, CategorySerializer # Create a CategorySerializer
class ProductListAPIView(APIView):
    def get(self, request):
        search_query = request.query_params.get('search', None)
        category_name = request.query_params.get('category', None) # Renamed for clarity
        
        products = Product.objects.filter(is_active=True)
        
        # FIX: Filter by name (case-insensitive) instead of slug
        if category_name:
            products = products.filter(category__name__iexact=category_name)
            
        if search_query:
            products = products.filter(
                Q(name__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        
        # Optimization: Add select_related and prefetch_related here too!
        products = products.select_related('category').prefetch_related('images')
            
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# NEW: Add this so the Navbar can fetch categories
class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer