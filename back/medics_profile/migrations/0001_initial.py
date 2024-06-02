# Generated by Django 5.0.6 on 2024-06-01 01:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date_of_tuition', models.DateTimeField()),
                ('status', models.CharField(choices=[('P', 'PENDIENTE'), ('A', 'ACTIVO'), ('I', 'INACTIVO')], default='A', max_length=1)),
                ('observations', models.CharField(max_length=45)),
                ('added_by', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medics_profile', to='api.apiuser')),
            ],
            options={
                'db_table': 'medics_profile',
            },
        ),
    ]
