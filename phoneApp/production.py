import os
from .settings import *
from .settings import BASE_DIR

SECRET_KEY = os.environ['SECRET']
STRIPE_PUBLIC_KEY = os.environ['STRIPE_PUBLIC_KEY']
STRIPE_SECRET_KEY = os.environ['STRIPE_SECRET_KEY']
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'spoofed.azurewebsites.net', 'youbeenspoofed.com', 'https://www.spoofed.azurewebsites.net', 'https://www.youbeenspoofed.com']
CSRF_TRUSTED_ORIGINS = ['https://www.spoofed.azurewebsites.net', 'https://www.youbeenspoofed.com']
DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Add this line
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'DB_Admin',
        'PASSWORD': 'TeleTech320$',
        'HOST': 'postgresql-server.postgres.database.azure.com',
        'PORT': '5432',
    }
}


