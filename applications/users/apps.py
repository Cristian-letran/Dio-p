from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.users'
    icon_name = 'person'

    def ready(self):
        from . import signals


