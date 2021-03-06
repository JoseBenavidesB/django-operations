# Generated by Django 3.2.4 on 2021-07-19 00:12

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0009_auto_20210717_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='prefix',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Prefijo'),
        ),
        migrations.AlterField(
            model_name='services',
            name='typeService',
            field=models.CharField(max_length=40, unique=True, verbose_name='Tipo Servicio'),
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='deliveryDate',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(datetime.date.today)], verbose_name='Fecha Entrega'),
        ),
    ]
