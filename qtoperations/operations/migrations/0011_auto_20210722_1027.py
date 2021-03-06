# Generated by Django 3.2.4 on 2021-07-22 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0010_auto_20210718_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastralplans',
            name='solicitud_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='solicitudCadastral', to='operations.solicitudes', verbose_name='Solicitud'),
        ),
        migrations.AlterField(
            model_name='fieldsurvey',
            name='solicitud_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='operations.solicitudes', verbose_name='solicitudField'),
        ),
        migrations.AlterField(
            model_name='levelcurves',
            name='solicitud_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='solicitudLevel', to='operations.solicitudes', verbose_name='Solicitud'),
        ),
        migrations.AlterField(
            model_name='replant',
            name='solicitud_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='solicitudReplant', to='operations.solicitudes', verbose_name='Solicitud'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='solicitud_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='solicitudReport', to='operations.solicitudes', verbose_name='Solicitud'),
        ),
    ]
