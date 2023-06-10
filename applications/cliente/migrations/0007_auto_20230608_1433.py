# Generated by Django 3.2.5 on 2023-06-08 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_alter_cliente_rol'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='departamento',
            name='localidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.localidad'),
        ),
    ]
