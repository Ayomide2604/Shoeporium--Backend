from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileImageViewSet

router = DefaultRouter()
router.register(r'profile-images', ProfileImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
