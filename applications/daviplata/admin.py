from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from import_export.widgets import DateWidget
from related_admin import RelatedFieldAdmin

from . models import (
    Daviplata, Red,
    TipoEstablecimiento, 
    Acude,
    AcudeOtro,
    Vinculacion,
    TipoGestion,
    Categorias,
    MotivoNoRegistro, 
    TipoActivacion,
    NovedadVinculacion,
    Gestores
    )

class GestoresResource(resources.ModelResource):
    user__d_i = Field(attribute='user__d_i', column_name='Documento')
    user__nombres = Field(attribute='user__nombres', column_name='Nombre')
    user__tipo_d_i = Field(attribute='user__tipo_d_i', column_name='Tipo ID')
    celular = Field(attribute='celular', column_name='Celular')
    user__genero = Field(attribute='user__genero', column_name='Genero')
    fecha_contrato = Field(attribute='fecha_contrato', column_name='Fecha de contratación')
    user__ciudad__ciudad = Field(attribute='user__ciudad__ciudad', column_name='Ciudad en la que labora actualmente el asesor')
    user__ciudad__departamento = Field(attribute='user__ciudad__departamento', column_name='Departamento en la que labora actualmente el asesor')
    barrio = Field(attribute='barrio', column_name='Barrio en el cual labora actualmente')
    proveedor = Field(attribute='proveedor', column_name='Nombre Proveedor')
    fecha_retiro = Field(attribute='fecha_retiro', column_name='Fecha de Retiro del asesor')
    estado = Field(attribute='estado', column_name='Estado')
    
    class Meta:
        model = Gestores
        fields = (
           'user__d_i', 'user__nombres', 'user__tipo_d_i',
            'celular', 'user__genero', 'fecha_contrato',
             'user__ciudad__ciudad', 'user__ciudad__departamento',
            'barrio', 'proveedor', 'fecha_retiro', 'estado'
          
           )
        export_order = (
           'user__d_i', 'user__nombres', 'user__tipo_d_i',
            'celular', 'user__genero', 'fecha_contrato',
             'user__ciudad__ciudad', 'user__ciudad__departamento',
            'barrio', 'proveedor', 'fecha_retiro', 'estado'
        )

class DaviplataResource(resources.ModelResource):
    
    class Meta:
        model = Daviplata
        import_id_fields = ('id_ruta',) #

