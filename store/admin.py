from django.contrib import admin
from .models import Product, Collection
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'collection', 'price', 'date_created')
    list_filter = ('collection', 'date_created')
    search_fields = ('name', 'description')
    list_select_related = ('collection',)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_count')
    search_fields = ('name',)
