from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import SettingsView

app_name = 'settings'

urlpatterns = [
    path('', login_required(SettingsView.as_view()), name='index'),
]
