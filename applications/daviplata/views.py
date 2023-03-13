from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from.models import Daviplata
from django.urls import reverse_lazy
from .forms import DaviplataForm

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

class DaviplataUpdateView(UpdateView):
    template_name = "daviplata/daviplata_editar.html"
    form_class = DaviplataForm
    model = Daviplata
    success_url = reverse_lazy('daviplata-app:list-daviplata')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
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
    
