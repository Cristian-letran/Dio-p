# Generated by Django 3.2.5 on 2022-12-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_logsesion_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='logsesion',
            name='registro',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
