from django.contrib import admin
from .models import Produto, Categoria


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = ('id', 'nome', 'preco', 'estoque', 'quantidade_vendida')
    list_filter = ('quantidade_vendida', 'preco')
    search_fields = ('nome', 'descricao')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = ('id', 'nome', 'descricao', 'data_criacao', 'hora_criacao')
    search_fields = ('nome', 'descricao')