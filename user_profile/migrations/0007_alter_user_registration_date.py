# Generated by Django 5.1.1 on 2024-09-10 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_alter_user_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateField(default=datetime.datetime(2024, 9, 10, 10, 42, 10, 815194, tzinfo=datetime.timezone.utc)),
        ),
    ]
