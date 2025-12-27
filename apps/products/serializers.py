from rest_framework import serializers
from apps.products.models import Product, Category, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'stock',
            'is_active',
            'category',
            'thumbnail',
            'images',
        ]

    def get_thumbnail(self, obj):
        """Get the first image URL or None"""
        # FIXED: Use .all() then .first() instead of [0]
        images = obj.images.all()
        if images.exists():
            return images.first().image.url
        return None