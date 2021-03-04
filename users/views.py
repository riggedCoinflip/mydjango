from django.shortcuts import get_object_or_404
from django.views import generic

from .models import User


class UserView(generic.DetailView):
    template_name = 'users/user.html'
    model = User

    def get_object(self, queryset=None):
        return get_object_or_404(User, username=self.kwargs['username'])

# TODO passwordResetForm