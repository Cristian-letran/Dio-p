from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from applications.call.models import Telefono, Informe_call

@receiver(post_save, sender=Telefono)
def create_telefono_profile(sender, instance, created, **kwargs):
    
    if created:
        Informe_call.objects.create(
            id=instance,
            )