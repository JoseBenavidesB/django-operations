# Generated by Django 3.2.4 on 2021-10-10 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0048_auto_20211008_2017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preliminary',
            options={'ordering': ('-id',), 'verbose_name': 'Preliminar', 'verbose_name_plural': 'Preliminares'},
        ),
        migrations.AlterField(
            model_name='draw',
            name='status',
            field=models.CharField(choices=[('sin_concluir', 'Sin concluir'), ('finalizado', 'Finalizado')], default='Sin concluir', max_length=15, verbose_name='Estado'),
        ),
    ]
