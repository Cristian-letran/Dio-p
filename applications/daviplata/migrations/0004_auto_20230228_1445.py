# Generated by Django 3.2.5 on 2023-02-28 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0003_auto_20230228_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daviplata',
            name='url_img_f',
            field=models.ImageField(default=1, upload_to='IMG FACHADA', verbose_name='URL IMAGEN FACHADA'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='url_img_m',
            field=models.ImageField(default=1, upload_to='IMG MATERIAL', verbose_name='URL IMAGEN IMPL. MATERIAL'),
            preserve_default=False,
        ),
    ]
