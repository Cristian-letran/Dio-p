from django import forms
from .models import No_fisico

class No_fisicoForm(forms.ModelForm):
    
    class Meta:
        model = No_fisico
        fields = (
            'seudo', 
        )

        widgets = {
            'seudo': forms.TextInput(
                attrs = {
                    'placeholder': 'Codigo se barrras Seudo...',
                    'class': 'input-group-field',
                    
                }
            ),
            
            }