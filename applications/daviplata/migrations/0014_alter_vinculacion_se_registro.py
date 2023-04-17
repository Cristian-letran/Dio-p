# Generated by Django 3.2.5 on 2023-04-17 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0013_alter_vinculacion_registro_daviplata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='se_registro',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO'), ('Ya esta activo', 'Ya esta activo'), ('Modo contingencia', 'Modo contingencia')], max_length=20, null=True, verbose_name='¿Se realizó registro en perfil mi negocio?'),
        ),
    ]
