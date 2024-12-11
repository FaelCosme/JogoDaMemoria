from django.shortcuts import render, redirect
from galeria.models import Jogo, Jogador
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import JsonResponse


def format_time(seconds):
    try:
        seconds = int(seconds)  # Converte para inteiro, se possível
    except ValueError:
        return "0m 00s"  # Caso o valor não seja um número válido

    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}m {remaining_seconds:02d}s"

def listar_jogos():
    jogos = Jogo.objects.all().order_by('tentativas', 'tempo', '-data_hora')
    jogo_listar = []
    posicao = 1
    for jogo in jogos:
        local_time = jogo.data_hora
        jogo.tempo = format_time(jogo.tempo)
        jogo_listar.append({
            "Posição": f"{posicao}°",
            "Nome": jogo.nome,
            "Tentativas": jogo.tentativas,
            "Tempo": jogo.tempo,
            "Data": local_time.strftime("%d/%m/%Y"),
            "Hora": local_time.strftime("%H:%M:%S"),
        })
        posicao += 1
    return jogo_listar


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {'error': 'Usuário ou senha inválidas'})

    jogo_listar = listar_jogos()
    return render(request, 'registration/login.html', {'jogo_listar': jogo_listar})


@login_required
def index(request):
    jogo_listar = listar_jogos()
    return render(request, 'index.html', {'jogo_listar': jogo_listar})

# view do ranking
def ranking(request):
    jogo_listar = listar_jogos()
    return render(request, 'ranking.html', {'jogo_listar': jogo_listar})


@login_required
def jogoSave(request):
    if request.method == "POST":
        tentativas = request.POST.get('tentativas')
        tempo = request.POST.get('tempo')

        # Verificar se o Jogador já existe ou criar um novo
        jogador, created = Jogador.objects.get_or_create(user=request.user)

        # Criar o objeto Jogo
        jogo = Jogo(nome=request.user.username, tentativas=tentativas, tempo=tempo, jogador=jogador)
        jogo.save()

        # Retornar uma resposta JSON
        return JsonResponse({'status': 'success', 'message': 'Jogo salvo com sucesso!'})
    
    return JsonResponse({'status': 'error', 'message': 'Método inválido.'})






       

