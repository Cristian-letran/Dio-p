# Generated by Django 3.2.5 on 2023-05-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0034_gestores_barrio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestores',
            name='fecha_retiro',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Retiro del asesor'),
        ),
    ]