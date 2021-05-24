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


class Empresa(Base):
    razao_social = models.CharField(
        verbose_name='Razão Social',
        max_length=100
    )

    cnpj = models.CharField(
        verbose_name='CNPJ',
        max_length=18
    )

    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=10,
        blank=True
    )

    endereco = models.CharField(
        verbose_name='Endereço',
        max_length=100
    )

    link_endereco = models.URLField(
        verbose_name='Link Endereço',
        max_length=250
    )

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'{self.razao_social} - {self.cnpj}'
