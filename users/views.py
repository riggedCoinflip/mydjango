from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from activate.verifiy import send_verification_email
from .forms import CustomUserCreationForm
from .models import User


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        self.object = form.save()
        user = self.object


        send_verification_email(user, self.request)

        return HttpResponseRedirect(self.get_success_url())


# TODO passwordResetForm


class UserView(generic.DetailView):
    template_name = 'users/user.html'
    model = User

    def get_object(self, queryset=None):
        return get_object_or_404(User, username=self.kwargs['username'])
