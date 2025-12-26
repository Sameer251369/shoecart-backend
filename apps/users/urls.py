from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import register_user, EmailTokenObtainPairView

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', EmailTokenObtainPairView.as_view(), name='login'),  # ADD THIS
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # ADD THIS
]