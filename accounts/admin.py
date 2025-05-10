from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ProfileImage
# Register your models here.


class ProfileImageInline(admin.TabularInline):
    model = ProfileImage
    extra = 1
    fields = ['image', 'image_preview']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return obj.image.url
        return None

    image_preview.short_description = 'Image Preview'


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    inlines = [ProfileImageInline]
