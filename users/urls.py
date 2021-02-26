from django.urls import path
from .views import UserView
app_name = 'users'
urlpatterns = [
    path('<username>/', UserView.as_view(), name='detail'),
]
