# Generated by Django 5.0.4 on 2024-06-11 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_order', '0002_alter_workorder_observation'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='cause',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
