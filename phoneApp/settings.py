import os
#import environ
import dj_database_url
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

# Define BASE_DIR as the directory containing your manage.py file
BASE_DIR = Path(__file__).resolve().parent.parent

#env = environ.Env()
#environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Print the DATABASE_URL for debugging
print("DATABASE_URL:", os.getenv('DATABASE_URL'))
# Debug print statements
database_url = os.getenv('DATABASE_URL')
print(f"Loaded DATABASE_URL: {database_url}")

# Redirect to the home page after login
LOGIN_REDIRECT_URL = '/profile/'
LOGOUT_REDIRECT_URL = '/home/'
ACCOUNT_LOGOUT_ON_GET = True

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# Use environment variable for the secret key
SECRET_KEY = os.getenv('SECRET_KEY', 'n4^y3+mjbrkass$a@#r5ov!og!1a^xg1y^=#^5f178mxqk1l(a)')

# Check that the secret key is set
if not SECRET_KEY:
    raise ImproperlyConfigured("Set the SECRET_KEY environment variable")

# SECURITY WARNING: don't run with debug turned on in production!
# settings.py or production.py
STRIPE_PUBLIC_KEY = os.environ['STRIPE_PUBLIC_KEY']
STRIPE_SECRET_KEY = os.environ['STRIPE_SECRET_KEY']

DEBUG = True

SECURE_SSL_REDIRECT = True

# Use Secure Cookies
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Enable HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

CSRF_TRUSTED_ORIGINS = [
    'https://youbeenspoofed.com', 'https://spoofed.azurewebsites.net', 'https://www.spoofed.azurewebsites.net', 'https://www.youbeenspoofed.com'
]

# Add any other domains you trust
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'spoofed.azurewebsites.net', 'youbeenspoofed.com', 'https://www.spoofed.azurewebsites.net', 'https://www.youbeenspoofed.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',  # Add twitter provider
    'phoneApp.apps.PhoneAppConfig',
    'base.apps.BaseConfig',
    #'sslserver',
    'django_extensions', 
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v7.0',
    },
    'twitter': {
        'SCOPE': ['email'],
        'AUTH_PARAMS': {},
        'METHOD': 'oauth',
        'VERIFIED_EMAIL': True,
    }
}

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

ROOT_URLCONF = 'phoneApp.urls'

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
        },
    },
]

WSGI_APPLICATION = 'phoneApp.wsgi.application'

# Database
# Configure the database using dj_database_url
#DATABASES = {
#    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
#}
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

print("Parsed DATABASES:", DATABASES)

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/images/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
