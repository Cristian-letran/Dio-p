# Generated by Django 3.2.5 on 2023-05-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0082_daviplata_minuto'),
    ]

    operations = [
        migrations.AddField(
            model_name='daviplata',
            name='continecia',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='latitud',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='longitud',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
    ]