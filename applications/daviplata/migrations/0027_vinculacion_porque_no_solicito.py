# Generated by Django 3.2.5 on 2023-03-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0026_auto_20230330_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinculacion',
            name='porque_no_solicito',
            field=models.CharField(choices=[('1', 'No esta interesado'), ('2', 'NO le llama la atención '), ('3', 'Solo trabaja con Nequi '), ('4', 'Le parece Complicado Manejarlo')], default=1, max_length=2, verbose_name='¿Por qué no se solicitó la tentcard?'),
            preserve_default=False,
        ),
    ]