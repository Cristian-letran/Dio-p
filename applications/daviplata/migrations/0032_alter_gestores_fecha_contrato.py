# Generated by Django 3.2.5 on 2023-05-02 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0031_auto_20230428_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestores',
            name='fecha_contrato',
            field=models.DateField(blank=True),
        ),
    ]
