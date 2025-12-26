from rest_framework import serializers
from .models import Product, Category, ProductImage

# 1. Define Category first
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

# 2. Define Image second
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_feature']

# 3. Define Product LAST (because it uses the two above)
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'is_active', 'images', 'category', 'thumbnail']

    def get_thumbnail(self, obj):
        # Using .first() is safe even if images don't exist
        first_image = obj.images.filter(is_feature=True).first() or obj.images.first()
        if first_image and hasattr(first_image, 'image') and first_image.image:
            return first_image.image.url
        return None