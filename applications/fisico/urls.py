from django.urls import path
from . import views

app_name = "fisico_app"

urlpatterns = [
    path(
        'add-fisico-paquete/',
         views.BolsaCreateView.as_view(),
         name = 'fisico-paquete',
         ),

    path(
        'estado-ruta/',
         views.EstadoRutaListView.as_view(),
         name = 'estado-ruta',
         ),

    path(
        'cobertura-fisico/',
        views.CoberturaCreateView.as_view(),
        name = 'cobertura-fisico',
    ),
    
    path(
        'bolsa-create/',
        views.Bolsa_add_CreateView.as_view(),
        name = 'bolsa-create',
    ),
    
   
    

]