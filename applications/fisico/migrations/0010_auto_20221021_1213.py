# Generated by Django 3.2.5 on 2022-10-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0009_auto_20221021_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fisico',
            name='fecha_recepcion',
        ),
        migrations.AddField(
            model_name='bolsa',
            name='fecha_recepcion',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha gestion'),
        ),
    ]
