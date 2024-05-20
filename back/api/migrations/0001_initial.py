# Generated by Django 5.0.6 on 2024-05-19 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso3', models.CharField(max_length=3, unique=True)),
                ('isonum', models.CharField(max_length=3, unique=True)),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('country_code', models.CharField(choices=[('ARG', 'ARGENTINA'), ('MEX', 'MEXICO'), ('PER', 'PERU'), ('VEN', 'VENEZUELA')], max_length=3)),
                ('uniqueid', models.CharField(max_length=100)),
                ('role_choices', models.CharField(choices=[('PAC', 'PACIENTE'), ('PRO', 'MEDICO'), ('OSA', 'ORGANISMO DE SALUD'), ('OAU', 'ORGANISMO DE AUTENTICACION')], default='PAC', max_length=3)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.country')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.role')),
            ],
        ),
    ]
