# Generated by Django 3.2.5 on 2023-04-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0033_alter_vinculacion_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='direccion',
            field=models.CharField(max_length=150, verbose_name='Dirección Comercio'),
        ),
    ]