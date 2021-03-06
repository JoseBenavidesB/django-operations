# Generated by Django 3.2.4 on 2021-08-24 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0017_auto_20210823_1909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterField(
            model_name='draw',
            name='status',
            field=models.CharField(choices=[('sin_concluir', 'Sin concluir'), ('finalizado', 'Finalizado')], default='Sin concluir', max_length=15, verbose_name='Estado'),
        ),
    ]
