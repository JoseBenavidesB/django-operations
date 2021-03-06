# Generated by Django 3.2.4 on 2021-10-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0036_auto_20211004_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Digite el monto con 2 decimales', max_digits=9, null=True, verbose_name='Monto en $'),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='status',
            field=models.CharField(choices=[('Pendiente Revisión', 'Pendiente Revisión'), ('Enviado al Cliente', 'Enviado al Cliente'), ('Pendiente de Envio', 'Pendiente de Envio'), ('Rechazado', 'Rechazado'), ('Aprobada', 'Aprobada')], default='PR', max_length=50, null=True, verbose_name='Estatus'),
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='plan',
            field=models.URLField(blank=True, help_text='Link del plano, por favor', verbose_name='Plano'),
        ),
    ]
