# Generated by Django 3.0.6 on 2020-06-01 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toto', '0012_auto_20200601_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='answer',
            name='datePublished',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 1, 15, 38, 2, 616297)),
        ),
        migrations.AlterField(
            model_name='question',
            name='datePublished',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 1, 15, 38, 2, 612289)),
        ),
    ]
