from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import Cliente, Ciudad, Departamento, Oficinas, Localidad, Zona, Barrio

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
    list_display = ('id_clie', 'r_s')

@admin.register(Oficinas)
class OficinasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','direccion')
    search_fields = ('id',)
    list_per_page = 7

class LocalidadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)           

class ZonaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'zona') 

class BarrioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name_barrio', 'zona')
    #readonly_fields = ('zona',)

admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Zona, ZonaAdmin)
admin.site.register(Barrio, BarrioAdmin)
