# Generated by Django 3.2.4 on 2021-10-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0059_alter_draw_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='date_bill1',
        ),
        migrations.AlterField(
            model_name='quotes',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Cotización creada el'),
        ),
    ]
