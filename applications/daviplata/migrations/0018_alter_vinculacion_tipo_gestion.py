# Generated by Django 3.2.5 on 2023-04-20 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0017_alter_vinculacion_nombre_comercio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='tipo_gestion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='daviplata.tipogestion'),
            preserve_default=False,
        ),
    ]
