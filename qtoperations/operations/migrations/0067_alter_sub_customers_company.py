# Generated by Django 3.2.4 on 2021-10-10 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0066_auto_20211010_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_customers',
            name='company',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='operations.customers'),
        ),
    ]
