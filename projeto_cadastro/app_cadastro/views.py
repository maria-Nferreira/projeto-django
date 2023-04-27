from django.shortcuts import render
from .models import Cadastro #importando o banco de dados do PYTHON

def home(request):
    return render(request, 'cadastro/home.html')

def cadastro(request):
    #get = buscar os dados
    novo_produto = Cadastro()
    novo_produto.produto = request.POST.get('produto')
    novo_produto.valor = request.POST.get('valor')
    novo_produto.quantidade = request.POST.get('quantidade')
    novo_produto.save() #salvar as informações fornecidas


    #EXIBIR TODOS OS PRODUTOS JÁ CADASTRADOS EM UMA NOVA PÁGINA
    produtos = {
        'produtos': Cadastro.objects.all()
    }

    #retornar os dados para a página de listagem de produtos
    return render(request, 'cadastro/produtos-supermercado.html', produtos)