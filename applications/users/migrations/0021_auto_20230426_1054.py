# Generated by Django 3.2.5 on 2023-04-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_historicaluser'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='tipo_d_i',
            field=models.CharField(choices=[(1, 'CC')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='tipo_d_i',
            field=models.CharField(choices=[(1, 'CC')], max_length=2, null=True),
        ),
    ]
