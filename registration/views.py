from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from activate.verifiy import send_verification_email
from users.forms import CustomUserCreationForm
from users.models import User


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('welcome')

    def form_valid(self, form):
        self.object = form.save()
        user = self.object
        send_verification_email(user, self.request)
        # TODO messages.info(request, "Thanks for registering. You are now logged in.")
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'],
                            )
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class WelcomeView(generic.TemplateView):
    template_name = 'registration/welcome.html'
