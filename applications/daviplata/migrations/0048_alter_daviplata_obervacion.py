# Generated by Django 3.2.5 on 2023-05-04 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0047_alter_daviplata_grupo_etnico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daviplata',
            name='obervacion',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
