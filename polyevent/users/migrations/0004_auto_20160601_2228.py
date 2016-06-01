# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-01 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('users', '0003_auto_20160601_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polyeventusermanager',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='polyeventusermanager',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='polyeventuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='polyeventuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='polyeventuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.DeleteModel(
            name='PolyEventUserManager',
        ),
    ]
