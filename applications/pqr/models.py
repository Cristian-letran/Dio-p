from distutils.text_file import TextFile
import email
from pyexpat import model
from typing import Text
from django.db import models
from applications.cliente.models import Departamento

# Create your models here.



class Pqr(models.Model):
    TIPOS = (
        ('C', 'CC'),
        ('CE', 'CE'),
    )
    ciudad_radi = models.ForeignKey(
        Departamento, 
        on_delete=models.CASCADE,
        verbose_name='Ciudad radicado'
        )
    fecha = models.DateField()
    # tipo_pqr 
    # tipo_soli
    otro_cual = models.CharField(max_length=30)
    tipo_do = models.CharField(
        max_length=4,
        choices=TIPOS,)
    n_documento = models.CharField(max_length=12)
    apellidos = models.CharField(max_length=60)
    nombre = models.CharField(max_length=70)
    email = models.EmailField()
    n_contacto = models.CharField(max_length = 10)
    direccion = models.CharField(max_length=120)
    # ciudad_env = models.ForeignKey(
    #     Departamento, 
    #     on_delete=models.CASCADE,
    #     verbose_name='Ciudad envio'
    #     )
    n_guia = models.IntegerField()
    desc_pqr = models.TextField()