from rest_framework import filters
from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Product, Collection, Cart, CartItem, ProductImage, Order
from .serializers import CollectionSerializer, ProductSerializer, CartSerializer, CartItemSerializer, ProductImageSerializer, AddCartItemSerializer, UpdateCartItemSerializer, OrderCreateSerializer, OrderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .pagination import BasicPagination

# Create your views here.


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related(
        'images').select_related('collection').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['collection']
    ordering_fields = ['price', 'name', 'date_created']
    search_fields = ['name', 'description', 'collection__name']
    ordering = ['-date_created']
    pagination_class = BasicPagination


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensures the user always has a cart
        Cart.objects.get_or_create(user=self.request.user)
        return Cart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        return CartSerializer

    @action(detail=False, methods=['get'])
    def me(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)


class CartItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensures the cart exists before accessing items
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return {'cart_id': cart.id}


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = BasicPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.order_by('-date_created').all()
        return Order.objects.filter(user=user)

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return OrderSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    @action(detail=False, methods=['get'])
    def me(self, request):
        orders = Order.objects.filter(user=request.user).all()
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)
