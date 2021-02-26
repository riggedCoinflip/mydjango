from pathlib import Path

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template import Template, Context
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode

from users.models import User


def send_verification_email(user: User, request):
    # requires a request to create the uri
    token = urlsafe_base64_encode(str(default_token_generator.make_token(user)).encode('utf-8'))

    link = request.build_absolute_uri(
        reverse('activate:verify_link', kwargs={'username': user.username, 'token': token}))

    parent = Path(__file__).resolve().parent
    with open(parent / 'templates/activate/email_templates/email_verification_body.txt') as plain_message, \
            open(parent / 'templates/activate/email_templates/email_verification_body.html') as html_message:
        context = Context(
            {
                'user': user,
                'link': link
            }
        )

        rendered_plain_message = Template(plain_message.read()).render(context)
        rendered_html_message = Template(html_message.read()).render(context)
        send_mail(
            subject='Your registration is almost complete',
            message=rendered_plain_message,
            html_message=rendered_html_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False
        )
