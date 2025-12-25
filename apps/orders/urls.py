from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create-order'),
    # Add this line below:
    path('my-orders/', views.get_user_orders, name='my-orders'),
]