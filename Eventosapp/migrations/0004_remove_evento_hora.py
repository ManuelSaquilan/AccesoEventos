# Generated by Django 5.0.1 on 2024-01-29 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eventosapp', '0003_alter_invitados_hora_ingreso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='hora',
        ),
    ]