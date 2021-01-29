"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path


if os.getenv('DYNO'):
    DJANGO_HOST = 'production'
elif os.getenv('GITHUB_WORKFLOW'):
    DJANGO_HOST = 'testing'
else:
    DJANGO_HOST = 'development'




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

ALLOWED_HOSTS = []

# Application definition

if DJANGO_HOST != 'production':
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '2x$6a^ai+)@zp+sbypq2i_qjyh*6exi+mnb*8*d+llubwaciq4'  # local secret, exposing it to github

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

INSTALLED_APPS = [
    ## my apps
    'polls.apps.PollsConfig',
    'core.apps.CoreConfig',
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
    ## DJANGO internal
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

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

'''
#https://devcenter.heroku.com/articles/memcachier#django
if DJANGO_HOST == 'production':
    #use caching
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }
'''



WSGI_APPLICATION = 'mysite.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

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

LOGIN_REDIRECT_URL = '/polls'
LOGOUT_REDIRECT_URL = '/polls'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


## enable code conditional depending on the environment
if DJANGO_HOST == 'production':
    # if on prod environment (heroku) - see details:
    # https://stackoverflow.com/questions/9383450/how-can-i-detect-herokus-environment/20227148

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    import django_heroku
    django_heroku.settings(locals())

if DJANGO_HOST == 'testing':
    DATABASES = {
        'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'github_actions',
           'USER': 'postgres',
           'PASSWORD': 'postgres',
           'HOST': '127.0.0.1',
           'PORT': '5432',
        }
    }

if DJANGO_HOST == 'development':
    #TODO use env variables
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'mydjango',
            'USER': 'riggedCoinflip',
            'PASSWORD': 'Z6bnj6jkgtrPhzZz89',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }