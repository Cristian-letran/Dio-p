# Generated by Django 3.2.5 on 2023-06-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_alter_zona_zona'),
    ]

    operations = [
        migrations.AddField(
            model_name='zona',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
