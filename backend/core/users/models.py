import uuid
import json
import secrets


from django.contrib.auth.models import AbstractUser
from django.db import models

from users.manager import CustomUserManager



class UserRoles(models.TextChoices):
    ADMIN = 'ADMIN', ('Admin')
    GENERAL_USER = 'GENERAL_USER', ('General User')


def generate_shared_secret() -> str:
    return secrets.token_hex(16)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(unique=True, max_length=200)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    role = models.CharField(choices=UserRoles.choices, default=UserRoles.ADMIN, max_length=50, blank=False, null=False)
    shared_secret = models.CharField(blank=False, default=generate_shared_secret, max_length=100)
    has_used_default_password = models.BooleanField(default=False)
    password_updated_at = models.DateTimeField(blank=True, null=True)
    registration_complete = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_code = models.UUIDField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'mobile_number']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
