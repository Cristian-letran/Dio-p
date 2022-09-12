from django.db import models
from applications.cliente.models import Cliente

class Tipo(models.Model):
    id_tip = models.IntegerField(
        primary_key=True
    )
    tipo = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipo"

    def __str__(self):
        return str(self.tipo)

class Estado (models.Model):
    id = models.IntegerField(
        primary_key = True
    )
    Estado = models.CharField(
        max_length=35
    )

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estado"

    def __str__(self):
        return str(self.Estado)

class Motivo(models.Model):
    
    id = models.IntegerField(primary_key=True, default = 0)

    motivo = models.CharField(
        max_length=50
    )

    id_tip = models.ForeignKey(
        Tipo, 
        on_delete=models.CASCADE,
        blank=True, 
        null=True
    )
    
    def __str__(self):
        return str(self.motivo) #+ "-" + self.motivo
    
    class Meta:
        verbose_name = "Motivo"
        verbose_name_plural = "Motivo"

class Cod_vis(models.Model):    

    id = models.CharField(
        primary_key= True,
        max_length=8,
        verbose_name='Codigo de visita',
    )
    visita = models.CharField(
        max_length= 36
    )
    tipo = models.CharField(max_length=12)

    def __str__(self):
        return str(self.visita)

class Nom_producto(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    nom_producto = models.CharField(max_length=3)

    def __str__(self):
        return str(self.id)

class Proceso(models.Model):
    
    id = models.IntegerField(primary_key=True)
    proceso = models.CharField(
        max_length=30
        )
    cod_dir = models.CharField(max_length=4)
    tipo_e = models.CharField(max_length=5)

    def __str__(self):
        return str(self.proceso)

class Emision(models.Model):

    t_emi = models.CharField(
        primary_key = True, 
        max_length=4, 
        verbose_name = 'Tipo emision'
    )

    emision = models.CharField(
        max_length= 35
    )
    
    class Meta:
        verbose_name = "Emision"
        verbose_name_plural = "Emision"

    def __str__(self):
        return self.emision

class Producto (models.Model):

    id_pro = models.CharField(  
        primary_key = True,     
        unique = True,
        max_length = 5,
        verbose_name = 'Id producto'
    )
    id_clie = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        verbose_name = 'Id cliente'
    )
    producto = models.CharField(
        max_length = 50
    )
    proceso = models.CharField(
        max_length = 50, blank = True, null = True,
    )
    tipo = models.CharField(
        max_length = 5,
        verbose_name = 'Tipos distribucion', blank = True, null = True,
    )
    homologacion = models.CharField(
        max_length=50, blank = True, null = True,
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Producto"
        unique_together = ('id_pro', 'id_clie')

    def __str__(self):
        return self.producto

class Est_clie (models.Model):
    
    id = models.CharField(
        primary_key = True,
        max_length = 10
    )
    cod_est = models.IntegerField()
    estado = models.CharField(max_length = 55)
    descripcion = models.CharField(max_length = 55)
    mot_est = models.CharField(max_length=50)
    t_entrega = models.CharField(max_length=30, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    verbose_name = "Estado Cliente"
    verbose_name_plural = "Estado del cliente"

    def __str__(self):
        return str (self.id)

class Motivo_call(models.Model):
    motivo = models.CharField(max_length=35)
    tipificacion = models.CharField(max_length=18)

    def __str__(self):
        return self.motivo

class Franquicia(models.Model):
    franqucia = models.CharField(max_length=30)

    def __str__(self):
        return self.franqucia

class Zona(models.Model):
    localidad = models.CharField(
        max_length=30
        )

    def __str__(self):
        return self.localidad