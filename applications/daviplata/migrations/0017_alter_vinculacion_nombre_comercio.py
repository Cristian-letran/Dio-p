# Generated by Django 3.2.5 on 2023-04-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0016_alter_vinculacion_sticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='nombre_comercio',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]
