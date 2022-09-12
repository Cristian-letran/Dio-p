from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import datos_g, Orden, Cubrimiento, Agenda, Postal
from import_export.fields import Field

class CubrimientoResource(resources.ModelResource):
    
    class Meta:
        model = Cubrimiento
        import_id_fields = ('id_cubrimiento',) 

class datos_gResource(resources.ModelResource):
    
    class Meta:
        model = datos_g     
        import_id_fields = ('seudo_dg',)   
       

class AgendaResource(resources.ModelResource):
    # id_agenda__fecha = Field(attribute='id_agenda__fecha', column_name='FECHA FISICO')
    # id_agenda__fecha_recepcion = Field(attribute='id_agenda__fecha_recepcion', column_name='FECHA GESTION')
    # id_agenda__mot = Field(attribute='id_agenda__mot', column_name='MOTIVO')
    # id_agenda__id_est = Field(attribute='id_agenda__id_est', column_name='ESTADO')
    # id_agenda__bolsa = Field(attribute='id_agenda__bolsa', column_name='BOLSA')
    # id_agenda__id_guia = Field(attribute='id_agenda__id_guia', column_name='GUIA')

    class Meta:
        model = Agenda  
        import_id_fields = ('id_agenda',)   
        fields = (
            'id_agenda', 'id_agenda__fecha', 
            'id_agenda__fecha_recepcion','id_agenda__mot', 
            'id_agenda__id_est', 'id_agenda__bolsa',
            'id_agenda__id_guia', 'id_agenda__cod_vis',
            )
#####################################################################
@admin.register(datos_g)
class datos_gAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = datos_gResource
    list_per_page = 12
    search_fields = ("seudo_dg__id_guia",)
    list_display = ('seudo_dg', 'direccion', 'd_i', 'id_ciu', 'barrio', 'fecha', )
    list_filter = ('fecha', 'mot')
    icon_name  =  'directions'
    date_hierarchy = ('fecha')
    raw_id_fields = ['id_ciu',]

@admin.register(Orden)
class ordenAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('orden',)

@admin.register(Cubrimiento)
class CubrimientoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id_cubrimiento', 'oficina', 'direccion', 'dane')
    resource_class = CubrimientoResource

@admin.register(Agenda)
class CubrimientoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id_agenda",)
    raw_id_fields = ['id_agenda',]
    resource_class = AgendaResource

@admin.register(Postal)
class PostalAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id","departamento",)
    list_per_page = 12
    search_fields = ("id",)






    
