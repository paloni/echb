# Generated by Django 2.0.7 on 2019-02-19 10:30

import accounts.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayerrequest',
            name='description',
            field=models.TextField(max_length=250, validators=[django.core.validators.MaxLengthValidator(
                limit_value=250, message='Сообщение должно быть длиной не более 250')]),
        ),
        migrations.AlterField(
            model_name='prayerrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
