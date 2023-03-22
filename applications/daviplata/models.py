from django.db import models
from applications.cliente.models import Departamento, Ciudad
from django.conf import settings 

class Red(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class TipoNoEfectiva(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoEstablecimiento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class OtroTipoEstablecimiento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoSenalizacion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class OtroTipoSenalizacion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Acude(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class AcudeOtro(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Medio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Daviplata(models.Model):

    RESPUESTA = [
    ('NO', 'NO'),
    ('SI', 'SI')
]

    fecha_cargue = models.DateField(auto_now_add=True)
    id_ruta = models.AutoField(primary_key=True)
    codigo_total = models.IntegerField(blank=True, null=True)
    nombre_establecimiento = models.CharField(max_length=200)
    red = models.ForeignKey(Red, on_delete=models.CASCADE)#
    codigo_dian = models.IntegerField()
    direccion_base = models.CharField(max_length=400)
    rdab = models.CharField(
        max_length=100, 
        verbose_name='REFERENCIAS DETALLES ADICIONALES BASE'
        )
    direccion_c_b = models.CharField(
        max_length=400, 
        verbose_name='DIRECCIÓN COMPLETA BASE'
        )
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fecha_encuesta = models.DateField()
    visita_efectiva = models.CharField(max_length=2, choices=RESPUESTA)
    tipo_no_efectiva = models.ForeignKey(TipoNoEfectiva, on_delete=models.CASCADE)
    otro_especificado = models.CharField(max_length=50, blank = True, null=True)
    pdv = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='¿PDV permite realizar la visita?'
        )
    obervacion = models.TextField(max_length=300)
    direccion_actualizada = models.CharField(
        max_length=400,
        verbose_name='Dirección Actualizada'
        )
    detalle_direccion = models.CharField(
        max_length=200, 
        verbose_name='Detalle Dir actualizada'
        )
    direccion_completo = models.CharField(
        max_length=200, 
        verbose_name='Completo actualizada'
        )
    coincide_direccion = models.CharField(max_length=2, choices=RESPUESTA)
    mobre_e_a = models.CharField(
        max_length=200, 
        verbose_name='Nombre del establecimiento actualizado'
        )
    nombre_coincide = models.CharField(max_length=2, choices=RESPUESTA)

    nombre_atiende = models.CharField(
        max_length=150, 
        verbose_name='Nombre de quien atendió la visita'
        )
    es_dueño = models.CharField(max_length=2, choices=RESPUESTA)
    numero_movil = models.IntegerField()
    establecimiento_cambio = models.CharField(
         max_length=2,
         choices=RESPUESTA,
         verbose_name='El establecimiento cambió de dueño en el ultimo año?'
     )
    tipo_establecimiento = models.ForeignKey(TipoEstablecimiento, on_delete=models.CASCADE)
    otro_d_e = models.ForeignKey(
        OtroTipoEstablecimiento, 
        on_delete=models.CASCADE, 
        verbose_name='Otro tipo de establecimiento'
        )
    t_senalizacion = models.ForeignKey(
        TipoSenalizacion, 
        on_delete=models.CASCADE, 
        verbose_name='Tipo de señalizacion'
        )
    otro_senalizacion =  models.ForeignKey(
        OtroTipoSenalizacion, 
        on_delete=models.CASCADE, 
        verbose_name='Otro especificado'
        )
    se_implementa = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name ='Se logro Implementar el Rompetráfico'
        )
    razon_no = models.CharField(
        max_length=150, verbose_name='Razón indicada de no implementacion')
    impresora = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Herramientas: Impresora'
        )
    datafono = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Herramientas: Datafono'
        )
    lector = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Herramientas: Lector de código de barras'
        )
    computador = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Herramientas: Computador'
        )
    pago_propios = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Servicio: Pago de productos propios'
        )
    deposito_retiro_propio = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Servicio: Depósito de retiro DaviPlata'
        )
    servicio_pagos = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Servicio: Pagos de subsidios por giros'
        )
    servicio_recaudo = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Servicio: Recaudo servicios públicos y privados'
        )
    servicio_depositos = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Servicio: Depósitos y retiros de cuentas ahorro y corriente'
        )
    transacciones = models.CharField(
        max_length=50, choices=RESPUESTA, 
        verbose_name='Conocimiento para realizar transacciones'
        )
    deposito_retiro = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Depósito y Retiro DAVIVIENDA'
        )
    pago_subsidios = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Pagos de Subsidios por Giro'
        )
    tip_seguridad = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Tips de Seguridad'
        )
    Sarlaft_activos = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Sarlaft/Lavado de activos'
        )
    recaudo_servicios = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Recaudo servicios públicos y privados'
        )
    tip_riesgo = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='Tips de Riesgo'
        )
    fecha_capacitacion = models.DateField(
        verbose_name='Fecha de la última capacitación'
        )
    acude = models.ForeignKey(
        Acude, 
        on_delete=models.CASCADE, 
        verbose_name='¿A quien acude?'
        )
    medio = models.ForeignKey(
        Medio, 
        on_delete=models.CASCADE
        )
    medio_especificado = models.CharField(
        max_length=30, 
        verbose_name='Medio especificado'
        )
    sarlaft_informa = models.ForeignKey(
        AcudeOtro, 
        on_delete=models.CASCADE, 
        verbose_name='SARLAFT. ¿A quien informaría?'
        )
    material = models.CharField(max_length=50, choices=RESPUESTA)
    ninguno_especificado = models.CharField(max_length=30)
    firma = models.CharField(max_length=100)
    url_img_f = models.ImageField(
        upload_to = 'IMG FACHADA',
        verbose_name='URL IMAGEN FACHADA',
        )
    url_img_m = models.ImageField(
        upload_to = 'IMG MATERIAL', 
        verbose_name='URL IMAGEN IMPL. MATERIAL',
        )
    url_img_o = models.ImageField(
        upload_to = 'IMG OTRA', 
        verbose_name='URL IMAGEN OTRA',
        blank=True,
        null=True
        )
    latitud = models.FloatField()
    longitud = models.FloatField()
    visualizar = models.CharField(max_length=250)
    grupo_etnico = models.CharField(max_length=50, choices=RESPUESTA, verbose_name='HACE PARTE DE UN GRUPO ETNICO')
    cual = models.CharField(
        max_length=80, 
        verbose_name='especificado Grupo Etnico'
        )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        verbose_name= 'Usuario'
    )
    
    def __str__(self):
        return str(self.id_ruta)