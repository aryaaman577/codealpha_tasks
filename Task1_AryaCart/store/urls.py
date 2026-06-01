from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/add-review/', views.add_review, name='add_review'),
    path('product/<int:product_id>/toggle-wishlist/', views.toggle_wishlist, name='toggle_wishlist'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('search/', views.search, name='search'),
    path('watch-history/', views.watch_history, name='watch_history'),
    path('wishlist/', views.wishlist_view, name='wishlist_view'),
]
