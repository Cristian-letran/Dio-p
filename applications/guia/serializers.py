from rest_framework import serializers
from .models import Guia

class GuiaSerializer(serializers.ModelSerializer):
    id_ciu = serializers.SlugRelatedField(
        
        read_only=True,
        slug_field='ciudad'
    )
    class Meta:
        model = Guia
        fields = (
            'id_guia',
            'direccion',
            'destinatario',
            'id_ciu',
            'tel'
        )
