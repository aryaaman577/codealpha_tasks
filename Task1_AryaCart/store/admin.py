from django.contrib import admin
from .models import Category, Product, ProductImage, WatchHistory, ProductVariant, Review, Wishlist


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'category', 'price', 'discount_price',
        'stock', 'is_available', 'is_featured', 'created_at',
    ]
    list_filter = ['is_available', 'is_featured', 'category', 'created_at']
    list_editable = ['price', 'discount_price', 'stock', 'is_available', 'is_featured']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    inlines = [ProductImageInline]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']


admin.site.register(ProductVariant)
admin.site.register(Review)
admin.site.register(Wishlist)
@admin.register(WatchHistory)
class WatchHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'viewed_at']
    list_filter = ['viewed_at']
