# Generated by Django 3.2.5 on 2023-05-11 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0069_auto_20230511_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='daviplata',
            name='tiempo',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
    ]
