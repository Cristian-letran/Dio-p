from django.shortcuts import render
from django.views.generic import CreateView, ListView
from applications.courrier.models import courrier

class CourrierCreate(CreateView, ListView):
    template_name = "courrier/courrier.html"
    model = courrier
    fields = ('__all__')
    success_url = '.' 

    def get_queryset(self):
        queryset = courrier.objects.filter(
            
            id_ciu__departamento=self.request.user.ciudad.departamento
            )
        return queryset   