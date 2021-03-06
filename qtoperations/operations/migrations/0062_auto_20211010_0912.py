# Generated by Django 3.2.4 on 2021-10-10 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0061_payments_date_bill1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draw',
            name='status',
            field=models.CharField(choices=[('sin_concluir', 'Sin concluir'), ('finalizado', 'Finalizado')], default='Sin concluir', max_length=15, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='fieldsurvey',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='fieldsurvey_assigned', to='operations.employees', verbose_name='Asignado a:'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='date_bill1',
            field=models.DateField(blank=True, help_text='Colocar Fecha dd/mm/año', null=True, verbose_name='Fecha de 1 factura'),
        ),
    ]
