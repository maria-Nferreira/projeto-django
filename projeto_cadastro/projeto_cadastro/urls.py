from django.urls import path
from app_cadastro import views

urlpatterns = [
    path('', views.home, name='home'), #rota, view responsável (a função vai ser executada), nome de referência

    #cadastro.com/listagem-cadastro
    path('cadastro/', views.cadastro, name='listagem_cadastro')
]
