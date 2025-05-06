from rest_framework import viewsets
from .models import Product, Collection, Cart, CartItem, ProductImage
from .serializers import CollectionSerializer, ProductSerializer, CartSerializer, CartItemSerializer, ProductImageSerializer
from django.db.models import Prefetch

# Create your views here.


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related(
        'images').select_related('collection').all()
    serializer_class = ProductSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
