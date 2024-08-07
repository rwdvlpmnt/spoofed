from .settings import *

# Set DEBUG to False for production
DEBUG = False

# Production-specific allowed hosts
ALLOWED_HOSTS += [
    'spoofed.azurewebsites.net',
    'youbeenspoofed.com',
    'www.youbeenspoofed.com',
    'www.spoofed.azurewebsites.net'
]

# Security settings for production
SECURE_SSL_REDIRECT = True  # Ensure all requests are made over HTTPS
SECURE_HSTS_SECONDS = 31536000  # Enable HSTS for a year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
CSRF_COOKIE_SECURE = True  # Ensure cookies are secure
SESSION_COOKIE_SECURE = True

# Email settings for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'webmaster@example.com')

# Stripe configuration
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
