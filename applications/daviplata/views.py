from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from.models import Daviplata, Vinculacion, RutaDaviplata
from django.urls import reverse_lazy
from .forms import DaviplataForm, VinculacionForm, RutaDaviplataForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import datetime, timedelta
from applications.users.models import User
from django.db.models import Count, F, Value
from applications.cliente.models import Departamento
from applications.courrier.models import courrier
from applications.users.mixins import CustodiaPermisoMixin


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
from django.db.models import Q
class DaviplataUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "daviplata/daviplata_editar.html"
    form_class = DaviplataForm
    model = Daviplata
    success_url = reverse_lazy('daviplata-app:list-daviplata')

    def form_valid(self, form):######aca
        ################ HOUR TIEMPO ##################
        hour_last = Daviplata.objects.filter(Q(fecha_encuesta__contains=datetime.today().date()) | Q(fecha_encuesta=None),
            user = self.request.user
            
            ).values_list("hora", flat=True).latest('hora')
        hour_now = datetime.today().time().strftime("%H")

        if hour_last == None:
            hour_calculo = 1
        else:
            hour_calculo = int(hour_now) - int(hour_last)
        
        print("hhhhhhhhhhhhhh",hour_calculo)
        
        ################ MINUTE TIEMPO  ##################
        minute1 = Daviplata.objects.filter(Q(fecha_encuesta__contains=datetime.today().date()) | Q(fecha_encuesta=None),
           user = self.request.user,
           
           ).values_list("minuto", flat=True).latest('minuto')
        minute2 = datetime.now().time().strftime("%M")

        if minute1 == None:
            hour_calculo = 1
        else:
            minute_calculo = int(minute2) - int(minute1)
        
        ########################
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.fecha_encuesta = datetime.now()
        ###################ACTUAL#######################
        self.object.hora = datetime.today().time().strftime("%H").lstrip('+-0')#("%H:%M")
        self.object.minuto = datetime.now().time().strftime("%M").lstrip('+-0')

        if hour_last == None and minute1 == None:
            self.object.tiempo = 1
        else:
            self.object.tiempo = str(hour_calculo) + ":" + str(minute_calculo)

        #calculo = str(hour_calculo) + ":" + str(minute_calculo)
        #self.object.tiempo = str(calculo) 

        
        #self.object.tiempo = calculo
        
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
            cambio = True
        )
        return queryset
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        contexto = super().get_context_data(**kwargs)
        contexto ['count'] = self.get_queryset().count
        return contexto

class NovedadUpdateView(LoginRequiredMixin, UpdateView):
    
    model = Vinculacion
    fields = ["tipo_gestion", "celular", 
              'dir_a', 'num_dir1', 'num_dir2', 'complemento', 'detail_complemento',
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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.cambio = False
        self.object.save()
        return super(NovedadUpdateView, self).form_valid(form)   

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
        ).order_by('-hora', '-minuto')
        return queryset
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        contexto = super(DashboardListView, self).get_context_data(**kwargs)
        contexto ['count_completo'] = Daviplata.objects.all().count
        contexto ['sin_gestion'] = Daviplata.objects.filter(visita_efectiva = None).count
        contexto ['user'] = User.objects.filter(roles = 5)
        contexto ['departamento'] = Departamento.objects.all()
        
        ###############################################
        contexto ['gestionados'] = self.get_queryset().count
        contexto ['count_efectivo'] = self.get_queryset().filter(visita_efectiva = "SI").count
        contexto ['cambio_dir'] = self.get_queryset().filter(tipo_no_efectiva = "Cambio de Direccion PVD").count
        contexto ['dir_errrada'] = self.get_queryset().filter(tipo_no_efectiva = "Direccion Errada").count
        contexto ['cliente_no_encuesta'] = self.get_queryset().filter(tipo_no_efectiva = "El Cliente No Permitio Realizar encuesta").count
        contexto ['lcl_cerrado'] = self.get_queryset().filter(tipo_no_efectiva = "Local Cerrado").count
        contexto ['no_pdv'] = self.get_queryset().filter(tipo_no_efectiva = "No Existe PVD").count
        contexto ['otros'] = self.get_queryset().filter(tipo_no_efectiva = "Otros").count
        contexto ['ya_marcado'] = self.get_queryset().filter(tipo_no_efectiva = "Ya esta Marcado").count
        
        return contexto

class RutaUpdate(LoginRequiredMixin, CreateView):
    
    form_class = RutaDaviplataForm
    template_name = "daviplata/zona.html"
    
    success_url = reverse_lazy('daviplata-app:list-daviplata')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context ['form'].fields['direccion'].queryset = Daviplata.objects.filter(
    #         municipio__departamento =self.request.user.ciudad.departamento
    #         )
        
    #     return context
    
class CoorMarcacionListView(CustodiaPermisoMixin, ListView):
    model = Daviplata
    template_name = "daviplata/coor_marcacion.html"
    paginate_by = 15

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

        ####
        contexto ['gestionados'] = self.get_queryset().count
        contexto ['count_efectivo'] = self.get_queryset().filter(visita_efectiva = "SI").count
        contexto ['cambio_dir'] = self.get_queryset().filter(tipo_no_efectiva = "Cambio de Direccion PVD").count
        contexto ['dir_errrada'] = self.get_queryset().filter(tipo_no_efectiva = "Direccion Errada").count
        contexto ['cliente_no_encuesta'] = self.get_queryset().filter(tipo_no_efectiva = "El Cliente No Permitio Realizar encuesta").count
        contexto ['lcl_cerrado'] = self.get_queryset().filter(tipo_no_efectiva = "Local Cerrado").count
        contexto ['no_pdv'] = self.get_queryset().filter(tipo_no_efectiva = "No Existe PVD").count
        contexto ['otros'] = self.get_queryset().filter(tipo_no_efectiva = "Otros").count
        contexto ['ya_marcado'] = self.get_queryset().filter(tipo_no_efectiva = "Ya esta Marcado").count
        
        return contexto

    
class MaracionCoorUpdateView(CustodiaPermisoMixin, UpdateView):
    template_name = "daviplata/coor_update.html"
    form_class = DaviplataForm
    model = Daviplata
    success_url = reverse_lazy('daviplata-app:list-daviplata')
    list

class ListCoorUpdateView(CustodiaPermisoMixin, ListView):
    template_name = "daviplata/list-coor-update.html"
    form_class = DaviplataForm
    model = Daviplata
    success_url = reverse_lazy('daviplata-app:list-daviplata')
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        queryset = Daviplata.objects.filter(
            visita_efectiva__icontains = kword,
            contingencia_img1 = True,
            municipio__departamento = self.request.user.ciudad.departamento
        )
        return queryset
    
class EnrutadoListView(ListView):
    template_name = "daviplata/enrutado.html"
    model = Daviplata
    paginate_by = 100

    def get_queryset(self):
        queryset = Daviplata.objects.filter(
            municipio__departamento = self.request.user.ciudad.departamento,
            visita_efectiva = None
        ).exclude(user = None).order_by("user")
        return queryset 
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        contexto = super(EnrutadoListView, self).get_context_data(**kwargs)
        contexto ['total'] = self.get_queryset().count
        return contexto

class EnrrutadoUpdateView(UpdateView):
    template_name = "daviplata/marcacion/enrutado-update.html"
    fields = ['user']
    model = Daviplata
    success_url = reverse_lazy('daviplata-app:enrrutado')
    

    
    