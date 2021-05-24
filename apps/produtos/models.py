from django.db import models


class Base(models.Model):
    data_criacao = models.DateField(
        verbose_name='Data da Criação',
        auto_now_add=True
    )

    hora_criacao = models.TimeField(
        verbose_name='Hora da Criação',
        auto_now_add=True
    )

    data_edicao = models.DateField(
        verbose_name='Data da Edição',
        auto_now=True
    )

    hora_edicao = models.TimeField(
        verbose_name='Hora da Edição',
        auto_now=True
    )

    ativo = models.BooleanField(
        verbose_name='Ativo',
        default=True
    )

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    preco = models.DecimalField(
        verbose_name='Preço',
        decimal_places=2,
        max_digits=8,
        default=0.00
    )

    descricao = models.TextField(
        verbose_name='Descrição',
        blank=True
    )

    estoque = models.IntegerField(
        verbose_name='Estoque',
        null=True,
        default=0
    )

    quantidade_vendida = models.PositiveIntegerField(
        verbose_name='Quantidade Vendida',
        null=True,
        default=0
    )

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.nome} - R${self.preco}'


class Categoria(Base):
    nome = models.CharField(
        verbose_name='nome',
        max_length=100
    )

    descricao = models.TextField(
        verbose_name='descricao',
        blank=True
    )

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome
