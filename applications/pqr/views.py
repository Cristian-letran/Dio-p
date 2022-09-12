from dataclasses import field
from django.shortcuts import render
from django.views.generic import CreateView
from . models import Pqr

class PqrCreateView(CreateView):
    model = Pqr
    template_name = "publico/pqr.html"
    fields = ['ciudad_radi','fecha', 'tipo_do', 'n_documento','apellidos', 'nombre','email', 'n_contacto', 'direccion', 'n_guia','desc_pqr']
    success_url = '.'   

