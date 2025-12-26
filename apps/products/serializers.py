# serializers.py
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    # Add a flat field for the first image to simplify frontend access
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'is_active', 'images', 'category', 'thumbnail']

    def get_thumbnail(self, obj):
        first_image = obj.images.first()
        if first_image and first_image.image:
            return first_image.image.url
        return None