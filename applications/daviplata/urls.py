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
        'daviplata-create/',
         views.DaviplataCreateView.as_view(),
         name='daviplata-create',
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
    
]