# Generated by Django 3.1.3 on 2021-03-16 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barrel',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 11, 48, 24, 963791)),
        ),
        migrations.AddField(
            model_name='barrel',
            name='fill_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 11, 48, 24, 963811)),
        ),
        migrations.AlterField(
            model_name='barrel',
            name='pull_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 11, 48, 24, 963852)),
        ),
    ]
