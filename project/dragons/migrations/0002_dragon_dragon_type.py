# Generated by Django 5.1.3 on 2024-11-16 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dragon',
            name='dragon_type',
            field=models.CharField(choices=[('green', 'Green'), ('blue', 'Blue'), ('red', 'Red')], default='red', max_length=10),
            preserve_default=False,
        ),
    ]
