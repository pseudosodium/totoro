# Generated by Django 3.0.6 on 2020-05-31 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='datePublished',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 15, 16, 16, 529514)),
        ),
    ]