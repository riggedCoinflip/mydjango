from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from .views import HomeView, SignupView, ImpressumView

app_name = 'core'
urlpatterns = [
    #home
    path('', HomeView.as_view(), name='index'),
    #legal
    path('legal/', ImpressumView.as_view(), name='impressum'),
    #user
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
