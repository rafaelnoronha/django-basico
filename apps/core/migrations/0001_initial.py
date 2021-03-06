# Generated by Django 3.2.3 on 2021-05-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True, verbose_name='Data da Criação')),
                ('hora_criacao', models.TimeField(auto_now_add=True, verbose_name='Hora da Criação')),
                ('data_edicao', models.DateField(auto_now=True, verbose_name='Data da Edição')),
                ('hora_edicao', models.TimeField(auto_now=True, verbose_name='Hora da Edição')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('razao_social', models.CharField(max_length=100, verbose_name='Razão Social')),
                ('cnpj', models.CharField(max_length=18, verbose_name='CNPJ')),
                ('telefone', models.CharField(blank=True, max_length=10, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('link_endereco', models.URLField(max_length=250, verbose_name='Link Endereço')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
