# Generated by Django 3.2.5 on 2023-06-28 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0010_zona_name'),
        ('daviplata', '0118_delete_asistencia_vinculacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinculacion',
            name='zona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.zona'),
        ),
    ]
