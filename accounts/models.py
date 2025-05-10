from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')
    USERNAME_FIELD = ('email')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'


class ProfileImage(models.Model):
    user = models.OneToOneField(
        CustomUser, related_name='profile_image', on_delete=models.CASCADE)
    image = CloudinaryField('profile_image')

    def __str__(self):
        return f"Image for {self.user.email}"
