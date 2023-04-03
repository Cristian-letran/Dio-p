from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from . models import (
    Daviplata, Red, TipoNoEfectiva, 
    TipoEstablecimiento, 
    OtroTipoEstablecimiento, 
    TipoSenalizacion, 
    OtroTipoSenalizacion,
    Acude,
    AcudeOtro,
    Medio,
    Vinculacion,
    TipoGestion,
    Categorias,
    MotivoNoRegistro, 
    TipoActivacion
    )

class DaviplataResource(resources.ModelResource):
    
    class Meta:
        model = Daviplata
        import_id_fields = ('id_ruta',) #

class VinculacionResource(resources.ModelResource):
   
    class Meta:
        
        model = Vinculacion
        name = "Export/Import only book names"
        fields = (
           'tipo_activacion__nombre', 'tipo_gestion__nombre', 
           'celular', 'celular_confirma', 'nombre',
            'nombre_comercio', 'categoria__nombre', 'registro_daviplata',
            'motivo_no_registro__nombre', 'se_registro', 'no_registro',
            'solicito_tencard', 'porque_no_solicito', 'sticker',
            'razon_no_sticker', 'flanger', 'razon_no_flanger',
            'fecha_visita', 'user__d_i', 'direccion', 'dane',
            'dane__ciudad', 'dane__departamento__departamento', 
            'localidad', 'barrio', 'latitud', 'longitud',
            'c_rut', 'datafono', 'interesado', 'proveedor', 'contingencia',
            'etnico', 'author'

           )
        export_order = (
           'tipo_activacion__nombre', 'tipo_gestion__nombre', 
           'celular', 'celular_confirma', 'nombre',
            'nombre_comercio', 'categoria__nombre', 'registro_daviplata',
            'motivo_no_registro__nombre', 'se_registro', 'no_registro',
            'solicito_tencard', 'porque_no_solicito', 'sticker',
            'razon_no_sticker', 'flanger', 'razon_no_flanger',
            'fecha_visita', 'user__d_i', 'direccion', 'dane',
            'dane__ciudad', 'dane__departamento__departamento', 
            'localidad', 'barrio', 'latitud', 'longitud',
            'c_rut', 'datafono', 'interesado', 'proveedor', 'contingencia',
            'etnico', 
            )
        

@admin.register(Daviplata)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('id_ruta', 'nombre_establecimiento', 'direccion_base', 'user')
   resource_class = DaviplataResource

@admin.register(Red)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(TipoNoEfectiva)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(TipoEstablecimiento)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(OtroTipoEstablecimiento)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(TipoSenalizacion)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(OtroTipoSenalizacion)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(Acude)
class DaviplaAcudetaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(AcudeOtro)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)
   
@admin.register(Medio)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(Vinculacion)
class VinculacionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('identificacion',)
   resource_class = VinculacionResource


@admin.register(TipoGestion)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('id',)

@admin.register(Categorias)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(MotivoNoRegistro)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(TipoActivacion)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)







