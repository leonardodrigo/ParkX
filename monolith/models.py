from django.db import models


class Estacionamento(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    cnpj = models.CharField(max_length=100, unique=True)
    vagas_carros = models.IntegerField(default=0)
    vagas_motos = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

    class Meta():
        ordering = ['nome']


class Veiculo(models.Model):
    PLACA_CHOICES = [
        ('CARRO', 'Carro'),
        ('MOTOCICLETA', 'Motocicleta')
    ]

    placa = models.CharField(max_length=10, unique=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    tipo = models.CharField(max_length=50, choices=PLACA_CHOICES, default='CARRO')
    vaga = models.ForeignKey('Vaga', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.placa
    

class Vaga(models.Model):
    estacionamento = models.ForeignKey(Estacionamento, on_delete=models.CASCADE)
    cadastrada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)
    tipo = models.CharField(max_length=50, choices=Veiculo.PLACA_CHOICES)
    ocupada = models.BooleanField(default=False)
