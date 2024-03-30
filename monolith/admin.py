from django.contrib import admin
from . import models

LIST_PER_PAGE = 10

@admin.register(models.Estacionamento)
class EstacionamentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'telefone', 'email', 'cnpj', 'ativo']
    list_editable = ['telefone', 'email', 'ativo']
    ordering = ['nome']
    list_per_page = LIST_PER_PAGE

@admin.register(models.Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'numero', 'criada_em', 'atualizada_em', 'ocupada', 'estacionamento']
    list_editable = ['ocupada']
    ordering = ['numero']
    list_per_page = LIST_PER_PAGE

@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'email', 'telefone', 'endereco', 'salario', 'data_nascimento', 'data_admissao', 'criado_em', 'atualizado_em', 'cargo', 'ativo']
    list_editable = ['telefone', 'email', 'salario', 'cargo', 'ativo']
    ordering = ['nome']
    list_per_page = LIST_PER_PAGE

@admin.register(models.Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'placa',  'cadastrado_em', 'atualizado_em', 'cor_primaria', 'cor_secundaria', 'ano', 'proprietario', 'vaga']
    list_editable = ['vaga']
    ordering = ['atualizado_em']
    list_per_page = LIST_PER_PAGE

@admin.register(models.Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ['valor', 'pago_em', 'veiculo', 'status', 'metodo_pagamento']
    list_editable = ['status', 'metodo_pagamento']
    ordering = ['pago_em']
    list_per_page = LIST_PER_PAGE