from django import forms
from django.forms import widgets
from .models import Cargue, Planilla, Recepcion, Destino, Descargue, Punteo, Imprimir
from applications.guia.models import Guia
from applications.courrier.models import courrier
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

class CargueForm(forms.ModelForm):

    class Meta:
        model = Cargue
        fields = (
            'full_name', 
            'guia',
        )

        widgets = {
            'guia': forms.SelectMultiple(
                attrs = {
                    'placeholder': 'Codigo se barrras Seudo...',
                    'class': 'input-group-field',
                    
                }
            ),
            'full_name': forms.Select(
                attrs = {
                'class': 'input-group-field',
                }
            ),
            }
        

class AsignarForms(forms.ModelForm):  


    # def __init__(self, user, *args, **kwargs):
    #     request = kwargs.pop('request', None)
    #     user = kwargs.pop('user', None)
    #     hola = request.user.ciudad.departamento
    #     super(AsignarForms, self).__init__(*args, **kwargs)
    #     self.fields['full_name'].queryset = courrier.objects.filter(est_courrier= True)
    #     self.fields["full_name"].queryset = courrier.objects.filter(id_ciu__departamento=self.hola, est_courrier= True)

    
    class Meta:
        model = Planilla
        fields = ['full_name', 'guia', 'user']
        widgets = {
            
            'full_name': forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            }
       
class RecepcionForm(forms.ModelForm):   
    class Meta:
        model = Recepcion
        fields = ['guia', 'estado', 'motivo',]

        widgets = {
            'motivo': forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'input-group-field',
                    'readonly': True
                }
            ),
            }

class DestinoForm(forms.ModelForm):   
    class Meta:
        model = Destino
        fields = ['sucursal', 'destino', 'guia',]

        widgets = {
            'sucursal': forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            'guia': forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            'destino': forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            
            }

class DescargueForm(forms.ModelForm):   
    class Meta:
        model = Descargue
        fields = ['guia', 'user']

        widgets = {
            'guia': forms.Select(
                attrs={
                    'class': 'input-group-field',
                }
            ),
            
            }

class PunteoForm(forms.ModelForm):

    class Meta:
        model = Punteo
        fields = (
            'guia_punteo', 
        )

        widgets = {
            'guia_punteo': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo se barrras Guia...',
                    'class': 'input-group-field',       
                }
            ),
           
            }

class ImprimirForms(forms.ModelForm):
    class Meta:
        model = Imprimir
        fields = (
            'guia_imprimir', 
        )

        widgets = {
            'guia_imprimir': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo se barrras Guia...',
                    'class': 'input-group-field', 
                    'autofocus': 'autofocus',      
                }
            ),
           
            }

class DefaultUpdateForm(forms.ModelForm):   
    class Meta:
        model = Guia
        fields = ['mot', 'id_est']

        widgets = {
            'mot': forms.Select(
                attrs={
                    'class': 'input-group-field',
                    'disabled' : 'disabled'
                }
            ),
            'id_est': forms.Select(
                attrs={
                    'class': 'input-group-field',
                    'disabled' : 'disabled'
                }
            ),
            }