# Generated by Django 3.2.5 on 2023-06-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0093_alter_vinculacion_detail_complemento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daviplata',
            name='tipo_no_efectiva',
            field=models.CharField(blank=True, choices=[('Direccion Errada', 'Direccion Errada'), ('Local Cerrado', 'Local Cerrado'), ('No Existe PVD', 'No Existe PVD'), ('El Cliente No Permitio Realizar encuesta', 'El Cliente No Permitio Realizar encuesta'), ('Cambio de Direccion PVD', 'Cambio de Direccion PVD'), ('Ya esta Marcado', 'Ya esta Marcado')], max_length=43, null=True),
        ),
    ]
