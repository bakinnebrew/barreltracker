# Generated by Django 3.1.3 on 2021-04-02 20:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0022_auto_20210402_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='alert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='barrel',
            name='pull_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 29, 20, 6, 4, 926187)),
        ),
    ]
