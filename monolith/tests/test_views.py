from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import JsonResponse
from ..models import Estacionamento, Veiculo, Vaga
from ..forms import EstacionamentoForm, VeiculoForm

class EstacionamentoViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

        self.estacionamento = Estacionamento.objects.create(nome='Estacionamento Teste', vagas_carros=10, vagas_motos=5)
        self.vaga_carro = Vaga.objects.create(tipo='CARRO', ocupada=False)
        self.vaga_moto = Vaga.objects.create(tipo='MOTOCICLETA', ocupada=False)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_vagas_disponiveis_view(self):
        response = self.client.get(reverse('vagas_disponiveis') + '?tipo=CARRO')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, 'utf8'), '[{"id": ' + str(self.vaga_carro.id) + '}]')

        response = self.client.get(reverse('vagas_disponiveis') + '?tipo=MOTOCICLETA')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, 'utf8'), '[{"id": ' + str(self.vaga_moto.id) + '}]')

        response = self.client.get(reverse('vagas_disponiveis'))
        self.assertEqual(response.status_code, 400)

    def test_cadastrar_estacionamento_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('cadastrar_estacionamento'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro_estacionamento.html')

        data = {'nome': 'Estacionamento Teste 2', 'vagas_carros': 20, 'vagas_motos': 10}
        response = self.client.post(reverse('cadastrar_estacionamento'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Estacionamento cadastrado com sucesso!')

    def test_cadastrar_veiculo_view(self):
        data = {
            'placa': 'ABC1234',
            'tipo': 'CARRO',
            'vaga': self.vaga_carro.id
        }
        response = self.client.post(reverse('cadastrar_veiculo'), data)
        self.assertEqual(response.status_code, 302)
        self.vaga_carro.refresh_from_db()
        self.assertTrue(self.vaga_carro.ocupada)

    def test_verificar_placa_view(self):
        Veiculo.objects.create(placa='ABC1234', tipo='CARRO', vaga=self.vaga_carro)
        response = self.client.post(reverse('verificar_placa'), {'placa': 'ABC1234'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, 'utf8'), '{"status": "placa_existe"}')

        response = self.client.post(reverse('verificar_placa'), {'placa': 'XYZ9876'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, 'utf8'), '{"status": "ok"}')

    def test_excluir_veiculo_view(self):
        veiculo = Veiculo.objects.create(placa='XYZ9876', tipo='CARRO', vaga=self.vaga_carro)
        vaga_id = self.vaga_carro.id
        response = self.client.post(reverse('excluir_veiculo', args=[veiculo.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.vaga_carro.ocupada)
        with self.assertRaises(Veiculo.DoesNotExist):
            veiculo.refresh_from_db()
