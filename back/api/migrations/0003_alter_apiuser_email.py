# Generated by Django 5.0.6 on 2024-06-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_apiuser_user_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
