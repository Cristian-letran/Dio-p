from dataclasses import dataclass, field
from re import template
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic import ListView, CreateView, View
from applications.guia.models import Guia
from django.urls import reverse_lazy
from .forms import CallfisicoForm, CallUpdateForm, CacUpdateForm, CallGuiaUpdateForm, TelefonoMotivoForm, GestionForm
from django.db.models import Q
from applications.users.mixins import CallPermisoMixin
from . models import Telefono
from django.http import HttpResponse, HttpResponseRedirect
from applications.call.models import Telefono
from applications.datos_g.models import datos_g
from applications.courrier.models import courrier
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.timezone import datetime 
from django.db.models import Count
import datetime
from datetime import datetime, date

class CacUpdateView(CallPermisoMixin, UpdateView):
    template_name = "call/update_form.html"
    form_class = CacUpdateForm
    model= Guia
    # fields = ['direccion', 'id_ciu', 'postal', 'mot', 'cod_vis', 'motivo_call','oficina']
    success_url = reverse_lazy('call_app:lista-call')
    
    # def get_context_data(self, **kwargs):
    #     contexto = {}
    #     contexto ['lista'] = self.get_queryset()
    #     contexto ['form'] = self.form_class
    #     return contexto

from datetime import datetime, date
class CallUpdateView(CallPermisoMixin, UpdateView, ListView):
    template_name = "call/call-update.html"
    form_class = CallUpdateForm
    second_form_class = CallGuiaUpdateForm
    model= Telefono
    second_model = Guia
    three_model = datos_g
    queryset =  Guia.objects.all()
    # fields = ['direccion', 'id_ciu', 'postal', 'mot', 'cod_vis', 'motivo_call','oficina']
    success_url = reverse_lazy('call_app:call-consultar')
    
    def get_context_data(self, **kwargs):
        context = super(CallUpdateView, self).get_context_data(**kwargs)
        
        pk = self.kwargs.get('pk', 0)
        telefono = self.model.objects.get(id=pk)
        guia = self.second_model.objects.get(seudo_id=telefono.id)
        if 'form' not in context:
            context['form'] = self.form_class()
        
        if 'form2' not in context:
            context['form2'] =self.second_form_class(instance= guia)
        context['id']= pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        telefono = self.model.objects.get(id=id_solicitud)
        guia = self.second_model.objects.get(seudo_id=telefono.id)
        form = self.form_class(request.POST, instance=telefono)
        form2 = self.second_form_class(request.POST, instance=guia)
        if form.is_valid() and form2.is_valid():
            
            self.h= 33
            self.object = form.save(commit=False)
            self.objectl = form2.save(commit=False)
            self.object.user = self.request.user
            self.objectl.fecha_visita = datetime.today()
            self.objectl.mot_id = 20
            self.objectl.__guia_d_g__orimp = -12
            self.objectl.user = self.request.user   
            form.save()
           
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

#
class CallEstadoUpdateView(UpdateView):
    template_name = "call/update-estado-call.html"
    form_class = TelefonoMotivoForm
    model= Telefono
    success_url = reverse_lazy('call_app:call-consultar')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.estado = True
        self.object.save()
        return super(CallEstadoUpdateView, self).form_valid(form)
    
class CacListView(CallPermisoMixin, ListView):
    template_name = "call/cac_gestion.html"
    context_object_name = 'call'
    # queryset = Guia.objects.filter(Q(id_est = 3), Q(mot=5) | Q(mot=6)| Q(mot=7)| Q(mot=8)). order_by('-fecha')
    # context_object_name = 'call'
    paginate_by = 3

    def get_queryset(self, **kwargs):
        
        producto = self.request.GET.get("producto", "")
        reason = self.request.GET.get("reason", "")
        seudo = self.request.GET.get("kword", "")
        fecha = self.request.GET.get("date_start", "")
        lista = Guia.objects.filter(id_est = 3, 
            producto__producto__contains = producto,
            mot__motivo__icontains = reason,
            fecha_recepcion__icontains = fecha
        ).filter(
            Q(seudo__seudo_bd__icontains=seudo)|
            Q(id_ciu__ciudad__icontains = seudo)|
            Q(d_i__icontains =seudo)|
            Q(id_guia__icontains = seudo)
        # ).order_by("-motivo_call"
        ).exclude(mot = 1).exclude(mot = 22).exclude(mot = 21).exclude(mot = 20).exclude(mot=19)
        
        return lista
