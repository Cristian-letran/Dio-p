from django.db import models
from applications.cliente.models import Departamento, Ciudad, Zona
from applications.users.models import User
from django.conf import settings 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Red(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoEstablecimiento(models.Model):
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

class Daviplata(models.Model): 

    SARLAFT_INFORMA = [
        ('Servicio al Cliente','Servicio al Cliente'),
        ('Operador','Operador' ),
        ('puntored ','puntored'),
        ('Chat Plataforma', 'Chat Plataforma'),
        ('Asesor Comercial ','Asesor Comercial'),
        ('Conred ','Conred'),
        ('No sabe','No sabe'),
        ('Supervisor','Supervisor'),
        ('Punto de Pago','Punto de Pago'),
    ]

    MEDIO = [
        ('Telefono','Telefono'),
        ('Internet','Internet' ),
        ('E-Mail ','E-Mail '),
        ('Otro', 'Otro'),
        ('WhatsApp','WhatsApp')

    ]

    TIPO_NO_EFECTIVA = [

        ('Direccion Errada','Direccion Errada'),
        ('Local Cerrado', 'Local Cerrado'),
        ('No Existe PVD','No Existe PVD'),
        ('El Cliente No Permitio Realizar encuesta','El Cliente No Permitio Realizar encuesta'),
        ('Cambio de Direccion PVD','Cambio de Direccion PVD'),
        ('Ya esta Marcado', 'Ya esta Marcado'),

    ]

    OTRO_SENALIZACION = [
        ('Flanger', 'Flanger'),
        ('Hablador', 'Hablador'),
        ('Peldaño', 'Peldaño'),
        ('Pendon', 'Pendon')
    ]

    T_SENALIZACION = [
        ('Otro', 'Otro'),
        ('Rompetrafico', 'Rompetrafico'),
        ('Aviso ', 'Aviso')
    ]

    RED = [
        ('PuntoRed (ConexRed)', 'PuntoRed (ConexRed)'),
        ('Conred', 'Conred'),
        ('Punto de Pago ', 'Punto de Pago'),
        ('PuntoRed (ConexRed) Onboarding', 'PuntoRed (ConexRed) Onboarding'),
        ('Conred (Super Pagos)', 'Conred (Super Pagos)'),
        ('Reval', 'Reval')
    ]

    RESPUESTA = [
    ('NO', 'NO'),
    ('SI', 'SI')
]

    fecha_cargue = models.DateField(auto_now_add=True)
    id_ruta = models.AutoField(primary_key=True)
    codigo_total = models.IntegerField(
        blank=True, 
        null=True,
        unique=True)
    nombre_establecimiento = models.CharField(max_length=200)
    red = models.CharField(max_length=60,
        choices=RED
        )#
    codigo_dian = models.IntegerField()
    direccion_base = models.CharField(max_length=400)
    rdab = models.CharField(
        max_length=100, 
        verbose_name='REFERENCIAS DETALLES ADICIONALES BASE',
        blank = True,
        null = True
        )
    direccion_c_b = models.CharField(
        max_length=400, 
        verbose_name='DIRECCIÓN COMPLETA BASE'
        )
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fecha_encuesta = models.DateField(
        blank=True,
        null=True
    )
    visita_efectiva = models.CharField(
        max_length=2, 
        choices=RESPUESTA,
        blank=True,
        null=True
        )
    tipo_no_efectiva = models.CharField(
        max_length=43, 
        choices=TIPO_NO_EFECTIVA,
        blank=True,
        null=True
        )
    otro_especificado = models.CharField(max_length=50, blank = True, null=True)
    pdv = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        verbose_name='¿PDV permite realizar la visita?',
        blank=True,
        null=True
        )
    obervacion = models.CharField(
        max_length=300,
        blank=True,
        null=True)
    direccion_actualizada = models.CharField(
        max_length=400,
        verbose_name='Dirección Actualizada',
        blank=True,
        null = True
        )
    detalle_direccion = models.CharField(
        max_length=200, 
        verbose_name='Detalle Dir actualizada',
        blank=True,
        null=True
        )
    direccion_completo = models.CharField(
        max_length=200, 
        verbose_name='Completo actualizada',
        blank=True,
        null=True
        )
    coincide_direccion = models.CharField(
        max_length=2, 
        choices=RESPUESTA,
        null=True
        )
    mobre_e_a = models.CharField(
        max_length=200, 
        verbose_name='Nombre del establecimiento actualizado',
        blank=True,
        null=True
        )
    nombre_coincide = models.CharField(
        max_length=2, choices=RESPUESTA,
        null=True
        )

    nombre_atiende = models.CharField(
        max_length=150, 
        verbose_name='Nombre de quien atendió la visita',
        blank=True,
        null=True
        )
    es_dueño = models.CharField(
        max_length=2, choices=RESPUESTA,
        blank=True,
        null=True)
    numero_movil = models.CharField(
        max_length=11,
        blank=True,
        null=True
    )
    establecimiento_cambio = models.CharField(
         max_length=2,
         choices=RESPUESTA,
         blank=True,
         null=True,
         verbose_name='El establecimiento cambió de dueño en el ultimo año?'
     )
    tipo_establecimiento = models.ForeignKey(
        TipoEstablecimiento, 
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    otro_d_e = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Otro tipo de establecimiento'
        )
    t_senalizacion = models.CharField(
        max_length=30, 
        choices=T_SENALIZACION,
        null=True,
        blank=True,
        verbose_name='Tipo de señalizacion',
        )
    otro_senalizacion =  models.CharField(
        max_length=30,  
        choices=OTRO_SENALIZACION,
        blank=True,
        null=True,
        verbose_name='Otro especificado'
        )
    se_implementa = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        null=True,
        verbose_name ='Se logro Implementar el Rompetráfico'
        )
    razon_no = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Razón indicada de no implementacion')
    impresora = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Herramientas: Impresora'
        )
    datafono = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Herramientas: Datafono'
        )
    lector = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Herramientas: Lector de código de barras'
        )
    computador = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Herramientas: Computador'
        )
    pago_propios = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Servicio: Pago de productos propios'
        )
    deposito_retiro_propio = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Servicio: Depósito de retiro DaviPlata'
        )
    servicio_pagos = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Servicio: Pagos de subsidios por giros'
        )
    servicio_recaudo = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Servicio: Recaudo servicios públicos y privados'
        )
    servicio_depositos = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Servicio: Depósitos y retiros de cuentas ahorro y corriente'
        )
    transacciones = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Conocimiento para realizar transacciones'
        )
    deposito_retiro = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Depósito y Retiro DAVIVIENDA'
        )
    pago_subsidios = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Pagos de Subsidios por Giro'
        )
    tip_seguridad = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Tips de Seguridad'
        )
    Sarlaft_activos = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Sarlaft/Lavado de activos'
        )
    recaudo_servicios = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Recaudo servicios públicos y privados'
        )
    tip_riesgo = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='Tips de Riesgo'
        )
    fecha_capacitacion = models.DateField(
        verbose_name='Fecha de la última capacitación',
        blank=True,
        null=True,
        )
    acude = models.ForeignKey(
        Acude, 
        on_delete=models.CASCADE, 
        verbose_name='¿A quien acude?',
        blank=True,
        null=True,
        )
    medio = models.CharField(
        max_length=30, 
        choices=MEDIO,
        blank=True,
        null=True,
        )
    medio_especificado = models.CharField(
        max_length=30, 
        blank=True,
        null=True,
        verbose_name='Medio especificado'
        )
    sarlaft_informa = models.CharField(
        max_length=30,
        choices=SARLAFT_INFORMA,
        blank=True,
        null=True,
        verbose_name='SARLAFT. ¿A quien informaría?'
        )
    material = models.CharField(
        max_length=50, 
        choices=RESPUESTA,
        blank=True,
        null=True
        )
    ninguno_especificado = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        )
    firma = models.CharField(
        max_length=100,
        blank=True,
        null=True,)
    url_img_f = models.ImageField(
        upload_to = 'IMG FACHADA',
        verbose_name='URL IMAGEN FACHADA',
        null=True,
        blank=True
        )
    url_img_m = models.ImageField(
        upload_to = 'IMG MATERIAL', 
        verbose_name='URL IMAGEN IMPL. MATERIAL',
        blank=True,
        null=True,
        )
    url_img_o = models.ImageField(
        upload_to = 'IMG OTRA', 
        verbose_name='URL IMAGEN OTRA',
        blank=True,
        null=True
        )
    latitud = models.CharField(
        max_length=22,
        blank=True,
        null=True,)
    longitud = models.CharField(
        max_length=22,
        blank=True,
        null=True,)
    visualizar = models.CharField(
        max_length=250,
        blank=True,
        null=True,)
    grupo_etnico = models.CharField(
        max_length=50, 
        choices=RESPUESTA, 
        blank=True,
        null=True,
        verbose_name='HACE PARTE DE UN GRUPO ETNICO')
    cual = models.CharField(
        max_length=80, 
        blank=True,
        null=True,
        verbose_name='especificado Grupo Etnico')
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        verbose_name= 'Usuario',
        related_name = "user_marcacion"
    )
    hora = models.CharField(max_length=30,
                            blank = True, 
                            null=True,
                            default=0
                            )
    minuto = models.CharField(max_length=22,
                            blank = True, 
                            null=True,
                            default=0)
    tiempo = models.CharField(max_length=22, blank=True, null=True)

    contingencia_img1 = models.BooleanField(
        default = False,
         )

    def save(self, *args, **kwargs):
    
        self.direccion_completo = str(self.direccion_actualizada) + " " + str(self.detalle_direccion)
        self.material = self.visita_efectiva

        ######### VISITA EFECTIVA + NO EFECTIVA #######################################
        if self.visita_efectiva == "SI":
            self.tipo_no_efectiva = None

        ######### TIPO SENALIZACION ##################

        #visita_efectiva + pdv
        if self.visita_efectiva == "SI":
            self.pdv = "SI"
            self.t_senalizacion = "Rompetrafico"

        elif self.visita_efectiva == "NO":
            self.pdv = "NO"

        else:
            self.pdv = ""
         
        super(Daviplata, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.bolsa)

    def __str__(self):
        return str(self.id_ruta)

