# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 20:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20161005_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedingrecord',
            name='day',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
    ]