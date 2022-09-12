from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import Cliente, Ciudad, Departamento, Oficinas

class CiudadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    raw_id_fields = ('departamento',)
    list_display = ('id', 'ciudad', 'departamento', 'cubrimiento')
    search_fields = ('id', 'ciudad')
    list_filter = ('ciudad', 'departamento', 'cubrimiento')
    icon_name  =  'location_city'

@admin.register(Departamento)
class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('departamento', )

@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    raw_id_fields = ('id_ciu',)

@admin.register(Oficinas)
class OficinasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','direccion')
    search_fields = ('id',)
    list_per_page = 7

admin.site.register(Ciudad, CiudadAdmin)
