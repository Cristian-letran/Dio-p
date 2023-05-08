from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from.models import Daviplata, Vinculacion
from django.urls import reverse_lazy
from .forms import DaviplataForm, VinculacionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import datetime

class DaviplataListView(LoginRequiredMixin, ListView):
    template_name = "daviplata/lista_daviplata.html"
    model = Daviplata
    paginate_by = 4 

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        queryset = Daviplata.objects.filter(
            nombre_establecimiento__icontains = kword,
            user = self.request.user,
            visita_efectiva = None
        )
        return queryset
#
class DaviplataUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "daviplata/daviplata_editar.html"
    form_class = DaviplataForm
    model = Daviplata
    success_url = reverse_lazy('daviplata-app:list-daviplata')

    def form_valid(self, form):######aca
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.fecha_encuesta = datetime.now()
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
        contexto ['object_list'] = self.get_queryset()[:6]
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

class NovedadUpdateView(UpdateView):
    
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

    
    
    

    
    