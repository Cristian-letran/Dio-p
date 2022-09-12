from django.apps import AppConfig

class GuiaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.guia'
    icon_name = 'public'

    def ready(self):
        from . import signals



    
