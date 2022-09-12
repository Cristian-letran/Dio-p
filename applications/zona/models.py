from django.db import models
from applications.fisico.models import Fisico
from applications.argumento.models import Zona


class ZonaGuia(models.Model):
    guia = models.ForeignKey(
        Fisico, on_delete=models.CASCADE)

    zona = models.ForeignKey(
        Zona,
        on_delete=models.CASCADE
    )
    
    def save(self, *args, **kwargs):
        self.guia.estado_zona = self.zona
        
        
        self.guia.save() 
              
        super(ZonaGuia,  self).save(*args, **kwargs)
    
