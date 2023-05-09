# Generated by Django 3.2.5 on 2023-05-04 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daviplata', '0041_alter_daviplata_rdab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daviplata',
            name='coincide_direccion',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='detalle_direccion',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Detalle Dir actualizada'),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='direccion_actualizada',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Dirección Actualizada'),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='direccion_completo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Completo actualizada'),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='es_dueño',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='establecimiento_cambio',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True, verbose_name='El establecimiento cambió de dueño en el ultimo año?'),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='mobre_e_a',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre del establecimiento actualizado'),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='nombre_atiende',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre de quien atendió la visita'),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='nombre_coincide',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='numero_movil',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='otro_d_e',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daviplata.otrotipoestablecimiento', verbose_name='Otro tipo de establecimiento'),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='otro_senalizacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daviplata.otrotiposenalizacion', verbose_name='Otro especificado'),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='pdv',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=50, null=True, verbose_name='¿PDV permite realizar la visita?'),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='t_senalizacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daviplata.tiposenalizacion', verbose_name='Tipo de señalizacion'),
        ),
        migrations.AlterField(
            model_name='daviplata',
            name='tipo_establecimiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daviplata.tipoestablecimiento'),
        ),
    ]