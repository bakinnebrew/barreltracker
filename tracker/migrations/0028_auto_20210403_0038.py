# Generated by Django 3.1.3 on 2021-04-03 00:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0027_auto_20210403_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrel',
            name='pull_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 0, 38, 56, 593936)),
        ),
    ]
