from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from jogoMemoria.models import Jogador

@receiver(post_save, sender=User)
def criar_jogador(sender, instance, created, **kwargs):
    if created:
        Jogador.objects.create(user=instance, nickname=instance.username)

@receiver(post_save, sender=User)
def salvar_jogador(sender, instance, **kwargs):
    instance.jogador.save()
