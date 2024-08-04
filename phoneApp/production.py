import os
from .settings import *
from .settings import BASE_DIR
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Security settings
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Allowed Hosts
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'spoofed.azurewebsites.net',
    'youbeenspoofed.com',
    'www.youbeenspoofed.com',
    'www.spoofed.azurewebsites.net'
]

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'https://youbeenspoofed.com',
    'https://spoofed.azurewebsites.net',
    'https://www.youbeenspoofed.com',
    'https://www.spoofed.azurewebsites.net'
]

# Database configuration
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# Email settings for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'webmaster@example.com')

# Stripe configuration
STRIPE_PUBLIC_KEY = os.environ['STRIPE_PUBLIC_KEY']
STRIPE_SECRET_KEY = os.environ['STRIPE_SECRET_KEY']
