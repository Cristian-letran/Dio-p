# Generated by Django 3.2.5 on 2023-06-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0089_auto_20230601_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='direccion',
            field=models.CharField(blank=True, max_length=150, verbose_name='Dirección Comercio'),
        ),
    ]