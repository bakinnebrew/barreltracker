# Generated by Django 3.1.3 on 2021-03-16 20:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20210316_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrel',
            name='pull_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 20, 25, 20, 585099)),
        ),
    ]