from django.shortcuts import render
from .models import Empresa


def home(request):
    empresa = Empresa.objects.get(id=1)

    context = {
        'empresa': empresa
    }
    return render(request, 'home.html', context)
