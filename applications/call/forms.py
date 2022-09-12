from email.policy import default
from django import forms
from .models import Auditoria
from applications.guia.models import Guia
from applications.argumento.models import Motivo, Cod_vis, Motivo_call
from applications.cliente.models import Ciudad
from django.db.models import Q
from .models import Telefono


class CallfisicoForm(forms.ModelForm):
    
    class Meta:
        model = Auditoria
        fields = (
            '__all__'
        )

        widgets = {
            'entregas': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo de barras Bolsa', 'autofocus': 'autofocus',
                    'class': 'input-group-field',
                    
                }
            ),

            'pregunta_1': forms.TextInput(
                attrs = {
                    'class': 'input-group-field', 
                    'disabled' : 'disabled'
                }
            ),
            'calificacion_1': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    'width': 1100
                }
            ),
            'pregunta_2': forms.TextInput(
                attrs = {
                    'class': 'input-group-field',
                    'disabled' : 'disabled'
                    
                }
            ),
            'calificacion_2': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                }
            ),
            'pregunta_3': forms.TextInput(
                attrs = {
                    'class': 'input-group-field',
                    'disabled' : 'disabled'
                }
            ),
            'calificacion_3': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                }
            ),
            'pregunta_4': forms.TextInput(
                attrs = {
                    'class': 'input-group-field',
                    'disabled' : 'disabled'
                }
            ),
            'calificacion_4': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                }
            ),
            'pregunta_5': forms.TextInput(
                attrs = {
                    'class': 'input-group-field',
                    'disabled' : 'disabled'
                }
            ),
            'calificacion_5': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                }
            ),
            'observacion': forms.TextInput(
                attrs = {
                    'class': 'input-group-field',
                    'placeholder': 'Observación'
                }
            ),
            
            

        }
class guiafisicoForm(forms.ModelForm):
    
    class Meta:
        model = Guia
        fields = (
            'id_guia',
            'bolsa',
            'seudo',   
            'user',   
        )

class CacUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CacUpdateForm, self).__init__(*args, **kwargs)
        self.fields['id_ciu'].queryset = Ciudad.objects.filter(cubrimiento = "COBERTURA")
        self.fields['mot'].queryset = Motivo.objects.filter(Q (id = 19)|Q(id = 20))
        self.fields['cod_vis'].queryset = Cod_vis.objects.filter(
            Q (id = 21)|Q(id = 22)|Q(id = 23)|Q(id = 24)|Q(id = 25)
            |Q(id = 26)|Q(id = 27)|Q(id = 28)|Q(id = 29)|Q(id = 30)
            |Q(id = 31)|Q(id = 32)|Q(id = 33)|Q(id = 34)|Q(id = 35)
            )
    
    class Meta:
        model = Guia
        fields = (
            'direccion',
            'id_ciu',
            'postal',
            'mot',
            'cod_vis',
            'oficina',
            'proceso',
            
        )

        widgets = {
            'direccion': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo de barras Bolsa', 'autofocus': 'autofocus',
                    'autocomplete': "off"
                }
            ),
            'postal': forms.TextInput(
                attrs = {
                    'placeholder': 'Postal',
                    'class': 'input-group-field',         
                    
                }
            ),
            'id_ciu': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                    
                }
            ),
            'mot': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                       
                }
            ),
            'cod_vis': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                    
                }
            ),
            'motivo_call': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                      
                }
            ),
            'oficina': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                    
                }
            ),
            'proceso': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                    
                }
            ),
            
}

class CallUpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CallUpdateForm, self).__init__(*args, **kwargs)
        self.fields['motivo_call'].queryset = Motivo_call.objects.filter(Q (id = 11)|Q(id = 12))
    
    class Meta:     
        model = Telefono
        exclude = ('user', 'tel', 'indicativo', 'id')

        widgets = {
            
            'motivo_call': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                }

            ),
            
            'observacion': forms.Textarea(
                attrs = {
                    'class': 'myradio',
                    'placeholder': 'Observacion', 
                    'size': 500
                }

            ),
                    
}   

class CallGuiaUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CallGuiaUpdateForm, self).__init__(*args, **kwargs)
        self.fields['cod_vis'].queryset = Cod_vis.objects.filter(id = 33)
    
    class Meta:
        model = Guia
        
        exclude = ('m', 'ancho', 'alto',
         'largo', 'copia', 'unidad', 'contiene', 'orden', 'domicilio', 'acarreo', 'flete',
         'origen', 'destino', 'codigo', 'declarado', 'cantidad_vi', 'd_i', 'producto',
         'id_clie', 'proceso', 'destinatario', 'postal', 'id_ser', 
         'mensajero', 'tel', 'oficina', 'fecha_descargue', 'users', 'user',
         'cantidad', 'est_planilla', 'id_planilla', 'cod_ins', 'estado', 'bolsa',
         'estado_destino', 'seudo', 'id_est')

    widgets = {
            'direccion': forms.TextInput(
                attrs = {
                    'placeholder': 'Direccion',
                    'autocomplete': "off"
                }
            ),

            'id_ciu': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    'size': 5
                }
            ),
            'cod_vis': forms.TextInput(
                attrs = {
                    'class': 'input-group-field',
                }
            ),
            'mot': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                    
                }
            )
            

    }

class TelefonoMotivoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TelefonoMotivoForm, self).__init__(*args, **kwargs)
        self.fields['motivo_call'].queryset = Motivo_call.objects.exclude(Q (id = 11)|Q(id = 12))

    class Meta:
        model = Telefono
        fields = ('observacion', 'motivo_call')

