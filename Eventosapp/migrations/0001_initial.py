# Generated by Django 5.0.1 on 2024-01-18 04:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('idEvento', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50, verbose_name='Nombre')),
                ('fechaInicio', models.DateTimeField(verbose_name='fecha')),
                ('lugar', models.CharField(max_length=30, verbose_name='Lugar')),
                ('hora', models.DateField(verbose_name='Hora')),
            ],
            options={
                'db_table': 'eventos',
            },
        ),
        migrations.CreateModel(
            name='Invitados',
            fields=[
                ('idInvitado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=70, verbose_name='Nombre')),
                ('ingreso', models.BooleanField(default=False, null=True, verbose_name='Ingresó')),
                ('hora_ingreso', models.DateField(null=True, verbose_name='Hora de Ingreso')),
                ('IdEvento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eventosapp.evento')),
            ],
            options={
                'verbose_name': 'invitado',
                'verbose_name_plural': 'invitados',
                'db_table': 'invitados',
            },
        ),
    ]