# Generated by Django 3.2.5 on 2023-05-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0038_gestores_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestores',
            name='fecha_retiro',
            field=models.DateField(blank=True, null=True),
        ),
    ]
