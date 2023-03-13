# Generated by Django 3.2.5 on 2022-12-21 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('argumento', '0001_initial'),
        ('courrier', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fisico', '0002_initial'),
        ('ruta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepcion',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Gestion'),
        ),
        migrations.AddField(
            model_name='punteo',
            name='guia_punteo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fisico.fisico'),
        ),
        migrations.AddField(
            model_name='planilla',
            name='cargue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ruta.cargue', verbose_name='Planilla'),
        ),
        migrations.AddField(
            model_name='planilla',
            name='full_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='courrier.courrier', verbose_name='Mensajero'),
        ),
        migrations.AddField(
            model_name='planilla',
            name='guia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planilla_filtro', to='fisico.fisico'),
        ),
        migrations.AddField(
            model_name='planilla',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Gestion'),
        ),
        migrations.AddField(
            model_name='imprimir',
            name='guia_imprimir',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fisico.fisico'),
        ),
        migrations.AddField(
            model_name='imprimir',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='historicalrecepcion',
            name='estado',
            field=models.ForeignKey(blank=True, db_constraint=False, default=3, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='argumento.estado'),
        ),
        migrations.AddField(
            model_name='historicalrecepcion',
            name='guia',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', related_query_name='recepcion', to='fisico.fisico'),
        ),
        migrations.AddField(
            model_name='historicalrecepcion',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalrecepcion',
            name='motivo',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='argumento.motivo'),
        ),
        migrations.AddField(
            model_name='historicalrecepcion',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Gestion'),
        ),
        migrations.AddField(
            model_name='historicalplanilla',
            name='cargue',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ruta.cargue', verbose_name='Planilla'),
        ),
        migrations.AddField(
            model_name='historicalplanilla',
            name='full_name',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='courrier.courrier', verbose_name='Mensajero'),
        ),
        migrations.AddField(
            model_name='historicalplanilla',
            name='guia',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='fisico.fisico'),
        ),
        migrations.AddField(
            model_name='historicalplanilla',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalplanilla',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Gestion'),
        ),
        migrations.AddField(
            model_name='historicaldestino',
            name='destino',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ruta.sucursales'),
        ),
        migrations.AddField(
            model_name='historicaldestino',
            name='guia',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='fisico.fisico'),
        ),
        migrations.AddField(
            model_name='historicaldestino',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldestino',
            name='sucursal',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ruta.sucursales'),
        ),
        migrations.AddField(
            model_name='historicaldestino',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='historicaldescargue',
            name='guia',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='fisico.fisico'),
        ),
        migrations.AddField(
            model_name='historicaldescargue',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldescargue',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='destino',
            name='destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinos', to='ruta.sucursales'),
        ),
        migrations.AddField(
            model_name='destino',
            name='guia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guia_destino', to='fisico.fisico'),
        ),
        migrations.AddField(
            model_name='destino',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guia_destino', to='ruta.sucursales'),
        ),
        migrations.AddField(
            model_name='destino',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='descargue',
            name='guia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guia_descargue', to='fisico.fisico'),
        ),
        migrations.AddField(
            model_name='descargue',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='cargue',
            name='full_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courrier.courrier', verbose_name='Mensajero'),
        ),
        migrations.AddField(
            model_name='cargue',
            name='guia',
            field=models.ManyToManyField(through='ruta.Planilla', to='fisico.Fisico'),
        ),
        migrations.AlterUniqueTogether(
            name='recepcion',
            unique_together={('guia', 'fecha')},
        ),
    ]
