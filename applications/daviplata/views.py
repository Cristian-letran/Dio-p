from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from.models import Daviplata, Vinculacion
from django.urls import reverse_lazy
from .forms import DaviplataForm, VinculacionForm

class DaviplataListView(ListView):
    template_name = "daviplata/lista_daviplata.html"
    model = Daviplata
    paginate_by = 4 

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        queryset = Daviplata.objects.filter(
            nombre_establecimiento__icontains = kword
        )
        return queryset
#
class DaviplataUpdateView(UpdateView):
    template_name = "daviplata/daviplata_editar.html"
    form_class = DaviplataForm
    model = Daviplata
    success_url = reverse_lazy('daviplata-app:list-daviplata')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.visualizar = "https://www.google.com/maps/search/?api=1&query=" + self.object.latitud +"," + self.object.longitud
        self.object.save()
        return super(DaviplataUpdateView, self).form_valid(form)

class DaviplataCreateView(CreateView):
    model = Daviplata
    template_name = "daviplata/daviplata_create.html"
    form_class = DaviplataForm
    # model = Daviplata
    # fields = ('__all__')
    success_url = reverse_lazy('daviplata-app:list-daviplata')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(DaviplataCreateView, self).form_valid(form)
    
class VinculacionListView(ListView):
    template_name = "daviplata/list_vinculacion.html"
    model= Vinculacion
    paginate_by = 5
    
class VinculacionCreateView(CreateView):
    model = Vinculacion 
    form_class = VinculacionForm
    template_name = "daviplata/vinculacion_create.html"
    success_url = reverse_lazy('daviplata-app:vinculacion-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.dane_id  = str(self.request.user.ciudad.id)
        print(self.object.dane_id)
        
        self.object.save()
        return super(VinculacionCreateView, self).form_valid(form)
    