from django import forms
from .models import Guia, LogBusqueda
from applications.base_cliente.models import Bd_clie
from .models import img
from applications.fisico.models import Fisico

class MensajeroUpdateForm(forms.ModelForm):

    class Meta:
        model = Fisico
        fields = (
            'mot', 
            'img_guia_courrier', 
            'img_fachada_courrier'
        )
        widgets = {
            'img_guia_courrier': forms.FileInput(
                attrs = {
                    'accept': 'image/*', 'capture':'camera',
                }
            ),
            'img_fachada_courrier': forms.FileInput(
                attrs = {
                    'accept': 'image/*', 
                    'capture':'camera',
                    'value': 'hola'
                }
            ),
        }

class guiafisicoForm(forms.ModelForm):

    def __init__(self, fisicos=2, **kwargs):
        super(guiafisicoForm, self).__init__(**kwargs)
        if fisicos:
            self.fields['seudo'].queryset = Bd_clie.objects.filter(fisicos =2)

    class Meta:
        model = Guia
        fields = (
            'bolsa',
            'seudo',   
              
        )

        widgets = {
            'bolsa': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo de barras Bolsa', 'autofocus': 'autofocus',
                    'class': 'input-group-field',
                    # 'maxlength' : 10,
                    # 'minlength' : 7

                }
            ),

            'seudo': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo se barrras Seudo...',
                    'class': 'input-group-field',
                    #'maxlength' : 22,
                    #'minlength' : 22
                    
                }
            ),

        }
    # def clean_Bolsa(self):
    #     bolsa = self.cleaned_data['bolsa']
    #     if len(bolsa) < 5:
    #         raise forms.ValidationError('Ingrese codigo de barras correcto')

    #     return bolsa
    
    # def clean_Seudo(self):
    #     seudo = self.cleaned_data['seudo']
    #     if (seudo) == 2229742839211278919978:
    #         raise forms.ValidationError('Ingrese un codigo de barras correcto')

    #     return seudo
# 
class ImgForm(forms.ModelForm):
    
    class Meta:
        model = img
        fields = (
            'image',
            'id_guia',
            'user',
            
            'mod_date'
        )

class UpdateCourrierForm(forms.ModelForm):
    
    class Meta:
        model = Fisico
        fields = (
            'mot',
            
        )

class UserLogCreateForm(forms.ModelForm):
    
    class Meta:
        model = LogBusqueda
        fields = (
            'id_log',
            
        )
    

    