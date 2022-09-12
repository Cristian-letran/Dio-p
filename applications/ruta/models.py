from django.db import models
from django.forms.widgets import NumberInput
from  django.db.models.signals import post_save
from django.conf import settings 
from simple_history.models import HistoricalRecords
from simple_history import register
import datetime
from django.urls import reverse
from applications.argumento.models import Estado
from applications.courrier.models import courrier
from applications.datos_g.models import Motivo
from applications.fisico.models import Fisico, Bolsa
from applications.guia.models import Guia
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from model_utils.models import TimeStampedModel
from .managers import ProductManager

class Est_planilla(models.Model):
    estado = models.CharField(max_length=20)

    def __str__(self):
        return str(self.estado)

class Cargue(TimeStampedModel):

    id = models.AutoField(
        primary_key=True,
        verbose_name ='Planilla',
    )
    guia = models.ManyToManyField(
        Fisico, 
        through= 'Planilla', 
  
    )

    full_name = models.ForeignKey(
        courrier, 
        on_delete=models.CASCADE, 
        verbose_name= 'Mensajero'
        )

    fecha = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de entrega')

    objects = ProductManager()

     
    class Meta: 
        verbose_name = "Cargue"
        verbose_name_plural = "Cargue"

    def __str__(self):
        return str(self.id)
  
class Planilla(TimeStampedModel) :

    guia = models.ForeignKey(
        Fisico, 
        related_name= "planilla_filtro",
        on_delete=models.CASCADE
    )
    cargue = models.ForeignKey(
        Cargue, 
        on_delete=models.CASCADE,
        blank=True, null=True,
        verbose_name="Planilla"
    )
    full_name = models.ForeignKey(
        courrier, 
        on_delete=models.CASCADE, 
        verbose_name= 'Mensajero',
        blank = True
        )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario Gestion',
    )

    fecha = models.DateField(
        auto_now=True
    )
    cont = models.IntegerField(blank=True, null=True)

    history = HistoricalRecords()    
    
    def authenticated(self, user):
        return self.filter(user=user)

    def __str__(self):
        return str(self.guia)

    @property
    def cargues(self):
        return str(self.cargue)

    @property
    def mensajeros(self):
        return self.full_name

    @property
    def id_planilla(self):
        return self.id

    @property
    def contar(self):
        return self.cont

    @property
    def fecha_planilla(self):
        return self.fecha

#f
    def save(self, *args, **kwargs):
        self.guia.fecha_planilla = datetime.datetime.now()
        
        self.guia.id_est_id = self.guia.id_est_id = 4
        self.guia.mensajero = self.mensajeros
        self.guia.est_planilla = self.guia.est_planilla = 1
        self.guia.id_planilla = self.id_planilla  
        self.guia.fecha_visita = datetime.datetime.now()
        
        self.guia.save() 
              
        super(Planilla,  self).save(*args, **kwargs)
  
