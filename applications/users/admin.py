from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import User, Profile, Areas,LogSesion

@admin.register(User)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'nombres', 'apellidos', 'genero', 'ciudad')
    search_fields = ('username', 'nombres')
    raw_id_fields = ['ciudad']
    list_filter = ('ocupation', 'cliente', 'ciudad')

@admin.register(Areas)
class AreasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('Areas',)

@admin.register(LogSesion)
class LogSesion(admin.ModelAdmin):
    list_display = ('id', 'log', 'cliente')
