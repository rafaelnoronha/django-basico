# Generated by Django 3.2.3 on 2021-05-19 02:01

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True, verbose_name='Data da Criação')),
                ('hora_criacao', models.TimeField(auto_now_add=True, verbose_name='Hora da Criação')),
                ('data_edicao', models.DateField(auto_now=True, verbose_name='Data da Edição')),
                ('hora_edicao', models.TimeField(auto_now=True, verbose_name='Hora da Edição')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='id',
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefone',
            field=models.CharField(blank=True, max_length=10, verbose_name='Telefone'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='base_ptr',
            field=models.OneToOneField(auto_created=True, default=datetime.datetime(2021, 5, 19, 2, 1, 8, 371965, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base'),
            preserve_default=False,
        ),
    ]