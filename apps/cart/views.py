from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem

class AddToCartView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        # Logic to get user's cart (assuming Auth is set up)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, 
            product_id=product_id
        )
        
        if not created:
            cart_item.quantity += 1
            cart_item.save()
            
        return Response({"message": "Added to cart"}, status=status.HTTP_200_OK)