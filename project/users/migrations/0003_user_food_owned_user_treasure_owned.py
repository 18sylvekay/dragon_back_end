# Generated by Django 5.1.3 on 2024-11-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='food_owned',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='treasure_owned',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
