from django.urls import path
from .views import HomeView, ImpressumView

app_name = 'core'
urlpatterns = [
    #home
    path('', HomeView.as_view(), name='index'),
    #legal
    path('legal/', ImpressumView.as_view(), name='impressum'),
]
