# Generated by Django 5.0.3 on 2024-03-28 01:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('cnpj', models.CharField(max_length=14)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=100)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_nascimento', models.DateField()),
                ('data_admissao', models.DateField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('cargo', models.CharField(max_length=50)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('M', 'Moto'), ('C', 'Carro'), ('D', 'Deficiente')], max_length=1)),
                ('numero', models.IntegerField()),
                ('criada_em', models.DateTimeField(auto_now_add=True)),
                ('atualizada_em', models.DateTimeField(auto_now=True)),
                ('ocupada', models.BooleanField(default=False)),
                ('estacionamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monolith.estacionamento')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=7)),
                ('cadastrado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('cor_primaria', models.CharField(max_length=20)),
                ('cor_secundaria', models.CharField(max_length=20)),
                ('ano', models.IntegerField()),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monolith.funcionario')),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monolith.vaga')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pago_em', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(choices=[('D', 'Débito'), ('C', 'Crédito'), ('B', 'Boleto'), ('P', 'Pix')], max_length=1)),
                ('status', models.CharField(choices=[('P', 'Pendete'), ('C', 'Concluído'), ('R', 'Recusado'), ('E', 'Erro')], max_length=1)),
                ('metodo_pagamento', models.CharField(choices=[('D', 'Débito'), ('C', 'Crédito'), ('B', 'Boleto'), ('P', 'Pix')], default='P', max_length=1)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monolith.veiculo')),
            ],
        ),
    ]
