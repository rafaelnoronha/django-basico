from django.contrib import admin
from .models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'razao_social', 'cnpj', 'telefone', 'endereco')
    ordering = ('-id', )