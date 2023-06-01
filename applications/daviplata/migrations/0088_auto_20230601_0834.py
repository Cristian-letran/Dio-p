# Generated by Django 3.2.5 on 2023-06-01 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0087_auto_20230530_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplementoDireccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complemento', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='vinculacion',
            name='complemento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='daviplata.complementodireccion'),
        ),
        migrations.AddField(
            model_name='vinculacion',
            name='dir_a',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='daviplata.direccion'),
        ),
    ]
