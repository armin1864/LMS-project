# Generated by Django 5.1.1 on 2024-09-15 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0028_alter_user_registration_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='total_reserves',
            new_name='total_borrows',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateField(default=datetime.datetime(2024, 9, 15, 12, 31, 2, 22995, tzinfo=datetime.timezone.utc)),
        ),
    ]
