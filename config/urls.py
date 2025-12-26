from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView
from apps.users.views import register_user, EmailTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Products API (/api/products/ and /api/products/categories/)
    path('api/products/', include('apps.products.urls')),
    
    # Orders API (/api/orders/)
    path('api/orders/', include('apps.orders.urls')),

    # Auth Routes
    path('api/token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', register_user, name='register'),
]

# Serving media files during local development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)