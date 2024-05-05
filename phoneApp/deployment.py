import os
from .settings import *
from .settings import BASE_DIR

#SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = ['spoofed.azurewebsites.net', 'youbeenspoofed.com', 'https://www.spoofed.azurewebsites.net', 'https://www.youbeenspoofed.com']
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
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
#parameters = {tuple(pair.split('=')): pair.split('=')[1] for pair in connection_string.split(' ')}

#parameters = {pair.split('='):pair.split('=')[1] for pair in connection_string.split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'spoofed-database',
        'USER': 'lojpqrcenx',
        'PASSWORD': 'Sp808MLLfKTniy$q',
        'HOST': 'spoofed-server.postgres.database.azure.com',
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'}
    }
}