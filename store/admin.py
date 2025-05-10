from django.contrib import admin
from .models import Product, Collection, Cart, CartItem, ProductImage, Order
from django.urls import reverse
from django.utils.html import format_html
# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'image_preview']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return obj.image.url
        return None

    image_preview.short_description = 'Image Preview'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'collection', 'price', 'date_created')
    list_filter = ('collection', 'date_created')
    search_fields = ('name', 'description')
    list_select_related = ('collection',)
    inlines = [ProductImageInline]


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user__username", "cart_items_count",
                    "view_cart_items_link", "created_at")

    def cart_items_count(self, obj):
        return obj.items.count()
    cart_items_count.short_description = "Total Cart Items"

    def view_cart_items_link(self, obj):
        url = reverse("admin:store_cartitem_changelist") + \
            f"?cart__id__exact={obj.id}"
        return format_html('<a href="{}">View Cart Items</a>', url)
    view_cart_items_link.short_description = "Cart Items"


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product__name', 'quantity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
