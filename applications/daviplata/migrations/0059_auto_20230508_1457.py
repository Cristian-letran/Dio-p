# Generated by Django 3.2.5 on 2023-05-08 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0058_auto_20230508_1449'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoNoEfectiva',
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='medio',
            field=models.CharField(blank=True, choices=[('Telefono', 'Telefono'), ('Internet', 'Internet'), ('E-Mail ', 'E-Mail '), ('Otro', 'Otro'), ('WhatsApp', 'WhatsApp')], max_length=30, null=True),
        ),
    ]