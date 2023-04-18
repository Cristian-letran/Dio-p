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
   
    class Meta:
        model = Vinculacion
        fields = (
        '__all__'   )
           
        widgets = {
            'celular': forms.NumberInput(
                
            ),
            'identificacion': forms.NumberInput(
            ),
            'celular_confirma': forms.NumberInput(
                
            )
            
            }

    
    def clean(self):
        cleaned_data = super().clean()
        celular = cleaned_data.get('celular')
        celular_confirma  = cleaned_data.get('celular_confirma')
        #############Tipo gestion#######################
        tipo_gestion  = cleaned_data.get('tipo_gestion')
        nombre  = cleaned_data.get('nombre')
        nombre_comercio = cleaned_data.get('nombre_comercio')
        categoria = cleaned_data.get('categoria')
        direccion = cleaned_data.get('direccion')
        codigo_transaccion = cleaned_data.get('codigo_transaccion')
        no_transaccion = cleaned_data.get('no_transaccion')
        se_registro = cleaned_data.get('se_registro')

        if celular != celular_confirma:
            raise forms.ValidationError( "Celular incorrecto." )
        
        if tipo_gestion.id ==1 and nombre == None:
            raise forms.ValidationError( "Completar Nombre del cliente DaviPlata" )
        
        elif tipo_gestion.id ==1 and celular == None:
            raise forms.ValidationError( "Completar No. celular activado en DaviPlata" )
        
        elif tipo_gestion.id ==1 and nombre_comercio == None:
            raise forms.ValidationError( "Completar Nombre comercio" )
        
        elif tipo_gestion.id ==1 and categoria == None:
            raise forms.ValidationError( "Completar ¿A cuál de las siguientes categorías pertenece el comercio?" )
        
        ###################################EMARCACIÓN#########################################
        
        if tipo_gestion.id ==2 and nombre == None:
            raise forms.ValidationError( "Completar Nombre del cliente DaviPlata" )
        
        elif tipo_gestion.id ==2 and celular == None:
            raise forms.ValidationError( "Completar No. celular activado en DaviPlata" )
        
        elif tipo_gestion.id ==2 and nombre_comercio == None:
            raise forms.ValidationError( "Completar Nombre comercio" )
        
        elif tipo_gestion.id ==2 and categoria == None:
            raise forms.ValidationError( "Completar ¿A cuál de las siguientes categorías pertenece el comercio?" )
        
        ########## DIRECCION  ###########################

        if direccion == None:
            raise forms.ValidationError( "Completar Dirección Comercio" )
        
        ############## Codigo transaccion #######################

        if codigo_transaccion == None and no_transaccion == None:
            raise forms.ValidationError( "Completar ¿Por qué no se realizó la transacción de $1?" )
        
        # if se_registro == "NO":
        #     raise forms.ValidationError( "¿Por que no se realizo el registro en perfil mi negocio?" )
        
        return self.cleaned_data
        
    


        
    
        

        
        
    
        
        
        
    

    
    
    
    
        
        
    
        
    