# Generated by Django 3.2.5 on 2023-04-12 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0008_vinculacion_no_transaccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daviplata.categorias', verbose_name='¿A cual de las siguientes categorias pertenece el comercio?'),
        ),
        migrations.AlterField(
            model_name='vinculacion',
            name='celular',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='No. celular activado en DaviPlata'),
        ),
        migrations.AlterField(
            model_name='vinculacion',
            name='celular_confirma',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Confirmación No. celular activado en DaviPlata'),
        ),
        migrations.AlterField(
            model_name='vinculacion',
            name='nombre',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre del cliente DaviPlata'),
        ),
        migrations.AlterField(
            model_name='vinculacion',
            name='nombre_comercio',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]