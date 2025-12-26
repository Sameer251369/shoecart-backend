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
    # Nested serializers to show related data
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 
            'stock', 'is_active', 'category', 'images', 'thumbnail'
        ]

    def get_thumbnail(self, obj):
        # Safely get the first image URL for the frontend
        first_image = obj.images.first()
        if first_image and first_image.image:
            return first_image.image.url
        return None