# Generated by Django 3.2.5 on 2023-04-17 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0014_alter_vinculacion_se_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='solicito_tencard',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO'), ('Ya tiene la tencard', 'Ya tiene la tencard'), ('Modo Contingencia', 'Modo Contingencia')], max_length=40, null=True, verbose_name='¿Se solicitó la tentcard?'),
        ),
    ]