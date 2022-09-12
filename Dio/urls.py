"""Dio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static 
from applications.guia.views import export, export_address
from applications.base_cliente.views import exportSig, exportSig_paquete
from applications.home.views import probando

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    # path('', handleMultipleImagesUpload, name="home"),
    path('export-oficinas/', export, name="oficinas"),
    path('export-address-principal/', export_address, name="export-address"),
    path('informe-sig/', exportSig, name="sig"),
    path('informe-sig-paquete/', exportSig_paquete, name="sig-paquete"),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.guia.urls')),
    re_path('', include('applications.fisico.urls')),
    re_path('', include('applications.ruta.urls')),
    re_path('', include('applications.datos_g.urls')),
    re_path('', include('applications.call.urls')),
    re_path('', include('applications.base_cliente.urls')),
    re_path('', include('applications.pqr.urls')),
    re_path('', include('applications.courrier.urls')),
    # re_path('', include('applications.zona.urls')),
    
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
