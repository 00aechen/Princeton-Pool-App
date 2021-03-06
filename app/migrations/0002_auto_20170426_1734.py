# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rides',
            name='full_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='rides',
            name='other_destination',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='rides',
            name='own_car',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rides',
            name='ride_type',
            field=models.CharField(choices=[('Airport', 'Airport'), ('Shopping', 'Shopping'), ('Other', 'Other')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='users',
            name='netid',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='full_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
