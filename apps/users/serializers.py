from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    # IMPORTANT: Override to accept 'email' instead of default 'username'
    username_field = 'email'
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims to JWT
        token['username'] = user.username
        token['email'] = user.email
        
        return token
    
    def validate(self, attrs):
        # This will now accept 'email' and 'password' from the request
        data = super().validate(attrs)
        
        # Add extra info to response
        data['username'] = self.user.username
        data['email'] = self.user.email
        
        return data