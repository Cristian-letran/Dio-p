# Generated by Django 3.2.5 on 2023-03-08 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0003_auto_20230308_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='fisico',
            name='img_fachada_courrier',
            field=models.ImageField(blank=True, null=True, upload_to='img_fachada_courriers'),
        ),
        migrations.AddField(
            model_name='historicalfisico',
            name='img_fachada_courrier',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
