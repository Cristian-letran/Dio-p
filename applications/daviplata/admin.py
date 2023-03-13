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


admin.site.register(Red)
admin.site.register(TipoNoEfectiva)
admin.site.register(TipoEstablecimiento)
admin.site.register(OtroTipoEstablecimiento)
admin.site.register(TipoSenalizacion)
admin.site.register(OtroTipoSenalizacion)
admin.site.register(Acude)
admin.site.register(AcudeOtro)
admin.site.register(Medio)
