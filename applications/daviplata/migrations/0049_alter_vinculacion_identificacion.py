# Generated by Django 3.2.5 on 2023-04-04 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0048_alter_vinculacion_identificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='identificacion',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
