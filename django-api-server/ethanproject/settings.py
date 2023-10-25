"""
Django settings for ethanproject project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import json
import os
from pathlib import Path
from urllib import request
import dotenv
dotenv.load_dotenv()

DEBUG = os.environ.get('DEBUG')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['localhost']


# Cognito stuff
SECRET_KEY = os.environ.get("SECRET_KEY")
print("SECRET KEY", SECRET_KEY)
COGNITO_AWS_REGION = os.environ.get("COGNITO_AWS_REGION", default=None)
COGNITO_USER_POOL = os.environ.get("COGNITO_USER_POOL", default=None)
SOCIALACCOUNT_PROVIDERS_STR = os.environ.get('SOCIALACCOUNT_PROVIDERS')
print("SOCAL", SOCIALACCOUNT_PROVIDERS_STR)
SOCIALACCOUNT_PROVIDERS = json.loads(SOCIALACCOUNT_PROVIDERS_STR)
# Provide this value if `id_token` is used for authentication (it contains 'aud' claim).
# `access_token` doesn't have it, in this case keep the COGNITO_AUDIENCE empty
COGNITO_AUDIENCE = None
COGNITO_POOL_URL = (
    None  # will be set few lines of code later, if configuration provided
)

rsa_keys = {}
# To avoid circular imports, we keep this logic here.
# On django init we download jwks public keys which are used to validate jwt tokens.
# For now there is no rotation of keys (seems like in Cognito decided not to implement it)
if COGNITO_AWS_REGION and COGNITO_USER_POOL:
    COGNITO_POOL_URL = (
        f"https://cognito-idp.{COGNITO_AWS_REGION}.amazonaws.com/{COGNITO_USER_POOL}"
    )
    pool_jwks_url = COGNITO_POOL_URL + "/.well-known/jwks.json"
    jwks = json.loads(request.urlopen(pool_jwks_url).read())  # nosec B310
    rsa_keys = {key["kid"]: json.dumps(key) for key in jwks["keys"]}


# Application definition

INSTALLED_APPS = [
    'ethanapp',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #     'django.contrib.auth',
    # 'django.contrib.messages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # include the providers you want to enable:
    'allauth.socialaccount.providers.amazon_cognito',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'ethanproject.urls'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("core.api.permissions.DenyAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
    ),}

# COGNITO / JWT stuff
# Cognito stuff
COGNITO_AWS_REGION = os.environ.get("COGNITO_AWS_REGION", default=None)
COGNITO_USER_POOL = os.environ.get("COGNITO_USER_POOL", default=None)
# Provide this value if `id_token` is used for authentication (it contains 'aud' claim).
# `access_token` doesn't have it, in this case keep the COGNITO_AUDIENCE empty
COGNITO_AUDIENCE = None
COGNITO_POOL_URL = (
    None  # will be set few lines of code later, if configuration provided
)

rsa_keys = {}
# To avoid circular imports, we keep this logic here.
# On django init we download jwks public keys which are used to validate jwt tokens.
# For now there is no rotation of keys (seems like in Cognito decided not to implement it)
if COGNITO_AWS_REGION and COGNITO_USER_POOL:
    COGNITO_POOL_URL = (
        f"https://cognito-idp.{COGNITO_AWS_REGION}.amazonaws.com/{COGNITO_USER_POOL}"
    )
    pool_jwks_url = COGNITO_POOL_URL + "/.well-known/jwks.json"
    jwks = json.loads(request.urlopen(pool_jwks_url).read())  # nosec B310
    rsa_keys = {key["kid"]: json.dumps(key) for key in jwks["keys"]}

JWT_AUTH = {
    "JWT_PAYLOAD_GET_USERNAME_HANDLER": "core.utils.jwt.get_username_from_payload_handler",
    "JWT_DECODE_HANDLER": "core.utils.jwt.cognito_jwt_decode_handler",
    "JWT_PUBLIC_KEY": rsa_keys,
    "JWT_ALGORITHM": "RS256",
    "JWT_AUDIENCE": COGNITO_AUDIENCE,
    "JWT_ISSUER": COGNITO_POOL_URL,
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'ethanproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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



LOGIN_REDIRECT_URL = 'home'

ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SOCIALACCOUNT_STORE_TOKENS = True
