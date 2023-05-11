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
    
]