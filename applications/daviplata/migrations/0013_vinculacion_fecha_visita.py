# Generated by Django 3.2.5 on 2023-03-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0012_vinculacion_nombre_comercio'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinculacion',
            name='fecha_visita',
            field=models.DateField(auto_now=True),
        ),
    ]