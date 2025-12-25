from rest_framework import serializers
from .models import Product, ProductImage, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text']

    def get_image(self, obj):
        if obj.image:
            return f"http://127.0.0.1:8000{obj.image.url}"
        return None

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    # This allows the frontend to see the category name/slug easily
    category = CategorySerializer(read_only=True) 

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'is_active', 'images', 'category']