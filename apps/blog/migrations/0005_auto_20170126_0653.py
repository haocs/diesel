# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-26 06:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170126_0639'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Article',
        ),
    ]
