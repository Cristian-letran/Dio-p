# Generated by Django 3.2.5 on 2023-06-29 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0119_vinculacion_zona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daviplata',
            name='url_img_f',
            field=models.ImageField(blank=True, null=True, upload_to='IMG FACHADA', verbose_name='URL IMAGEN FACHADA'),
        ),
    ]