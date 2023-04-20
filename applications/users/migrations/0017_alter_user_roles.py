# Generated by Django 3.2.5 on 2023-04-19 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_user_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.IntegerField(blank=True, choices=[(1, 'Consulta'), (2, 'Davivienda Administrador'), (3, 'Daviplata'), (4, 'Custodia'), (5, 'Courrier'), (6, 'Mesa de control')], null=True),
        ),
    ]
