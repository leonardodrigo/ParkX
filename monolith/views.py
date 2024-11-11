from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Estacionamento, Veiculo, Vaga
from .forms import EstacionamentoForm, VeiculoForm
from django.contrib import messages


def cards_veiculos_estacionamento():
    # Carros
    quantidade_carros = Veiculo.objects.filter(tipo='CARRO').count()
    estacionamento = Estacionamento.objects.first()
    total_vagas_carros = estacionamento.vagas_carros if estacionamento else 0
    taxa_ocupacao_carros = int((quantidade_carros / total_vagas_carros) * 100) if total_vagas_carros != 0 else 0
    vagas_carros_livres = total_vagas_carros - quantidade_carros 

    # Motocicletas
    quantidade_motocicletas = Veiculo.objects.filter(tipo='MOTOCICLETA').count()
    total_vagas_motocicletas = estacionamento.vagas_motos if estacionamento else 0
    taxa_ocupacao_motocicletas = int((quantidade_motocicletas / total_vagas_motocicletas) * 100) if total_vagas_motocicletas != 0 else 0
    vagas_motocicletas_livres = total_vagas_motocicletas - quantidade_motocicletas

    # Vagas Disponíveis
    vagas_disponiveis = Vaga.objects.filter(ocupada=False)

    # Tabela de Veículos
    veiculos = Veiculo.objects.all()

    cards_dictionary = {
        'taxa_ocupacao_carros': taxa_ocupacao_carros,
        'vagas_carros_livres': vagas_carros_livres,
        'taxa_ocupacao_motocicletas': taxa_ocupacao_motocicletas,
        'vagas_motocicletas_livres': vagas_motocicletas_livres,
        'vagas_disponiveis': vagas_disponiveis,
        'veiculos': veiculos
    }

    return cards_dictionary


def index(request):
    cards = cards_veiculos_estacionamento()
    return render(request, 'index.html', cards)

def vagas_disponiveis(request):
    tipo_veiculo = request.GET.get('tipo')
    if tipo_veiculo:
        if tipo_veiculo == 'CARRO':
            vagas_disponiveis = Vaga.objects.filter(ocupada=False, tipo='CARRO')
        elif tipo_veiculo == 'MOTOCICLETA':
            vagas_disponiveis = Vaga.objects.filter(ocupada=False, tipo='MOTOCICLETA')
        else:
            vagas_disponiveis = Vaga.objects.filter(ocupada=False)

        vagas = [{'id': vaga.id} for vaga in vagas_disponiveis]
        return JsonResponse(vagas, safe=False)
    else:
        return JsonResponse({'error': 'Tipo de veículo não especificado'}, status=400)

def cadastrar_estacionamento(request):
    if request.method == 'POST':
        form = EstacionamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cadastro_estacionamento.html', {'form': EstacionamentoForm(), 'success_message': 'Estacionamento cadastrado com sucesso!'})
    else:
        form = EstacionamentoForm()
    return render(request, 'cadastro_estacionamento.html', {'form': form})

def cadastrar_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            veiculo = form.save()
            vaga_id = request.POST.get('vaga')
            vaga = Vaga.objects.get(pk=vaga_id)
            vaga.ocupada = True
            vaga.save()
            return redirect('home')
    return redirect('home')

def verificar_placa(request):
    if request.method == 'POST':
        placa = request.POST.get('placa', None)
        if placa:
            if Veiculo.objects.filter(placa=placa).exists():
                return JsonResponse({'status': 'placa_existe'})
    return JsonResponse({'status': 'ok'})

def excluir_veiculo(request, veiculo_id):
    if request.method == 'POST':
        veiculo = Veiculo.objects.get(pk=veiculo_id)
        vaga = veiculo.vaga
        veiculo.delete()
        vaga.ocupada = False
        vaga.save()
        messages.success(request, 'Veículo excluído com sucesso!')
    return redirect('home')
