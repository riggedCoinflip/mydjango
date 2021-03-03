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

IS_PRODUCTION = os.getenv("IS_PRODUCTION") == "true"
IS_GITHUB_WORKFLOW = os.getenv("GITHUB_WORKFLOW") == "true"
IS_DEVELOPMENT = os.getenv("DEVELOPMENT") == "true"

if IS_PRODUCTION:
    print(f"{IS_PRODUCTION=}")
    DEBUG = False
elif IS_GITHUB_WORKFLOW:
    print(f"{IS_GITHUB_WORKFLOW=}")
    DEBUG = False
elif IS_DEVELOPMENT:
    print(f"{IS_DEVELOPMENT=}")
    DEBUG = True
else:
    print("could not find the right environment. Script will now exit for safety")
    exit()

SECRET_KEY = os.getenv('SECRET_KEY')

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
    'settings.apps.SettingsConfig',
    'registration.apps.RegistrationConfig',

    ##################
    # Other packages #
    ##################
    # show better error messages
    # https://github.com/boxed/django-fastdev
    'django_fastdev',
    # allow for more detailed and complex views
    # https://github.com/AndrewIngram/django-extra-views/
    'extra_views',
    # allow for forms that already use bootstrap classes
    # https://github.com/django-crispy-forms/django-crispy-forms
    'crispy_forms',
    # bootstrap 5 for crispy forms
    # https://github.com/django-crispy-forms/crispy-bootstrap5
    'crispy_bootstrap5',
    # template filters for easy math
    # https://pypi.org/project/django-mathfilters/
    'mathfilters',
    # enable image processing
    # https://github.com/matthewwithanm/django-imagekit
    'imagekit',
    # serve media files for prod
    # https://github.com/etianen/django-s3-storage
    'django_s3_storage',
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


# Media files, served by ASW S3 on prod - on dev, this solution is used:
# https://docs.djangoproject.com/en/3.1/howto/static-files/#serving-static-files-during-development

USES_S3 = os.getenv("USES_S3") == "true"

if USES_S3:
    DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage"
    STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
    AWS_REGION = "eu-central-1"
    AWS_ACCESS_KEY_ID = os.getenv("AMAZON_S3_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AMAZON_S3_SECRET_ACCESS_KEY")
    # The optional AWS session token to use.
    AWS_SESSION_TOKEN = ""
    # The name of the bucket to store files in.
    AWS_S3_BUCKET_NAME = os.getenv("AMAZON_S3_BUCKET_NAME")
    AWS_S3_BUCKET_NAME_STATIC = os.getenv("AMAZON_S3_BUCKET_NAME")
    # How to construct S3 URLs ("auto", "path", "virtual").
    AWS_S3_ADDRESSING_STYLE = "auto"
    # The full URL to the S3 endpoint. Leave blank to use the default region URL.
    AWS_S3_ENDPOINT_URL = ""
    # A prefix to be applied to every stored file. This will be joined to every filename using the "/" separator.
    AWS_S3_KEY_PREFIX = "media/"
    AWS_S3_KEY_PREFIX_STATIC = "static/"
    # Whether to enable authentication for stored files. If True, then generated URLs will include an authentication
    # token valid for `AWS_S3_MAX_AGE_SECONDS`. If False, then generated URLs will not include an authentication token,
    # and their permissions will be set to "public-read".
    AWS_S3_BUCKET_AUTH = False
    # How long generated URLs are valid for. This affects the expiry of authentication tokens if `AWS_S3_BUCKET_AUTH`
    # is True. It also affects the "Cache-Control" header of the files.
    # Important: Changing this setting will not affect existing files.
    AWS_S3_MAX_AGE_SECONDS = 60 * 60 * 24 * 30  # 1 month
    # A URL prefix to be used for generated URLs. This is useful if your bucket is served through a CDN.
    AWS_S3_PUBLIC_URL = ""
    # If True, then files will be stored with reduced redundancy. Check the S3 documentation and make sure you
    # understand the consequences before enabling.
    # Important: Changing this setting will not affect existing files.
    AWS_S3_REDUCED_REDUNDANCY = False
    # The Content-Disposition header used when the file is downloaded. This can be a string, or a function taking a
    # single `name` argument.
    # Important: Changing this setting will not affect existing files.
    AWS_S3_CONTENT_DISPOSITION = ""
    # The Content-Language header used when the file is downloaded. This can be a string, or a function taking a
    # single `name` argument.
    # Important: Changing this setting will not affect existing files.
    # ISO-639
    AWS_S3_CONTENT_LANGUAGE = "en"
    # A mapping of custom metadata for each file. Each value can be a string, or a function taking a
    # single `name` argument.
    # Important: Changing this setting will not affect existing files.
    AWS_S3_METADATA = {}
    # If True, then files will be stored using AES256 server-side encryption.
    # If this is a string value (e.g., "aws:kms"), that encryption type will be used.
    # Otherwise, server-side encryption is not be enabled.
    # Important: Changing this setting will not affect existing files.
    AWS_S3_ENCRYPT_KEY = False
    # The AWS S3 KMS encryption key ID (the `SSEKMSKeyId` parameter) is set from this string if present.
    # This is only relevant if AWS S3 KMS server-side encryption is enabled (above).
    AWS_S3_KMS_ENCRYPTION_KEY_ID = ""
    # If True, then text files will be stored using gzip content encoding. Files will only be gzipped if their
    # compressed size is smaller than their uncompressed size.
    # Important: Changing this setting will not affect existing files.
    AWS_S3_GZIP = True
    # The signature version to use for S3 requests.
    AWS_S3_SIGNATURE_VERSION = None
    # If True, then files with the same name will overwrite each other. By default it's set to False to have
    # extra characters appended.
    AWS_S3_FILE_OVERWRITE = False
else:
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# Database
if IS_PRODUCTION:
    django_heroku.settings(locals())
else:
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
