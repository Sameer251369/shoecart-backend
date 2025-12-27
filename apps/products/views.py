from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.products.models import Product, Category
from apps.products.serializers import ProductSerializer, CategorySerializer


@method_decorator(cache_page(60 * 5), name='dispatch')
class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = (
            Product.objects
            .filter(is_active=True)
            .select_related('category')
            .prefetch_related('images')
        )

        search_query = self.request.query_params.get('search')
        category_name = self.request.query_params.get('category')

        if category_name:
            queryset = queryset.filter(category__name__iexact=category_name)

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        return queryset.order_by('-id')


@method_decorator(cache_page(60 * 10), name='dispatch')
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = (
        Product.objects
        .filter(is_active=True)
        .select_related('category')
        .prefetch_related('images')
    )
    serializer_class = ProductSerializer
