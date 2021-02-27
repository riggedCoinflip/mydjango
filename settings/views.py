from django.shortcuts import reverse

# Create your views here.
from django.views import generic

from users.models import User
from .forms import SettingsUpdateForm


class SettingsView(generic.UpdateView):
    template_name = "settings/settings.html"
    form_class = SettingsUpdateForm
    model = User

    def get_queryset(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('index')  # redirect to self to stay on settings page
        # TODO use django messages framework to show message "changes saved"

    # TODO validate form
    #todo write settings.html
    #todo step 2: add the avatar image field