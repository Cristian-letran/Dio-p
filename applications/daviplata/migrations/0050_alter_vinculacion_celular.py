# Generated by Django 3.2.5 on 2023-04-04 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0049_alter_vinculacion_identificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='celular',
            field=models.CharField(max_length=12, unique=True, verbose_name='No. celular activado en DaviPlata'),
        ),
    ]
