# Generated by Django 3.0.6 on 2020-06-01 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toto', '0019_auto_20200601_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='datePublished',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 1, 22, 31, 1, 802711)),
        ),
        migrations.AlterField(
            model_name='question',
            name='datePublished',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 1, 22, 31, 1, 802711)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_slug',
            field=models.SlugField(unique=True),
        ),
    ]