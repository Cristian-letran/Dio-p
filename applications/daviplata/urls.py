from django.urls import path
from . import views

app_name = "daviplata-app"

urlpatterns = [
    path(
        'list-daviplata/',
         views.DaviplataListView.as_view(),
         name='list-daviplata',
    ),

    path(
        'daviplata-update/<int:pk>/',
         views.DaviplataUpdateView.as_view(),
         name='daviplata-update',
    ),
    
    path(
        'vinculacion-create/',
         views.VinculacionCreateView.as_view(),
         name='vinculacion-create',
    ),
    
    path(
        'vinculacion-list/',
         views.VinculacionListView.as_view(),
         name='vinculacion-list',
    ),
    
    path(
        'novedad-list/',
         views.NovedadListView.as_view(),
         name='novedad-list',
    ),

    path(
        'novedad-update/<int:pk>/',
         views.NovedadUpdateView.as_view(),
         name='novedad-update',
    ),
    
    path(
        'dashboard-marcacion/',
         views.DashboardListView.as_view(),
         name='dashboard-marcacion',
    ),
    
    # path(
    #     '   ',
    #      views.RutaUpdate.as_view(),
    #      name='zona-update',
    # ),
    
    path(
        'lista-marcacion/',
         views.CoorMarcacionListView.as_view(),
         name='lista-marcacionn',
    ),
    
    path(
        'list-coor-update',
         views.ListCoorUpdateView.as_view(),
         name='list-coor-update',
    ),
    
    path(
        'coor-update/<int:pk>/',
         views.MaracionCoorUpdateView.as_view(),
         name='coor-update',
    ),
    
    path(
        'enrrutado',
         views.EnrutadoListView.as_view(),
         name='enrrutado',
    ),
    path(
        'enrrutado-update/<int:pk>/',
         views.EnrrutadoUpdateView.as_view(),
         name='enrrutado-update',
    ),  
    
    path(
        'dash-vinculacion',
         views.DashVinculacionView.as_view(),
         name='dash-vinculacion',
    ),  
    
    path(
        'vinculacion-no-activo',
         views.DashVinculacionNoActivoView.as_view(),
         name='vinculacion-no-activo',
    ),  

]