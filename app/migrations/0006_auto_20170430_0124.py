# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 06:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170429_0304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rides',
            options={'ordering': ['-date_time']},
        ),
    ]