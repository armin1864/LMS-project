# Generated by Django 5.1.1 on 2024-09-13 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0022_alter_user_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateField(default=datetime.datetime(2024, 9, 13, 20, 50, 46, 362673, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='total_reserves',
            field=models.IntegerField(default=0),
        ),
    ]
