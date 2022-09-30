from django.views.generic import ListView
from.models import datos_g, Orden
from .utils import render_to_pdf
from django.http import HttpResponse
from applications.users.mixins import CustodiaPermisoMixin
from django import template
from django.views.generic.dates import TodayArchiveView
from django.db.models import Count
from applications.argumento.models import Motivo_call, Motivo
from applications.guia.models import Guia

register = template.Library()

class OrdenListView(CustodiaPermisoMixin, ListView):
    template_name = "datos_g/orden_guia.html"
    paginate_by = 8

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        queryset = Orden.objects.order_by('-orden'
        ). exclude(orden = -1). exclude(orden =-2
        ).exclude(orden =-3).exclude(orden =-4
        ).exclude(orden =-5).exclude(orden =-6
        ).exclude(orden =-7).exclude(orden =-8
        ).exclude(orden =-9).exclude(orden =-9
        ).exclude(orden =-10).exclude(orden =-11
        ).exclude(orden =-12
        ).filter(orden__icontains=kword
        ).annotate(num_books=Count('orden_dat_g')
        )
        return queryset
        
class ListGuiaPdf(CustodiaPermisoMixin, ListView):
        
    def get(self, request, *args, **kwargs):
        nombre = self.kwargs['id_datos_g']
        guia =datos_g.objects.filter(
            orimp = nombre, 
            seudo_dg__user=self.request.user
            ). order_by('seudo_dg__id_guia' 
            ).exclude(seudo_dg__mot = 3
            )
        data = {
            'count': guia.count(),
            'pdf_guia': guia
        }
        pdf = render_to_pdf('datos_g/pdf_guia.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

###################################################
class GuiaListView(CustodiaPermisoMixin, ListView):
    template_name = "guia/imprimir_guia.html"
    context_object_name = 'guia'

    def get_queryset(self):
        queryset = datos_g.objects.filter(
            seudo_dg__id_guia=self.request.GET.get('id_guia'),
        )
        return queryset   

#################### Buscar guia agenda ########################
class BuscarGuiaPdf(CustodiaPermisoMixin, ListView):
        
    def get(self, request, *args, **kwargs):
        nombre = self.kwargs['id_datos_g']
        guia =datos_g.objects.filter(
            seudo_dg__id_guia = nombre, 
            )
        data = {
            'count': guia.count(),
            'pdf_guia': guia
        }
        pdf = render_to_pdf('datos_g/pdf_guia.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

##################### Agendamientos ################################
from django.db.models import Q
from django.db.models import Count, F, Value
class OrdenAgendaListView(CustodiaPermisoMixin, ListView):
    template_name = "datos_g/orden_guia_agendamiento.html"
    context_object_name = 'orden'
    paginate_by = 20

    def get_queryset(self):
        queryset = Orden.objects.filter(
            tipo = 1, 
            orden_dat_g__seudo_dg__mot = 20, 
            orden_dat_g__seudo_dg__id_est = 3,
            # orden_dat_g__seudo_dg__estado_zona = 0,
            orden_dat_g__seudo_dg__id_ciu__departamento = self.request.user.ciudad.departamento
            ).order_by('-orden'
            ).annotate(
                num_orden=Count('orden_dat_g__seudo_dg__mot')
            ).exclude(orden =-12)
        return queryset

    def get_querydoble(self):
        queryset = Orden.objects.filter(
            tipo = 2, 
            # orden_dat_g__seudo_dg__estado_zona = 0,
            orden_dat_g__seudo_dg__mot = 19,
            orden_dat_g__seudo_dg__id_est = 3,
            orden_dat_g__seudo_dg__id_ciu__departamento = self.request.user.ciudad.departamento
            ).order_by('-orden'
            ).annotate(num_orden_two=Count('orden_dat_g__seudo_dg__mot'))
        return queryset

    def get_telefono(self):
        queryset = Motivo.objects.filter(id= 20,).annotate(cant_orden_call=Count('motivo'))
        return queryset

    def get_count_call(self):
        queryset = Guia.objects.filter(id= 20)
        return queryset

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto ['orden'] = self.get_queryset()
        contexto ['ordentwo'] = self.get_querydoble()
        contexto ['call'] = self.get_telefono()
        contexto ['cont_call'] = self.get_count_call()
        return contexto  
#
class Lista_gendamientosListView(CustodiaPermisoMixin, TodayArchiveView, ListView):
    date_field = "pub_date"
    allow_future = True
    def get(self, request, *args, **kwargs):
        nombre = self.kwargs['id_agenda']
        guia =datos_g.objects.filter(
            orimp = nombre, 
            id_ciu__departamento=self.request.user.ciudad.departamento,
            seudo_dg__mot = 20, 
            # zona = 0,
            ).order_by(
                'seudo_dg__id_guia'
                ).exclude(seudo_dg__user__ocupation = 2
                ).exclude(seudo_dg__id_est = 4)
        data = {
            'count': guia.count(),
            'pdf_guia': guia
        }
        pdf = render_to_pdf('datos_g/pdf_guia.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class Lista_reagendamientosCallListView(CustodiaPermisoMixin, TodayArchiveView, ListView):
    date_field = "pub_date"
    allow_future = True
    def get(self, request, *args, **kwargs):
        nombre = self.kwargs['id_agenda']
        guia =datos_g.objects.filter(
            seudo_dg__user__ocupation = 2,
            id_ciu__departamento=self.request.user.ciudad.departamento,
            seudo_dg__mot = 20, 
            ).exclude(seudo_dg__id_est__id = 4)
        data = {
            'count': guia.count(),
            'pdf_guia': guia
        }
        pdf = render_to_pdf('datos_g/pdf_guia.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

