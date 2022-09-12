import datetime
from re import template
#
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView, View,
    ListView
)

###### pagina ###############################

class probando(TemplateView):
    template_name = "publico/index.html"

#-----------Servicios---------------------------------
class mesa_docu(TemplateView):
    template_name = "publico/servicios/mensajeria_documentos.html"

class Paqueteo(TemplateView):
    template_name = "publico/servicios/paqueteo.html"

class Servicios_adicionales(TemplateView):
    template_name = "publico/servicios/serv_adi.html"

#-------------------------------------------------------    

class Terminos_cond(TemplateView):
    template_name = "publico/terminos_condi.html"

class Docu_masiva(TemplateView):
    template_name = "publico/docu_masiva.html"

class politica_priva(TemplateView):
    template_name = "publico/polica_priva.html"

class politica_t_datos(TemplateView):
    template_name = "publico/general/polica_t_datos.html"

class Sedes(TemplateView):
    template_name = "publico/general/sedes.html"

class Quienes_somos(TemplateView):
    template_name = "publico/general/quienes-somos.html"

class Politica_SGC(TemplateView):
    template_name = "publico/politica_sgc.html"

###########################################

class PanelHomeView(LoginRequiredMixin, TemplateView):
    template_name = "home/index.html"

class FechaMixin(object):
    
    def get_context_data(self, **kwargs):
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now()
        return context

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "home/index.html"
    login_url = reverse_lazy('users_app:user-login')

class TemplatePruebaMixin(FechaMixin, TemplateView):
    template_name = "home/mixin.html"


######################################

class GreetingView(View):
    greeting = "Eso es una prueba"

    def get(self, request):
        return HttpResponse(self.greeting)
