from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from apps.products.models import Product

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    user = request.user
    data = request.data
    try:
        order = Order.objects.create(
            user=user,
            total_amount=data.get('amount'),
            is_paid=True 
        )
        items = data.get('items', [])
        for item in items:
            product = Product.objects.get(id=item['product_id'])
            OrderItem.objects.create(
                order=order,
                product=product,
                price=product.price,
                quantity=item['quantity']
            )
            product.stock -= item['quantity']
            product.save()
        return Response({'message': 'Order created successfully', 'order_id': order.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    data = []
    
    for order in orders:
        items_data = []
        for item in order.items.all():
            # Get the first image of the product if it exists
            product_image = None
            if item.product.images.exists():
                product_image = item.product.images.first().image.url
            
            items_data.append({
                'name': item.product.name,
                'qty': item.quantity,
                'image': product_image # Now sending the image URL
            })

        data.append({
            'id': order.id,
            'total_amount': str(order.total_amount),
            'status': getattr(order, 'status', 'Confirmed'),
            'created_at': order.created_at.strftime("%b %d, %Y"),
            'items': items_data
        })
    return Response(data)