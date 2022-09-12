from django.contrib import admin
from . models import Rastreo
from related_admin import RelatedFieldAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class BookResource(resources.ModelResource):

    class Meta:
        model = Rastreo

@admin.register(Rastreo)
class PdfCobertura(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'id_guia', 'fecha', 'motivopr', 'estado')
    search_fields = ('id', 'id_guia__id_guia' , 'id_fisico_track__id_guia')
    list_per_page = 8
    date_hierarchy = ('fecha')
    
    