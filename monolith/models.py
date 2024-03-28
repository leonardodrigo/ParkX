from django.db import models

# Create your models here.
class Estacionamento(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    cnpj = models.CharField(max_length=14)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Vaga(models.Model):
    TIPO_VAGA = (
        ('M', 'Moto'),
        ('C', 'Carro'),
        ('D', 'Deficiente'),
    )

    tipo = models.CharField(max_length=1, choices=TIPO_VAGA)
    numero = models.IntegerField()
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)
    ocupada = models.BooleanField(default=False)
    estacionamento = models.ForeignKey(Estacionamento, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.numero)

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_nascimento = models.DateField()
    data_admissao = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cargo = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cor_primaria = models.CharField(max_length=20)
    cor_secundaria = models.CharField(max_length=20)
    ano = models.IntegerField()
    proprietario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa
    
class Pagamento(models.Model):
    TIPO_PAGAMENTO = (
        ('D', 'Débito'),
        ('C', 'Crédito'),
        ('B', 'Boleto'),
        ('P', 'Pix')
    )

    STATUS_PAGAMENTO = (
        ('P', 'Pendete'),
        ('C', 'Concluído'),
        ('R', 'Recusado'),
        ('E', 'Erro')
    )

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    pago_em = models.DateTimeField(auto_now_add=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_PAGAMENTO)
    metodo_pagamento = models.CharField(max_length=1, choices=TIPO_PAGAMENTO, default='P')

    def __str__(self):
        return str(self.valor)

