from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # This gets the standard token (usually just user_id)
        token = super().get_token(user)

        # ADD THIS LINE: This puts the 'username' inside the encrypted JWT
        token['username'] = user.username
        
        return token