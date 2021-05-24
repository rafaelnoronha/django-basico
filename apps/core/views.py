from django.shortcuts import render
from .models import Empresa
from apps.produtos.models import Produto, Categoria


def home(request):
    empresa = Empresa.objects.last()
    categorias = Categoria.objects.filter(ativo=True).order_by('id')
    produtos = Produto.objects.filter(ativo=True)
    produtos_mais_vendidos = produtos.filter(quantidade_vendida__gt=0).order_by('-quantidade_vendida')[:5]

    context = {
        'empresa': empresa,
        'categorias': categorias,
        'produtos': produtos,
        'produtos_mais_vendidos': produtos_mais_vendidos
    }
    return render(request, 'home.html', context)
