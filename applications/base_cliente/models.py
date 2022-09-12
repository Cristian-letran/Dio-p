from django.db import models
from applications.cliente.models import Cliente
from applications.argumento.models import (
    Nom_producto, Emision, Producto, 
    Est_clie, Franquicia, Tipo
    )
from django.utils import timezone
from .managers import BdManager

class Bd_clie (models.Model):

    TIPOS = (
       
        ('1', 'Fisico'),
        ('2', 'No llego fisico'),
        ('3', 'Fisico paquete')
        
    )

    seudo_bd = models.CharField(
        max_length=35,
        primary_key=True,       
    )

    id_clie = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE,
        verbose_name = 'Id cliente'
    )
    nombre = models.CharField(max_length=180)

    cc = models.CharField(max_length=12)
    
    t_emi = models.ForeignKey(
        Emision, 
        on_delete=models.CASCADE, 
        max_length = 4, 
        verbose_name = 'Tipo Emision'
    )

    archivo = models.CharField(
        max_length= 15,
        null=True,
        blank = True)

    MONTH_CHOICES = [
    ("AM", "AM"),
    ("PM", "PM"),
    ]
    jornada = models.CharField(
        max_length=3, 
        choices=MONTH_CHOICES, 
        null=True, 
        blank = True
    )
    
    canal = models.CharField(
        max_length=8, 
        null=True, 
        blank = True
    )
    realz = models.CharField(
        max_length = 30, 
        null=True, 
        blank = True,
        verbose_name = 'Realzador'
    )
    tipo = models.CharField(
        max_length = 30, 
        null=True, 
        blank = True
    )
    
    tarjeta = models.CharField(
        max_length = 30, 
        null=True, 
        blank = True
    )
    id_est_clie = models.ForeignKey(
        Est_clie, 
        on_delete=models.CASCADE,
        verbose_name = 'Id estado cliente ',
        blank = True,
        null = True,

    )
    
    referencia = models.CharField(
        max_length= 50, 
        null=True, 
        blank = True
    )    
    convenio = models.CharField(
        max_length = 50, 
        null=True, 
        blank = True
    )
    id_serv = models.IntegerField(
        verbose_name = 'Id Servicio'
    )

    fecha = models.DateField()

    sucursal = models.CharField(
        max_length=50,
        blank=True,  null =True,
    )  

    nom_pro = models.ForeignKey(Nom_producto, default=0, on_delete=models.CASCADE, verbose_name='Nombre del producto')

    fisicos = models.CharField(
        max_length=8,
        choices=TIPOS,)

    telefono = models.CharField(
        max_length=80,
        null=True, 
        blank = True
    )

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank = True, null=True)

    franquicia= models.ForeignKey(Franquicia, on_delete=models.CASCADE, blank = True, null=True)

    objects = BdManager()

    class Meta:
        verbose_name = "Base Cliente"
        verbose_name_plural = "Base Cliente"

    def __str__(self):
        return str(self.seudo_bd)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() 

class No_fisico(models.Model):
    seudo = models.OneToOneField(
        Bd_clie,
        on_delete=models.CASCADE, 
        primary_key = True
    )

class Agenda_bd(models.Model):
    id_agenda = models.OneToOneField(
        Bd_clie,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name= 'agenda'
        
    )

