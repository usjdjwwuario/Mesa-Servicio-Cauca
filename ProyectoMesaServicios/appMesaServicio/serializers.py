from rest_framework import serializers
from .models import *

class OficinaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OficinaAmbiente
        fields = '_all_' 
        
        
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '_all_' 
        
        
        
class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '_all_' 
        
        
        
class CasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caso
        fields = '__all__'                 
                
                
                
class TipoProcedimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProcedimiento
        fields = '__all__'
        
        
class SolucionCasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolucionCaso
        fields = '__all__'        
        
        
        
class SolucionCasoTipoProcedimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolucionCasoTipoProcedimientos
        fields = '__all__'