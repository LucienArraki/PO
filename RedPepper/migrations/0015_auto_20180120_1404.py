# Generated by Django 2.0.1 on 2018-01-20 13:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('RedPepper', '0014_auto_20180120_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skladniki',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='zamówienie',
            name='created_date',
            field=models.TimeField(verbose_name=datetime.datetime(2018, 1, 20, 13, 4, 15, 907618, tzinfo=utc)),
        ),
    ]
