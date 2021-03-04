from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # what does this line do exactly?
    form = CustomUserChangeForm  # what does this line do exactly?
    model = User
    list_display = ['email', 'username']

    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2',),
        }),
    )
    fieldsets = UserAdmin.fieldsets + (
        ('confirmed_email', {'fields': ('is_validated',)}),
        ('Profile Picture', {'fields': ('avatar',)}),
    )

    list_filter = UserAdmin.list_filter + ('is_validated',)


admin.site.register(User, CustomUserAdmin)
