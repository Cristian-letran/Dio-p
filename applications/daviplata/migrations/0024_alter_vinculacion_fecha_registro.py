# Generated by Django 3.2.5 on 2023-04-25 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0023_vinculacion_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='fecha_registro',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
