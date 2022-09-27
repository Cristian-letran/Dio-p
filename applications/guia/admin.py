from dataclasses import field
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from related_admin import RelatedFieldAdmin
from django.contrib.admin.models import ADDITION, LogEntry, CHANGE
from . models import Servicio, Guia, img, CoberturaPdf
from simple_history.admin import SimpleHistoryAdmin
from import_export import resources

class GuiaResource(resources.ModelResource):
    
    class Meta:
        model = Guia
        import_id_fields = ('seudo', 'id_guia') 

class ImagenGuiaResource(resources.ModelResource):
    
    class Meta:
        model = img
        field = ('id_guia', 'id_guia__destinatario', 'id_guia__destinatario__d_i') 
#---------------------------------------------------------
@admin.register(Guia)
class guiaAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, RelatedFieldAdmin):
    history_list_display = ["mot", "fecha_recepcion", "direccion", "courrier"]
    resource_class = GuiaResource
    date_hierarchy = ('fecha_visita')
    list_per_page = 5
    raw_id_fields = ["seudo", "mot", "id_est", "cod_vis", "id_ciu"]
    fieldsets = [
        (None,  {'fields':[(
            'seudo', 'bolsa', 'destinatario'), 
            ('producto', 'estado', 'id_ciu', 'est_planilla'), 
            ('direccion', 'barrio', 'postal','fecha_recepcion' ), ]}),

        ('Estados', {'fields':[
                
            ('id_est', 'mot', 'id_ser',), 
            ('cod_vis', 'proceso'),
            ('cantidad_vi', 'cantidad', 'codigo', ), ]}) 
    ]
    search_fields = ('id_guia', 'seudo__seudo_bd', 'mot__motivo', 'd_i', 'bolsa')
    list_display = (
        'id_guia','fecha_visita', 'image_mesa__image', 
        'mot__motivo', 'd_i', 'seudo__telefono', 
        'fecha_recepcion', 'seudo', 
        'direccion', 'id_ciu', 'fecha', 
        'user', 'destinatario', 
        'mensajero', 'estado',
        'cobertura_bolsa__pdf_cobertura')
    ordering = ('id_guia',)
    list_filter = ('user', 'id_ciu__departamento','fecha_recepcion', 'mot__motivo','id_est', 'fecha_visita' )
  

#     actions = None
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.user = request.user 
        obj.save()
    
class MoniterLog(admin.ModelAdmin):
    
    list_display = (
        'action_time','user',
        'content_type','object_repr',
        'change_message','action_flag'
        )
    list_filter = ['action_time','user','content_type']
    ordering = ('-action_time',)

@admin.register(img)
class ImgAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ('id_guia', 'image', 'fecha', 'user')
    LogEntry.objects.filter(action_flag=ADDITION)
    list_filter = ('fecha', 'user')
    date_hierarchy = ('fecha')
    search_fields = ('id_guia__id_guia',)
    resource_class = ImagenGuiaResource

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.user = request.user 
        obj.save()

@admin.register(CoberturaPdf)
class PdfCobertura(admin.ModelAdmin):
    list_display = ('id', 'pdf')


    
admin.site.register(Servicio)
admin.site.register(LogEntry, MoniterLog)




