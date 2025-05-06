from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')
    USERNAME_FIELD = ('email')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
