# Generated by Django 3.2.5 on 2023-06-13 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0102_alter_daviplata_fecha_eliminar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daviplata',
            name='fecha_eliminar',
        ),
    ]
