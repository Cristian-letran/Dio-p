# Generated by Django 3.2.5 on 2023-04-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_user_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.IntegerField(blank=True, choices=[(1, 'Consulta'), (2, 'Davivienda Administrador'), (3, 'Daviplata')], null=True),
        ),
    ]
