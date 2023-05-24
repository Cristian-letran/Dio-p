from rest_framework import serializers
from .models import Guia
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from applications.tracking.models import Rastreo

class GuiaSerializer(serializers.ModelSerializer):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    estado = serializers.SlugRelatedField(
    
        
        read_only=True,
        slug_field='Estado'
    )
    class Meta:
        model = Rastreo
        fields = (
            'id_guia',
            'motivopr',
            'estado',
            'mensajero',
            'fecha',
            'estado',
            'guia_tracking'
        )
