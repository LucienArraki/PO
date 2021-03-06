# Generated by Django 2.0.1 on 2018-01-20 00:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('RedPepper', '0004_auto_20180120_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skladniki',
            fields=[
                ('idS', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='oferta',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='zamówienie',
            options={'ordering': ('created_date',)},
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='info',
        ),
        migrations.AlterField(
            model_name='zamówienie',
            name='created_date',
            field=models.TimeField(verbose_name=datetime.datetime(2018, 1, 20, 0, 17, 41, 36378, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='oferta',
            name='info',
            field=models.ManyToManyField(to='RedPepper.Skladniki'),
        ),
    ]
