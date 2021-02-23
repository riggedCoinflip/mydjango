# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_validated = models.BooleanField(default=False)
    email = models.EmailField('email address', blank=False, unique=True)

    def __str__(self):
        return self.username

