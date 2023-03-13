from django import forms
from .models import Daviplata
from django.forms import ModelForm, Textarea

class DaviplataForm(forms.ModelForm):
    
    class Meta:
        model = Daviplata
        fields = (
            '__all__'
        )
        exclude = ('user',)

        widgets = {

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
    }

        