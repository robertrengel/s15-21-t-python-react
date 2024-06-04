
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('speciality_name', models.CharField(max_length=50, unique=True)),
                ('speciality_img_url', models.URLField(max_length=120)),
                ('speciality_description', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'verbose_name': 'speciality',
                'verbose_name_plural': 'specialities',
                'db_table': 'specialities',
            },
        ),
    ]
