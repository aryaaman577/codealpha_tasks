from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product_name', 'price', 'quantity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'full_name', 'total_amount', 'status', 'is_paid', 'created_at']
    list_filter = ['status', 'is_paid', 'created_at']
    list_editable = ['status', 'is_paid']
    search_fields = ['order_number', 'full_name', 'email']
    inlines = [OrderItemInline]
    readonly_fields = ['order_number']
