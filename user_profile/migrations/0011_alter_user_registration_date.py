# Generated by Django 5.1.1 on 2024-09-10 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0010_alter_user_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateField(default=datetime.datetime(2024, 9, 10, 11, 40, 7, 647511, tzinfo=datetime.timezone.utc)),
        ),
    ]
