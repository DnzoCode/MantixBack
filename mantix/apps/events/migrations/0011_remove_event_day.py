# Generated by Django 5.0.4 on 2024-06-12 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_event_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='day',
        ),
    ]
