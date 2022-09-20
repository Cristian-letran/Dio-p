from re import search
from django.contrib import admin
from related_admin import RelatedFieldAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from . models import Cargue, Recepcion, Planilla, Est_planilla, Sucursales, Destino, Descargue, Imprimir
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.text import format_lazy
from applications.fisico.models import Fisico
from simple_history.admin import SimpleHistoryAdmin
from django.http import HttpResponse
import datetime

class PlanillaResource(resources.ModelResource):
    guia = Field(attribute='guia', column_name='GUIA')
    guia__direccion = Field(attribute='guia__direccion', column_name='DIRECCION')
    guia__destinatario = Field(attribute='guia__destinatario', column_name='DESTINATARIO')
    guia__id_ciu = Field(attribute='guia__id_ciu', column_name='CIUDAD')
    guia__bolsa = Field(attribute='guia__bolsa', column_name='BOLSA')
    guia__mensajero__courrier = Field(attribute='guia__mensajero__courrier', column_name='COURRIER')
    guia__fecha_recepcion = Field(attribute='guia__fecha_recepcion', column_name='FECHA GESTION')
    guia__mot = Field(attribute='guia__mot', column_name='CALIFICACION')

    class Meta:
        model = Planilla

        fields = (
            'guia', 'guia__direccion', 
            'guia__destinatario', 'guia__id_ciu', 
            'guia__bolsa', 'guia__mensajero__courrier',
            'guia__fecha_recepcion', 'guia__mot')

class Recepinline (admin.StackedInline):
    model = Fisico
    fields = ('recepcion',)
    raw_id_fields = ["recepcion"]
    
class Planillainline (admin.TabularInline):
    model = Planilla
    extra = 5
    raw_id_fields = ["guia"]

##################################################

@admin.register(Cargue)
class CargueAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    inlines = [Planillainline,]
    save_on_top = False
    # fields = ('id', 'guia'),
    filter_horizontal = ('guia', )
    list_display = ['id', 'fecha',]
    search_fields = ('id', 'full_name__courrier')
    list_filter = ['full_name__id', 'fecha']
    date_hierarchy = 'fecha'
    list_per_page = 12
    success_url = '.'
    icon_name  =  'motorcycle'

@admin.register(Planilla)
class PlanillaAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('id', 'guia', 'full_name',  'fecha', 'user')
    search_fields = ('id', 'guia__id_guia')
    list_filter = ('full_name', 'fecha')
    list_per_page = 10
    date_hierarchy = ('fecha')
    resource_class = PlanillaResource
    

@admin.register(Recepcion)
class RecepcionAdmin(ImportExportModelAdmin, RelatedFieldAdmin):
    fields = (('motivo'), 'estado', 'guia', 'user')
    # inlines = [Recepinline ,]
    raw_id_fields = ["motivo"]
    list_display = (
        'guia', 'motivo', 'fecha', 'motivo__id')
    # readonly_fields = ('estado',)
    list_per_page = 10
    search_fields = ('guia__id_guia',)

@admin.register(Est_planilla)
class Est_plaAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado')

@admin.register(Destino)
class DestinoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('sucursal', 'destino', 'fecha', 'guia')
    list_filter = ('destino', 'fecha')
    date_hierarchy = ('fecha')

@admin.register(Imprimir)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_imprimir')

admin.site.register(Sucursales)
admin.site.register(Descargue)










    

    

