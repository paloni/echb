# Generated by Django 2.0.7 on 2019-02-19 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190219_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prayerrequest',
            name='user',
        ),
        migrations.DeleteModel(
            name='PrayerRequest',
        ),
    ]
