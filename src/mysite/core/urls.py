from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('signup', views.SignupView.as_view(), name='signup'),
]
