# Generated by Django 3.2.4 on 2021-10-10 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0052_alter_preliminary_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preliminary',
            options={'ordering': ['id'], 'verbose_name': 'Preliminar', 'verbose_name_plural': 'Preliminares'},
        ),
    ]
