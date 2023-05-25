from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from.models import Daviplata, Vinculacion, RutaDaviplata
from django.urls import reverse_lazy
from .forms import DaviplataForm, VinculacionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import datetime
from applications.users.models import User
from django.db.models import Count, F, Value
from applications.cliente.models import Departamento
from applications.courrier.models import courrier


class DaviplataListView(LoginRequiredMixin, ListView):
    template_name = "daviplata/lista_daviplata.html"
    model = Daviplata
    paginate_by = 20

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        queryset = Daviplata.objects.filter(
            nombre_establecimiento__icontains = kword,
            user = self.request.user,
            visita_efectiva = None
        )
        return queryset
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        contexto = super().get_context_data(**kwargs)
        contexto ['count'] = self.get_queryset().count()
        
        return contexto

class DaviplataUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "daviplata/daviplata_editar.html"
    form_class = DaviplataForm
    model = Daviplata
    success_url = reverse_lazy('daviplata-app:list-daviplata')

    def form_valid(self, form):######aca
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.fecha_encuesta = datetime.now()
        self.object.hora = datetime.now().time()
        self.object.visualizar = "https://www.google.com/maps/search/?api=1&query=" + self.object.latitud +"," + self.object.longitud
        self.object.save()
        return super(DaviplataUpdateView, self).form_valid(form)

    
class VinculacionListView(LoginRequiredMixin, ListView):
    template_name = "daviplata/list_vinculacion.html"
    model= Vinculacion
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        queryset = Vinculacion.objects.filter(
            celular__icontains = kword, 
            user = self.request.user,
            fecha_visita__contains=datetime.today().date()
        )
        return queryset
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        contexto = super().get_context_data(**kwargs)
        contexto ['count'] = self.get_queryset().count
        contexto ['count_nuevo'] = self.get_queryset().filter(tipo_gestion = 1).count
        contexto ['count_nspn'] = self.get_queryset().filter(tipo_gestion = 2).count
        contexto ['count_r'] = self.get_queryset().filter(tipo_gestion = 3).count
        contexto ['count_n_a'] = self.get_queryset().filter(tipo_gestion = 4).count
        
        return contexto
    
class VinculacionCreateView(LoginRequiredMixin, CreateView):
    model = Vinculacion 
    form_class = VinculacionForm
    template_name = "daviplata/vinculacion_create.html"
    success_url = reverse_lazy('daviplata-app:vinculacion-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.dane = self.request.user.ciudad
        self.object.fecha_visita = datetime.now()
        self.object.save()
        return super(VinculacionCreateView, self).form_valid(form)
    
class NovedadListView(LoginRequiredMixin, ListView):
    template_name = "daviplata/novedades.html"
    filed= ['identificacion', ]
    model = Vinculacion 
    paginate_by = 5

    def get_queryset(self):
        queryset = Vinculacion.objects.filter(
            user = self.request.user,
            novedad = False
        )
        return queryset

class NovedadUpdateView(LoginRequiredMixin, UpdateView):
    
    model = Vinculacion
    fields = ["tipo_gestion", "celular", 
              "celular_confirma", "nombre", "nombre_comercio",
              "c_rut", "categoria",
              "direccion", "barrio", "localidad",
              "registro_daviplata", "motivo_no_registro",
              "se_registro", "no_register",
              "solicito_tencard","porque_no_solicito",
              "sticker", "razon_no_sticker",
              "flanger", "razon_no_flanger",
              "datafono", "interesado",
              "etnico", "transaccion", "codigo_transaccion"
              ]
    template_name = "daviplata/update_novedad.html"
    success_url = reverse_lazy('daviplata-app:vinculacion-list')

import statistics
class DashboardListView(LoginRequiredMixin, ListView): 
    model = Daviplata
    template_name = "daviplata/dashboard.html"
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        date = self.request.GET.get("date", '')
        courrier = self.request.GET.get("id", '')
        departamento = self.request.GET.get("id_dep", '')
        queryset = Daviplata.objects.filter(
            visita_efectiva__icontains = kword,
            fecha_encuesta__contains = date,
            user__nombres__contains = courrier,
            departamento__departamento__contains = departamento,
        ).order_by('hora', '-fecha_encuesta')
        return queryset
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        contexto = super(DashboardListView, self).get_context_data(**kwargs)
        contexto ['count_efectivo'] = self.get_queryset().count
        contexto ['count_completo'] = Daviplata.objects.all().count
        contexto ['sin_gestion'] = Daviplata.objects.filter(visita_efectiva = None).count
        contexto ['user'] = User.objects.filter(roles = 5)
        contexto ['departamento'] = Departamento.objects.all()
        
        return contexto

class RutaUpdate(LoginRequiredMixin, CreateView):
    model = RutaDaviplata
    template_name = "daviplata/zona.html"
    fields =  ['user', 'direccion']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['object_list'] = Daviplata.objects.all
        context['form'].fields['direccion'].queryset = Daviplata.objects.all() 
        context
        
        return context
    
class CoorMarcacionListView(LoginRequiredMixin, ListView):
    model = Daviplata
    template_name = "daviplata/coor_marcacion.html"
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        date = self.request.GET.get("date", '')
        courrier = self.request.GET.get("id", '')

        queryset = Daviplata.objects.filter(
            visita_efectiva__icontains = kword,
            fecha_encuesta__contains = date,
            user__nombres__contains = courrier,
            municipio__departamento = self.request.user.ciudad.departamento
        )
        return queryset
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        contexto = super(CoorMarcacionListView, self).get_context_data(**kwargs)
        contexto ['count_efectivo'] = self.get_queryset().count
        contexto ['count_completo'] = Daviplata.objects.all().count
        contexto ['sin_gestion'] = Daviplata.objects.filter(visita_efectiva = None).count
        contexto ['user'] = User.objects.filter(roles = 5)
        contexto ['departamento'] = Departamento.objects.all()
        
        return contexto

    
    

    
    