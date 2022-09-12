# from rest_framework import serializers

# from .models import Cargue
# from applications.courrier.models import courrier
# from applications.fisico.models import Fisico


# class CargueSerializer(serializers.ModelSerializer):
#     guia = serializers.PrimaryKeyRelatedField(queryset=Fisico.objects.all(), many=True)
#     class Meta:
#         model = Cargue
#         fields = ('id', 'guia', 'full_name', )
        
# class FisicoSerializer(serializers.ModelSerializer):
        
#     class Meta:
#         model = courrier
#         fields = ('id_courrier', 'courrier', )
        

    