from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import EmailTokenObtainPairSerializer
# ... your other imports
from .serializers import EmailTokenObtainPairSerializer



User = get_user_model()

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_user(request):
    data = request.data
    # Extract data from the React frontend
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')

    # Validation: Since email is your USERNAME_FIELD, it is mandatory
    if not email or not password or not username:
        return Response(
            {'detail': 'Email, Username, and Password are all required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Check if email (your new primary identifier) already exists
        if User.objects.filter(email=email).exists():
            return Response({'detail': 'A user with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create user: Note that for AbstractUser with email as USERNAME_FIELD,
        # we pass email as the first argument or explicitly.
        user = User.objects.create_user(
            email=email,
            username=username,
            password=password
        )
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'token': str(refresh.access_token),
            'email': user.email,
            'username': user.username
        }, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        print(f"Registration Error: {e}") # This will show in your Django terminal
        return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


