from django.db import models
from django.core.signals import request_finished
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext, ugettext_lazy as _
import datetime
from simple_history.models import HistoricalRecords
from simple_history import register
from applications.cliente.models import Ciudad, Cliente

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION

class Modulos(models.Model):
    
    modulo = models.CharField(max_length=30)

    def __str__(self):
        return self.modulo

class Areas(models.Model):
    Areas = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.Areas

class User(AbstractBaseUser, PermissionsMixin):

    TIPO_DI = [
        ('Cedula', 'Cedula'),
        
    ]
    
    ROL_USER_FINAL = [

        (1, 'Consulta'),
        (2, 'Davivienda Administrador'),
        (3, 'Daviplata'),
        (4, 'Custodia'),
        (5, 'Courrier'),
        (6, 'Mesa de control'),
        (7, 'Sig'),
        (8, 'call center'),
        (9, 'DASHBOARD')
            
    ]
    
    CUSTODIA = '0'
    MESA = '1'
    CALL = '2'
    COURRIER = '3'
    SIG = '4'
    TECNOLOGIA = '5'
    ADMINISTRADOR = '6'
    CLIENTE = '7'
    COOR_RETAIL ="8"

    OCUPATION_CHOICES = [
        (CUSTODIA, 'Custodia'),
        (MESA, 'Mesa'),
        (CALL, 'Call'),
        (COURRIER, 'Courrier'),
        (SIG, 'Sig'),
        (TECNOLOGIA, 'Tecnologia'),
        (ADMINISTRADOR, 'Administrador'),
        (CLIENTE, 'Cliente'),
        (COOR_RETAIL, 'COOR_RETAIL')
    ]

    GENDER_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otros', 'Otros'),
    )
    username = models.CharField(
        max_length=20, 
        unique=True,
        verbose_name= 'Usuario'
    )
    email = models.EmailField(blank=True, null=True)

    nombres = models.CharField(
        max_length=30, 
        blank=True
    )
    apellidos = models.CharField(
        max_length=30, 
        blank=True
    )
    genero = models.CharField(
        max_length=9, 
        choices=GENDER_CHOICES, 
        blank=True
    )

    ocupation = models.CharField(
        max_length=1, 
        choices=OCUPATION_CHOICES, 
        verbose_name= 'Ocupacion',
        blank=True,
        null=True
        
    )
    
    ciudad = models.ForeignKey(
        Ciudad,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name= "user_ciudad"
    )
    tipo_d_i = models.CharField(
        max_length=10,
        choices=TIPO_DI,
        null=True,
        blank=True
    )
    d_i = models.CharField(
        max_length=12,
        verbose_name="Documento de identidad")

    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE, 
        blank=True, null=True,
        verbose_name="Cliente")
    
    roles = models.IntegerField(
        choices=ROL_USER_FINAL,
        blank=True,
        null=True)
    
    rol_m = models.ManyToManyField(
        Modulos, 
        blank=True,
        related_name= 'modulo_user')

    is_staff = models.BooleanField(
        default=True
    )
    is_active = models.BooleanField(
        default=False
    )

    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]   

    objects = UserManager()

    history = HistoricalRecords()    

    class Meta:
        verbose_name = "Permisos de usuarios"
        verbose_name_plural = "Permisos de usuario"

    # def get_short_name(self):
    #      return str(self.nombres + ' ' + self.apellidos )

    def __str__(self):
        return str(self.username) + ' ' +str(self.ciudad)

###################################################

class LogSesion(models.Model):
    id = models.AutoField(primary_key=True)
    log = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cliente = models.CharField(max_length=90, blank=True, null=True)
    usuario = models.CharField(max_length=150, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    registro = models.CharField(max_length=30, blank=True, null=True)
    accion = models.CharField(max_length=100, blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     self.accion(update_fields=["documento"])
        
    #     super(LogSesion, self).save(*args, **kwargs)  

@receiver(post_save, sender=User)
def create_user_log(sender, instance, created, **kwargs):
    if created:
        LogSesion.objects.create(
            log=instance,
            documento = instance.d_i,
            usuario = instance.nombres,
            registro = datetime.datetime.now(),
            cliente = instance.cliente
        )
    elif not created:
        LogSesion.objects.create(
            log=instance,
            documento = instance.d_i,
            usuario = instance.nombres,
            registro = datetime.datetime.now(),
            cliente = instance.cliente
        )


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.logsesion.save()   

####################################################
class Profile(models.Model):
    id = models.OneToOneField(
        User, primary_key=True, 
        on_delete=models.CASCADE,
        )
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(id=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()   

class Asistencia(models.Model):
    check = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    date = models.DateTimeField(auto_now=True)

    

