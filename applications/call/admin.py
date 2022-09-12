from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from . models import Datos_t, Indicativo, Telefono, Pregunta, Auditoria, calificacion, Tel, Informe_call
from django.db import transaction
from simple_history.admin import SimpleHistoryAdmin



class DatossResource(resources.ModelResource):
    class Meta:
        model = Datos_t
        fields = (('id', 'd_i', 'telefono', 'indicativo', 'activo' ))

class AuditoriaResource(resources.ModelResource):

    entregas__seudo__fecha = Field (attribute='entregas__seudo__fecha', column_name='FECHA BASE')
    entregas__bolsa = Field (attribute='entregas__bolsa', column_name='BOLSA')
    entregas__id_est = Field (attribute='entregas__id_est', column_name='ESTADO')
    entregas__d_i = Field (attribute='entregas__d_i', column_name='ID CLIENTE')
    entregas__destinatario = Field (attribute='entregas__destinatario', column_name='CLIENTE')
    entregas__mensajero = Field (attribute='entregas__mensajero', column_name='MENSAJERO')
    entregas__direccion = Field (attribute='entregas__direccion', column_name='DIRECCION CITA')
    entregas__id_ciu__ciudad = Field (attribute='entregas__id_ciu__ciudad', column_name='CIUDAD')
    entregas__guia_descargue__fecha = Field (attribute='entregas__guia_descargue__fecha', column_name='FECHA VISITA')
    motivo_call = Field (attribute='motivo_call', column_name='RESULTADO')
    entregas__tel = Field (attribute='entregas__tel', column_name='TELEFONO')
    fecha = Field (attribute='fecha', column_name='FECHA CALL')
    
    class Meta:
        model = Auditoria
        fields = (( 'entregas__seudo__fecha', 'entregas__bolsa',
                    'entregas__id_est', 'entregas__d_i',
                    'entregas__destinatario', 'entregas__mensajero',
                    'entregas__direccion', 'entregas__id_ciu__ciudad',
                    'entregas__guia_descargue__fecha', 'motivo_call',
                    'entregas__tel', 'fecha',
                    'pregunta_1', 'calificacion_1__calficacion', 
                    'pregunta_2', 'calificacion_2__calficacion',
                    'pregunta_3', 'calificacion_3__calficacion',
                    'pregunta_4', 'calificacion_4__calficacion',
                    'observacion',

                   ))
        export_order = (
                    'entregas__seudo__fecha', 'entregas__bolsa',
                    'entregas__id_est', 'entregas__d_i',
                    'entregas__destinatario', 'entregas__mensajero',
                    'entregas__direccion', 'entregas__id_ciu__ciudad',
                    'entregas__guia_descargue__fecha', 'motivo_call',
                    'entregas__tel', 'fecha',
                    'pregunta_1', 'calificacion_1__calficacion', 
                    'pregunta_2', 'calificacion_2__calficacion',
                    'pregunta_3', 'calificacion_3__calficacion',
                    'pregunta_4', 'calificacion_4__calficacion',
                    'observacion',
        )

