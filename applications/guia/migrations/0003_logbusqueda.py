# Generated by Django 3.2.5 on 2023-02-21 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogBusqueda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guia.guia')),
            ],
        ),
    ]