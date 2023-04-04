from django import forms
from .models import Daviplata, Vinculacion
from django.forms import ModelForm, Textarea
from django.core.exceptions import ValidationError

class DaviplataForm(forms.ModelForm):
    
    class Meta:
        model = Daviplata
        fields = (
            '__all__'
        )
        exclude = ('user',)

        widgets = {

            'url_img_f': forms.FileInput(
                attrs = {
                    'accept': 'image/*', 'capture':'camera',
                }
            ),
            'url_img_m': forms.FileInput(
                attrs = {
                    'accept': 'image/*', 'capture':'camera',
                }
            ),
            'url_img_o': forms.FileInput(
                attrs = {
                    'accept': 'image/*', 'capture':'camera',
                }
            ),

            'obervacion': Textarea(attrs={'cols': 80, 'rows': 4}),
               
            
            'fecha_capacitacion': forms.DateInput(
            format=(
                '%m/%d/%Y'
                ), 
            attrs={
                'class':'form-control', 
                'placeholder':'Select a date', 
                'type':'date'
            }),

            'fecha_encuesta': forms.DateInput(
            format=(
                '%m/%d/%Y'
                ), 
            attrs={
                'class':'form-control', 
                'placeholder':'Select a date', 
                'type':'date'
            }),

            'nombre_establecimiento': forms.TextInput(
                attrs = {
                    'class': 'input-group-field',
                    'readonly':'readonly'
                }
            ),
            'direccion_base': forms.TextInput(
                attrs = {
                    'class': 'input-group-field',
                    'readonly':'readonly'
                }
            ),
    }

class VinculacionForm(forms.ModelForm):
    celular = forms.CharField(
        label='Celular',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Celular'
            }
        )
    )
    celular_confirma = forms.CharField(
        label='Celular',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Repetir Celular'
            }
        )
    )
    class Meta:
        model = Vinculacion
        fields = (
        '__all__'   )
           
        widgets = {
            'celular': forms.NumberInput(
            ),
            'identificacion': forms.NumberInput(
            ),
            'celular_confirma': forms.NumberInput()
            
            }

    
    def clean(self):
        cleaned_data = super().clean()
        celular = cleaned_data.get('celular')
        celular_confirma  = cleaned_data.get('celular_confirma')

        if celular != celular_confirma:
            raise forms.ValidationError( "Celular incorrecto." )

    
    
    
    
        
        
    
        
    