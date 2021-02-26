from django.urls import path

from .views import VerifyView, VerifyFailedView, VerifyUserRedirectView, VerifySucceededView, EMailSentView

app_name = 'activate'
urlpatterns = [
    path('', VerifyView.as_view(), name='verify'),
    path('check_email', EMailSentView.as_view(), name='email_sent'),
    path('<username>/<token>/', VerifyUserRedirectView.as_view(), name='verify_link'),
    path('success', VerifySucceededView.as_view(), name='verify_succeeded'),
    path('failed', VerifyFailedView.as_view(), name='verify_failed'),
]