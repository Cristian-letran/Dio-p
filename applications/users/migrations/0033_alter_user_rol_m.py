# Generated by Django 3.2.5 on 2023-06-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_alter_user_rol_m'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rol_m',
            field=models.ManyToManyField(blank=True, related_name='modulo_user', to='users.Modulos'),
        ),
    ]