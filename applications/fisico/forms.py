from django import forms
from .models import Paquete, Cobertura
from applications.argumento.models import Estado


class ProductForm(forms.ModelForm):

    class Meta:
        model = Paquete
        fields = (
            'bolsa',
            'seudo',
            'user'          
        )

        widgets = {
            'bolsa': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo de barras Bolsa', 'autofocus': 'autofocus',
                    'class': 'input-group-field',
                }
            ),

            'seudo': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo se barrras Seudo...',
                    'class': 'input-group-field',
                    
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
# class FisicoForm(forms.ModelForm):

#     class Meta:
#         model = Fisico
#         fields = ('bolsa', 'seudo')

class CoberturaForm(forms.ModelForm):

    class Meta:
        model = Cobertura
        fields = (
            'bolsa', 'estado'
                  
        )
        widgets = {
            
            'estado': forms.Select(
                attrs = {
                    'placeholder': 'Codigo de barras Bolsa', 'autofocus': 'autofocus',
                    'class': 'input-group-field',
                }
            ),
        }
    



    
    
