# Generated by Django 3.2.5 on 2023-05-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0054_alter_daviplata_otro_d_e'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OtroTipoEstablecimiento',
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='t_senalizacion',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Tipo de señalizacion'),
        ),
    ]
