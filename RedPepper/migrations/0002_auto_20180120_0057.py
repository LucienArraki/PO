# Generated by Django 2.0.1 on 2018-01-19 23:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('RedPepper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zamówienie',
            name='created_date',
            field=models.TimeField(verbose_name=datetime.datetime(2018, 1, 19, 23, 57, 46, 367446, tzinfo=utc)),
        ),
    ]
