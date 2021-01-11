from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic


# Create your views here.

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    model = User
    form_class = UserCreationForm
