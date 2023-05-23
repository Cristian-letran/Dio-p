from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.timezone import datetime #important if using timezones
import csv
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View, TemplateView
from .forms import guiafisicoForm, ImgForm, UpdateCourrierForm, UserLogCreateForm, MensajeroUpdateForm
from . models import Guia, img
from applications.users.mixins import CustodiaPermisoMixin, MesaPermisoMixin, MensajeroPermisoMixin
from django.shortcuts import render
from .utils import render_to_pdf
from django.db.models import Count
from django.template.defaulttags import register
from applications.fisico.models import Fisico, Paquete
from applications.base_cliente.models import Bd_clie
from applications.tracking.models import Rastreo
from django.core.paginator import Paginator   
from rest_framework.generics import ListAPIView
from .serializers import GuiaSerializer

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
            ).order_by('fecha')
        return queryset

class ProductListView(LoginRequiredMixin, CreateView, ListView):
    template_name = "producto/cliente.html"
    model = Guia
    form_class = UserLogCreateForm
    paginate_by = 4
    success_url = '.'  

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Guia.objects.buscar_producto(kword, order)
        return queryset
    
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     contexto = super().get_context_data(**kwargs)
    #     contexto ['object_list'] = self.get_queryset()[:5]
    #     contexto ['count'] = self.form_class
    #     return contexto
           

class ProductDetailView(LoginRequiredMixin, TemplateView):
    template_name = "producto/detail.html"

    def get_context_data(self, *args, **kwargs):
         # El pk que pasas a la URL
         pk = self.kwargs.get('pk')
         context = super(ProductDetailView, self).get_context_data(**kwargs)
         context['object'] = Guia.objects.get(pk=pk)
         context['object_lista'] = Rastreo.objects.filter(seudo=pk).order_by('-fecha__minute').distinct('fecha__minute')
        # context['object_lista'] = Rastreo.objects.filter(id_guia=pk)
         
         return context

class FisicoCreateView(CustodiaPermisoMixin, LoginRequiredMixin, CreateView):
    template_name = "guia/guia-fisico.html"
    form_class = guiafisicoForm
    success_url = '.'   
    model= Guia
    
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
        self.object.mot_id = 4
        self.object.id_est_id = 3
        self.object.id_ciu = self.request.user.ciudad
        self.object.save()
        return super(FisicoCreateView, self).form_valid(form)    
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        contexto = super().get_context_data(**kwargs)
        contexto ['page_obj'] = self.get_queryset()
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
    

class MensajeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "guia/mensajero_ruta_update.html"
    form_class = MensajeroUpdateForm
    model = Fisico
    # fields = ['mot', 'img_guia_courrier', 'img_fachada_courrier']
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

    for guia in Guia.objects.filter(
        id_est = 2, mot = 3, 
        ).values_list(
        'guia_d_g__oficina', 'guia_d_g__oficina__nom_ofi', #1
        'direccion', 'id_ciu__ciudad', #2
        'tel', 'd_i', #3
        'destinatario', 'seudo', #4
        'bolsa', 'proceso__tipo_e', #5
        'seudo__producto__homologacion', 'id_guia', #6
        ###
       
        ).exclude(guia_d_g__oficina = 0
        ):
        
        writer.writerow(guia)

    # for paquetes in Guia.objects.filter(
    #     id_est = 2, mot = 3, producto = 3
    #     ).values_list(
    #     'guia_d_g__oficina', 'guia_d_g__oficina__nom_ofi', #1
    #     'direccion', 'id_ciu__ciudad', #2
    #     'tel', 'bolsapaquete__seudo__cc', #3
    #     'bolsapaquete__seudo__nombre', 'bolsapaquete__seudo', #4
    #     'bolsa', 'proceso__tipo_e', #5
    #     'seudo__producto__homologacion', 'id_guia', #6
    #     ###
       
    #     ):
    #     writer.writerow(paquetes)
        
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

    for guia in Guia.objects.filter(id_est = 2, mot = 3, guia_d_g__oficina = 0).values_list(
        
        'id_ciu__id', 'id_ciu__ciudad', #1
        'direccion', 'tel', #2
        'd_i', 'destinatario', #3
        'seudo', #4
        'proceso__cod_dir', 'bolsa', #5
        'proceso__tipo_e', 'seudo__producto__homologacion',#6
        'id_guia',
        
        ):
        
        writer.writerow(guia)
        
    return response

from time import time
class ActualizarPrueba(LoginRequiredMixin, TemplateView):
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
    
class GuiListApiView(ListAPIView):

    serializer_class = GuiaSerializer

    def get_queryset(self):       
        return Guia.objects.filter(
            seudo__id_clie__r_s = "Falabella"
            ) 




    
    

