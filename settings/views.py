from django.shortcuts import render

# Create your views here.
from django.views import generic
from .forms import SettingsUpdateForm

class SettingsView(generic.UpdateView):
    template_name = "settings/settings.html"
    form_class = SettingsUpdateForm
    # TODO validate form
    #todo write settings.html
    #todo step 2: add the avatar image field