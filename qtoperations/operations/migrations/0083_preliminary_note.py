# Generated by Django 3.2.4 on 2021-10-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0082_auto_20211024_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='preliminary',
            name='note',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Comentario'),
        ),
    ]