# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-15 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='assistant_big',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='assistant_big_2',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='big_2',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
