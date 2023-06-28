from email.errors import MultipartConversionError
from django.db import models

class Localidad(models.Model):
    nombre = models.CharField(max_length=40)

class Departamento(models.Model):
    departamento = models.CharField(max_length=30)
    capital = models.IntegerField()
    localidad = models.ForeignKey(
        Localidad, 
        on_delete=models.CASCADE,
        null=True)

    def __str__(self):
        return self.departamento

class Ciudad (models.Model):
    id = models.CharField(
        max_length=10,
        primary_key = True,
        unique = True, 
        verbose_name = 'Dane'
    )
    ciudad = models.CharField(
        max_length= 80
    )
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE,
        verbose_name = 'departamento_ciudad'
    )

    cubrimiento = models.CharField(
        max_length=15,
        null = True,
        blank = True
    )

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudad"

    def __str__(self):
        return self.ciudad + ' ' + self.departamento.departamento

    def __unicode__(self): 
        return self.ciudad

    class Meta:
        ordering = ['ciudad'] # Nota el guión

class Cliente (models.Model):
    ROL = (
        ('1', 'Administracion'),
        ('2', 'Asesor'),
        
    )
    id_clie = models.CharField(max_length=10,
        primary_key = True,
        verbose_name = 'Id cliente'
    )
    nit = models.CharField(
        max_length = 20
    )
    r_s = models.CharField(
        max_length = 70,
        verbose_name = 'Razon social'
    )
    contact = models.CharField(
        max_length = 50,
        verbose_name = 'Contacto'
    )
    dir = models.CharField(
        max_length = 120,
        verbose_name = 'Direccion'
    )
    id_ciu = models.ForeignKey(
        Ciudad, 
        on_delete=models.CASCADE,
        verbose_name = 'Id ciudad'
    )
    tel = models.IntegerField(
        verbose_name = 'Tel fijo'
    )
    cel = models.IntegerField(
        verbose_name = 'Celular'
    )
    
    radicacion = models.IntegerField()

    fact = models.CharField(
        max_length = 4,
        verbose_name = 'Factura'
    )
    rol = models.CharField(
        max_length=2, 
        choices=ROL, 
        blank=True, 
        null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Cliente"

    def __str__(self):
        return self.r_s

class Oficinas(models.Model):
    id= models.CharField(max_length=6, primary_key=True)
    nom_ofi = models.CharField(max_length=80)
    direccion = models.CharField(max_length=200)
    dane = models.ForeignKey(Ciudad, on_delete=models.CASCADE,)
    hora_norm = models.CharField(max_length=90, verbose_name= 'Horario normal')
    hora_adi = models.CharField(max_length=90, verbose_name= 'Horario adicional')
    hora_sab = models.CharField(max_length=90, verbose_name='Horario sabado')
    categoria = models.CharField(max_length=20)
    num_dia_entr = models.CharField(max_length=8, verbose_name = 'N° Días Entrega_(hábiles)')
    lunes = models.CharField(max_length=3)
    martes = models.CharField(max_length=3)
    miercoles = models.CharField(max_length=3)
    jueves = models.CharField(max_length=3)
    viernes = models.CharField(max_length=3)
    sabado = models.CharField(max_length=3)
    fusionada = models.CharField(max_length=60, blank=True, null=True)
    observacion = models.TextField()
    fecha_actu = models.DateField(verbose_name = 'Fecha ultima actualizacion')
    dir_cita = models.CharField(max_length=150, verbose_name='Direccion cita')
    cub = models.CharField (max_length=16)


    def __str__(self):
        return (self.dir_cita)
    
class Zona(models.Model):
    zona = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad")
    name = models.CharField(max_length=30)

    def __str__(self):
        return (self.name)






    