from rest_framework import serializers
from .models import Estacionamento


class EstacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacionamento
        fields = ['id', 'nome', 'endereco', 'telefone', 'email', 'cnpj', 'ativo']
