# Generated by Django 3.2.5 on 2022-12-29 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogSesion',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('cliente', models.CharField(max_length=90)),
                ('usuario', models.CharField(max_length=150)),
                ('documento', models.CharField(max_length=15)),
            ],
        ),
    ]
