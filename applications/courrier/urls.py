from django.urls import path, re_path
from . import views

app_name = "courrier_app"

urlpatterns = [

path(
    'courrier-perfiles/', 
    views.CourrierCreate.as_view(), 
    name='courrier-perfiles'
    ),

    ]