class TelefonoResource(resources.ModelResource):
    
    id = Field (attribute='id', column_name='PSEUDO')
    id__id__seudo__tarjeta = Field (attribute='id__id__seudo__tarjeta', column_name='TARJETA')
    id__id__guia_d_g__marca = Field (attribute='id__id__guia_d_g__marca', column_name='MARCA')
    id__id__d_i = Field (attribute='id__id__d_i', column_name='CEDULA')
    id__id__destinatario = Field (attribute='id__id__destinatario', column_name='CLIENTE')
    id__id__user__ciudad__ciudad = Field (attribute='id__id__user__ciudad__ciudad', column_name='BODEGA')
    id__id__id_ciu__ciudad = Field (attribute='id__id__id_ciu__ciudad', column_name='CIUDAD BASE')
    id__id__guia_d_g__direccion = Field (attribute='id__id__guia_d_g__direccion', column_name='DIRECCION')
    id__id__mot__motivo = Field (attribute='id__id__mot__motivo', column_name='RESULTADO')
    id__id__fecha_recepcion = Field (attribute='id__id__fecha_recepcion', column_name='FECHA GESTIÓN')
    id__tel = Field (attribute='id__tel', column_name='TEL')
    id__motivo_call = Field (attribute='id__motivo_call', column_name='ESTADO CALL')
    id__fecha_call = Field (attribute='id__fecha_call', column_name='FECHA CALL')
    id__observacion = Field (attribute='id__observacion', column_name='OBSERVACIONES')
    id__user = Field (attribute='id__user', column_name='ASESOR')
    id__id__direccion = Field (attribute='id__id__direccion', column_name='DIRECCION CITA')
    id__id__id_ciu__ciudad = Field (attribute='id__id__id_ciu__ciudad', column_name='CIUDAD CITA')
    id__id__id_ciu__departamento__departamento = Field (attribute='id__id__id_ciu__departamento__departamento', column_name='DEPARTAMENTO')
    id__id__proceso__tipo_e = Field (attribute='id__id__proceso__tipo_e', column_name='TIPO DE ENTREGA')
    id__id__guia_d_g__oficina = Field(attribute='id__id__guia_d_g__oficina',column_name='OFICINA CITA')
    id__id__guia_d_g__autor = Field(attribute='id__id__guia_d_g__autor',column_name='AUTORIZADO')
    id__fecha = Field(attribute='id__fecha',column_name='FECHA AGENDAMIENTO')
    id__motivo_call__tipificacion = Field (attribute='id__motivo_call__tipificacion', column_name='TIPIFICACION')
    id__id__id_est__motivo = Field (attribute='id__id__id_est__motivo', column_name='ESTADO CUSTODIA')
    

    class Meta:
        model = Telefono
        
        fields = (
            'id', 'id__id__seudo__tarjeta', 
            'id__id__guia_d_g__marca', 'id__id__d_i', 
            'id__id__destinatario', 'id__id__user__ciudad__ciudad', 
            'id__id__id_ciu__ciudad', 'id__id__guia_d_g__direccion', 
            'id__id__mot__motivo', 'id__id__fecha_recepcion',
            'id__tel', 'id__motivo_call', 'id__fecha_call', 
            'id__observacion', 'id__user', 
            'id__id__direccion', 'id__id__id_ciu__ciudad', 
            'id__id__id_ciu__departamento__departamento', 'id__id__proceso__tipo_e', 
            'id__motivo_call__tipificacion', 'id__id__id_est__motivo'
        )
        export_order = (
            'id', 'id__id__seudo__tarjeta', 
            'id__id__guia_d_g__marca', 'id__id__d_i', 'id__id__destinatario', 
            'id__id__user__ciudad__ciudad', 'id__id__id_ciu__ciudad', 
            'id__id__guia_d_g__direccion', 'id__id__mot__motivo', 
            'id__id__fecha_recepcion', 'id__tel', 
            'id__motivo_call', 'id__fecha_call', 
            'id__observacion', 'id__user', 
            'id__id__direccion', 'id__id__id_ciu__ciudad', 
            'id__id__id_ciu__departamento__departamento', 'id__id__proceso__tipo_e', 
            'id__id__guia_d_g__oficina', 'id__id__guia_d_g__autor', 
            'id__fecha', 'id__motivo_call__tipificacion',
        )

class datos_tAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    
    fields = (('d_i', 'telefono',))
    resource_class = DatossResource
    list_per_page = 12
    history_list_display = ["status"]
    list_display = ('telefono', 'activo', 'user', 'd_i')
    SIMPLE_HISTORY_REVERT_DISABLED=True
    raw_id_fields = ["telefono",]
    search_fields = ('d_i',)
    # fields = ('d_i', 'telefono', 'indicativo')

    icon_name  =  'call'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.user = request.user 
        obj.save()    

class IndicativoAdmin(admin.ModelAdmin):
    
    list_display = ('ind', 'Region')

class TelefonoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'fecha_call' )
    search_fields = ('id',)
    list_filter = ('fecha_call', 'user')
    raw_id_fields = ["id",]
    date_hierarchy = ('fecha_call')

class AuditoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    date_hierarchy = ('fecha')
    resource_class = AuditoriaResource
    list_filter  = ('pregunta_1', 'fecha', 'calificacion_1')       
    raw_id_fields = ["entregas",]
    list_display = ('fecha', 'user', 'pregunta_1', 'calificacion_1','pregunta_2', 'calificacion_2', 'pregunta_3', 'calificacion_3', 'pregunta_4', 'calificacion_4')
    fields =(('entregas', ), 
             ('pregunta_1', 'calificacion_1', 'pregunta_2', 'calificacion_2'),
             
             ('pregunta_3', 'calificacion_3', 'pregunta_4', 'calificacion_4'),
             
             ('pregunta_5', 'calificacion_5'),
             ('observacion', 'motivo_call'),
             ) 

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.user = request.user 
        obj.save()

class PregutasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pregunta', )

class InformeCallAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    resource_class = TelefonoResource
    date_hierarchy = ('fecha')
    list_filter  = ('id__user',)
    list_per_page = 5

admin.site.register(Datos_t, datos_tAdmin)

admin.site.register(Indicativo, IndicativoAdmin)

admin.site.register(Telefono, TelefonoAdmin)

admin.site.register(Pregunta, PregutasAdmin)

admin.site.register(Auditoria, AuditoriaAdmin)

admin.site.register(calificacion)

admin.site.register(Tel)

admin.site.register(Informe_call, InformeCallAdmin)



