from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('polls:index')

class ImpressumView(generic.TemplateView):
    template_name = 'legal/impressum.html'
