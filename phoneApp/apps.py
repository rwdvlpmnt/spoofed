#phoneApp/apps.py

from django.apps import AppConfig

class PhoneAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'phoneApp'

    def ready(self):
        import phoneApp.signals