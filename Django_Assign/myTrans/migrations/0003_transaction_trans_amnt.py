# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myTrans', '0002_auto_20170331_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='Trans_Amnt',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=150),
        ),
    ]
