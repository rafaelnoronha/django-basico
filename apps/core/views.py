from django.shortcuts import render
from .models import Empresa


def home(request):
    empresa = Empresa.objects.last()

    context = {
        'empresa': empresa
    }
    return render(request, 'home.html', context)
