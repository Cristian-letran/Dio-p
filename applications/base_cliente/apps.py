from django.apps import AppConfig


class BaseClienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.base_cliente'
    icon_name = 'wb_cloudy'