class VinculacionResource(resources.ModelResource):
      tipo_activacion = Field(attribute='tipo_activacion', column_name='Tipo activación')
      tipo_gestion__nombre = Field(attribute='tipo_gestion__nombre', column_name='Tipo de gestion')
      celular = Field(attribute='celular', column_name='No. celular activado en DaviPlata')
      celular_confirma = Field(attribute='celular_confirma', column_name='Confirmación No. celular activado en DaviPlata')
      nombre = Field(attribute='nombre', column_name='Nombre del cliente DaviPlata')
      nombre_comercio = Field(attribute='nombre_comercio', column_name='Nombre del comercio')
      categoria__nombre = Field(attribute='categoria__nombre', column_name='¿A cual de las siguientes categorias pertenece el comercio?')
      registro_daviplata = Field(attribute='registro_daviplata', column_name='¿Se realizo registro en DaviPlata?')
      registro_daviplata = Field(attribute='registro_daviplata', column_name='¿Se realizo registro en DaviPlata?')
      motivo_no_registro__nombre = Field(attribute='motivo_no_registro__nombre', column_name='¿Por qué no se realizo el registro DaviPlata?')
      se_registro = Field(attribute='se_registro', column_name='¿Se realizo  registro en perfil mi negocio?')
      no_register = Field(attribute='no_register', column_name='¿Por qué no se realizo el registro en perfil mi negocio?')
      solicito_tencard = Field(attribute='solicito_tencard', column_name='¿Se solicitó la tentcard?')
      porque_no_solicito = Field(attribute='porque_no_solicito', column_name='¿Por qué no se solicitó la tentcard?')
      transaccion = Field(attribute='transaccion', column_name='¿Se realizó transacción de $1?')
      no_transaccion = Field(attribute='no_transaccion', column_name='¿Por qué no se realizó la transacción de $1?')
      sticker = Field(attribute='sticker', column_name='Se pego Sticker')
      razon_no_sticker = Field(attribute='razon_no_sticker', column_name='Razon por la cual no se pegó el sticker')
      flanger = Field(attribute='flanger', column_name='Se instalo Flanger')
      razon_no_flanger = Field(attribute='razon_no_flanger', column_name='Razon por la cual no se instaló el flanger')
      fecha_visita = Field(attribute='fecha_visita', column_name='Fecha de la visita',
                           widget=DateWidget(format='%d/%m/%Y')) 
      user__d_i = Field(attribute='user__d_i', column_name='Cedula del asesor visitador')
      direccion = Field(attribute='direccion', column_name='Dirección Comercio')
      dane__id = Field(attribute='dane__id', column_name='Código de Ciudad ')
      dane__departamento__departamento = Field(attribute='dane__departamento__departamento', column_name='Departamento')
      dane__ciudad = Field(attribute='dane__ciudad', column_name='Municipio')
      localidad = Field(attribute='localidad', column_name='Localidad o Zona')
      barrio= Field(attribute='barrio', column_name='Barrio')
      c_rut= Field(attribute='c_rut', column_name='¿Comercio cuenta con RUT?')
      datafono= Field(attribute='datafono', column_name='¿Comercio está interesado en Datafóno?')
      interesado= Field(attribute='interesado', column_name='¿Comercio está interesado en ser corresponsal?')
      proveedor= Field(attribute='proveedor', column_name='Nombre de empresa (Proveedor)')
      contingencia= Field(attribute='contingencia', column_name='¿Cliente contingencia?')
      etnico= Field(attribute='etnico', column_name='El comercio se identifica con algún grupo etnico en particular?')
      
      class Meta:
        
        model = Vinculacion
        name = "Export/Import only book names"
        fields = (
           'tipo_activacion', 'tipo_gestion__nombre', 
           'celular', 'celular_confirma', 'nombre',
            'nombre_comercio', 'categoria__nombre', 'registro_daviplata',
            'motivo_no_registro__nombre', 'se_registro', 'no_register',
            'solicito_tencard', 'porque_no_solicito', 'sticker',
            'razon_no_sticker', 'flanger', 'razon_no_flanger',
            'fecha_visita', 'user__d_i', 'direccion', 'dane__id',
            'dane__ciudad', 'dane__departamento__departamento', 
            'localidad', 'barrio', 'latitud', 'longitud',
            'c_rut', 'datafono', 'interesado', 'proveedor', 'contingencia',
            'etnico', 'author', 'transaccion', 'no_transaccion', 'identificacion'

           )
        export_order = (
           'tipo_activacion', 'tipo_gestion__nombre', 
           'celular', 'celular_confirma', 'nombre',
            'nombre_comercio', 'categoria__nombre', 'registro_daviplata',
            'motivo_no_registro__nombre', 'se_registro', 'no_register',
            'solicito_tencard', 'porque_no_solicito', 
            'transaccion', 'no_transaccion', 'sticker',
            'razon_no_sticker', 'flanger', 'razon_no_flanger',
            'fecha_visita', 'user__d_i', 'direccion', 'dane__id',
            'dane__ciudad', 'dane__departamento__departamento', 
            'localidad', 'barrio', 'latitud', 'longitud',
            'c_rut', 'datafono', 'interesado', 'proveedor', 'fecha_visita', 'contingencia',
            'etnico', 'identificacion'
            )
        

@admin.register(Daviplata)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('id_ruta', 'nombre_establecimiento', 'visita_efectiva', 'fecha_encuesta', 'direccion_base', 'user')
   resource_class = DaviplataResource
   date_hierarchy = ('fecha_encuesta')
   list_filter = ('fecha_cargue', 'visita_efectiva', 'user')
   search_fields = ('nombre_establecimiento', 'id_ruta')

@admin.register(Red)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(TipoEstablecimiento)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(Acude)
class DaviplaAcudetaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(AcudeOtro)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(Vinculacion)
class VinculacionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('fecha_registro', 'celular', 'fecha_visita', 'user','latitud','registro_daviplata','motivo_no_registro','se_registro', 'no_register')
   list_filter = ('fecha_visita','tipo_gestion')
   date_hierarchy = ('fecha_visita')
   search_fields = ('user__nombres', 'celular')
   resource_class = VinculacionResource


@admin.register(TipoGestion)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('id',)

@admin.register(Categorias)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(MotivoNoRegistro)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('id','nombre',)

@admin.register(TipoActivacion)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(NovedadVinculacion)
class novedadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('id_vinculacion',)


class GestorAdmin(ImportExportModelAdmin, RelatedFieldAdmin):
   list_display = ('user__d_i', 'user__nombres', 
                   'estado', 'user__d_i', 'fecha_contrato',
                   'celular', 'user__genero', 'user__ciudad__ciudad',
                     'user__ciudad__departamento', 'user__is_staff')
   resource_class = GestoresResource
   exclude = ('proveedor',)
   list_filter = ('estado',)

admin.site.register(Gestores, GestorAdmin)

##
   
   







