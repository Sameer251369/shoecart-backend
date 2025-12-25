from django.contrib import admin
from .models import Order, OrderItem

# This allows you to edit OrderItems directly inside the Order page
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # Prevents showing extra empty rows
    readonly_fields = ('product', 'price', 'quantity') # Prevents accidental changes to old orders

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # What to show in the main list
    list_display = ('id', 'user', 'total_amount', 'is_paid', 'created_at')
    
    # Add filters on the right side
    list_filter = ('is_paid', 'created_at')
    
    # Add a search bar
    search_fields = ('user__username', 'stripe_payment_intent_id')
    
    # Attach the items to the bottom of the order
    inlines = [OrderItemInline]

# Optional: Register OrderItem separately if you want to see all sold items in one list
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'price')