from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import (
    Estado, Motivo, Cod_vis,
    Nom_producto, Emision, Est_clie, 
    Proceso, Producto, Motivo_call, Tipo, Franquicia
    )

#---------------------------------------------------------------------
class EmiResource(resources.ModelResource):
    class Meta:
        model = Emision
        import_id_fields = ('t_emi',)

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto
        import_id_fields = ('id_pro',)

#--------------------------------------------------------------------
@admin.register(Estado)
class EstadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'Estado',)

@admin.register(Motivo)
class MotivoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'motivo', )

@admin.register(Cod_vis)
class MotivoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'visita', 'tipo')

@admin.register(Nom_producto)
class NomproductoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)
    list_per_page = 7

@admin.register(Emision)
class emisionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EmiResource
    list_display = ('t_emi', 'emision')

@admin.register(Est_clie)
class est_clieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'estado', 'descripcion', 'cod_est')
    search_fields = ('id',)
    list_per_page = 7

@admin.register(Proceso)
class ProcesoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'proceso', 'cod_dir', 'tipo_e')

@admin.register(Producto)
class productoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProductoResource
    list_display = ('id_pro', 'id_clie', 'producto', 'tipo', 'homologacion')

@admin.register(Motivo_call)
class productoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('motivo', 'id')

@admin.register(Tipo)
class productoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)

@admin.register(Franquicia)
class productoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','franqucia',)


