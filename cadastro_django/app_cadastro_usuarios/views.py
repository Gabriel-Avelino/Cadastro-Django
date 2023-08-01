from django.shortcuts import render
from django.db import IntegrityError
from .models import Usuario


def home(request):
    return render(request, 'usuarios/home.html')

# Create your views here.

def usuarios(request):
    # Salvar os dados da tela para o banco.
    '''
    if request.method == 'POST':
            nome = request.POST.get('nome')
            idade = request.POST.get('idade')

            try:
                novo_usuario = Usuario.objects.create(nome=nome, idade=idade)
            except IntegrityError:
                # Tratar o caso de violação de chave única (usuário duplicado)
                # Caso deseje, você pode logar o erro ou tomar outras ações apropriadas.
                pass
    '''

    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        try:
            novo_usuario = Usuario.objects.create(nome=nome, idade=idade)
        except IntegrityError:
            # Tratar o caso de violação de chave única (usuário duplicado)
            # Caso deseje, você pode logar o erro ou tomar outras ações apropriadas.
            pass
    # Exibir usuários cadastrados.
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    # Retornar dados para a página de usuários.
    return render(request, 'usuarios/usuarios.html', usuarios)