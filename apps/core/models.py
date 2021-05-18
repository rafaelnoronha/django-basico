from django.db import models


class Empresa(models.Model):
    razao_social = models.CharField('Razão Social', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=18)
    telefone = models.CharField('Telefone', max_length=10, blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=100)
    link_endereco = models.URLField('Link Endereço', max_length=250)

    def __str__(self):
        return f'{self.razao_social} - {self.cnpj}'
