# Generated by Django 5.0.6 on 2024-05-28 22:38

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
                ('role', models.CharField(choices=[('PAC', 'PACIENTE'), ('MED', 'MEDICO'), ('OSA', 'ORGANISMO DE SALUD'), ('OAU', 'ORGANISMO DE AUTENTICACION')], default='PAC', max_length=3)),
                ('first_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('id_type', models.CharField(default='', max_length=255)),
                ('id_value', models.CharField(default='', max_length=255)),
                ('genre', models.CharField(default='', max_length=255)),
                ('civil_status', models.CharField(default='', max_length=255)),
                ('birth_date', models.DateField(editable=False, null=True)),
                ('password', models.CharField(max_length=255)),
                ('created_by', models.CharField(default='Usuario', max_length=50, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('notifications', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('P', 'PENDIENTE'), ('A', 'ACTIVO'), ('I', 'INACTIVO')], default='P', max_length=1)),
            ],
        ),
    ]
