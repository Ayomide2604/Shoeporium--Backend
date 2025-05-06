from rest_framework.serializers import ModelSerializer
from .models import Product, Collection, Cart, CartItem


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'product_count']


class ProductSerializer(ModelSerializer):
    collection = CollectionSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'collection',
                  'price', 'description', 'date_created']


class CartItemSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CartSerializer(ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'user', 'items']
