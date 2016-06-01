# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='polyeventuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Défini si cet utilisateur doit être considéré comme actif. Désactiver ceci au lieu de supprimer le compte.'),
        ),
    ]