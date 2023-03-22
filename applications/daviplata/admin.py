from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from . models import (
    Daviplata, Red, TipoNoEfectiva, 
    TipoEstablecimiento, 
    OtroTipoEstablecimiento, 
    TipoSenalizacion, 
    OtroTipoSenalizacion,
    Acude,
    AcudeOtro,
    Medio,
    )

@admin.register(Daviplata)
class DaviplataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   list_display = ('id_ruta', 'nombre_establecimiento', 'direccion_base', 'user')

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

