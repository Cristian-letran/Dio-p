# Generated by Django 3.2.5 on 2023-03-27 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_ocupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='logsesion',
            name='accion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]