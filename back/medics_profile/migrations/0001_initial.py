
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
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medics_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'medics_profile',
            },
        ),
    ]
