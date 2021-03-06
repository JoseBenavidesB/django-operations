# Generated by Django 3.2.4 on 2021-08-24 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0022_auto_20210823_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='status',
            field=models.CharField(choices=[('PR', 'Pendiente Revisión'), ('EC', 'Enviado al Cliente'), ('PE', 'Pendiente de Envio'), ('R', 'Rechazado'), ('A', 'Aprobada')], max_length=15, null=True, verbose_name='Estatus'),
        ),
        migrations.AlterField(
            model_name='draw',
            name='status',
            field=models.CharField(choices=[('finalizado', 'Finalizado'), ('sin_concluir', 'Sin concluir')], default='Sin concluir', max_length=15, verbose_name='Estado'),
        ),
    ]
