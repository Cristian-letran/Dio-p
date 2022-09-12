from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.timezone import datetime #important if using timezones
import csv
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View, TemplateView
from .forms import guiafisicoForm, ImgForm, UpdateCourrierForm
from . models import Guia, img
from applications.users.mixins import CustodiaPermisoMixin, MesaPermisoMixin, MensajeroPermisoMixin
from django.shortcuts import render
from .utils import render_to_pdf
from django.db.models import Count
from django.template.defaulttags import register
from applications.fisico.models import Fisico
from applications.base_cliente.models import Bd_clie
from applications.tracking.models import Rastreo
from django.core.paginator import Paginator   

@register.filter
def cuts(value):
    return (value)[4:10]

@register.filter
def cadena_texto(value):
    return str(value)


class TrackingView(ListView):
    template_name = "producto/tracking.html"
    model = Rastreo
    
    def get_queryset(self):
        kword = self.kwargs["pk"]
        queryset = Rastreo.objects.filter(
            id_fisico_track = kword
            )
        return queryset

class ProductListView(LoginRequiredMixin, ListView):
    template_name = "producto/cliente.html"
    paginate_by = 4

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Guia.objects.buscar_producto(kword, order)
        return queryset
           
class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = "producto/detail.html"
    model = Guia

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        context['recepcion_list'] = Guia.objects.all()[:1]
        return context

class FisicoCreateView(CustodiaPermisoMixin, LoginRequiredMixin, CreateView, ListView):
    template_name = "guia/guia-fisico.html"
    form_class = guiafisicoForm
    success_url = '.'   
    
    def get_queryset(self):
        vargui = Guia.objects.filter(user=self.request.user).order_by('-fecha')[:5]
        paginator = Paginator(vargui, 25)
        page = self.request.GET.get('page')
        contacts = paginator.get_page(page)
        return vargui
    
    def get_cantidad(self):
        # return Guia.objects.filter(user=self.request.user).filter('fecha__day')
        return Guia.objects.filter(user=self.request.user, fecha__contains=datetime.today().date())

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(FisicoCreateView, self).form_valid(form)    

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto ['page_obj'] = self.get_queryset()
        contexto ['form'] = self.form_class
        contexto ['count'] = self.get_cantidad().count
        return contexto

class ima_cargar(MesaPermisoMixin, View):
    form_class = ImgForm
    template_name = "index.html"
    success_url = '.'
    initial = {'key': 'value'}
    model = img
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        kword = self.request.GET.get('kword', '')
        contact_list = img.objects.filter(
            # user = request.user,
            id_guia__id_guia__contains = kword
        )
        paginator = Paginator(contact_list, 5) 

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        count_day = img.objects.all().count
            # fecha__contains=datetime.today().date()).count
        data = {
            'page_obj': page_obj,
            'count': count_day
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
                images = request.FILES.getlist('images')
            
                for image in images:
                    img.objects.create(image = image, user = request.user)
    
                
                uploaded_images = img.objects.all()
                count = uploaded_images
            # return JsonResponse({"imagenes": [{"url": image.image.url} for image in uploaded_images]})
                # return HttpResponse("Total guias digitalizadas" + " " + str(len(images)))
                
                return render(request, 'guia/post_imagen.html', {'contar':str(len(images))})

        return render(request, self.template_name)

class MensajeroListView(MensajeroPermisoMixin, ListView ):
    template_name = "guia/mensajero_ruta.html"
    context_object_name = 'guia_mensajeros'
    model = Guia
    paginate_by =  5
    ordering = 'id_guia'

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        queryset = Guia.objects.filter(
            id_guia__icontains= kword,
            mensajero__d_i=self.request.user.d_i
            ).order_by('id_guia').exclude(id_est = 3)
        return queryset   

class MensajeroUpdateView(UpdateView):
    template_name = "guia/mensajero_ruta_update.html"
    model = Fisico
    fields = ['mot',]
    success_url = reverse_lazy('producto_app:courrier-ruta')

    def form_valid(self, form):
        cantidad = 0
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.id_est_id = 3
        
        #self.object.cantidad_vi = self.object.mot.id
        self.object.cantidad += 1
        
        if int(self.object.mot.id) ==16:
            if self.object.cantidad_vi <=2:
                self.object.cantidad_vi += 1

        elif int(self.object.mot.id) ==17:
            if self.object.cantidad_vi <=2:
                self.object.cantidad_vi += 1

        elif int(self.object.mot.id) ==18:
            if self.object.cantidad_vi <=2:
                self.object.cantidad_vi += 1

        elif int(self.object.cantidad_vi) > 18:
            self.object.cantidad_vi = 0

        elif int(self.object.cantidad_vi) < 16:
            self.object.cantidad_vi = 0


        self.object.save()
        return super(MensajeroUpdateView, self).form_valid(form)

    

@login_required
def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow([
        'CODIGO DE OFICINA', 'NOMBRE OFICINA', #1
        'DIRECCION DESTINO', 'CIUDAD DESTINO', #2
        'TELEFONO', 'CEDULA',          #3
        'NOMBRE_USUARIO', 'PSEUDOCODIGO', #4 
        'BOLSA', 'TIPO DE EMISION',    #5
        'PROCESO', 'GUIA' #6 
        ])

    for guia in Bd_clie.objects.filter(
        guias__id_est = 2, guias__mot = 3, guias__producto = 3
        ).values_list(
        'guias__guia_d_g__oficina', 'guias__guia_d_g__oficina__nom_ofi', #1
        'guias__direccion', 'guias__id_ciu__ciudad', #2
        'guias__tel', 'guias__d_i', #3
        'guias__destinatario', 'guias__seudo', #4
        'guias__bolsa', 'guias__proceso__tipo_e', #5
        'guias__seudo__producto__homologacion', 'guias__id_guia', #6
        'guias__bolsa'
        
        ):
        writer.writerow(guia)
        
    return response

@login_required
def export_address(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow([
        'COD DANE', 'CIUDAD', #1
        'DIRECCION 1', 'TELEFONO', #2
        'CEDULA', 'NOMBRE_USUARIO', #3
        'PSEUDOCODIGO', #4 
        'TIPO ENTREGA', 'BOLSA', #5
        'TIPO DE EMISION', 'PROCESO', #6 
        'GUIA'
        ])

    for guia in Guia.objects.filter(id_est = 2, mot = 3).values_list(
        
        'id_ciu__id', 'id_ciu__ciudad', #1
        'direccion', 'tel', #2
        'd_i', 'destinatario', #3
        'seudo', #4
        'proceso__cod_dir', 'bolsa', #5
        'proceso__tipo_e', 'seudo__producto__homologacion',#6
        'id_guia',
        

        ).exclude(producto = 3):
        
        writer.writerow(guia)
        
    return response

from time import time
class ActualizarPrueba(TemplateView):
    template_name = "guia/template_prueba.html"
    permission_required = ('guia.add_guiap', 'guia.change_guiap')

    def get(self, request, *args, **kwars):
        guia = Guia.objects.all()
        tiempo_inicial = time () 
        for postal in guia :
            postal.postal = 11004
            postal.save()
        tiempo_final = time() - tiempo_inicial
        print (f'Tiempo de ejecucion del metodo 1: {tiempo_final}')
        return render(request, self.template_name, {'guia': guia})




    
    

