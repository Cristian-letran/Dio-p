# Generated by Django 3.2.5 on 2023-04-04 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0044_remove_vinculacion_tipo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='latitud',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='vinculacion',
            name='longitud',
            field=models.CharField(max_length=20),
        ),
    ]
