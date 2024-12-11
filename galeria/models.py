from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jogador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Outros campos relacionados ao jogador

    def __str__(self):
        return self.nome
    
class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    tentativas = models.CharField(max_length=10, null=False)
    tempo = models.CharField(max_length=10, null=False)
    data_hora = models.DateTimeField(auto_now_add=True)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name="jogos") #vincula o jogador à partida
    
    def __str__(self):
        return self.nome
    

    