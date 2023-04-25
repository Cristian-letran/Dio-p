from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import User, Profile, Areas,LogSesion
import datetime
from simple_history.admin import SimpleHistoryAdmin
from related_admin import RelatedFieldAdmin

@admin.register(User)
class UserAdmin(SimpleHistoryAdmin,ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'nombres', 'apellidos', 'genero', 'ciudad')
    search_fields = ('username', 'nombres')
    raw_id_fields = ['ciudad']
    list_filter = ('ocupation', 'cliente')

@admin.register(Areas)
class AreasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('Areas',)

@admin.register(LogSesion)
class LogSesion(admin.ModelAdmin):
    list_display = ('id', 'log', 'cliente')


