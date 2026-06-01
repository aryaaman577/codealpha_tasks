from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Cart, CartItem, Coupon
from store.models import Product


def _get_cart(request):
    """Get or create cart for current user/session."""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key, user=None)
    return cart


def cart_view(request):
    cart = _get_cart(request)
    items = cart.items.select_related('product').all()
    context = {
        'cart': cart,
        'items': items,
    }
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_available=True)
    cart = _get_cart(request)
    
    variant_details = ""
    if request.method == 'POST':
        size = request.POST.get('size')
        color = request.POST.get('color')
        parts = []
        if size: parts.append(f"Size: {size}")
        if color: parts.append(f"Color: {color}")
        if parts:
            variant_details = ", ".join(parts)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, 
        product=product, 
        variant_details=variant_details
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f'{product.name} {"("+variant_details+")" if variant_details else ""} added to cart!')
    next_url = request.GET.get('next', request.META.get('HTTP_REFERER', '/'))
    return redirect(next_url)


def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated.')
        else:
            cart_item.delete()
            messages.info(request, 'Item removed from cart.')
    return redirect('cart:cart_view')


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.info(request, f'{product_name} removed from cart.')
    return redirect('cart:cart_view')


def apply_coupon(request):
    if request.method == 'POST':
        code = request.POST.get('coupon_code')
        cart = _get_cart(request)
        try:
            coupon = Coupon.objects.get(
                code__iexact=code,
                active=True,
                valid_from__lte=timezone.now(),
                valid_to__gte=timezone.now()
            )
            cart.coupon = coupon
            cart.save()
            messages.success(request, f'Coupon {code} applied successfully!')
        except Coupon.DoesNotExist:
            cart.coupon = None
            cart.save()
            messages.error(request, 'Invalid or expired coupon code.')
            
    return redirect('cart:cart_view')
