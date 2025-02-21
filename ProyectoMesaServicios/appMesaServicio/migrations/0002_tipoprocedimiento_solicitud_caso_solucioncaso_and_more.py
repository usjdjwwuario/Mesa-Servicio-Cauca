# Generated by Django 5.0.6 on 2024-05-20 13:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMesaServicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProcedimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipNombre', models.CharField(db_comment='Nombre del tipo de procedimiento', max_length=20, unique=True)),
                ('tipDescripcion', models.TextField(db_comment='Descripcion del tipo de procedimiento', max_length=1000)),
                ('fechaHoraCreacion', models.DateTimeField(auto_now_add=True, db_comment='Fecha y hora del registro')),
                ('fechaHoraActualizacion', models.DateTimeField(auto_now=True, db_comment='Fecha y hora de la ultima actualzacion')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solDescripcion', models.TextField(db_comment='Texto que escribe la solicitud del empleado', max_length=1000)),
                ('fechaHoraCreacion', models.DateTimeField(auto_now_add=True, db_comment='Fecha y hora del registro')),
                ('fechaHoraActualizacion', models.DateTimeField(auto_now=True, db_comment='Fecha y hora de la ultima actualzacion')),
                ('solOficinaAmbiente', models.ForeignKey(db_comment='Hace referencia a la oficina o ambiente donde se encuentrar en equipo de la solicitud', on_delete=django.db.models.deletion.PROTECT, to='appMesaServicio.oficinaambiente')),
                ('solUsuario', models.ForeignKey(db_comment='Hce referencia al empleado que ahce la solicitud', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casCodigo', models.CharField(db_comment='El codigo es unico', max_length=10, unique=True)),
                ('casEstado', models.CharField(choices=[('Solicitada', 'Solicitada'), ('En proceso', 'En proceso'), ('Finalizada', 'Finalizada')], max_length=15)),
                ('fechaHoraActualizacion', models.DateTimeField(auto_now=True, db_comment='Fecha y hora de la ultima actualzacion')),
                ('casUsuario', models.ForeignKey(db_comment='Empleado de soporte tecnico asignado', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('casSolicitud', models.ForeignKey(db_comment='Hace referencia a la solicitud que generea........', on_delete=django.db.models.deletion.PROTECT, to='appMesaServicio.solicitud')),
            ],
        ),
        migrations.CreateModel(
            name='SolucionCaso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solProcedimiento', models.TextField(db_comment='Hace referencia al tipo de procedimiento', max_length=1000)),
                ('fechaHoraCreacion', models.DateTimeField(auto_now_add=True, db_comment='Fceha y hora del registro')),
                ('fechaHoraActualizacion', models.DateTimeField(auto_now=True, db_comment='Fecha y hora de la actualizacion')),
                ('solCaso', models.ForeignKey(db_comment='Hace referencia al caso que genera la solucion del problema', on_delete=django.db.models.deletion.PROTECT, to='appMesaServicio.caso')),
            ],
        ),
        migrations.CreateModel(
            name='SolucionCasoTipoProcedimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solSolucionCaso', models.ForeignKey(db_comment='Hace referencia a la solucion del caso', on_delete=django.db.models.deletion.PROTECT, to='appMesaServicio.solucioncaso')),
                ('solTipoProcedimiento', models.ForeignKey(db_comment='Hace referencia al tipo de procedimiento de la solucion', on_delete=django.db.models.deletion.PROTECT, to='appMesaServicio.tipoprocedimiento')),
            ],
        ),
    ]
