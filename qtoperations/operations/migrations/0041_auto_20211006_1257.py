# Generated by Django 3.2.4 on 2021-10-06 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0040_alter_draw_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudes',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='solicitudes',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='solicitudes',
            name='service_id',
        ),
    ]
