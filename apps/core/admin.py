from django.contrib import admin
from .models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    ordering = ('-id', )
    list_display = ('id', 'razao_social', 'cnpj', 'telefone', 'endereco')
    list_filter = ('ativo',)
    search_fields = ('razao_social', 'cnpj')
