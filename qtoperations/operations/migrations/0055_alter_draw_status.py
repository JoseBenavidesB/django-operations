# Generated by Django 3.2.4 on 2021-10-10 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0054_alter_quotes_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draw',
            name='status',
            field=models.CharField(choices=[('finalizado', 'Finalizado'), ('sin_concluir', 'Sin concluir')], default='Sin concluir', max_length=15, verbose_name='Estado'),
        ),
    ]