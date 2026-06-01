from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderItem
from .forms import CheckoutForm
from cart.models import Cart, CartItem


@login_required
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
    except Cart.DoesNotExist:
        cart = None
        cart_items = []

    if not cart_items:
        messages.warning(request, 'Your cart is empty.')
        return redirect('store:product_list')

    form = CheckoutForm()
    context = {
        'form': form,
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def place_order(request):
    if request.method != 'POST':
        return redirect('orders:checkout')

    form = CheckoutForm(request.POST)
    if not form.is_valid():
        messages.error(request, 'Please correct the errors below.')
        return redirect('orders:checkout')

    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
    except Cart.DoesNotExist:
        messages.warning(request, 'Your cart is empty.')
        return redirect('store:product_list')

    if not cart_items:
        messages.warning(request, 'Your cart is empty.')
        return redirect('store:product_list')

    # Create order
    order = Order.objects.create(
        user=request.user,
        full_name=form.cleaned_data['full_name'],
        email=form.cleaned_data['email'],
        phone=form.cleaned_data['phone'],
        address=form.cleaned_data['address'],
        city=form.cleaned_data['city'],
        state=form.cleaned_data['state'],
        zipcode=form.cleaned_data['zipcode'],
        total_amount=cart.total_price,
        discount_amount=cart.discount_amount,
        coupon_code=cart.coupon.code if cart.coupon else '',
        payment_method=form.cleaned_data['payment_method'],
    )

    # Create order items
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            product_name=item.product.name,
            variant_details=item.variant_details,
            price=item.product.discount_price or item.product.price,
            quantity=item.quantity,
        )

    # Handle Payment Gateway
    if order.payment_method == 'online':
        return redirect('orders:payment_gateway', order_number=order.order_number)

    # For COD, complete the order
    order.status = 'confirmed'
    order.save()
    
    # Send Email Notification
    send_order_email(order, request)

    # Clear cart
    cart.coupon = None
    cart.save()
    cart_items.delete()

    messages.success(request, f'Order {order.order_number} placed successfully!')
    return redirect('orders:order_confirmation', order_number=order.order_number)


@login_required
def payment_gateway(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    if order.is_paid:
        return redirect('orders:order_confirmation', order_number=order.order_number)
    
    context = {'order': order}
    return render(request, 'orders/payment.html', context)


@login_required
def process_payment(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    
    # Simulate a successful payment
    if request.method == 'POST':
        order.is_paid = True
        order.status = 'confirmed'
        order.save()
        
        # Clear Cart
        try:
            cart = Cart.objects.get(user=request.user)
            cart.coupon = None
            cart.save()
            cart.items.all().delete()
        except Cart.DoesNotExist:
            pass
            
        # Send Email Notification
        send_order_email(order, request)
        
        messages.success(request, 'Payment successful! Your order is confirmed.')
        return redirect('orders:order_confirmation', order_number=order.order_number)
        
    return redirect('orders:payment_gateway', order_number=order.order_number)


def send_order_email(order, request):
    subject = f'Order Confirmation - {order.order_number}'
    message = f'''
Hi {order.full_name},

Thank you for your order! Your order {order.order_number} has been confirmed.
Total Amount: ₹{order.total_amount}

We will notify you once it ships.

Thanks,
The AryaCart Team
    '''
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [order.email],
        fail_silently=True,
    )


@login_required
def order_confirmation(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'orders/order_confirmation.html', context)


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'orders/order_history.html', context)


@login_required
def order_detail(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'orders/order_detail.html', context)
