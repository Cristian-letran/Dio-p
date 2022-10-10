from django.db import models
from applications.base_cliente.models import Producto
from applications.cliente.models import Ciudad, Oficinas
from applications.argumento.models import Estado, Motivo, Cod_vis, Proceso
from applications.guia.models import Guia
from django.conf import settings 
import datetime

class Postal(models.Model):
    departamento = models.CharField(max_length=60)

    def __str__(self):
        return str(self.id)

class Orden (models.Model):
    orden = models.IntegerField(primary_key= True)
    fecha = models.DateTimeField(auto_now=True, blank=True, null=True)
    nombre_orden = models.CharField(max_length=25)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return str(self.orden)

class datos_g (models.Model):

    seudo_dg = models.OneToOneField(
        Guia,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name= 'guia_d_g'
        
    )

    fecha = models.DateField(auto_now_add=True,
        verbose_name = 'Fecha fisico')

    d_i = models.BigIntegerField(
        blank=True, 
        null=True,
        verbose_name = 'Documento de identidad'
    )
    
    direccion = models.CharField(
        max_length= 255,
        blank=True, 
        null=True,
    )
    dest = models.CharField(
        max_length=100, blank=True, null = True, verbose_name='Destinatario'
    )

    d_i_a = models.CharField(
        max_length=12,
        null=True, 
        blank = True,
        verbose_name = 'CC autorizado'
    )
    autor = models.CharField(
        max_length=100, 
        null=True, 
        blank = True, 
        verbose_name = 'Autorizado'
    )

    postal = models.ForeignKey(Postal,
        on_delete=models.CASCADE,
        
    )
    id_ciu = models.ForeignKey(
        Ciudad, 
        on_delete=models.CASCADE,
        verbose_name = 'Id ciudad',
        null=True,
        blank=True,
        
    )
    barrio = models.CharField(
        max_length = 70,
        null=True,
        blank=True,
    )  
    marca = models.CharField(
        max_length= 15,
        null=True, 
        blank = True
    )  
    id_pro = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Producto'
    )
    proc = models.ForeignKey(Proceso,
        on_delete=models.CASCADE, blank = True, null = True, verbose_name='Proceso'
        )

    cod_vis = models.ForeignKey(
        Cod_vis,
        on_delete=models.CASCADE,
        blank = True,
        null = True,
    )

    gx = models.BigIntegerField(
        null=True,
        blank=True,
    )

    gy = models.BigIntegerField(
        null=True,
        blank=True,
    )

    mot = models.ForeignKey(
        Motivo, 
        on_delete=models.CASCADE, 
        verbose_name = 'motivo',
        null=True,
        blank=True,)

    id_estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE, 
        null=True, 
        blank = True,
        verbose_name = 'Estado'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        verbose_name= 'Usuario_datog'
    )

    # cantidad = models.IntegerField(blank=True, null=True)

    orimp = models.ForeignKey(
        Orden, on_delete= models.CASCADE,
        blank=True,
        null=True,
        related_name = 'orden_datos_g',
        verbose_name = 'Orden impresion',
        related_query_name="orden_dat_g"
        )

    zona = models.CharField(max_length=30, blank=True, null=True)

    oficina= models.ForeignKey(
        Oficinas, 
        on_delete= models.CASCADE,
        blank=True,
        null=True,
        )

    cantidad = models.IntegerField()
        
    class Meta:
        verbose_name = "Datos de gestion"
        verbose_name_plural = "Datos de gestion"
              
    def __str__(self):
        return str(self.seudo_dg)

    @property
    def desti(self):
        return self.dest

    @property
    def dire(self):
        return self.direccion

    @property
    def bar(self):
        return self.barrio

    @property
    def post(self):
        return self.postal

    @property
    def cod_vi(self):
        return self.cod_vis

    @property
    def motivo(self):
        return self.mot

    @property
    def id_est(self):
        return self.id_estado

    @property
    def ciudad(self):
        return (self.id_ciu)

    @property
    def documento(self):
        return (self.d_i)

    @property
    def or_imp(self):
        return self.orimp.orden

    @property
    def proceso(self):
        return self.proc
    
    @property
    def producto(self):
        return self.id_pro
    
    @property
    def cantidades(self):
        return self.cantidad

    @property
    def usuariod(self):
        return self.user

    @property
    def union(self):
        return str(self.cantidad) + str(self.motivo.id) + str(self.id_est.id) + str(self.cod_vi)

    def save(self, *args, **kwargs):
        # self.seudo.bolsa  = self.vars

        self.seudo_dg.destinatario = self.desti
        self.seudo_dg.id_ciu = self.ciudad
        self.seudo_dg.direccion  = self.dire
        self.seudo_dg.barrio = self.bar
        self.seudo_dg.postal = str(self.post)
        self.seudo_dg.cod_vis = self.cod_vi
        self.seudo_dg.mot = self.motivo
        self.seudo_dg.id_est = self.id_est
        self.seudo_dg.d_i = self.documento
        self.seudo_dg.proceso = self.proceso
        self.seudo_dg.cantidad_vi = self.cantidad
        self.seudo_dg.producto = self.producto
        self.seudo_dg.codigo = self.union
        self.seudo_dg.fecha_visita = datetime.datetime.now()
        self.seudo_dg.user_id = self.usuariod

        if self.seudo_dg.save == None:
            None
        else:
            self.seudo_dg.save()

        super(datos_g, self).save(*args, **kwargs)

class Cubrimiento(models.Model):
      id_cubrimiento = models.IntegerField(
          primary_key= True,
          verbose_name='Codigo'
        )
      oficina = models.CharField(max_length=80)
      direccion = models.CharField(max_length=100)
      dane = models.ForeignKey(Ciudad,
        on_delete=models.CASCADE,
        related_name = 'Ciudad'
        )
      dias = models.CharField(max_length=6)
      direccion_cita = models.CharField(max_length=180)
      postal = models.IntegerField()

class Agenda(models.Model):
    id_agenda = models.OneToOneField(
        Guia,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name= 'agenda'
        
    )

