# Generated by Django 3.2.5 on 2023-03-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0016_auto_20230329_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoGestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
    ]
