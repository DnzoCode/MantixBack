# Generated by Django 5.0.4 on 2024-06-10 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_end_time_event_init_time_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='shift',
            field=models.CharField(default='A', max_length=1),
        ),
    ]
