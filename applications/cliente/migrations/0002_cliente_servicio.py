# Generated by Django 3.2.5 on 2023-04-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='Servicio',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
