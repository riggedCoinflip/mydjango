from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from .models import User


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('core:index')
