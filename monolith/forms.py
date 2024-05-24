from django import forms
from .models import Estacionamento, Veiculo

class EstacionamentoForm(forms.ModelForm):
    class Meta:
        model = Estacionamento
        fields = ['nome', 'endereco', 'telefone', 'email', 'cnpj', 'vagas_carros', 'vagas_motos']

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'vaga', 'tipo']
