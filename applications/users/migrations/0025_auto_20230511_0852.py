# Generated by Django 3.2.5 on 2023-05-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20230503_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='roles',
            field=models.IntegerField(blank=True, choices=[(1, 'Consulta'), (2, 'Davivienda Administrador'), (3, 'Daviplata'), (4, 'Custodia'), (5, 'Courrier'), (6, 'Mesa de control'), (7, 'Sig'), (8, 'call center'), (9, 'DASHBOARD')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.IntegerField(blank=True, choices=[(1, 'Consulta'), (2, 'Davivienda Administrador'), (3, 'Daviplata'), (4, 'Custodia'), (5, 'Courrier'), (6, 'Mesa de control'), (7, 'Sig'), (8, 'call center'), (9, 'DASHBOARD')], null=True),
        ),
    ]