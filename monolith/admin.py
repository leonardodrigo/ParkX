from django.contrib import admin
from . import models


LIST_PER_PAGE = 10


@admin.register(models.Estacionamento)
class EstacionamentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'telefone', 'email', 'cnpj']
    list_editable = ['telefone', 'email']
    ordering = ['nome']
    list_per_page = LIST_PER_PAGE