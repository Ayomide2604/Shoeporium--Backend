from .models import CustomUser, ProfileImage
from djoser.serializers import UserSerializer
from rest_framework import serializers


class ProfileImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProfileImage
        fields = ['id', 'user', 'image', 'image_url']
        read_only_fields = ['id', 'user', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None


class CustomUserSerializer(UserSerializer):
    profile_image = ProfileImageSerializer()

    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ['id', 'email', 'first_name',
                  'last_name', 'username', 'profile_image']
