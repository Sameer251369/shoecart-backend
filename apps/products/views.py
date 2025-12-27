from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.products.models import Product, Category
from apps.products.serializers import ProductSerializer, CategorySerializer


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    # Disable pagination for this view specifically
    pagination_class = None

    def get_queryset(self):
        queryset = (
            Product.objects
            .filter(is_active=True)
            .select_related('category')
            .prefetch_related('images')
        )

        search_query = self.request.query_params.get('search')
        category_slug = self.request.query_params.get('category')  # Changed from category_name

        # Filter by category slug (matches what frontend sends)
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        # Search in name and description
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        return queryset.order_by('-id')

    def list(self, request, *args, **kwargs):
        """Override to add better error handling"""
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Disable pagination for categories
    pagination_class = None


class ProductDetailAPIView(RetrieveAPIView):
    queryset = (
        Product.objects
        .filter(is_active=True)
        .select_related('category')
        .prefetch_related('images')
    )
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        """Override to add better error handling"""
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(
                {'error': 'Product not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )