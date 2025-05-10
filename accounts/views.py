from django.shortcuts import render
from .models import ProfileImage
from .serializers import ProfileImageSerializer
from rest_framework import viewsets
# Create your views here.


class ProfileImageViewSet(viewsets.ModelViewSet):
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer
