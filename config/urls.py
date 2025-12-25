from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Import the JWT views and your custom registration view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.users.views import register_user 
from apps.users.views import EmailTokenObtainPairView# Make sure this function exists in apps/users/views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include('apps.products.urls')),
    path('api/token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # --- Authentication Routes ---
    # This is for Login (returns the 'access' token)
  
    # This allows the frontend to refresh the login session
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # This is for Registering a new user
    path('api/register/', register_user, name='register'),
    
    # --- Orders/Payments ---
    path('api/orders/', include('apps.orders.urls')),
]

# THIS LINE IS CRITICAL FOR IMAGES TO SHOW
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)