# Generated by Django 3.2.5 on 2023-03-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0022_auto_20230329_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotivoNoRegistro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='vinculacion',
            name='registro_daviplata',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default=1, max_length=2, verbose_name='¿Se realizó registro en DaviPlata?'),
            preserve_default=False,
        ),
    ]