from datetime import datetime, date
class CallListView(CallPermisoMixin, View):
    template_name = "call/call_gestion.html"
    context_object_name = 'call'
    initial = {'key':'value'}
    form_class = GestionForm
    
    
    def get(self, request, *args, **kwargs):
        mensajero = request.GET.get("id_mensajero", "")
        producto = request.GET.get("producto", "")
        reason = request.GET.get("reason", "")
        seudo = request.GET.get("kword", "")
        fecha = request.GET.get("date_start", "")
        contact_list = Guia.objects.filter(
            id_est = 3,  telefono_guia__estado = False,
            producto__producto__contains = producto,
            mot__motivo__icontains = reason,
            fecha_recepcion__icontains = fecha, 
            mensajero__courrier = mensajero
            
        ).filter(
            Q(seudo__seudo_bd__icontains=seudo)|
            Q(id_ciu__ciudad__icontains = seudo)|
            Q(d_i__icontains =seudo)|
            Q(id_guia__icontains = seudo)

        ).exclude(mot = 1).exclude(mot = 22).exclude(mot = 21).order_by('-fecha')

        paginator = Paginator(contact_list, 5) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        cantidad = Guia.objects.filter(
            user=self.request.user, 
            fecha_recepcion__contains=datetime.today().date()).count

        count_tel = Telefono.objects.filter(
            estado=True, 
            user=self.request.user, 
            fecha_call__contains=datetime.today().date()).count
        
        filtro = courrier.objects.all().annotate(
            num_guias = Count('user_guia', filter=Q(user_guia__mot = 7))
            ).annotate(no_existe = Count('user_guia', filter=Q(user_guia__mot = 6))
            ).order_by('-num_guias','-no_existe')
        fils =  courrier.objects.annotate(number_of_entries=Count('user_guia'))
        page_obj = paginator.get_page(page_number)
        data = {
            'page_obj': page_obj,
            'count': cantidad,
            'counts': count_tel,
            'filtro': filtro,
            'count_total': contact_list.count(),
            'plan': fils,
        }
        return render(request, self.template_name, data)

class AuditoriaListView(CallPermisoMixin, View):
    template_name = "call/auditoria.html"
    context_object_name = 'auditoria'
    model = Guia

    def get(self, request, **kwargs):
        mensajero = request.GET.get("id_mensajero", "")
        ciudad = request.GET.get("ciudad", "")
        kword = request.GET.get("kword", "")
        fecha = request.GET.get("date_start", "")
        contact_list = Guia.objects.filter(mot = 21, estado=1).filter(
            fecha_recepcion__icontains = fecha,
            id_ciu__ciudad__icontains = ciudad,
            mensajero__courrier__contains = mensajero
        ).filter(
            Q(seudo__seudo_bd__icontains=kword)
        )

        paginator = Paginator(contact_list, 3) # Show 25 contacts per page.

        filtro = courrier.objects.all()

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {
            'page_obj': page_obj,
            'count': Guia.objects.filter(estado=0, user=self.request.user, fecha_recepcion__contains=datetime.today().date()).count,
            'filtro': filtro
        }
            
        return render(request, self.template_name, data)

    # def count(self):
    #     return Guia.objects.filter(estado=0, user=self.request.user, fecha_recepcion__contains=datetime.today().date())
            

class AuditoriaCreateView(CreateView):
    template_name = "call/create_auditoria.html"
    form_class = CallfisicoForm
    success_url = reverse_lazy('call_app:lista-call-auditoria')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(AuditoriaCreateView, self).form_valid(form)



