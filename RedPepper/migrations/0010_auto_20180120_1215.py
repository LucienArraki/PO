# Generated by Django 2.0.1 on 2018-01-20 11:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('RedPepper', '0009_auto_20180120_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oferta',
            name='howMuch',
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='price',
        ),
        migrations.AddField(
            model_name='oferta',
            name='priceBig',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='oferta',
            name='priceSmall',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='zamówienie',
            name='created_date',
            field=models.TimeField(verbose_name=datetime.datetime(2018, 1, 20, 11, 15, 40, 653656, tzinfo=utc)),
        ),
    ]
