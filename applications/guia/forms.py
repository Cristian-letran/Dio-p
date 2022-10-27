from django import forms
from .models import Guia
from .models import img
from applications.fisico.models import Fisico

class guiafisicoForm(forms.ModelForm):

    class Meta:
        model = Guia
        fields = (
            'id_guia',
            'bolsa',
            'seudo',   
            'user',   
        )

        widgets = {
            'bolsa': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo de barras Bolsa', 'autofocus': 'autofocus',
                    'class': 'input-group-field',
                    'maxlength' : 10,
                    'minlength' : 7

                }
            ),

            'seudo': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo se barrras Seudo...',
                    'class': 'input-group-field',
                    'maxlength' : 22,
                    'minlength' : 22
                    
                }
            ),

        }
    def clean_Bolsa(self):
        bolsa = self.cleaned_data['bolsa']
        if len(bolsa) < 5:
            raise forms.ValidationError('Ingrese codigo de barras correcto')

        return bolsa

        
    def clean_Seudo(self):
        Seudo = self.cleaned_data['Seudo']
        if len(Seudo) < 22:
            raise forms.ValidationError('Ingrese un codigo de barras correcto')

        return Seudo

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
    

    