# Generated by Django 3.2.5 on 2023-04-24 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0018_alter_vinculacion_tipo_gestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='fecha_visita',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='vinculacion',
            name='se_registro',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO'), ('Ya esta activo', 'Ya está activo'), ('Modo contingencia', 'Modo contingencia')], max_length=20, null=True, verbose_name='¿Se realizó registro en perfil mi negocio?'),
        ),
    ]