class RutaDaviplata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion = models.ManyToManyField(Daviplata)

class TipoGestion(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return self.descripcion
        

class Categorias(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre
    
class MotivoNoRegistro(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre
    
class TipoActivacion(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    direccion = models.CharField(max_length=30)

    def __str__(self):
        return self.direccion

class ComplementoDireccion(models.Model):
    complemento = models.CharField(max_length=30)

    def __str__(self):
        return self.complemento

class Vinculacion(models.Model):
    PORQUENOREGISTRO = [
        ('Cliente ya estaba registrado', 'Cliente ya estaba registrado'),
        ('Fallas en la app', 'Fallas en la app'),
        ('Cliente no esta interesado', 'Cliente no esta interesado'),
        ('Cliente tercera edad', 'Cliente tercera edad'),
        ('Sistema operativo no permite registro', 'Sistema operativo no permite registro'),
        ('Cliente desconfia', 'Cliente desconfia'),
        ('Cliente no tiene tiempo', 'Cliente no tiene tiempo'),
        ('Cliente no tiene documentos en el momento', 'Cliente no tiene documentos en el momento'),
        

    ]

    PERFILNEGOCIO = [
        ('SI', 'SI'),
        ('NO', 'NO'),
        ('Ya esta activo', 'Ya está activo'),
        
        
        
    ]

    PREGUNTA4 = [
        ('Clinete ya tiene la tencard', 'Clinete ya tiene la tencard'),
        ('Fallas en la app', 'Fallas en la app'), 
        ('No permitió el registro en el perfil mi negocio', 'No permitió el registro en el perfil mi negocio'),
        ('Cliente no esta interesado', 'Cliente no esta interesado'),
        ('Solo activo Daviplata para subsidios del gobierno', 'Solo activo Daviplata para subsidios del gobierno'),
        ('Modo contigencia', 'Modo contigencia'), 
    
    ]
    PREGUNTA3 = [
        ('SI', 'SI'),
        ('NO', 'NO'), 
        ('Ya tiene la tencard', 'Ya tiene la tencard'),
        
    ]

    PREGUNTA2 = [
        ('SI', 'SI'),
        ('NO', 'NO'), 
        ('Ya esta activo', 'Ya esta activo'),
        
    ]

    PREGUNTA = [
    ('SI', 'SI'),
    ('NO', 'NO'),
]

    C_RUT = [
    ('SI', 'SI'),
    ('NO', 'NO'),
]
    
    ETNICO = [
    ('Ninguno', 'Ninguno'),
    ('Gitano o Rrom', 'Gitano o Rrom'),
    ('Palenquero', 'Palenquero'),
    ('Raizal', 'Raizal'),
    ('Negro(a), Mulato(a),afrodecendiente(a), afrocolombiano(a)', 'Negro(a), Mulato(a),afrodecendiente(a), afrocolombiano(a)'),
    ('Indigena', 'Indigena'),
    ('Prefiere no responder', 'Prefiere no responder'),
    
]
    tipo_gestion = models.ForeignKey(
        TipoGestion, 
        on_delete=models.CASCADE,
        related_query_name="tipo_gestion_vinculacion"
        )
    
    identificacion = models.AutoField(primary_key=True)

    celular = models.CharField(
        unique=True, 
        max_length=10,
        blank= True,
        null= True, 
        verbose_name="No. celular activado en DaviPlata")

    celular_confirma = models.CharField(
        unique=True, 
        max_length=10, 
        blank= True,
        null= True, 
        verbose_name="Confirmación No. celular activado en DaviPlata"
        )

    fecha_visita = models.DateField(
        auto_now=False,
        blank=True,
        null=True
        )

    nombre = models.CharField(
        max_length=150,
        blank= True,
        null= True, 
        verbose_name='Nombre del cliente DaviPlata')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        verbose_name= 'Usuario',
        related_query_name="user_vinculacion"
    )
    nombre_comercio = models.CharField(
        max_length=80,
         )
    c_rut = models.CharField(max_length=2, choices=C_RUT, verbose_name="¿Comercio cuenta con RUT?")
    categoria = models.ForeignKey(
        Categorias, 
        on_delete=models.CASCADE,
        blank= True,
        null= True, 
        verbose_name="¿A cual de las siguientes categorias pertenece el comercio?"
        )    
    direccion = models.CharField(
        max_length=150, 
        verbose_name="Dirección Comercio",
        blank=True)
    barrio = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    dane = models.ForeignKey(Ciudad, on_delete=models.CASCADE, blank=True)
    latitud = models.CharField(max_length=20, null=True)
    longitud = models.CharField(max_length=20, null=True)
    ############## Pestaña ###################
    registro_daviplata = models.CharField(
        max_length=20, 
        choices=PREGUNTA2,
        null=True,
        verbose_name= "¿Se realizó registro en DaviPlata?"
        )
    motivo_no_registro = models.ForeignKey(
        MotivoNoRegistro, 
        on_delete=models.CASCADE,
        verbose_name="¿Por qué no se realizó el registro DaviPlata?",
        blank=True,
        null=True
        )
    se_registro = models.CharField(
        max_length=20, 
        choices=PERFILNEGOCIO,
        null=True,
        verbose_name="¿Se realizó registro en perfil mi negocio?"
        )
    
    no_register = models.CharField(
        max_length=60, 
        choices=PORQUENOREGISTRO, 
        blank = True,
        null=True,
        verbose_name="¿Por que no se realizo el registro en perfil mi negocio?"
        )
    fecha_registro = models.DateTimeField(
        auto_now=True,
        null=True
        )
        
    ################### 4 Pestaña ######################

    MOTIVO = [
    ('No esta autorizado por el dueno', 'No está autorizado por el dueño'),
    ('No está interesado', 'No está interesado'),
    ('No se pudo registrar', 'No se pudo registrar'),
    ('Vendedor informal', 'Vendedor informal'),
    ('No hay espacio en el comercio', 'No hay espacio en el comercio'),
    ('No hay Stock', 'No hay Stock'),
    ('Se instaló flanger', 'Se instaló flanger'),
    ]
    
    solicito_tencard = models.CharField(
        max_length=40,
        choices=PREGUNTA3,
        null=True,
        verbose_name= "¿Se solicitó la tentcard?")
    
    porque_no_solicito = models.CharField(
        max_length = 80,
        choices = PREGUNTA4,
        blank=True,
        null=True,
        verbose_name= "¿Por qué no se solicitó la tentcard?"
        )
    sticker = models.CharField(
        max_length=2,
        choices=PREGUNTA,
        null=True,
        verbose_name= "Se pego Sticker"
        )
    razon_no_sticker = models.CharField(
        max_length = 60,
        choices = MOTIVO,
        blank=True, null=True,
        verbose_name= "Razón por la cual no se pegó el sticker"
    )
    flanger = models.CharField(
        max_length=2, 
        default= "No",
        verbose_name= "Se instaló Flanger",
        blank=True, 
        null=True
        )
    razon_no_flanger = models.CharField(
        max_length = 60,
        default= "No hay stock",
        verbose_name= "Razón por la cual no se instaló el flanger",
        blank=True,
        null=True
    )
    ############### 5 Pestaña ###############

    tipo_activacion = models.CharField(
        max_length=30,
        verbose_name="Tipo activación",
        default= "Presencial",
        blank=True,
        null=True
        )
    datafono = models.CharField(
        max_length=2,
        choices=PREGUNTA,
        verbose_name="¿Comercio está interesado en Datafóno?"
    )
    interesado = models.CharField(
        max_length=2,
        choices=PREGUNTA,
        verbose_name= "¿Comercio está interesado en ser corresponsal?"
    )
    proveedor = models.CharField(
        max_length=30,
        default="FirstSource",
        blank=True,
        null=True
        )
    
    contingencia = models.CharField(
        max_length=2, 
        choices=PREGUNTA,
        default="NO",
        blank=True,
        null=True,
        verbose_name='¿Cliente contingencia?'  
        )
    
    etnico = models.CharField(
        max_length=70, 
        choices=ETNICO, 
        verbose_name='El comercio se identifica con algún grupo etnico en particular?'
        )
    transaccion = models.CharField(
        max_length=2,
        choices=PREGUNTA,
        blank=True,
        null=True
        )
    codigo_transaccion = models.IntegerField(
        blank=True, null=True
    )
    no_transaccion =models.CharField(
        max_length=30, 
        blank=True, 
        null=True)

    cambio = models.BooleanField(
        default=False,
        )
    
    FACTURA = [
        ('Vinculacion Estandar', 'Vinculacion Estandar'),
        ('Vinculacion Sin activacion Perfil', 'Vinculacion Sin activacion Perfil'), 
        ('Remarcacion', 'Remarcacion'),
        ('Comercio No acepto', 'Comercio No acepto'),  
    ]
    
    sig_factura = models.CharField(
        max_length=45, choices=FACTURA,
        blank=True,
        null=True)
    
    dir_a = models.ForeignKey(
        Direccion,
        on_delete=models.CASCADE,
        
        null=True)
    
    num_dir1 = models.CharField(max_length=10, null=True)

    num_dir2 = models.CharField(max_length=10,null=True)
    
    complemento = models.ForeignKey(
        ComplementoDireccion,
        on_delete=models.CASCADE,
        null=True
        )
    detail_complemento = models.CharField(max_length=10, null=True, blank=True)

    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, blank=True, null=True)
        
    
    def save(self, *args, **kwargs):
    
        self.direccion = str(self.dir_a.direccion) + " " + str(self.num_dir1) + " # " + str(self.num_dir2) + " " + str(self.complemento.complemento)
    
        if self.celular == None:
            self.celular = self.identificacion
        
        ################ Se realizó registro en DaviPlata ##############

        if self.registro_daviplata == "SI":
            self.motivo_no_registro = None
        elif self.registro_daviplata == "Ya esta activo":
            self.motivo_no_registro = None
        elif self.registro_daviplata == "Modo Contingencia":
            self.motivo_no_registro_id = 9

        ##################PERFIL NEGOCIO ##########
        if self.se_registro == "SI":
            self.no_register = None
        elif self.se_registro == "Ya esta activo":
            self.no_register = None
        elif self.se_registro == "Modo contingencia":
            self.no_register = "Modo contingencia"
            self.contingencia = "SI"

        ##########TENCARD#################
        if self.solicito_tencard == "SI":
            self.porque_no_solicito = None
        elif self.solicito_tencard == "Ya tiene la tencard":
            self.porque_no_solicito = None
        elif self.solicito_tencard == "Modo Contingencia":
            self.porque_no_solicito = "Modo contingencia"
        ###############CODIGO TRANSACCION#############################
        if self.codigo_transaccion == None:
            self.transaccion = "NO"
        else:
            self.transaccion = "SI"
        ##################sticker########################
        if self.sticker == "SI":
            self.razon_no_sticker = None

        ########Condicion informe sig #########

        if self.tipo_gestion.id == 1 :
            self.registro_daviplata = "SI"
            self.motivo_no_registro = None
            self.se_registro = "SI"
            self.register = None
            self.solicito_tencard = "SI"
            self.porque_no_solicito = None
            self.sticker = "SI"

        elif self.tipo_gestion.id == 2 :
            self.registro_daviplata = "SI"
            self.motivo_no_registro = None
            self.se_registro = "NO"
            self.solicito_tencard = "NO"
            self.sticker = "SI"
        
        elif self.tipo_gestion.id == 3 :
            self.registro_daviplata = "Ya esta activo"
            self.se_registro = "SI"
            self.register = None
            self.solicito_tencard = "SI"
            self.porque_no_solicito = None
            self.sticker = "SI"
            if self.registro_daviplata == "Ya esta activo":
                self.motivo_no_registro_id = 1

        elif self.tipo_gestion.id == 4 :
            ###PASADO TIEMPO BORRAR ###
            # self.registro_daviplata = "NO"
            # self.se_registro = "NO"
            # self.solicito_tencard = "NO"
            # self.sticker = "NO"
            self.codigo_transaccion = None

        ################¿Se realizo  registro en perfil mi negocio?####
        super(Vinculacion, self).save(*args, **kwargs)    

    ############## 6 Pestaña ####################

class NovedadVinculacion(models.Model):
    id_vinculacion = models.ForeignKey(
        Vinculacion, 
        on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.id_vinculacion.cambio  = True
        
        self.id_vinculacion.save()

        super(NovedadVinculacion, self).save(*args, **kwargs)

class Gestores(models.Model):
    ESTADO= [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo')
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        verbose_name= 'Usuario',
        related_query_name= 'user_asistencia'
    )
    celular = models.CharField(max_length=10)
    barrio = models.CharField(max_length=35, null= True)
    fecha_contrato = models.DateField(blank=True, null = True)
    fecha_retiro = models.DateField(null=True, blank=True)
    estado = models.CharField(
        max_length=15, 
        choices=ESTADO,
        null=True,
        default = 'Activo')
    proveedor = models.CharField(
        max_length=30, 
        default="Firstsource", 
        null=True)

@receiver(post_save, sender=User)
def create_user_Gestores(sender, instance, created, **kwargs):
    if created and instance.cliente.r_s == "Daviplata":
        Gestores.objects.create(user=instance)
