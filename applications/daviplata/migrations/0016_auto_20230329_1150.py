# Generated by Django 3.2.5 on 2023-03-29 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0015_alter_comerciovinculacion_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinculacion',
            name='c_rut',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default=1, max_length=2, verbose_name='¿Comercio cuenta con RUT?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vinculacion',
            name='nombre_comercio',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ComercioVinculacion',
        ),
    ]