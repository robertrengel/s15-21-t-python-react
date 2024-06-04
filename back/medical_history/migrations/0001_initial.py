

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('added_by', models.PositiveIntegerField()),
                ('add_datetime', models.DateTimeField()),
                ('title', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('public', models.BooleanField(default=False)),
                ('private', models.BooleanField(default=False)),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speciality', to='catalogs.speciality')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_histories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'medical_history',
                'verbose_name_plural': 'medical_histories',
                'db_table': 'medical_histories',
            },
        ),
    ]
