# Generated by Django 5.1.3 on 2024-11-16 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragons', '0002_dragon_dragon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dragon',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
