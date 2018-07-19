# Generated by Django 2.0.7 on 2018-07-18 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsevents', '0012_remove_newsitem_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='description',
            field=models.TextField(blank=True, help_text="Проверяйте орфографию <a target='_blank' href='https://advego.com/text/'>здесь</a>", null=True),
        ),
    ]