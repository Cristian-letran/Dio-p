# Generated by Django 3.2.5 on 2023-05-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0037_alter_gestores_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestores',
            name='proveedor',
            field=models.CharField(default='Firstsource', max_length=30, null=True),
        ),
    ]
