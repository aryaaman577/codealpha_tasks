from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Product, Category, WatchHistory, Review, Wishlist, ProductVariant


def home(request):
    featured_products = Product.objects.filter(
        is_featured=True, is_available=True
    )[:8]
    latest_products = Product.objects.filter(is_available=True)[:8]
    categories = Category.objects.all()
    context = {
        'featured_products': featured_products,
        'latest_products': latest_products,
        'categories': categories,
    }
    return render(request, 'store/home.html', context)


def product_list(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()

    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    # Filter by price range
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Sorting
    sort = request.GET.get('sort')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    elif sort == 'name':
        products = products.order_by('name')

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'store/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    gallery = product.images.all()
    related_products = Product.objects.filter(
        category=product.category, is_available=True
    ).exclude(id=product.id)[:4]

    # Check wishlist status
    in_wishlist = False
    if request.user.is_authenticated:
        WatchHistory.objects.update_or_create(
            user=request.user,
            product=product,
        )
        in_wishlist = Wishlist.objects.filter(user=request.user, product=product).exists()

    reviews = product.reviews.all()
    variants = product.variants.all()

    context = {
        'product': product,
        'gallery': gallery,
        'related_products': related_products,
        'reviews': reviews,
        'variants': variants,
        'in_wishlist': in_wishlist,
    }
    return render(request, 'store/product_detail.html', context)

@login_required
def add_review(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        rating = request.POST.get('rating', 5)
        comment = request.POST.get('comment', '')
        
        Review.objects.update_or_create(
            user=request.user,
            product=product,
            defaults={'rating': rating, 'comment': comment}
        )
        messages.success(request, 'Your review has been submitted!')
        return HttpResponseRedirect(product.get_absolute_url())
    return HttpResponseRedirect(reverse('store:home'))

@login_required
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        wishlist_item.delete()
        messages.info(request, f'{product.name} removed from your wishlist.')
    else:
        messages.success(request, f'{product.name} added to your wishlist!')
        
    # Redirect back to the page the user came from
    next_url = request.META.get('HTTP_REFERER', product.get_absolute_url())
    return HttpResponseRedirect(next_url)

@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, 'store/wishlist.html', context)


def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.none()
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query),
            is_available=True,
        )
    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'store/search.html', context)


@login_required
def watch_history(request):
    history = WatchHistory.objects.filter(user=request.user).select_related(
        'product'
    )
    context = {
        'history': history,
    }
    return render(request, 'store/watch_history.html', context)


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(
        category=category, is_available=True
    )

    sort = request.GET.get('sort')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    elif sort == 'name':
        products = products.order_by('name')

    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'store/category_products.html', context)
