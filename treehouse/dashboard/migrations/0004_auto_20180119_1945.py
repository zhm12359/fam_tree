# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 19:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180119_1939'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([]),
        ),
    ]
