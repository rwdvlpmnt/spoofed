from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

class YourAppNameConfig(AppConfig):
    name = 'phoneApp'

    def ready(self):
        import phoneApp.signals