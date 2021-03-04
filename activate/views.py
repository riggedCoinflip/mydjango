from base64 import urlsafe_b64decode
from binascii import Error as BASE64ERROR

from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from users.models import User


# Create your views here.
class VerifyUserRedirectView(generic.RedirectView):
    model = User

    @property
    def usertoken(self):
        return self.kwargs['token']

    def get_redirect_url(self, *args, **kwargs):
        try:
            user = User.objects.get(username=self.kwargs['username'])
        except ObjectDoesNotExist:
            print('User does not exist')
            return reverse('activate:verify_failed')
        if self.verify_token(user):
            return reverse('activate:verify_succeeded')
        else:
            return reverse('activate:verify_failed')

    def verify_token(self, user):
        try:
            decoded_usertoken = urlsafe_b64decode(self.usertoken).decode('utf-8')
        except BASE64ERROR:
            return False

        if user:
            if default_token_generator.check_token(user, decoded_usertoken):
                self.activate_user(user)
                return True
        return False

    @staticmethod
    def activate_user(user):
        user.is_validated = True
        user.last_login = timezone.now()
        user.save()


#TODO make login required
class VerifyView(generic.TemplateView):
    template_name = 'activate/verify.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['failed'] = False
        return context


class VerifyFailedView(generic.TemplateView):
    template_name = 'activate/verify.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['failed'] = True
        return context


class VerifySucceededView(generic.TemplateView):
    template_name = 'activate/verification_succeeded.html'


class EMailSentView(generic.TemplateView):
    template_name = 'activate/verification_mail_sent.html'
