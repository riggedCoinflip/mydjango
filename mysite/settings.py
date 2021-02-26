"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from sys import exit
from pathlib import Path
from dotenv import load_dotenv
import django_heroku

load_dotenv()

#delete later again
[print(f'{key}:{value}') for key, value in os.environ.items()]
if os.getenv('PRODUCTION'):
    print("env found: prod")
    DJANGO_HOST = 'production'
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
elif os.getenv('GITHUB_WORKFLOW'):
    print("env found: github_workflow")
    DJANGO_HOST = 'testing'
    SECRET_KEY = 'u0&rixjzwlb76=sob2d1w8hf^7ivm7tsx#lk9_9d&pyl+gm!=a'
    # different key than on prod, exposing it is no security risk
    DEBUG = False
elif os.getenv('DEVELOPMENT'):
    print("env found: dev")
    DJANGO_HOST = 'development'
    SECRET_KEY = 'u0&rixjzwlb76=sob2d1w8hf^7ivm7tsx#lk9_9d&pyl+gm!=a'
    # different key than on prod, exposing it is no security risk
    DEBUG = True
else:
    print("could not find the right environment. Script will now exit for safety")
    exit()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

ALLOWED_HOSTS = []  # managed by django_heroku for prod

# Application definition

INSTALLED_APPS = [
    ## my apps
    'polls.apps.PollsConfig',
    'core.apps.CoreConfig',
    'aoc.apps.AOCConfig',  # advent of code
    'users.apps.UsersConfig',
    'activate.apps.ActivateConfig',
    ## other repos
    # https://github.com/boxed/django-fastdev
    'django_fastdev',
    # https://github.com/AndrewIngram/django-extra-views/
    'extra_views',
    # https://github.com/django-crispy-forms/django-crispy-forms
    'crispy_forms',
    # https://github.com/django-crispy-forms/crispy-bootstrap5
    'crispy_bootstrap5',
    # https://pypi.org/project/django-mathfilters/
    'mathfilters',
    # DJANGO INTERNAL
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

####################
### crispy_forms ###
####################
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'filters': 'templatetags.filters',
            },
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'users.User'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LOGIN_REDIRECT_URL = 'core:index'
LOGOUT_REDIRECT_URL = 'core:index'

# auth
PASSWORD_RESET_TIMEOUT = 60 * 60  # 1 hour

# email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('SMTP_HOST')
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.getenv('EMAIL_NOREPLY_USERNAME')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_NOREPLY_PASSWORD')



# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Database
if DJANGO_HOST != 'production':  # negation might be confusing, but is safer imo
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DATABASE_NAME'),
            'USER': os.getenv('DATABASE_USER'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD'),
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
else:
    django_heroku.settings(locals())
