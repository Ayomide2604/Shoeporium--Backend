from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CollectionViewSet, ProductViewSet, ProductImageViewSet,
    CartViewSet, CartItemViewSet, OrderViewSet
)

router = DefaultRouter()
router.register(r'collections', CollectionViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'carts', CartViewSet, basename='carts')
router.register(r'cart-items', CartItemViewSet, basename='cart-items')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
