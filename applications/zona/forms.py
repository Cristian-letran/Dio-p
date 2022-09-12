from django import forms
from .models import ZonaGuia

class ZonaForm(forms.ModelForm):

    class Meta:
        model = ZonaGuia
        fields = (
            'guia',
            'zona'
        )

        widgets = {
            'guia': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo de barras Bolsa', 'autofocus': 'autofocus',
                    'class': 'input-group-field',
                }
            ),

        }