import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured

# Load environment variables from a .env file
load_dotenv()

# Define BASE_DIR as the directory containing your manage.py file
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
# Default secret key for development; override this in production with an environment variable
SECRET_KEY = os.getenv('SECRET_KEY', 'n4^y3+mjbrkass$a@#r5ov!og!1a^xg1y^=#^5f178mxqk1l(a)')

# Debug mode should be turned off in production
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Define the hosts the application can serve
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

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
    'allauth.socialaccount.providers.twitter',
    'phoneApp.apps.PhoneAppConfig',  # Your custom app
    'base.apps.BaseConfig',          # Another custom app
    'django_extensions',             # Useful extensions for Django
]

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Serves static files efficiently
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'phoneApp.urls'

# Template settings
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

# WSGI application path
WSGI_APPLICATION = 'phoneApp.wsgi.application'

# Database configuration
# Use dj_database_url to configure the database from the DATABASE_URL environment variable
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files
MEDIA_URL = '/images/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication settings
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Login and logout redirects
LOGIN_REDIRECT_URL = '/profile/'
LOGOUT_REDIRECT_URL = '/home/'

# Site ID for django.contrib.sites
SITE_ID = 1

# Security settings (to be overridden in production.py)
SECURE_SSL_REDIRECT = False  # Redirect all HTTP to HTTPS
SECURE_HSTS_SECONDS = 0      # HTTP Strict Transport Security
CSRF_COOKIE_SECURE = False   # Use secure cookies
SESSION_COOKIE_SECURE = False

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'https://youbeenspoofed.com',
    'https://spoofed.azurewebsites.net',
    'https://www.youbeenspoofed.com',
    'https://www.spoofed.azurewebsites.net'
]

# Stripe settings (using environment variables)
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

# Email backend configuration for development (can be overridden in production.py)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
