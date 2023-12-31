# Generated by Django 3.2.5 on 2023-05-18 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('daviplata', '0075_alter_daviplata_pdv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daviplata',
            name='red',
            field=models.CharField(choices=[('PuntoRed (ConexRed)', 'PuntoRed (ConexRed)'), ('Conred', 'Conred'), ('Punto de Pago ', 'Punto de Pago'), ('PuntoRed (ConexRed) Onboarding', 'PuntoRed (ConexRed) Onboarding'), ('Conred (Super Pagos)', 'Conred (Super Pagos)'), ('Reval', 'Reval')], max_length=60),
        ),
        migrations.CreateModel(
            name='RutaDaviplata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.ManyToManyField(to='daviplata.Daviplata')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
