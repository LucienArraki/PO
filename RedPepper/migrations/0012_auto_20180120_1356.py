# Generated by Django 2.0.1 on 2018-01-20 12:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('RedPepper', '0011_auto_20180120_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='type',
            field=models.CharField(default='pizza', max_length=200),
        ),
        migrations.AlterField(
            model_name='zamówienie',
            name='created_date',
            field=models.TimeField(verbose_name=datetime.datetime(2018, 1, 20, 12, 56, 13, 274828, tzinfo=utc)),
        ),
    ]
