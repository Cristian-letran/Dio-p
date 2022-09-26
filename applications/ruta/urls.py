from django.urls import path
from . import views

app_name = "ruta_apps"

urlpatterns = [

    path(
        'add-cargue-recepcion/',
        views.RecepcioCreateView.as_view(),
        name = 'cargue-recepcion'
    ),

    path(
        'listar-planillas/<full_name>/',
        views.ListEmpleadosPdf.as_view(),
        name = 'impresion',
    ),
    
    path(
        'lista/planillas/asignar/', 
        views.AsignarCreateView.as_view(),
        name='asignar', 
    ),

     path(
        'lista/planillas/generar/', 
        views.AsignarListview.as_view(),
        name='planillas',
    ),

    path(
        'generar/destino/', 
        views.DestinoCreate.as_view(),
        name='destino'
    ),
    
    path(
        'generar/descargue/', 
        views.DescargueCreateView.as_view(),
        name='destino-descargue'
    ),
    
    # path(
    #     'generar/historial/', 
    #     views.HistorialListview.as_view(),
    #     name='historial'
    # ),
    path('<int:rr>/results/', views.detail, name='results'),
    
    path(
        'inf/destino/ciudad/', 
        views.InformeRutaCiudadListView.as_view(),
        name='informe-destino',
    ),
    
    path(
        'update/recepcion/view/<int:pk>/', 
        views.CorreccionRecepcion.as_view(),
        name='update-recepcion',
    ),
    
    path(
        'lista/recepcion/', 
        views.RecepcionListView.as_view(),
        name='lista-recepcion',
    ),
    
    
    path(
        'lista/punteo/', 
        views.PunteoCreateView.as_view(),
        name='lista-punteo',
    ),

    path(
        'lista/imprimir/', 
        views.ImprimirCreateView.as_view(),
        name='lista-imprimir',
    ),

    path(
        'imprimir-guia-regendamiento-call/<id_agenda>/',
         views.imprimir_reagendamientosCallListView.as_view(),
         name='imprimir-guia-regendamiento-call',
    ),
    
    path(
        'delete-guia/', 
        views.EliminarGuia.as_view(), 
        name='delete-guia'
    ),

     path(
        'lista/default/<int:pk>/', 
        views.DefaultGuiaUpdate.as_view(), 
        name='lista-default'
    ),

   
    
    ]