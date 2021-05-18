from django.shortcuts import render


def produtos(request):
    pass


def produto(request, id_produto):
    return render(request, 'produto.html')
