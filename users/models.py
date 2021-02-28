# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxLengthValidator

class User(AbstractUser):
    is_validated = models.BooleanField(default=False)
    email = models.EmailField('email address', blank=False, unique=True)
    about_text = models.TextField(max_length=1000, null=True, blank=True, validators=(MaxLengthValidator(1000),))
    github_name = models.CharField(max_length=100, null=True, blank=True, validators=(MaxLengthValidator(100),))
    avatar = models.ImageField(upload_to='users/avatars', default='users/avatars/default/default.png')

    def __str__(self):
        return self.username

