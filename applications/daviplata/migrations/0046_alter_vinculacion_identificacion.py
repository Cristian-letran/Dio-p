# Generated by Django 3.2.5 on 2023-04-04 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0045_auto_20230404_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculacion',
            name='identificacion',
            field=models.AutoField(max_length=16, primary_key=True, serialize=False),
        ),
    ]
