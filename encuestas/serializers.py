from rest_framework import serializers
from .models import *

class RedesSocialesCatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedesSocialesCatalogo
        fields= '__all__'

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields= 'redSocial','isFavorita','tiempo'
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['red_nombre'] = instance.redSocial.descripcion
        return repr


class EncuestasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuesta
        fields= 'correo', 'edad','sexo'
