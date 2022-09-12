from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import ZonaGuia, Zona


class ZonaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id", "localidad")

class ZonaGuiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("guia",)
    raw_id_fields = ("guia",)

# admin.site.register(Zona, ZonaAdmin)
admin.site.register(ZonaGuia, ZonaGuiaAdmin)
