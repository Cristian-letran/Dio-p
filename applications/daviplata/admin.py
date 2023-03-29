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
    Categorias
    )

class DaviplataResource(resources.ModelResource):
    
    class Meta:
        model = Daviplata
        import_id_fields = ('id_ruta',) #

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
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(AcudeOtro)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)
   
@admin.register(Medio)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)

@admin.register(Vinculacion)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('identificacion',)

@admin.register(TipoGestion)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('id',)

@admin.register(Categorias)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('nombre',)






