from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Estacionamento, Vaga

@receiver(post_save, sender=Estacionamento)
def criar_vagas(sender, instance, created, **kwargs):
    if created:
        # Delete todas as vagas associadas ao estacionamento atual
        instance.vaga_set.all().delete()

        # Recreate vagas for the estacionamento
        for _ in range(instance.vagas_carros):
            Vaga.objects.create(estacionamento=instance, tipo='CARRO')

        for _ in range(instance.vagas_motos):
            Vaga.objects.create(estacionamento=instance, tipo='MOTOCICLETA')
