from django.contrib import admin
from django.db.models.query_utils import FilteredRelation
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Paquete, Fisico, Bolsa, Mesa, Motivo_mesa, Cobertura
from simple_history.admin import SimpleHistoryAdmin
from related_admin import RelatedFieldAdmin
from applications.ruta.models import Recepcion
import datetime

@admin.action(description='actualizar fecha')
def update_date(modeladmin, request, queryset):
    now = datetime.datetime.now()
    queryset.update(fecha_visita = now)

class FisicoResource(resources.ModelResource):
    class Meta:
        model = Fisico
        import_id_fields = ('id_guia',) 
        fields = ("id_guia", "bolsa", "destinatario", "d_i", "proceso__proceso", "image_mesa__estado_img", "image_mesa__fecha", 'fecha_visita', 'mot__motivo', 'id_ciu__departamento__departamento')
        #
class BolsaResource(resources.ModelResource):
    class Meta:
        import_id_fields = ('bolsa',)
        model = Bolsa
        fields = ("bolsa", "mot")
        
class CoberturaResource(resources.ModelResource):
    class Meta:
        model = Cobertura
        import_id_fields = ('bolsa',)
        exclude = ('user',)

@admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    queryset.update(estado_mesa= True)
#--------------------------------------------------------------------
@admin.register(Paquete)    
class PaqueteAdmin(RelatedFieldAdmin,ImportExportModelAdmin, admin.ModelAdmin):
    list_filter = ('fecha',)
    raw_id_fields = ("seudo",)
    list_display = ('seudo', 'bolsa', 'fecha', 'estado')
    search_fields = ('bolsa__bolsa', )
    icon_name  =  'local_shipping'
    list_per_page = 5

@admin.register(Fisico)
class FisicoAdmin(RelatedFieldAdmin,SimpleHistoryAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    history_list_display = ["mot", "mensajero"]
    resource_class = FisicoResource
    list_display = ['id_guia', 'fecha_visita', 'fisico', 'bolsa', 'fecha', 'estado', 'mensajero', 'fecha_planilla', 'fecha_recepcion']
    date_hierarchy = ('fecha_visita')
    list_filter = ('est_planilla', 'mensajero', 'image_mesa__estado_img', 'mot', 'id_ciu__departamento__departamento')
    search_fields = ('bolsa', 'id_guia', 'bolsa')
    list_per_page = 100
    raw_id_fields = ['id_ciu',]
    actions = [update_date]
    
@admin.register(Bolsa)    
class BolsaAdmin(RelatedFieldAdmin,ImportExportModelAdmin, admin.ModelAdmin):
    
    search_fields = ('bolsa',)
    resource_class = BolsaResource
    list_per_page = 5
    list_display = ('bolsa', 'mot')

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    raw_id_fields = ["guia"]
    list_display = ('guia', 'id_motivo_m', 'observacion', )
    search_fields = ('guia__id_guia',)
    list_filter = ("id_motivo_m",)
    list_per_page = 5

@admin.register(Cobertura)
class CoberturaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = [make_published]
    resource_class = CoberturaResource
    date_hierarchy = ('fecha')
    list_display = ('bolsa', 'fecha', 'estado_mesa')
    list_per_page = 5
    search_fields = ('bolsa__bolsa',)
    raw_id_fields = ['bolsa',]



    
admin.site.register(Motivo_mesa)










