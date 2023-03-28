from django.db import models
from applications.guia.models import Guia
from applications.fisico.models import Fisico
from applications.argumento.models import Estado

class Rastreo(models.Model):
    
    id_guia = models.ForeignKey(
        Guia,
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name= 'trackin_guia'
        )

    id_fisico_track = models.ForeignKey(
        Fisico,
        on_delete=models.CASCADE,
        related_name = "fisco_tracking",
        blank=True, null=True
        )
#
    motivopr = models.CharField(
        max_length=30,
        blank=True,
        null=True)

    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE, 
        blank=True,
        null=True
    )
    mensajero = models.CharField(max_length = 120)

    fecha = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True)
    
    ciudad = models.CharField(
        max_length=100,
        blank=True,
        null=True
        )

    guia_tracking = models.IntegerField(
        blank=True,
        null=True)
    
    seudo = models.CharField(max_length=30)

    estado_final = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        if self.mensajero == None:
            self.mensajero = "No asignado"

        if self.estado == "CUSTODIA":
            self.estado == "CUSTODIA"

        elif self.estado == "RUTA":
            self.estado == "RUTA"
        
        elif self.motivopr == "Entregado":
            self.motivopr == "Entregado"
        
        elif self.motivopr == "Entregado":
            self.motivopr == "Entregado"

        
    
        super(Rastreo, self).save(*args, **kwargs)
    @property
    def usaurio(self):
        return self.id_guia.user
    
    class Meta:
        ordering = ['id']

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from applications.users.models import User, Profile

@receiver(post_save, sender=Guia)
def create_user_rastreo(sender, instance, created, **kwargs):
    
    if created:
        Rastreo.objects.create(
            
            id_guia=instance, 
            motivopr = instance.mot, 
            estado = instance.id_est,
            seudo = instance.seudo_track,
            ciudad = instance.id_ciu.ciudad
            # id_fisico_track = instance,
            )

    elif not created:
        Rastreo.objects.create(
            
            id_guia=instance, 
            motivopr = instance.mot, 
            estado = instance.id_est,
            seudo = instance.seudo_track,
            id_fisico_track = instance,
            ciudad = instance.id_ciu.ciudad
            )
    

@receiver(post_save, sender=Fisico)
def create_user_rastreo(sender, instance, created, **kwargs):
    
    if created:
        Rastreo.objects.create(
            
            id_fisico_track=instance, 
            motivopr = instance.mot, 
            estado = instance.id_est,
            mensajero = instance.mensajero,
            seudo = instance.seudo_track,
            ciudad = instance.id_ciu.ciudad
            )

    elif not created:
        Rastreo.objects.create(
            
            id_fisico_track=instance, 
            motivopr = instance.mot, 
            estado = instance.id_est,
            mensajero = instance.mensajero,
            seudo = instance.seudo_track,
            ciudad = instance.id_ciu.ciudad
            )