class Recepcion(models.Model):

    motivo = models.ForeignKey(
        Motivo, 
        on_delete=models.CASCADE
    )

    guia = models.ForeignKey(
        Fisico, 
        on_delete=models.CASCADE,
        related_name = 'recepcion_guia',
        related_query_name="recepcion",
    )

    fecha = models.DateField(
        auto_now=True,
        verbose_name = 'Fecha recepcion'
    )

    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        blank=True, 
        null=True, 
        default = 3
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario Gestion',
    )

    history = HistoricalRecords()    

    class Meta:
        verbose_name = "Recepcion"
        verbose_name_plural = "Recepciones"
        unique_together = ('guia', 'fecha')

    def __str__(self):
        return str(self.id)

    contador= 0 

    @property
    def varu(self):
      return self.motivo.id

    @property
    def motivo_img(self):
      return self.motivo.id

    @property
    def fecha_re(self):
        return self.fecha

    @property
    def estados(self):
        return self.estado
        
    def save(self, *args, **kwargs):
        self.guia.fecha_recepciond = self.fecha_re
        self.guia.mot_id = self.varu
        self.guia.id_est = self.estados

        self.guia.est_planilla = self.guia.est_planilla = 2 # estado de planiñlla activo o inactivo para mostrar en filtro nomas
        self.guia.cantidad = self.guia.cantidad + 1
        
        self.guia.id_est_id = self.guia.id_est_id = 3

    
        ####################Para contador#######################
        self.cantidad_vi = int(self.varu)
        if int(self.cantidad_vi) >= 16 and int(self.cantidad_vi) > 18:
                self.guia.cantidad_vi = self.contador
        
        elif int(self.cantidad_vi) > 18:
            self.guia.cantidad_vi = self.contador

        elif int(self.cantidad_vi) < 16:
            self.guia.cantidad_vi = self.contador
        
        elif self.guia.cantidad_vi <=2:
            self.guia.cantidad_vi +=1
        ##################verificar si es igual a entregado guardar estado_img############
        
        if self.motivo_img == 21:
            self.guia.estado_img = "ENTREGA_DIGITALIZADA"
        self.guia.save()

        super(Recepcion, self).save(*args, **kwargs)

 # def save(self, *args, **kwargs):
    # contador = 0
        # self.guia.mot = self.var
    # self.guia.id_est = self.estados
        # self.guia.id_est_id = self.guia.id_est_id = 3
        # self.guia.cantidad = self.guia.cantidad + 1
    # # Funcion contador ok copiar codigo para pruebas
        # self.guia.suma = self.guia.suma
        # si self.guia.suma <=2:
        # self.guia.suma +=1 # suma en campo sum en cada momento que se ejecuta el boton de guardar
                      
        # self.guia.save()

        # super(Recep_guia, self).save(*args, **kwargs)

class Sucursales(models.Model):
    sucursal= models.CharField(max_length=70)

    def __str__(self):
        return self.sucursal

class Destino(models.Model):
    sucursal= models.ForeignKey(
        Sucursales, 
        on_delete=models.CASCADE,
        related_name= "guia_destino",
        blank=True,
        null=True)
        
    destino= models.ForeignKey(Sucursales, on_delete=models.CASCADE, related_name='destinos')
    guia = models.ForeignKey(Fisico, on_delete=models.CASCADE, related_name = 'guia_destino')
    origen_destino = models.CharField(max_length=60, blank=True, null=True)
    fecha = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name= 'Fecha Destino'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario'
    )

    history = HistoricalRecords()    

    def __str__(self):
        return str(self.sucursal)

    @property
    def origen(self):
        return str(self.user.ciudad.ciudad) + '/' + str(self.destino)

    @property
    def destinoss(self):
        return str(self.destino)

    # @property
    # def origen_dest(self):
    #   return str(self.user)+ '/' +(self.destino.sucursal)
    # print(origen_dest)

    def save(self, *args, **kwargs):
        # self.origen_destino = self.origen_dest
        self.guia.id_est_id = self.guia.id_est_id = 10
        self.guia.origen = self.origen
        print(self.guia.origen)
        self.guia.destino = self.destinoss
        self.guia.estado_destino = self.guia.estado_destino = True

        self.guia.save()

        super (Destino, self).save()

class Descargue(models.Model):
    guia = models.ForeignKey(Fisico, on_delete=models.CASCADE, related_name = 'guia_descargue')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario'
    )
    fecha = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name= 'Descargue'
    )

    history = HistoricalRecords()    


    def __str__(self):
        return str(self.guia)
    
    @property
    def usuario(self):
        return self.user

    @property
    def fecha_re(self):
        return self.fecha

    def save(self, *args, **kwargs):
        (self.guia.id_est_id) = self.guia.id_est_id = 3
        print(self.guia.id_est.id)
        
        self.guia.users = self.usuario
        self.guia.estado_destino = self.guia.estado_destino = False

        print(self.guia.users)

        self.guia.save()

        super (Descargue, self).save()

class Punteo(models.Model):
    guia_punteo = models.ForeignKey(
        Fisico, 
        on_delete=models.CASCADE
        )

    def save(self, *args, **kwargs):
        (self.guia_punteo.id_est_id) = 3
        
        self.guia_punteo.save()   
         
        super(Punteo, self).save(*args, **kwargs)  

class Imprimir(models.Model):
    guia_imprimir = models.ForeignKey(
        Fisico, 
        on_delete=models.CASCADE)
    
    fecha_imprimir = models.DateField(
        auto_now_add=True,
        )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        verbose_name= 'Usuario'
    )

    def __str__(self):
        return str(self.fecha_imprimir)

  