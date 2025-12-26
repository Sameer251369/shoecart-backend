from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from django.db.models import Q

# Use absolute imports to prevent 500/Import errors on Render
from apps.products.models import Product, Category
from apps.products.serializers import ProductSerializer, CategorySerializer

class ProductListAPIView(APIView):
    def get(self, request):
        search_query = request.query_params.get('search', None)
        category_name = request.query_params.get('category', None)
        
        # Start with all active products
        products = Product.objects.filter(is_active=True)
        
        # Case-insensitive category filtering
        if category_name:
            products = products.filter(category__name__iexact=category_name)
            
        # Search by name or description
        if search_query:
            products = products.filter(
                Q(name__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        
        # Optimization to reduce database hits (N+1 problem)
        products = products.select_related('category').prefetch_related('images')
            
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer