from django.shortcuts import render, get_object_or_404
from apps.core.models import Empresa
from .models import Produto


def produtos(request):
    pass


def produto(request, id_produto):
    empresa = Empresa.objects.last()
    produto = get_object_or_404(Produto, id=id_produto)

    context = {
        'empresa': empresa,
        'produto': produto
    }
    return render(request, 'produto.html', context)
