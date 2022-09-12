
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from  . models import courrier, vehiculo, Tipo_vehiculo, Marca_vehiculo, Linea_vehiculo, Tipo_infraccion, Modelos

class VehiculoResource(resources.ModelResource):
    class Meta:
        model = vehiculo
        import_id_fields = ('id_veg',)

@admin.register(courrier)
class courrierAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    icon_name  =  'person_outline'
    raw_id_fields = ["id_ciu",]
    fields = (('d_i', 'courrier'),
            ('cel', 'dir'),('id_ciu','id_veh',),
            ('infraccion', 'licencia',), ('est_courrier'))
    list_filter = ('est_courrier',)
    raw_id_fields = ["id_veh", "id_ciu",]
    search_fields = ("d_i", "courrier")
    list_display = ('courrier', 'd_i', 'cel', 'est_courrier')
    list_per_page = 5

@admin.register(vehiculo)
class VehiculoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VehiculoResource
    list_display = ('id_veg', 'name', 'cc', 'marca', 'cilindraje')
    list_per_page = 5
    search_fields = ('cc',)

@admin.register(Modelos)
class EstadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('modelo',)

@admin.register(Marca_vehiculo)  
class MarcaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('marca',)

@admin.register(Linea_vehiculo)  
class LineaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('linea',)

@admin.register(Tipo_infraccion)
class LineaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('infraccion',)

admin.site.register(Tipo_vehiculo)
