from django.db import models
from django.utils import timezone


class Base(models.Model):
    data_criacao = models.DateField(verbose_name='Data da Criação', auto_now_add=True, default=timezone.now)
    hora_criacao = models.TimeField(verbose_name='Hora da Criação', auto_now_add=True, default=timezone.now)
    data_edicao = models.DateField(verbose_name='Data da Edição', auto_now=True)
    hora_edicao = models.TimeField(verbose_name='Hora da Edição', auto_now=True)
    ativo = models.BooleanField(verbose_name='Ativo', default=True)

    class Meta:
        abstract = True


class Empresa(Base):
    razao_social = models.CharField('Razão Social', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=18)
    telefone = models.CharField('Telefone', max_length=10, blank=True)
    endereco = models.CharField('Endereço', max_length=100)
    link_endereco = models.URLField('Link Endereço', max_length=250)

    def __str__(self):
        return f'{self.razao_social} - {self.cnpj}'
