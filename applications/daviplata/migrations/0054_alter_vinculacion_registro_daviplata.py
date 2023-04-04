# Generated by Django 3.2.5 on 2023-04-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0053_auto_20230404_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='registro_daviplata',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('Ya está activo', 'Ya está activo'), ('Modo Contingencia', 'Modo Contingencia')], max_length=20, verbose_name='¿Se realizó registro en DaviPlata?'),
        ),
    ]