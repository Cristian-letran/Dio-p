# Generated by Django 3.2.5 on 2023-04-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0029_gestores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestores',
            name='fecha_contrato',
            field=models.DateField(auto_now=True),
        ),
    ]