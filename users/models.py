from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    username = None
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email