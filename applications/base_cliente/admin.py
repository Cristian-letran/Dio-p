from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Bd_clie, Agenda_bd

#####funcion eliminar toda la data 
def Actualizar(modeladmin, request, queryset):
    queryset.update.all()

class BdResource(resources.ModelResource):
    class Meta:
        model = Bd_clie
        import_id_fields = ('seudo_bd',)

class AgendaResource(resources.ModelResource):
    class Meta:
        model = Agenda_bd
        import_id_fields = ('id_agenda',)   
        fields = (
            'id_agenda', 'id_agenda__fisicos', 'id_agenda__guias__fecha', 'id_agenda__bd_paquete__fecha',
            'id_agenda__guias__fecha_recepcion', 'id_agenda__guias__mot', 
            'id_agenda__guias__id_est', 'id_agenda__guias__bolsa',
            'id_agenda__guias__id_guia', 'id_agenda__guias__cod_vis',
            'id_agenda__bd_paquete__bolsa', 'id_agenda__guias'
            )
        
#----------------------------------------------------
@admin.register(Bd_clie)
class bd_clieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = [Actualizar]
    resource_class = BdResource
    model = Bd_clie
    date_hierarchy = ('fecha')
    readonly_fields = ('sucursal',)
    list_display = ('seudo_bd', 'jornada', 'tipo',  'id_est_clie')
    list_filter = ('fecha', 'fisicos')
    search_fields = ('seudo_bd',)
    raw_id_fields = ("id_est_clie",)
    icon_name  =  'cloud_upload'

@admin.register(Agenda_bd)
class Bd_agenda(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id_agenda",)
    raw_id_fields = ['id_agenda',]
    resource_class = AgendaResource
    








   



