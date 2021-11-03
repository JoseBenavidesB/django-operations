# Generated by Django 3.2.4 on 2021-10-10 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0065_alter_quotes_final_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draw',
            name='status',
            field=models.CharField(choices=[('finalizado', 'Finalizado'), ('sin_concluir', 'Sin concluir')], default='Sin concluir', max_length=15, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='final_customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='operations.sub_customers', verbose_name='Contratante de la empresa'),
        ),
    ]