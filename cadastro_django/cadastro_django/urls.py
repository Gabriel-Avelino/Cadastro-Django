
from django.urls import path
from app_cadastro_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de referência (No caso da página inicial, podemos apenas deixar em branco).
    # usuarios.com
    path('', views.home, name='home'),
    # usuarios.com/usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios')

]
