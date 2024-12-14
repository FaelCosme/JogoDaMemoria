from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from jogoMemoria.models import Jogo

# Register your models here.
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('jogador', 'tentativas', 'tempo', 'data_hora')

admin.site.register(Jogo, JogadorAdmin)

# class CustomUserAdmin(UserAdmin):
#     # Adicione customizações aqui, se necessário, como campos extras, filtros, etc.
#     pass
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)