from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.PositiveIntegerField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=255, null=True, blank=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user:
            return f'Cart of {self.user.username}'
        return f'Cart (session: {self.session_key})'

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())

    @property
    def subtotal(self):
        return sum(item.subtotal for item in self.items.all())
        
    @property
    def discount_amount(self):
        if self.coupon and self.coupon.active:
            return (self.subtotal * self.coupon.discount_percentage) / 100
        return 0
        
    @property
    def total_price(self):
        return self.subtotal - self.discount_amount


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant_details = models.CharField(max_length=255, blank=True)  # Store "Size: M, Color: Red"
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['cart', 'product', 'variant_details']

    def __str__(self):
        return f'{self.quantity}x {self.product.name} {self.variant_details}'

    @property
    def subtotal(self):
        return self.product.price * self.quantity
