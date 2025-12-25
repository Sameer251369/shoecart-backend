# apps/orders/serializers.py
from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    # Assuming your Product model has an 'images' relationship
    image = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['product', 'product_name', 'price', 'quantity', 'image']

    def get_image(self, obj):
        first_image = obj.product.images.first()
        if first_image:
            return f"http://127.0.0.1:8000{first_image.image.url}"
        return None

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    formatted_date = serializers.DateTimeField(source='created_at', format="%B %d, %Y", read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'total_amount', 'is_paid', 'status', 'created_at', 'formatted_date', 'items']