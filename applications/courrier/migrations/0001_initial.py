# Generated by Django 3.2.5 on 2022-12-21 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linea_vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linea', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Liena ',
                'verbose_name_plural': 'Linea',
            },
        ),
        migrations.CreateModel(
            name='Marca_vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marca',
            },
        ),
        migrations.CreateModel(
            name='Modelos',
            fields=[
                ('modelo', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_infraccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infraccion', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Tipo de infraccion',
                'verbose_name_plural': 'Tipo infraccion',
            },
        ),
        migrations.CreateModel(
            name='Tipo_vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipo',
            },
        ),
        migrations.CreateModel(
            name='vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_veg', models.CharField(max_length=20, verbose_name='Id vehiculo')),
                ('name', models.CharField(max_length=50, verbose_name='Propietario de vehiculo')),
                ('cc', models.CharField(max_length=13)),
                ('cilindraje', models.IntegerField()),
                ('capacidad', models.IntegerField()),
                ('placa', models.CharField(max_length=10)),
                ('soat', models.DateField()),
                ('tecnomecanica', models.DateField()),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courrier.linea_vehiculo')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courrier.marca_vehiculo')),
                ('modelos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courrier.modelos')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courrier.tipo_vehiculo', verbose_name='Tipo vehiculo')),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculo',
            },
        ),
        migrations.CreateModel(
            name='courrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_i', models.CharField(max_length=12, unique=True, verbose_name='Documento identidad')),
                ('courrier', models.CharField(max_length=70, verbose_name='Nombre courrier')),
                ('cel', models.CharField(max_length=12, verbose_name='Celular')),
                ('dir', models.CharField(max_length=120, verbose_name='Direccion')),
                ('licencia', models.DateField()),
                ('est_courrier', models.BooleanField(default=True, verbose_name='Estado courrier')),
                ('id_ciu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.ciudad', verbose_name='Ciudad')),
                ('id_veh', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='courrier.vehiculo', verbose_name='Datos vehiculo')),
                ('infraccion', models.ManyToManyField(to='courrier.Tipo_infraccion')),
            ],
            options={
                'verbose_name': 'Courrier',
                'verbose_name_plural': 'Courrier',
            },
        ),
    ]
