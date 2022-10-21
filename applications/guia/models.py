# from asyncio.windows_events import NULL
from contextlib import nullcontext
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
from datetime import date
from model_utils.models import TimeStampedModel
from .managers import ProductManagers
from applications.base_cliente.models import Bd_clie, Producto
from applications.users.models import User
from applications.cliente.models import Cliente, Oficinas
from applications.fisico.models import Fisico
from applications.argumento.models import Motivo_call
# from django.utils.encoding import smart_text
from django.conf import settings 
from simple_history.models import HistoricalRecords
from simple_history import register

class Servicio(models.Model):
    id_serv = models.IntegerField(
        primary_key = True
    )
    Servicio = models.CharField(
        max_length=25
    )

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicio"

    def __str__(self):
        return str(self.id_serv) + '-' + self.Servicio

class Guia(Fisico, TimeStampedModel):

    seudo = models.OneToOneField(
        Bd_clie,
        related_name = "guias",
        on_delete=models.CASCADE,
        primary_key=True)

    id_ser = models.ForeignKey(
        Servicio, 
        on_delete=models.CASCADE, 
        null=True, 
        blank = True,
        verbose_name = 'Servicio'            
    )    

    postal = models.CharField(
        max_length = 7,
        blank=True, 
        null=True,
    )
        
    barrio = models.CharField(
        max_length = 70,
        null=True,
        blank=True,
    )  

    contiene = models.CharField(
        max_length = 50, 
        null=True, 
        blank = True
    )
    orden = models.IntegerField(
        null=True, 
        blank = True
    )
    domicilio = models.IntegerField(
        default=0,
        null=True, 
        blank = True
    )
     
    declarado = models.IntegerField(
        default=0,
        null=True, 
        blank = True
    )
    
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE, 
        null=True, 
        blank = True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        verbose_name= 'Usuario'
    )

    tel = models.CharField(
        max_length=80,
        null=True, 
        blank = True
    )
    
    oficina= models.ForeignKey(
        Oficinas, 
        on_delete= models.CASCADE,
        blank=True,
        null=True,
        )
    
    history = HistoricalRecords()    

    class Meta:
        verbose_name = "Buscar"
        verbose_name_plural = "Guia"

        def __str__(self):
            return str(self.seudo) + self.destinatario

    objects = ProductManagers()
    @property
    def motivo_calls(self):
        return self.motivo_call.id

    # objects = LogEntryManager()

    var_g = ("guia")    
    varmot = 20 
#-------------------------------------------------------
    @property
    def can_vi(self):
        return str(self.cantidad_vi)#

    @property
    def motis(self):
        return str(self.mot.id)#

    @property
    def c_vis(self): 
        return str(self.cod_vis) #

    @property
    def estados(self):
        return self.id_est.id #

    @property
    def moti(self):
        return str(self.mot.id)

    @property
    def ofi(self):
        return self.oficina
    
    @property
    def concatenar(self):
        return  str(self.can_vi) + (self.motis) + str(self.estados) + str(self.cod_vis.id) 
#-------------------------------------------------------------
    
    @property
    def userbd(self):
      return str(self.user)

    def save(self, *args, **kwargs):
        self.seudo.sucursal = self.userbd
        self.codigo = self.concatenar   
        self.seudo.fisicos = self.seudo.fisicos = 1
        # self.mot.id = 20
        # print(self.mot.id)
        # self.ofi = str(self.ofi)
        if self.ofi == None:
            self.direccion = self.direccion
        
        else:
            self.direccion = str(self.ofi)
        self.seudo.save()   
         
            
        super(Guia, self).save(*args, **kwargs)  


    
class img(models.Model):
    ESTADO_DIGITALIZACION = (
        ('ENTREGA_DIGITALIZADA', 'ENTREGA DIGITALIZADA'),
    )
    
    id_guia = models.OneToOneField(
        Fisico, 
        on_delete=models.CASCADE, 
        related_name= 'image_mesa',
        blank = True, null = True)

    image = models.ImageField(
        upload_to = 'guia',
        null=True, 
        blank = True,   
    )
    fecha = models.DateTimeField(
        auto_now=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario',
        related_name='edited_by'
        
    )
    mod_date = models.DateField(default=date.today, blank=True, null=True)

    estado_img = models.CharField(
        max_length=22,
        choices=ESTADO_DIGITALIZACION, 
        blank=True,
        null=True,
        verbose_name= "gestion",
        default = "ENTREGA_DIGITALIZADA"
    )
    
    class Meta:
        verbose_name = "Imagenes Guia"
        verbose_name_plural = "Imagenes Guia"

    @property
    def fe(self):
        return str(self.image)

    def save(self, *args, **kwargs, ):
        self.estado_img = "ENTREGA_DIGITALIZADA"
        self.id_guia_id = (self.fe[-14:-4])
        # self.id_guia.estado_img = "ENTREGA_DIGITALIZADA"
        # self.id_guia.save()     
        super (img, self).save(*args, **kwargs)

def optimize_image(sender, instance, **kwargs):
    print("==========")
    print(instance)
    if instance.image:
            image = Image.open(instance.image.path)
            image.save(instance.image.path, quality=25, optimize = True)
        
post_save.connect(optimize_image, sender = img)
 
###Esto es una prueba para second form eliminar 

class CoberturaPdf(models.Model):
    pdf = models.FileField(
        upload_to = 'pdf_cobertura',
        null=True, 
        blank = True,   
    )
    fecha = models.DateTimeField(
        auto_now=True, blank = True, null= True, verbose_name='fecha cobertura')

    

class Guiap(models.Model):#Guia
    seudof = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()
    


    
    
# @receiver(post_save, sender=Rastreo)
# def save_profile(sender, instance, **kwargs):
#         instance.id_guia.save()

