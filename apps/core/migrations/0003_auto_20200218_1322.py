# Generated by Django 3.0.3 on 2020-02-18 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200218_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='desired_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
