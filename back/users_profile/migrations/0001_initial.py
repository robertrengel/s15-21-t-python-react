# Generated by Django 5.0.6 on 2024-06-06 05:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('unique_id', models.CharField(max_length=45)),
                ('id_type', models.CharField(max_length=45)),
                ('id_value', models.CharField(max_length=45)),
                ('genre', models.CharField(choices=[('H', 'HOMBRE'), ('M', 'MUJER'), ('O', 'OTRO')], max_length=3)),
                ('civil_status', models.CharField(choices=[('S', 'SOLTERO'), ('C', 'CASADO'), ('U', 'UNION LIBRE'), ('V', 'VIUDO O VIUDA'), ('O', 'OTRO')], max_length=1)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('notifications', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('S', 'SIN REGISTRO'), ('C', 'CANCELADO'), ('T', 'EN TRAMITE'), ('D', 'DEMANDADO'), ('O', 'OTRO'), ('V', 'VIGENTE')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'db_table': 'profile',
            },
        ),
    ]