from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxLengthValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Anchor


class User(AbstractUser):
    is_validated = models.BooleanField(default=False)
    email = models.EmailField('email address', blank=False, unique=True)
    about_text = models.TextField(max_length=1000, null=True, blank=True, validators=(MaxLengthValidator(1000),))
    github_name = models.CharField(max_length=100, null=True, blank=True, validators=(MaxLengthValidator(100),))
    avatar = ProcessedImageField(upload_to='users/avatars',
                                 processors=[
                                     ResizeToFill(width=400, height=400, anchor=Anchor.CENTER),
                                 ],
                                 default='users/avatars/default/default.jpg',
                                 format='JPEG',
                                 options={'quality': 90}
                                 )

    def __str__(self):
        return self.username