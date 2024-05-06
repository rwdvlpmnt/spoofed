#!/usr/bin/env python
import os
import sys

def get_current_host():
    if 'HTTP_HOST' in os.environ:
        return os.environ['HTTP_HOST']
    elif 'SERVER_NAME' in os.environ:
        return os.environ['SERVER_NAME']
    else:
        return None

ALLOWED_HOSTS = ['spoofed.azurewebsites.net', 'youbeenspoofed.com', 'www.spoofed.azurewebsites.net', 'www.youbeenspoofed.com']
current_host = get_current_host()

if current_host and any(host in current_host for host in ALLOWED_HOSTS):
    settings_module = 'phoneApp.production'
else:
    settings_module = 'phoneApp.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

try:
    from django.core.management import execute_from_command_line
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc

execute_from_command_line(sys.argv)
