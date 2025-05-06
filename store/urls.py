from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CollectionViewSet, ProductViewSet, ProductImageViewSet, CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r'collections', CollectionViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
