# Generated by Django 3.0.6 on 2020-06-01 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toto', '0009_auto_20200601_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='datePublished',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 1, 15, 31, 54, 30921)),
        ),
    ]
