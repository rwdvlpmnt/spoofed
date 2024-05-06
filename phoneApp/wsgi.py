import os

from django.core.wsgi import get_wsgi_application

if any(host in os.environ.get('ALLOWED_HOSTS', '').split(',') for host in ['spoofed.azurewebsites.net', 'youbeenspoofed.com', 'www.spoofed.azurewebsites.net', 'www.youbeenspoofed.com']):
    settings_module = 'phoneApp.production'
else:
    settings_module = 'phoneApp.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()

