# Generated by Django 3.2.5 on 2023-03-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0009_vinculacion_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='nombre',
            field=models.CharField(max_length=150, verbose_name='¿A cuál de las siguientes categorías pertenece el comercio?'),
        ),
    ]