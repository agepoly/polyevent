# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-01 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160601_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='polyeventuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='polyeventuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]