# Generated by Django 3.2.5 on 2023-05-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0072_alter_daviplata_url_img_f'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daviplata',
            name='codigo_total',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
