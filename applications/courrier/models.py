from tabnanny import verbose
from django.db import models
from applications.users.models import User

from applications.cliente.models import Ciudad
from .managers import CourrierManager

class Modelos(models.Model):
    modelo = models.IntegerField(primary_key=True)

class Tipo_infraccion(models.Model):
    infraccion = models.CharField(max_length=4)

    class Meta:
        verbose_name='Tipo de infraccion'
        verbose_name_plural = 'Tipo infraccion'

    def __str__(self):
        return self.infraccion

class Tipo_vehiculo(models.Model):
    tipo= models.CharField(max_length=25)

    class Meta:
        verbose_name= 'Tipo'
        verbose_name_plural = 'Tipo'

    def __str__(self):
        return str(self.tipo)
    
class Marca_vehiculo(models.Model):

    marca = models.CharField(max_length=40)

    class Meta:
        verbose_name= 'Marca'
        verbose_name_plural = 'Marca'

    def __str__(self):
        return str(self.marca)

class Linea_vehiculo(models.Model):
    linea = models.CharField(max_length=25)

    class Meta:
        verbose_name= 'Liena '
        verbose_name_plural = 'Linea'

    def __str__(self):
        return self.linea

class vehiculo(models.Model):
    id_veg = models.CharField(verbose_name = 'Id vehiculo', max_length=20)

    name = models.CharField(max_length=50, verbose_name = 'Propietario de vehiculo')

    cc = models.CharField(max_length=13)

    marca = models.CharField(max_length=20)

    cilindraje = models.IntegerField()

    capacidad = models.IntegerField()

    modelos = models.ForeignKey(Modelos, on_delete=models.CASCADE,)

    placa = models.CharField(max_length=10)

    soat = models.DateField()

    tecnomecanica = models.DateField()

    marca = models.ForeignKey(
        'Marca_vehiculo',
        on_delete=models.CASCADE,
    )
    linea = models.ForeignKey('Linea_vehiculo', on_delete=models.CASCADE,)

    tipo = models.ForeignKey(
        'Tipo_vehiculo',
        on_delete=models.CASCADE,
        verbose_name = 'Tipo vehiculo'
    )
    
    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculo"

    def __str__(self):
        return str(self.id_veg)

class courrier(models.Model):

    d_i = models.CharField(max_length=12, verbose_name='Documento identidad', unique=True)

    courrier = models.CharField(
        max_length=70, 
        verbose_name = 'Nombre courrier'
    )
    cel = models.CharField(max_length=12,
        verbose_name = 'Celular'
    )
    dir = models.CharField(
        max_length=120,
        verbose_name='Direccion'
    )
    id_ciu = models.ForeignKey(
        Ciudad, 
        on_delete=models.CASCADE,
        verbose_name = 'Ciudad'
    )

    id_veh = models.ForeignKey(
        vehiculo,
        on_delete=models.CASCADE,
        verbose_name = 'Datos vehiculo',
        blank=True,
        null=True
    )

    infraccion = models.ManyToManyField(Tipo_infraccion)

    licencia = models.DateField()

    est_courrier = models.BooleanField(default=True, verbose_name= 'Estado courrier')

    objects = CourrierManager()

    class Meta:
        verbose_name = "Courrier"
        verbose_name_plural = "Courrier"

    def __str__(self):
        return str(self.courrier ) + '-' + str(self.id_ciu)



