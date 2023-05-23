from django.urls import path
from . import views
from . views import export

app_name = "producto_app"

urlpatterns = [
    path(
        'lista-cliente/',
         views.ProductListView.as_view(),
         name='lista-cliente',
    ),
    
    path(
        'tracking-cliente/<pk>',
         views.TrackingView.as_view(),
         name='tracking-cliente',
    ),

    path(
        'producto/detalle/<pk>/', 
        views.ProductDetailView.as_view(),
        name='producto-detail',
    ),

    path(
        'add-fisico/', 
        views.FisicoCreateView.as_view(), 
        name='producto-crear',
    ),

    path(
        'upload/', 
        views.ima_cargar.as_view(), 
        name='index'
    ),

    path(
        'courrier-ruta/', 
        views.MensajeroListView.as_view(), 
        name='courrier-ruta'
    ),

    path(
        'update-prueba/<pk>/', 
        views.MensajeroUpdateView.as_view(), 
        name='courrier-update'
    ),
    
    path(
        'update-prueba/', 
        views.ActualizarPrueba.as_view(), 
        name='update-prueba'
    ),
    
    path(
        'api/guia/list', 
        views.GuiListApiView.as_view(), 
        
    ),

    
    ]