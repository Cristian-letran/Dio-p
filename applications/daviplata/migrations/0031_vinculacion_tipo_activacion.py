# Generated by Django 3.2.5 on 2023-03-30 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0030_tipoactivacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinculacion',
            name='tipo_activacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='daviplata.tipoactivacion', verbose_name='Tipo activación'),
            preserve_default=False,
        ),
    ]