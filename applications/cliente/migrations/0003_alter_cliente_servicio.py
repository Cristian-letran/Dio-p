# Generated by Django 3.2.5 on 2023-04-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Servicio',
            field=models.CharField(blank=True, choices=[('1', 'Davivienda'), ('2', 'Daviplata')], max_length=2, null=True),
        ),
    ]