from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('cadastro_estacionamento.html', views.cadastrar_estacionamento, name='cadastro_estacionamento'),
    path('cadastrar_veiculo', views.cadastrar_veiculo, name='cadastrar_veiculo'),
    path('excluir_veiculo/<int:veiculo_id>/', views.excluir_veiculo, name='excluir_veiculo'),
    path('vagas_disponiveis/', views.vagas_disponiveis, name='vagas_disponiveis'),
]
