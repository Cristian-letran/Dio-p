# Generated by Django 3.2.5 on 2023-05-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0046_alter_daviplata_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daviplata',
            name='grupo_etnico',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=50, null=True, verbose_name='HACE PARTE DE UN GRUPO ETNICO'),
        ),
    ]