# Generated by Django 3.2.5 on 2023-05-19 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0079_alter_daviplata_coincide_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daviplata',
            name='nombre_coincide',
            field=models.CharField(choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
    ]
