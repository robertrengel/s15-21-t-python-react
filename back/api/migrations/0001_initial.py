# Generated by Django 5.0.6 on 2024-05-23 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.CharField(max_length=50, unique=True)),
                ('country_code', models.CharField(choices=[('ARG', 'ARGENTINA'), ('MEX', 'MEXICO'), ('PER', 'PERU'), ('VEN', 'VENEZUELA')], max_length=3)),
                ('role', models.CharField(choices=[('PAC', 'PACIENTE'), ('PRO', 'MEDICO'), ('OSA', 'ORGANISMO DE SALUD'), ('OAU', 'ORGANISMO DE AUTENTICACION')], default='PAC', max_length=3)),
                ('first_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('id_type', models.CharField(default='', max_length=255)),
                ('id_value', models.CharField(default='', max_length=255)),
                ('genre', models.CharField(default='', max_length=255)),
                ('civil_status', models.CharField(default='', max_length=255)),
                ('birth_date', models.DateField(editable=False, null=True)),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'PENDIENTE'), ('A', 'ACTIVO'), ('I', 'INACTIVO'), ('D', 'DENEGADO')], default='P', max_length=1)),
                ('proffesional_identifier', models.CharField(default='', max_length=50, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.apiuser')),
            ],
            options={
                'verbose_name': 'MedicData',
                'verbose_name_plural': 'MedicData',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('notifications', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.apiuser')),
            ],
        ),
    ]
