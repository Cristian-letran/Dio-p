# Generated by Django 3.2.5 on 2023-05-02 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0035_alter_gestores_fecha_retiro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gestores',
            name='fecha_retiro',
        ),
        migrations.AddField(
            model_name='gestores',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], max_length=15, null=True),
        ),
    ]
